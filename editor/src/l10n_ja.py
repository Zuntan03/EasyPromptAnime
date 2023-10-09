l10nJa = {
    "lang": "ja",
    "error": "エラー",
    "sec": "秒",
    "title": "簡単プロンプトアニメ",
    "clear": "クリア",
    "negative_prompt": "ネガティブプロンプト",
    "swap": "入替",
    "generate_anime": "アニメ生成",
    "seed_gacha": "シードガチャ",
    "preview": "プレビュー",
    "preview_upscale": "アップスケール",
    # "preview_interpolation": "補間",
    "preview_start_frame": "プレビュー\n開始",
    "preview_length": "長さ 　\n",
    "task_forever": "連続実行",
    "task_pause_by_error": "エラーで一時停止",
    "preview_show_keyframe": "キーフレームを表示",
    "preview_show_header_footer": "ヘッダとフッタを表示",
    "preview_show_anime": "アニメを表示",
    "generate_length": "フレーム数\n{0:>8}秒",
    "generate_seed": "シード",
    "generate_model": "モデル",
    "generate_vae": "VAE",
    "generate_width": "幅",
    "generate_height": "高さ",
    "generate_motion_module": "モーション\nモジュール",
    "generate_context": "コンテキスト",
    "generate_scheduler": "スケジューラ",
    "generate_steps": "ステップ数",
    "generate_guidance_scale": "ガイダンススケール\n(CFG スケール)",
    "generate_clip_skip": "クリップ\nスキップ",
    "generate_prompt_fixed_ratio": "プロンプト\n固定割合",
    "generate_use_half_vae": "Half VAE を使用",
    "generate_use_x_formers": "xFormers を使用",
    "upscale1": "初回アップスケール",
    "upscale2": "二重アップスケール",
    "upscale_scale": "倍率",
    "upscale_scheduler": "スケジューラ",
    "upscale_steps": "ステップ数",
    "upscale_strength": "ノイズ除去強度",
    "upscale_guidance_scale": "ガイダンススケール\n(CFG スケール)",
    "upscale_use_half_vae": "Half VAE を使用（黒い画面出力の抑制事例あり）",
    "upscale_use_x_formers": "xFormers を使用",
    "preview_tab": "プレビュー",
    "basic_tab": "基本",
    "generate_tab": "生成",
    "upscale_tab": "アップスケール",
    "user_log_tab": "ユーザーログ",
    "system_log_tab": "システムログ",
    "m_file": "ファイル",
    "m_setting_file": "設定ファイル",
    "m_ini_file": "簡単プロンプトアニメの設定 ini ファイル",
    "m_default_prompt_file": "デフォルトのプロンプトファイル",
    "m_prompt_travel_template_file": "プロンプトトラベルのテンプレートファイル",
    "m_folder": "フォルダ",
    "m_output_folder": "アニメ出力先",
    "m_prompt_travel_folder": "プロンプトトラベル",
    "m_sd_model_folder": "モデル",
    "m_motion_module_folder": "モーションモジュール",
    "m_lora_folder": "LoRA",
    "m_embeddings_folder": "TI (Embedding)",
    "m_wildcard_folder": "ワイルドカード",
    "m_prompt_travel_output_folder": "プロンプトトラベル出力",
    "m_prompt_travel_generate_folder": "アニメ生成",
    "m_prompt_travel_tile_folder": "タイルアップスケール",
    "m_prompt_travel_refine_folder": "リファインアップスケール",
    "m_temp_folder": "テンポラリ",
    "m_log_folder": "ログ",
    "m_tool": "ツール",
    "m_tool_convert_lora": "LoRA 変換",
    "m_tool_easy_leco": "簡単LECO",
    "m_tool_easy_leco_url": "https://colab.research.google.com/drive/1LYi2kvZV1XN05MATqhqWs79cNdTkb33P",
    "m_download": "ダウンロード",
    "m_dl_model": "モデル",
    "m_dl_motion_module": "モーションモジュール",
    "m_dl_vae": "VAE",
    "m_dl_embedding": "TI (Embedding)",
    "m_help": "ヘルプ",
    "m_prompt_help": "プロンプトの書き方",
    "m_github": "簡単プロンプトアニメ GitHub",
    "m_reference": "参照",
    "dlg_convert_lora_title": "変換する LoRA を選択してください。",
    "log_initialization_end": "起動に掛かった時間: {0:.2f}秒",
    "log_task_start": "{0} を開始しました。",
    "log_task_success": "{0} に成功しました。 {1:.2f}秒",
    "log_task_failed": "{0} に失敗しました。 {1:.2f}秒\n[エラーで一時停止] を有効にして、エラーの内容を確認してください。",
    "log_ffplay": "シード値 {0} を再生します。\n再生設定は EasyPromptAnimeEditor.ini の ffplay_cmd で変更できます。",
    "log_convert_lora": "LoRA を dim:{0} で変換します。\n変換元 LoRA: {1}\n抽出用マージモデル: {2}\n出力先 LoRA: {3}",
    "log_start_download": "{0} のダウンロードを開始します。\n{1}",
    "err_inv_line": "行の表記が正しくありません。 {0}",
    "err_inv_frame_num": "フレームの値が正しくありません。{0}: {1}",
    "err_inv_lora_def": 'LoRA の定義が正しくありません。"{0}" {1}',
    "hlp_prompt": """
# フレーム数＋コロン(:)＋プロンプトで、アニメのキーフレームにプロンプトを指定します。
# フレーム数＋コロンではなく、「H:」「F:」「N:」「L:」の場合はアニメ全体に特別な設定をします。
# シャープ(#)以降はコメントです。

H: crowds, akihabara
# 「H:」か「h:」で始まる行はヘッダプロンプトの指定で、アニメのキーフレームのプロンプト先頭にヘッダプロンプトを足します。

 0: standing, upset
10: waving at viewer, surprised
20: waving at viewer, smile
# アニメの 0フレームに「standing, upset」、10フレームに「waving at viewer, surprised」、20フレームに「waving at viewer, smile」のプロンプトを使用します。
# 1秒間に 10枚の画像が表示され(10 Frame per second)で、キーフレームの間は補間されます。

F: 1girl, maid outfit
# 「F:」か「f:」で始まる行はフッタプロンプトの指定で、アニメのキーフレームのプロンプト末尾にフッタプロンプトを足します。

# 上記の指定で3秒間（30フレーム）生成した場合の、キーフレームのプロンプトは以下になります。
#  0フレーム「crowds, akihabara, standing, upset, 1girl, maid outfit」
# 10フレーム「crowds, akihabara, waving at viewer, surprised, 1girl, maid outfit」
# 20フレーム「crowds, akihabara, waving at viewer, smile, 1girl, maid outfit」
# 30フレーム「crowds, akihabara, standing, upset, 1girl, maid outfit」

# 細々とキーフレームを設定しなくとも、0フレームに「dancing」のような動きを表す言葉を入れておけば、AI が勝手に動かしてくれます。

N:(worst quality, low quality:1.4)
#「N:」か「n:」で始まる行は、アニメの全フレームで使用するネガティブプロンプトを指定します。

# L:explosion:-0.2 # 行頭の # でコメントになっています。LoRA を使う場合は先頭の # を消してください。
#「L:」か「l:」で始まる行は、LoRA のファイル名＋コロン(:)＋強度を、カンマ(,)区切りで複数指定できます。
# LoRAを使いたい場合は、メニューの [フォルダ - プロンプトトラベル - LoRA] に *.safetensors 形式の LoRA を置いてください。
# 使える LoRA は通常の LierLa 形式です。C3Lier(Locon) 形式はメニューの [ツール - LoRA 変換] で LierLa 形式に変換して利用できます。
""",
}
