# 簡単プロンプトアニメ

[AnimateDiff prompt travel](https://github.com/s9roll7/animatediff-cli-prompt-travel) を使って、ローカル PC で簡単に動画を生成する環境です。  
**<!--[[ 概要 ]() ]--> [[ Colab版 ](https://twitter.com/Zuntan03/status/1703674198101803268)]**  
[![title](./doc/img/title.webp)](https://yyy.wpx.jp/m/202309/KuronekoAkiba.mp4)

- プロンプトだけで FullHD 面積のスムーズな長尺動画を生成 (Geforce RTX 3060 12GB)
- インストール・2段アップスケール・フレームレート補間などが自動
	- 作例は生成設定ファイルを `Generate.bat` にドロップしただけです。
- [AnimateDiff prompt travel](https://github.com/s9roll7/animatediff-cli-prompt-travel) を利用していれば生成設定ファイルを流用可能

## サンプル

- 9/21: [KuronekoAkiba](https://yyy.wpx.jp/m/202309/KuronekoAkiba.mp4)
- 9/18: [nadenadesitai_v10](https://yyy.wpx.jp/m/202309/nadenadesitai_v10.mp4), [xxmix9realistic_v40](https://yyy.wpx.jp/m/202309/xxmix9realistic_v40.mp4), [onigiriMix_v10](https://yyy.wpx.jp/m/202309/onigiriMix_v10.mp4), [mistoonAnime_v20](https://yyy.wpx.jp/m/202309/mistoonAnime_v20.mp4)

## 動作環境

- Windows 10 PC
- 最近の NVIDIA Geforce RTX **VRAM 8BG 以上**
- パスを通した [Python 3.10.6](https://www.python.org/ftp/python/3.10.6/python-3.10.6-amd64.exe) と [Git for Windows](https://gitforwindows.org/)

## インストール

1. [Setup-EasyPromptAnime.bat](https://github.com/Zuntan03/EasyPromptAnime/raw/main/src/Setup-EasyPromptAnime.bat) を **右クリックから「名前をつけてリンク先を保存…」** でインストール先のフォルダ（英数字のみの浅いパス）にダウンロードして実行します。
	- **「WindowsによってPCが保護されました」と表示されたら、「詳細表示」から「実行」します。**  
2. インストールが終わると、Google Colabでプロンプト編集用の「[簡単プロンプトアニメエディタ](https://colab.research.google.com/drive/1XeVRMmw-dyALMacKU-_Xj2nMboZL_TM3)」が立ち上がります。

- [Civitai](https://civitai.com) がダウンしているとインストールに失敗する可能性があります。
	- インストールに失敗しているようでしたら、間をおいて `src/Setup.bat` を再実行してください。

## つかい方

とりあえず長尺アニメ (12秒 120コマ 672x768) を生成してみたい方は、`sample/UpscaleGacha.bat` を実行してみてください(RTX 3060 で約 15分)。

1. `OpenClabEditor.bat` で「[簡単プロンプトアニメエディタ](https://colab.research.google.com/drive/1XeVRMmw-dyALMacKU-_Xj2nMboZL_TM3)」を開きます。
2. ひとつめの`▶`を押してプロンプト入力欄を表示し、プロンプトやパラメータを編集して、ふたつめの`▶`を押すと動画生成用の生成設定ファイル (*.json) をダウンロードします。
3. 生成設定ファイルを `Generate.bat` にドラッグ＆ドロップすると、生成設定ファイルの場所に動画を生成します。
	- 生成した動画とフレームレート補間した動画と再エンコードした動画を生成します。

## FAQ

- 「[簡単プロンプトアニメエディタ](https://colab.research.google.com/drive/1XeVRMmw-dyALMacKU-_Xj2nMboZL_TM3)」の初期値や選択肢を変えたい
	- Colab のメニュー `ファイル - ドライブにコピーを保存` して、一番下の `コードを表示` から該当部分を編集します。
- モデルを追加したい
	- `animatediff-cli-prompt-travel/data/models/sd/` にモデルを置きます。
		- [stable-diffusion-model-toolkit](https://github.com/arenasys/stable-diffusion-webui-model-toolkit) などで VAE をモデルに埋め込んでください。
	- Colab ソースの `model_name = "nadenadesitai_v10" # @param ["mistoonAnime_v20", "nadenadesitai_v10", "onigiriMix_v10", "xxmix9realistic_v40", "Custom"]` を書き換えます。
- モーションモジュールを追加したい
	- `animatediff-cli-prompt-travel/data/models/motion-module/` にモーションモジュールを置きます。
	- Colab ソースの `motion_module = "mm_sd_v15_v2.ckpt" # @param ["mm_sd_v15_v2.ckpt", "mm_sd_v15.ckpt", "mm_sd_v14.ckpt"]` を書き換えます。
- LoRA を使いたい
	- `animatediff-cli-prompt-travel/data/lora/` に LoRA を置きます。
		- 使える LoRA は通常の LierLa 形式で、C3Lier(Locon) 以降は使えないっぽいです。
	- LoRA の読み込みは、プロンプトエディタの `L:` で始める行で指定します。
- TI を使いたい
	- `animatediff-cli-prompt-travel/data/embeddings/` に TI を置きます。
- ControlNet を使いたい
	- [AnimateDiff prompt travel](https://github.com/s9roll7/animatediff-cli-prompt-travel) がそのまま動作していますので、生成設定ファイルを手書きすれば使えます。
	- そのうち対応するかも？
- Refine がメモリ不足で落ちる
	- context を半分にしていますが、落ちますね。
	- 初回のアップスケールで解像度を抑えつつ Refine を使用、とかもできましたが、重い印象でした。
- Colabで編集する意味ある？
	- ありません。「[Colab版簡単プロンプトアニメ](https://colab.research.google.com/drive/1QVxBjAamxOIAAlSohQklZltRPx8WsxEN)」のコードを流用しただけなので、利用者が多そうだったらローカルエディタを用意する、かも。

## 各ツールの説明

- `OpenColabEditor.bat`
	- 「[簡単プロンプトアニメエディタ](https://colab.research.google.com/drive/1XeVRMmw-dyALMacKU-_Xj2nMboZL_TM3)」を開きます。
- `Generate.bat`
	- 生成設定ファイルをドラッグ＆ドロップすると、動画を生成します。
- `GenerateForever.bat`
	- 生成設定ファイルをドラッグ＆ドロップすると、動画を生成し続けます。終了時は `Ctrl+C` で止めてください。
- `Update.bat`
	- 簡単プロンプトアニメを更新します。
- `FpsX8.bat`, `FpsX8Fps60.bat`
	- mp4 をドラッグ＆ドロップすると、[RIFE](https://github.com/megvii-research/ECCV2022-RIFE/tree/main) で FPS を8倍にします。サイズが大きいので再エンコード版も生成します。`FpsX8Fps60.bat` は再エンコード時に 60FPS化します。
- `Frames2Mp4.bat`
	- Tile アップスケールは mp4 を生成しませんが、`animatediff-cli-prompt-travel\upscaled` にある連番 png が入っているフォルダをドラッグ＆ドロップすると、mp4 を生成します。

## [AnimateDiff prompt travel](https://github.com/s9roll7/animatediff-cli-prompt-travel) 利用者向け情報

既存のコンフィグファイルのファイル名にオプションを指定することで、`Generate.bat` が色々やってくれます。  
ハイフン(`-`)は引数の指定に使用するため、ファイル名には使えません。

例） `Config-L30-C16-W448-H544-T1088-T1632.json` を `Generate.bat` にドロップ
1. `animediff generate -L 30 -C 16 -W 448 -H544`
2. `animediff tile-upscale -H 1088` から ffmpeg で mp4 生成
	- `-R` なら `animediff refine -C (context / 2)`
3. `animediff tile-upscale -H 1632` から ffmpeg で mp4 生成
4. [RIFE](https://github.com/megvii-research/ECCV2022-RIFE/tree/main) でフレーム補間

## 参照

- [AnimateDiff prompt travel](https://github.com/s9roll7/animatediff-cli-prompt-travel) 
- [Codex FFmpeg](https://github.com/GyanD/codexffmpeg)
- [Real-Time Intermediate Flow Estimation for Video Frame Interpolation](https://github.com/megvii-research/ECCV2022-RIFE)

# ライセンス

このリポジトリのスクリプトやドキュメントは、[MIT License](./LICENSE.txt)です。

This software is released under the MIT License, see [LICENSE.txt](./LICENSE.txt).
