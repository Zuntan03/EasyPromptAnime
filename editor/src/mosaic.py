import os, glob, cv2
import numpy as np
from nudenet import NudeDetector
from l10n import L10n
from collections import OrderedDict
from log import Log


class Mosaic:
    partsTable = {
        "FACE_FEM" + "ALE": "mosaicFemFace",
        "FEM" + "ALE_BRE" + "AST_EXPOSED": "mosaicFemBrst",
        "FEM" + "ALE_BRE" + "AST_COVERED": "mosaicFemBrstCov",
        "FEM" + "ALE_GENI" + "TALIA_EXPOSED": "mosaicFemGntl",
        "FEM" + "ALE_GENI" + "TALIA_COVERED": "mosaicFemGntlCov",
        "FACE_MALE": "mosaicMaleFace",
        "MALE_BRE" + "AST_EXPOSED": "mosaicMaleBrst",
        "MALE_GENI" + "TALIA_EXPOSED": "mosaicMaleGntl",
        "ARMPITS_EXPOSED": "mosaicArmpit",
        "ARMPITS_COVERED": "mosaicArmpitCov",
        "BELLY_EXPOSED": "mosaicBelly",
        "BELLY_COVERED": "mosaicBellyCov",
        "BUT" + "TOCKS_EXPOSED": "mosaicHip",
        "BUT" + "TOCKS_COVERED": "mosaicHipCov",
        "AN" + "US_EXPOSED": "mosaicAns",
        "AN" + "US_COVERED": "mosaicAnsCov",
        "FEET_EXPOSED": "mosaicFeet",
        "FEET_COVERED": "mosaicFeetCov",
    }

    @classmethod
    def mosaicPngDir(cls, generate, pngDir):
        pngPaths = sorted(glob.glob(os.path.join(pngDir, "*.png")))
        if len(pngPaths) == 0:
            return ""

        mosaics = cls.detectMosaic(generate, pngPaths)

        if generate.temporalMosaic:
            mosaics = cls.temporalMosaic(mosaics)

        dstDirName = os.path.basename(pngDir) + "_mosaic"
        dstDir = os.path.join(os.path.dirname(pngDir), dstDirName)
        os.makedirs(dstDir, exist_ok=True)
        for mosaic in mosaics:
            cls.mosaic(generate, mosaic, dstDir)

        return dstDir

    @classmethod
    def detectMosaic(cls, generate, pngPaths):
        nude_detector = NudeDetector()
        results = []
        for pngPath in pngPaths:
            detections = []
            for detection in nude_detector.detect(pngPath):
                if detection["score"] < generate.mosaicThreshold:
                    continue
                if detection["class"] not in cls.partsTable:
                    Log.system(f'Unknown detection class: {detection["class"]}.')
                    continue
                if not getattr(generate, cls.partsTable[detection["class"]]):
                    continue
                detections.append(detection)
            results.append({"path": pngPath, "detections": detections})
        return results

    @classmethod
    def temporalMosaic(cls, mosaics):
        temporalMosaics = []
        mosaicsNum = len(mosaics)
        for i in range(mosaicsNum):
            temporalMosaic = {
                "path": mosaics[i]["path"],
                "detections": [],
            }

            for detection in mosaics[i]["detections"]:
                temporalMosaic["detections"].append(detection)
            counter = 1
            while True:
                if len(temporalMosaic["detections"]) > 0:
                    break
                if i >= counter:
                    for detection in mosaics[i - counter]["detections"]:
                        temporalMosaic["detections"].append(detection)
                if i < mosaicsNum - counter:
                    for detection in mosaics[i + counter]["detections"]:
                        temporalMosaic["detections"].append(detection)
                counter += 1
                if counter >= mosaicsNum:
                    break
            temporalMosaics.append(temporalMosaic)
        return temporalMosaics

    @classmethod
    def mosaic(cls, generate, mosaic, dstDir):
        srcImg = cv2.imread(mosaic["path"])
        srcH, srcW = srcImg.shape[:2]
        mosaicScale = 100 / srcW
        maskBlur = int(generate.mosaicMaskBlur * srcW)
        if srcH > srcW:
            mosaicScale = 100 / srcH
            maskBlur = int(generate.mosaicMaskBlur * srcH)

        mosaicImg = cv2.resize(srcImg, None, fx=mosaicScale, fy=mosaicScale)
        mosaicImg = cv2.resize(mosaicImg, (srcW, srcH), interpolation=cv2.INTER_NEAREST)

        mosaicMask = np.zeros((srcH, srcW), dtype=np.uint8)

        for detection in mosaic["detections"]:
            box = detection["box"]
            cx = box[0] + (box[2] * 0.5)
            cy = box[1] + (box[3] * 0.5)
            hw = box[2] * 0.5
            hh = box[3] * 0.5
            st = hh * generate.mosaicScaleTop
            sb = hh * generate.mosaicScaleBottom
            sl = hw * generate.mosaicScaleLeft
            sr = hw * generate.mosaicScaleRight
            if generate.ellipseMosaic:
                cx = int((sr - sl) * 0.5 + cx)
                cy = int((sb - st) * 0.5 + cy)
                rx = int((sl + sr) / 2)
                ry = int((st + sb) / 2)
                cv2.ellipse(mosaicMask, ((cx, cy), (rx, ry), 0), 255, -1)
            else:
                cv2.rectangle(
                    mosaicMask,
                    (int(cx - sl), int(cy - st)),
                    (int(cx + sr), int(cy + sb)),
                    255,
                    -1,
                )

        if generate.mosaicIgnoreTop > 0:
            top = int(srcH * generate.mosaicIgnoreTop)
            cv2.rectangle(mosaicMask, (0, 0), (srcW, top), 0, -1)
        if generate.mosaicIgnoreBottom > 0:
            bottom = int(srcH * (1 - generate.mosaicIgnoreBottom))
            cv2.rectangle(mosaicMask, (0, bottom), (srcW, srcH), 0, -1)
        if generate.mosaicIgnoreLeft > 0:
            left = int(srcW * generate.mosaicIgnoreLeft)
            cv2.rectangle(mosaicMask, (0, 0), (left, srcH), 0, -1)
        if generate.mosaicIgnoreRight > 0:
            right = int(srcW * (1 - generate.mosaicIgnoreRight))
            cv2.rectangle(mosaicMask, (right, 0), (srcW, srcH), 0, -1)

        if maskBlur > 0:
            maskBlur = maskBlur if (maskBlur % 2) == 1 else maskBlur + 1
            mosaicMask = cv2.blur(mosaicMask, (maskBlur, maskBlur))

        srcImg = np.array(srcImg)
        mosaicImg = np.array(mosaicImg)
        mosaicAlpha = np.dstack((mosaicMask,) * 3) / 255
        blendImg = srcImg * (1 - mosaicAlpha) + mosaicImg * mosaicAlpha

        dstPath = os.path.join(dstDir, os.path.basename(mosaic["path"]))
        cv2.imwrite(dstPath, blendImg.astype(np.uint8))
        # cv2.imwrite(dstPath, mosaicMask)
