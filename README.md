# 簡単プロンプトアニメ

[AnimateDiff prompt travel](https://github.com/s9roll7/animatediff-cli-prompt-travel) を使って、ローカル PC で簡単に動画を生成する環境です。  
**[[ 概要 ](https://twitter.com/Zuntan03/status/1704807854384066714) ] [[ Colab版（無料アカ不可） ](https://twitter.com/Zuntan03/status/1703674198101803268)]**  
[![title](./doc/img/title.webp)](https://yyy.wpx.jp/m/202309/KuronekoAkiba.mp4)

- プロンプトだけで FullHD のスムーズな長尺動画を生成
- セットアップ・2段アップスケール・フレームレート補間などが自動
- [AnimateDiff prompt travel](https://github.com/s9roll7/animatediff-cli-prompt-travel) の生成設定ファイルを流用可能

## 作例

- 利用者の人気つぶやき: 
[@Yokohara_h](https://twitter.com/Yokohara_h/status/1705981094473183699)
[@PhotogenicWeekE](https://twitter.com/PhotogenicWeekE/status/1705175475176530146)
[@cigmatari](https://twitter.com/cigmatari/status/1705225865356009612)
[@hirochuu8](https://twitter.com/hirochuu8/status/1706851109502128256)
[@ai_cute_girls](https://twitter.com/ai_cute_girls/status/1707632810599895112)
[@airi_wakui](https://twitter.com/airi_wakui/status/1709009440861782364)
[@hina_chocoboo13](https://twitter.com/hina_chocoboo13/status/1708354881143337268)
[@ai_cute_girls](https://twitter.com/ai_cute_girls/status/1707400802715984163)
[@aiko_ai_ai](https://twitter.com/aiko_ai_ai/status/1709127397159649375)
[@ai_cute_girls](https://twitter.com/ai_cute_girls/status/1712243339922461046)
[@hina_chocoboo13](https://twitter.com/hina_chocoboo13/status/1705213931466485813)
- 利用者の HowTo 記事:
[@samoHKP](https://twitter.com/samoHKP/status/1710769467142107327)
[@towya_aillust](https://twitter.com/towya_aillust/status/1707527055905267718)
[動画1](https://www.youtube.com/watch?v=qjPmAPyKSYY)
[動画2](https://www.youtube.com/watch?v=mHFBRXA1z58)
[taziku](https://www.youtube.com/shorts/Lq7kyWEhh3Q)
[1](https://taziku.co.jp/blog/easypromptanime-install)
[2](https://taziku.co.jp/blog/easypromptanimeai-c)
[3](https://taziku.co.jp/blog/easypromptanime-prompt)
[4](https://taziku.co.jp/blog/easypromptanime-model)
[5](https://taziku.co.jp/blog/easypromptanime-0)
[@nobu00740](https://twitter.com/nobu00740/status/1710911068648952299)
[@zono_0](https://qiita.com/zono_0/items/0f9b63f0b581721f01d9)
[@TakaWeekendProg](https://twitter.com/TakaWeekendProg/status/1705938614033801547)
[@miyukin_sj](https://twitter.com/miyukin_sj/status/1706966588061348243)
- 9/27: [AnimateDiff prompt travel のふたつのアニメと新機能 prompt_fixed_ratio](https://twitter.com/Zuntan03/status/1707323168707555329)
- 9/26: [実はプロンプトをアニメーションしなくてもいいんです](https://twitter.com/Zuntan03/status/1706602454476095701) の [きれいな動画](https://yyy.wpx.jp/m/202309/Oiyami.mp4)
- 9/25: [AnimateDiff prompt travelの更新比較](https://twitter.com/Zuntan03/status/1706246410851819836) の [きれいな動画](https://yyy.wpx.jp/m/202309/PromptTravelUpdateXxMix.mp4)
- 9/24: [モデルへの VAE 組み込み有無比較](https://twitter.com/Zuntan03/status/1705779826056147188) の [きれいな動画](https://yyy.wpx.jp/m/202309/ModelVae-crf26.mp4)
- 9/23: [motion-moduleのmm_sd_v15_v2とmm-Stabilized_high比較](https://twitter.com/Zuntan03/status/1705537060491432132) の [FullHD 超え動画](https://yyy.wpx.jp/m/202309/V152HighGrid.mp4)
- 9/21: FullHD 相当 [KuronekoAkiba](https://yyy.wpx.jp/m/202309/KuronekoAkiba.mp4)
- 9/18: [nadenadesitai_v10](https://yyy.wpx.jp/m/202309/nadenadesitai_v10.mp4), [xxmix9realistic_v40](https://yyy.wpx.jp/m/202309/xxmix9realistic_v40.mp4), [onigiriMix_v10](https://yyy.wpx.jp/m/202309/onigiriMix_v10.mp4), [mistoonAnime_v20](https://yyy.wpx.jp/m/202309/mistoonAnime_v20.mp4)
- 利用者のつぶやき（気づいたもののみ）:
[@llrinnell](https://twitter.com/llrinnell/status/1703711755128779226)
[@ai_gene_fumo7](https://twitter.com/ai_gene_fumo7/status/1704116905299382547)
[@moshimur](https://twitter.com/moshimur/status/1704322583095812332)
[@mouriAIart](https://twitter.com/mouriAIart/status/1704986700358013430)
[@katarina7410](https://twitter.com/katarina7410/status/1705152174471463009)
[@safa_dayo](https://twitter.com/safa_dayo/status/1705183157920616482)
[@keythpiece](https://twitter.com/keythpiece/status/1705605784091193717)
[@TakaWeekendProg](https://twitter.com/TakaWeekendProg/status/1705745532424233372)
[@llrinnell](https://twitter.com/llrinnell/status/1705898369586212877)
[@toki_mwc](https://twitter.com/toki_mwc/status/1705929754455794159)
[@towya_aillust](https://twitter.com/towya_aillust/status/1705957586636513745)
[@aicocoa982](https://twitter.com/aicocoa982/status/1705323937826304461)
[@Lover57227277](https://twitter.com/Lover57227277/status/1706000986509361201)
[@julajp](https://twitter.com/julajp/status/1706031579876012182)
[@towya_aillust](https://twitter.com/towya_aillust/status/1706280379454464103)
[@PhotogenicWeekE](https://twitter.com/PhotogenicWeekE/status/1706257379644572109)
[@Aki_AI2023](https://twitter.com/Aki_AI2023/status/1706626610273882397)
[@RAN_kimono_jp](https://twitter.com/RAN_kimono_jp/status/1706521498712945129)
[@MultusDim_AI](https://twitter.com/MultusDim_AI/status/1706645709011988925)
[@KO_ISZ](https://twitter.com/KO_ISZ/status/1706660431169982611)
[@Neosuchiai](https://twitter.com/Neosuchiai/status/1706906692401967551)
[@Masa_8823](https://twitter.com/Masa_8823/status/1706606068959494262)
[@hanpen_ai](https://twitter.com/hanpen_ai/status/1706176389551128874)
[@mogiken](https://twitter.com/mogiken/status/1705827822953263302)
[@PlayShingo](https://twitter.com/PlayShingo/status/1705356415194509634)
[@toki_mwc](https://twitter.com/toki_mwc/status/1706100234911392195)
[@AIbijo202304](https://twitter.com/AIbijo202304/status/1707591275590152219)
[@AudioReplayApp](https://twitter.com/AudioReplayApp/status/1707626067601883630)
[@toki_mwc](https://twitter.com/toki_mwc/status/1707609978738188599)
[@Masa_8823](https://twitter.com/Masa_8823/status/1707688665173176767)
[@mouriAIart](https://twitter.com/mouriAIart/status/1707668976262889656)
[@taziku_co](https://twitter.com/taziku_co/status/1707773693534130231)
[@ai_succubus](https://twitter.com/ai_succubus/status/1707795330836857281)
[@nanaynyorai](https://twitter.com/nanaynyorai/status/1707815227205849466)
[@towya_aillust](https://twitter.com/towya_aillust/status/1707784177607995832)
[@AiMu_Tech](https://twitter.com/AiMu_Tech/status/1707874139477074064)
[@ai_nontan_room](https://twitter.com/ai_nontan_room/status/1708122189835497602)
[@KOR_jiyugiga](https://twitter.com/KOR_jiyugiga/status/1708104597221552497)
[@aiojisan1234](https://twitter.com/aiojisan1234/status/1708147886041817223)
[@Lover57227277](https://twitter.com/Lover57227277/status/1708085311631397007)
[@AI_Lilith](https://twitter.com/AI_Lilith/status/1708144977627460000)
[@foxyy4i](https://twitter.com/foxyy4i/status/1708169197740818574)
[@a_i_art_girl](https://twitter.com/a_i_art_girl/status/1708058379707662374)
[@towya_aillust](https://twitter.com/towya_aillust/status/1708489618986082478)
[@yimamura](https://twitter.com/yimamura/status/1706560200734589207)
[@ai_nontan_room](https://twitter.com/ai_nontan_room/status/1708698807075266759)
[@yimamura](https://twitter.com/yimamura/status/1708744498782904828)
[@eiai_picfactory](https://twitter.com/eiai_picfactory/status/1708833306316562555)
[@zAIwrd_SFW](https://twitter.com/zAIwrd_SFW/status/1708861356827656222)
[@zono_0](https://twitter.com/zono_0/status/1709139526483087526)
[@towya_aillust](https://twitter.com/towya_aillust/status/1709244202264170774)
[@acloza_bot](https://twitter.com/acloza_bot/status/1709225174523068829)
[@zono_0](https://twitter.com/zono_0/status/1709178123051483136)
[@shinshin86](https://twitter.com/shinshin86/status/1709324698599969112)
[@vvf162c1](https://twitter.com/vvf162c1/status/1709166818898977146)
[@vvf162c1](https://twitter.com/vvf162c1/status/1709916173205418002)
[@mouriAIart](https://twitter.com/mouriAIart/status/1709840100153278502)
[@aicocoa982](https://twitter.com/aicocoa982/status/1710584766981165106)
[@tiyorin0924](https://twitter.com/tiyorin0924/status/1710622890369204296)
[@katarina7410](https://twitter.com/katarina7410/status/1710994031260709334)
[@FUKUAILabo](https://twitter.com/FUKUAILabo/status/1711489205660975329)
[@Rakhsh_](https://twitter.com/Rakhsh_/status/1711434624705102255)
[@julajp](https://twitter.com/julajp/status/1711720270061572306)
[@PlayShingo](https://twitter.com/PlayShingo/status/1710585195731247134)
[@ezakiairi](https://twitter.com/ezakiairi/status/1710647631448613208)
[@mouriAIart](https://twitter.com/mouriAIart/status/1710911353618370759)
[@kura_starwing](https://twitter.com/kura_starwing/status/1711626392297976257)
[@777_shinta](https://twitter.com/777_shinta/status/1711349591424311300)
[@Masa_8823](https://twitter.com/Masa_8823/status/1711557781357289670)
[@roiyaruRIZ](https://twitter.com/roiyaruRIZ/status/1711674005701423571)
[@aikoujp](https://twitter.com/aikoujp/status/1711668138281168931)
[@PlayShingo](https://twitter.com/PlayShingo/status/1711696881091567673)
[@ryoheiplus](https://twitter.com/ryoheiplus/status/1712774074664091727)
[@iriomotebox](https://twitter.com/iriomotebox/status/1711959604807283074)
[@koichi_business](https://twitter.com/koichi_business/status/1712392392907854207)
[@Neosuchiai](https://twitter.com/Neosuchiai/status/1712286175988416876)
[@sky252510](https://twitter.com/sky252510/status/1711943866520371522)

## 主な更新履歴

- 2023/10/14
	- `ダウンロード` メニューの `LoRA` に汎用的な LoRA を追加しました。
	- `設定` メニューに `現在のプロンプトを起動時のプロンプトにする` と `現在の設定を起動時の設定にする` と `ライト/ダークモードの切り替え（再起動後に適用）` を追加しました。
- 2023/10/12
	- プロンプト入力欄で `元に戻す(Ctrl+Z)` , `やり直し(Ctrl+Y)` を使えるようにしました。
	- `ダウンロード` メニューの項目を充実しました。
- 2023/10/10
	- `ツール` メニューの `使えない LoRA を使えるように変換` でこれまで使えなかった LoRA が使える場合があります。
	- `アニメ` メニューのアップスケールで、アニメ生成とアップスケールを別々に実行できます。
		- 生成と同じオプションでアプスケする `生成時の設定で初回アップスケール` と、エディタの設定を適用して色々変更できる `現在の設定で初回アップスケール` です。
		- 黒画面への対処や、モデルやLoRAパラメータを変えてのアップスケールができます。
		- これに合わせてタイルアップスケールの強度と開始と終了を設定できるようにしました。
	- `IPアダプタ` で[生成時に画像をプロンプトとして使えます](https://www.google.com/search?q=ip-adapter)。
		- プロンプトとして使いたい画像をフォルダにまとめ、ファイル名で 010.png などとフレーム数を指定する必要があります。
	- `ダウンロード` からモデルやモーションモジュールなどをダウンロードできます。
		- おすすめのものがあれば教えてください。
- 2023/10/09
	- ローカル版エディタをα版としてひっそり公開しました。
		- `EasyPromptAnimeEditor.bat` で起動します。
		- α版なのでドキュメントはまだありません。
		- Colab 版エディタは廃止予定です。
	- セットアップの仕組みを大幅に変更して、最初にダウンロードするファイルの量を大幅に減らしました。
		- ローカル版エディタの「ダウンロード」メニューでダウンロードできます。
		- これまでインストールできていたのに、再インストールしても動かない場合は知らせてください。
- 2023/09/29
	- フォルダ内の生成設定ファイルで一通り生成する `GenerateFolder.bat` と、これを連続生成し続ける `GenerateFolderForever.bat` を追加しました。
- 2023/09/28
	- 昨日の「インストール時のエラーチェックを強化しました。」に問題があり、インストールできなかった不具合を修正しました。
		- [Setup-EasyPromptAnime.bat](https://github.com/Zuntan03/EasyPromptAnime/raw/main/src/Setup-EasyPromptAnime.bat?20230928) を再ダウンロードして、インストールしてください。
	- animatediff のコマンドでエラーが発生した際に、処理を終了するようにしました。
		- GenerateForever.exe も同様に、処理を終了するようにしました。
- 2023/09/27
	- インストール時のエラーチェックを強化しました。
	- 0~9時に生成した際に、動画ファイル名の時間部分をゼロパディングするようにしました。
	- モデルファイルなどのシンボリックリンクを削除しないようにしました。
- 2023/09/26
	- サンプルに『[美味しいヤミー感謝感謝](https://www.google.com/search?q=%E7%BE%8E%E5%91%B3%E3%81%97%E3%81%84%E3%83%A4%E3%83%9F%E3%83%BC%E6%84%9F%E8%AC%9D%E6%84%9F%E8%AC%9D)』の `sample/Oiyami.bat` を追加しました。
- 2023/09/25
	- FFmpeg のインストールに失敗する不具合を修正しました。
		- `Update.bat` を実行すると修正します。
- 2023/09/24
	- **今回の更新では `Update.bat` を 2回！実行してください（`Update.bat` を更新したため）。**
	- [AnimateDiff prompt travel](https://github.com/s9roll7/animatediff-cli-prompt-travel) の更新に対応しました。
		- AnimateDiff 用にモデルを修正する `FixCheckpoint.bat` を追加しました。<br>
		が、手元で利用しているモデルは修正不要でした。
	- 生成した動画のサイズを低減する `Mp4Crf(26|32|38)` を追加しました。
	- 生成した動画から X(Twitter) 投稿用の動画を生成する `XMp4*.bat` を追加しました。
- 2023/09/23
	- 生成する動画のデフォルトの FPS を、様々なサービスとの互換性の観点から 40FPS にしました。
		- 生成設定ファイル名に `-D3` を付け足すと、以前と同様に 80FPS になります。
		- FPS 指定の詳細は [ファイル名オプション一覧](#ファイル名オプション一覧) や `FpsX4.bat` の説明を参照してください。
	- 生成した mp4 ファイル名に、日時のプレフィックスを追加するようにしました。
		- 同一シードで生成しても、mp4 ファイルを上書きしなくなります。
- 2023/09/22
	- motion-module に mm-Stabilized_high.pth と mm-Stabilized_mid.pth を追加しました。
		- `Update.bat` を実行するとダウンロードします。
	- 同一シードで同じフォルダに再出力した際に、正しくフレーム補間されない不具合を修正しました。
		- インストール済みの方は `Update.bat` を実行してください。
	- インストーラーで `C:\Windows\System32` にパスが通っていない場合にエラー扱いにしました。
- 2023/09/21
	- 公開

## 動作環境

- Windows 10 以降（Update済み、管理者権限あり）の PC で、/Windows/System32 にパスが通っている
- 最近の NVIDIA Geforce RTX **VRAM 8BG 以上**
- パスを通した [Python 3.10.6](https://www.python.org/ftp/python/3.10.6/python-3.10.6-amd64.exe) と [Git for Windows](https://gitforwindows.org/)

## セットアップ

**ウィルスチェックソフトの Avast の保護が有効だと、インストールに失敗します。<br>初回の動画生成の成功まで一時的に保護を無効にするか、他のウィルスチェックソフトをご利用ください。**

**Stable Diffusion web UI や ComfyUI は終了した状態で、セットアップしてください。**

1. 動作環境の [Python 3.10.6](https://www.python.org/ftp/python/3.10.6/python-3.10.6-amd64.exe) を導入していない場合は、[Python のインストール](https://github.com/Zuntan03/SdWebUiTutorial/blob/main/_/doc/SdWebUiInstall/SdWebUiInstall.md#python-%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB) をします。
2. 動作環境の [Git for Windows](https://gitforwindows.org/) を導入していない場合は、[Git for Windows のインストール](https://github.com/Zuntan03/SdWebUiTutorial/blob/main/_/doc/SdWebUiInstall/SdWebUiInstall.md#git-for-windows-%E3%81%AE%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB) をします。
2. [Civitai](https://civitai.com) がダウンしていないか確認します。
3. [Setup-EasyPromptAnime.bat](https://github.com/Zuntan03/EasyPromptAnime/raw/main/src/Setup-EasyPromptAnime.bat?20230928) を **右クリックから「名前をつけてリンク先を保存…」** でインストール先のフォルダ（英数字のみの浅いパス、 **スペース不可**）にダウンロードして実行します。
	- **「WindowsによってPCが保護されました」と表示されたら、「詳細表示」から「実行」します。**  
4. インストールが終わると、Google Colabでプロンプト編集用の「[簡単プロンプトアニメエディタ](https://colab.research.google.com/drive/1XeVRMmw-dyALMacKU-_Xj2nMboZL_TM3)」が立ち上がります。

### セットアップ FAQ

- セットアップや更新で `curl: (35) schannel: next InitializeSecurityContext failed: Unknown error (0x00000000) - 失効の関数は証明書の失効を確認 できませんでした。` といったエラーが発生する
	- ネットワークのセキュリティチェックに失敗しています。
	- アンチウィルスソフトの Avast 有効時に発生し、無効にしたら問題なくインストールできたとの事例報告がありました。
- 動画の生成が一晩経っても終わらない、サンプル（`sample/UpscaleGacha.bat`、RTX 3060 で約 15分）の生成に長い時間が掛かる
	- [AI 画像生成の VRAM オフロード問題](https://www.google.com/search?q=%E7%94%BB%E5%83%8F%E7%94%9F%E6%88%90+VRAM%E3%82%AA%E3%83%95%E3%83%AD%E3%83%BC%E3%83%89%E5%95%8F%E9%A1%8C)を踏んでいる可能性がありますので、グラフィックスドライバのバージョンを確認してください。
- セットアップでダウンロードされるモデルで動画を正常に生成できない
	- モデルのダウンロードに失敗している場合がありますので、`animatediff-cli-prompt-travel/data/models/sd/` にある該当ファイルを削除し、`src/Setup.bat` で再ダウンロードしてください。

## 更新方法

簡単プロンプトアニメを更新するには、`Update.bat` を実行します。

## つかい方

12秒のアニメをとりあえず生成してみたい方は、`sample/UpscaleGacha.bat` を実行してみてください(RTX 3060 で約 15分)。

1. `OpenClabEditor.bat` で「[簡単プロンプトアニメエディタ](https://colab.research.google.com/drive/1XeVRMmw-dyALMacKU-_Xj2nMboZL_TM3)」を開きます。
2. ひとつめの`▶`を押してプロンプト入力欄を表示し、プロンプトやパラメータを編集して、ふたつめの`▶`を押すと動画生成用の生成設定ファイル (*.json) をダウンロードします。
3. 生成設定ファイルをインストール先([Setup-EasyPromptAnime.bat](https://github.com/Zuntan03/EasyPromptAnime/raw/main/src/Setup-EasyPromptAnime.bat) を実行したフォルダ)にある `Generate.bat` にドラッグ＆ドロップすると、生成設定ファイルの場所に動画を生成します。
	- 生成した動画とフレームレート補間した動画と再エンコードした動画を生成します。

## FAQ

### 効率的にシードガチャをしたい

- アップスケールを無効にしたり、アップスケールのサイズを下げたりすることで効率的にシードガチャができます。
- プロンプトをざっくり詰める段階なら、最初の生成解像度を下げたり、短時間にして先頭付近のキーフレームで検証するのも手です。

### ガチャ結果動画のシード値を知りたい

- mp4 ファイル名先頭の `日時(MMDD_HHMM_SS)-数値` の `数値` 部分がシードです。
- `animatediff-cli-prompt-travel/(output|upscaled|refine)/` 以下にある `prompt.json` でも確認できます。

### 真っ黒の動画が生成されてしまう

以下のいずれかの手順で、改善するかもしれません。

1. `FixCheckpoint.bat` でモデルを修正します。モデルが書き換わる可能性があります。
2. 生成設定ファイルのファイル名に `-V` を付け足します（改善報告あり）。
3. [モデルの VAE を差し替え](#stable-diffusion-model-toolkit-によるモデルへの-vae-埋め込み方法)ます。
4. 生成設定ファイルのファイル名に `-X` を付け足します（未検証、`-V`, `-v`, `-x` との併用も）。
5. 別のモデルを使います。

### 「[簡単プロンプトアニメエディタ](https://colab.research.google.com/drive/1XeVRMmw-dyALMacKU-_Xj2nMboZL_TM3)」の初期値や選択肢を変えたい
- Colab のメニュー `ファイル - ドライブにコピーを保存` して、一番下の `コードを表示` から該当部分を編集します。

### モデルを追加したい

1. `FixCheckpoint.bat` でモデルを修正します。モデルが書き換わる可能性があります。
2. `animatediff-cli-prompt-travel/data/models/sd/` にモデルを置きます。
	- **[！注意！] [stable-diffusion-model-toolkit](https://github.com/arenasys/stable-diffusion-webui-model-toolkit) などで、[モデルに VAE を埋め込んでください](#stable-diffusion-model-toolkit-によるモデルへの-vae-埋め込み方法)。** <br>
	モデルに VAE を埋め込まないと、[このようになる](https://twitter.com/Zuntan03/status/1705779826056147188) 場合があります。
3. Colab ソースの `model_name = "nadenadesitai_v10" # @param [...]` の `...` を書き換えます。

AnimateDiff とモデルに相性があり、[黒画像になる](#真っ黒の動画が生成されてしまう)、あまりアニメーションしない、といった場合があります。

#### [stable-diffusion-model-toolkit](https://github.com/arenasys/stable-diffusion-webui-model-toolkit) によるモデルへの VAE 埋め込み方法

1. [Stable Diffusion web UI](https://github.com/AUTOMATIC1111/stable-diffusion-webui) に [stable-diffusion-model-toolkit](https://github.com/arenasys/stable-diffusion-webui-model-toolkit) をインストールします。
2. Stable Diffusion web UI の `Toolkit` タブで `リフレッシュ` してから `入力` で VAE を埋め込むモデルを選択して `読み込み` ます。
3. `高度な設定`	に移り、`Component - Class` から `VAE-v1` を選択します。
4. `実行 - ファイル` で埋め込む VAE を選択して `Import` します。
5. `名前` で VAE を埋め込んだモデルのファイル名を指定して `保存` で、モデルフォルダに VAE を埋め込んだモデルが保存されます。
6. `animatediff-cli-prompt-travel/data/models/sd/` に VAE を埋め込んだモデルを移動します。

### モーションモジュールを追加したい
1. `animatediff-cli-prompt-travel/data/models/motion-module/` にモーションモジュールを置きます。
2. Colab ソースの `motion_module = "mm_sd_v15_v2.ckpt" # @param [...]` の `...` を書き換えます。

### LoRA を使いたい
- `animatediff-cli-prompt-travel/data/lora/` に LoRA を置きます。
	- 使える LoRA は通常の LierLa 形式で、C3Lier(Locon) 以降は使えないっぽいです。
- LoRA の読み込みは、プロンプトエディタの `L:` で始める行で指定します。

### TI を使いたい
- `animatediff-cli-prompt-travel/data/embeddings/` に TI を置きます。

### ControlNet を使いたい
- [AnimateDiff prompt travel](https://github.com/s9roll7/animatediff-cli-prompt-travel) がそのまま動作していますので、生成設定ファイルを手書きすれば使えます。
- そのうち対応するかも？

### Widlcard を使いたい

- `animatediff-cli-prompt-travel/wildcards/` にワイルドカードを置きます。

### Refine がメモリ不足で落ちる
- context を半分にしていますが、落ちますね。
- 初回のアップスケールで解像度を抑えつつ Refine を使用、とかもできましたが、重い印象でした。

### ストレージ容量が足りない
- まずは [WizTree](https://forest.watch.impress.co.jp/library/software/wiztree/) で状況を確認してください。それでもストレージ容量が足りなかったら、買ってください。

### Colabで編集する意味ある？
- ありません。「[Colab版簡単プロンプトアニメ](https://colab.research.google.com/drive/1QVxBjAamxOIAAlSohQklZltRPx8WsxEN)」のコードを流用しただけなので、利用者が多そうだったらローカルエディタを用意する、かも。

## 各ツールの説明

### `OpenColabEditor.bat`

「[簡単プロンプトアニメエディタ](https://colab.research.google.com/drive/1XeVRMmw-dyALMacKU-_Xj2nMboZL_TM3)」を開きます。

### `Generate.bat`

生成設定ファイルをドラッグ＆ドロップすると、動画を生成します。

### `GenerateForever.bat`

生成設定ファイルをドラッグ＆ドロップすると、動画を生成し続けます。終了時は `Ctrl+C` で止めてください。

### `GenerateFolder.bat`

生成設定ファイルが入っているフォルダをドラッグ＆ドロップすると、生成設定ファイルの数だけ動画を生成します。

### `GenerateFolder.bat`

生成設定ファイルが入っているフォルダをドラッグ＆ドロップすると、生成設定ファイルの数だけ動画を生成し続けます。終了時は `Ctrl+C` で止めてください。

### `Update.bat`

簡単プロンプトアニメと [AnimateDiff prompt travel](https://github.com/s9roll7/animatediff-cli-prompt-travel) を更新します。

### `FixCheckpoint.bat`

 モデルをドラッグ＆ドロップすると、モデルに問題があれば AnimateDiff 用に修正します。モデルが書き換わったかどうかは更新日時で確認してください。

### `FpsX4.bat`

mp4 をドラッグ＆ドロップすると、[RIFE](https://github.com/megvii-research/ECCV2022-RIFE/tree/main) で FPS を4倍にします。サイズが大きくなるので再エンコード版も生成します。

- 第 2 引数に RIFE による中割りの分割回数（FPSの倍増を何回実施するかの）を指定できます。FPSが 1 なら 2倍、2 なら 4倍、3 なら 8倍、4 なら 16倍になります。未指定や 0 なら 2 になります。
- 第 3 引数に RIFE の分割後の FPS を指定できます。 **この FPS 指定では画像の枚数を変更せずに FPS を適用しますので、アニメーションの速度と長さが変わります。** 1秒の 10FPS の動画を RIFE で 4倍にして 40枚の画像がある状態で、第三引数で 60FPS を指定すると、アニメーションが早くなり 0.66秒で再生が終わります。逆に 8倍で80枚にして 60FPS を指定した場合は、ゆっくり再生されて 1.33秒で再生が終わります。0 なら未指定です。
- 第 4 引数で FFmpeg による再エンコード時の FPS を指定できます。再生速度や動画の長さは変わりません。0 なら未指定です。
- 第 5 引数で FFmpeg による再エンコード時の crf を指定できます。未指定や 0 なら 20 になります。

### `Frames2Mp4.bat`

Tile アップスケールは mp4 を生成しませんが、`animatediff-cli-prompt-travel\upscaled` にある連番 png が入っているフォルダをドラッグ＆ドロップすると、mp4 を生成します。

### `DeleteOutput.bat`

ストレージ容量を消費しがちな `animatediff-cli-prompt-travel/` の `output/*/`, `upscaled/*/`, `refine/*/` を削除します。

### `Mp4Crf26.bat`, `Mp4Crf32.bat`, `Mp4Crf38.bat`

mp4 をドラッグ＆ドロップすると、Crf26 で 1/2、Crf32 で 1/4、Crf38 で 1/8 ぐらいのサイズの mp4 に変換します。

### `XMp4.bat`, `XMp4W1920.bat`, `XMp4W1200.bat`, `XMp4H1900.bat`, `XMp4H1200.bat`

mp4 をドラッグ＆ドロップすると X(Twitter) アップロード用の動画(40FPS, 25Mbps)を生成します。<br>
アップロード時に再エンコードされる前提ですので、省サイズではありません。

- [Xで動画を共有および視聴する方法](https://help.twitter.com/ja/using-x/x-videos#:~:text=%E3%83%96%E3%83%A9%E3%82%A6%E3%82%B6%E3%81%8B%E3%82%89%E3%82%A2%E3%83%83%E3%83%97%E3%83%AD%E3%83%BC%E3%83%89%E3%81%A7%E3%81%8D%E3%82%8B%E5%8B%95%E7%94%BB%E3%81%AE%E8%A7%A3%E5%83%8F%E5%BA%A6%E3%81%A8%E7%B8%A6%E6%A8%AA%E6%AF%94%E3%82%92%E6%95%99%E3%81%88%E3%81%A6%E3%81%8F%E3%81%A0%E3%81%95%E3%81%84%E3%80%82)
- 動画の大きさが W1920 x H1200 か W1200 x H1900 に収まらない場合は、`XMp4W1920.bat`, `XMp4W1200.bat`, `XMp4H1900.bat`, `XMp4H1200.bat` を使用して、W1920 x H1200 か W1200 x H1900 に収まるように縮小します。
- mp4 ファイル名の末尾が `*-D2e.mp4` な再エンコード後の mp4 でなく、`*-D2.mp4` な再エンコード前の mp4 から生成したほうが、品質が高くなります。

## [AnimateDiff prompt travel](https://github.com/s9roll7/animatediff-cli-prompt-travel) 利用者向け情報

既存のコンフィグファイルのファイル名にオプションを指定することで、`Generate.bat` が色々やってくれます。  
ハイフン(`-`)は引数の指定に使用するため、ファイル名には使えません。

例） `Config-L30-C16-W448-H544-T1088-T1632.json` を `Generate.bat` にドロップ
1. `animediff generate -L 30 -C 16 -W 448 -H544`
2. `animediff tile-upscale -H 1088` から FFmpeg で mp4 生成
	- `-R` なら `animediff refine -C (context / 2)`
3. `animediff tile-upscale -H 1632` から FFmpeg で mp4 生成
4. [RIFE](https://github.com/megvii-research/ECCV2022-RIFE/tree/main) でフレーム補間

### ファイル名オプション一覧

|キー|デフォルト値|説明|
|---:|---:|----|
|L|30|動画のフレーム総数を指定します。|
|C|16|AnimeDiffのコンテキスト長を指定します。|
|W|384|動画の幅を指定します。|
|H|512|動画の高さを指定します。|
|T|-|Tile アップスケール後の動画の高さを指定します。2回指定できます。|
|R|-|Refine アップスケール後の動画の高さを指定します。2回指定できます。|
|D|2|RIFE による中割りの分割回数を指定します。`FpsX4.bat` の第 2 引数説明参照。|
|I|0|RIFE による中割り後の FPS を指定します。`FpsX4.bat` の第 3 引数説明参照。|
|F|0|FFmpeg で mp4 に変換する際の FPS を指定します。`FpsX4.bat` の第 4 引数説明参照。|
|M|20|FFmpeg で mp4 に変換する際の crf を指定します。`FpsX4.bat` の第 5 引数説明参照。|
|U|10|Tile アップスケール後の画像を MP4 にする際のFPSを指定します。|
|v|-|動画の生成で half-vae を有効にします。|
|V|-|動画のアップスケールで half-vae を有効にします。|
|x|-|動画の生成で xFormers を有効にします。|
|X|-|動画のアップスケールで xFormers を有効にします。|

## 参照

### ツール・ライブラリ

- [AnimateDiff prompt travel](https://github.com/s9roll7/animatediff-cli-prompt-travel)
- [Real-Time Intermediate Flow Estimation for Video Frame Interpolation](https://github.com/megvii-research/ECCV2022-RIFE)
- [sd-scripts](https://github.com/kohya-ss/sd-scripts)
- [Codex FFmpeg](https://github.com/GyanD/codexFFmpeg)

# ライセンス

このリポジトリのスクリプトやドキュメントは、[MIT License](./LICENSE.txt)です。

This software is released under the MIT License, see [LICENSE.txt](./LICENSE.txt).
