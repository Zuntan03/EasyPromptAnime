l10nEn = {
    "lang": "en",
    "error": "Error",
    "sec": "s",
    "title": "EasyPromptAnime",
    "clear": "Clear",
    "negative_prompt": "Negative prompt",
    "swap": "Swap",
    "generate_anime": "Generate Anime",
    "seed_gacha": "Seed Gacha",
    "preview": "Preview",
    "preview_upscale": "Upscale",
    # "preview_interpolation": "Interpolation",
    "preview_start_frame": "Preview\nStart",
    "preview_length": "Length\n",
    "task_forever": "Forever",
    "task_pause_by_error": "Pause by error",
    "preview_show_keyframe": "Show keyframe",
    "preview_show_header_footer": "Show header & footer",
    "preview_show_anime": "Show anime",
    "generate_length": "Length\n{0:>7}s",
    "generate_seed": "Seed",
    "generate_model": "Model",
    "generate_vae": "VAE",
    "generate_width": "Width",
    "generate_height": "Height",
    "generate_motion_module": "Motion\nmodule",
    "generate_context": "Context",
    "generate_scheduler": "Scheduler",
    "generate_steps": "Steps",
    "generate_guidance_scale": "Guidance scale\n(CFG scale)",
    "generate_clip_skip": "Clip\nskip",
    "generate_prompt_fixed_ratio": "Prompt\nfixed ratio",
    "generate_use_half_vae": "Use Half VAE",
    "generate_use_x_formers": "Use xFormers",
    "upscale1": "1st upscale",
    "upscale2": "2nd upscale",
    "upscale_scale": "Scale",
    "upscale_scheduler": "Scheduler",
    "upscale_steps": "Steps",
    "upscale_guidance_scale": "Guidance scale\n(CFG scale)",
    "upscale_use_half_vae": "Use Half VAE",
    "upscale_use_x_formers": "Use xFormers",
    "upscale_strength": "Denoise strength",
    "preview_tab": "Preview",
    "basic_tab": "Basic",
    "generate_tab": "Generate",
    "upscale_tab": "Upscale",
    "user_log_tab": "User Log",
    "system_log_tab": "System Log",
    "m_file": "File",
    "m_setting_file": "Setting files",
    "m_ini_file": "EasyPromptAnimeEditor.ini",
    "m_default_prompt_file": "Default prompt file",
    "m_prompt_travel_template_file": "Prompt travel template file",
    "m_folder": "Folder",
    "m_output_folder": "Output",
    "m_prompt_travel_folder": "Prompt travel",
    "m_sd_model_folder": "Model",
    "m_motion_module_folder": "Motion module",
    "m_lora_folder": "LoRA",
    "m_embeddings_folder": "TI (Embedding)",
    "m_wildcard_folder": "Wildcard",
    "m_prompt_travel_output_folder": "Prompt travel output",
    "m_prompt_travel_generate_folder": "Generate",
    "m_prompt_travel_tile_folder": "Tile upscale",
    "m_prompt_travel_refine_folder": "Refine upscale",
    "m_temp_folder": "Temp",
    "m_log_folder": "Log",
    "m_tool": "Tools",
    "m_tool_convert_lora": "Convert LoRA",
    "m_tool_easy_leco": "EasyLECO",
    "m_tool_easy_leco_url": "https://colab.research.google.com/drive/1cEoOeLbGmzCK5dP-Xa6Yx0B53uS461J8",
    "m_download": "Download",
    "m_model_download": "Model",
    "m_help": "Help",
    "m_prompt_help": "How to write prompts",
    "m_github": "EasyPromptAnime GitHub",
    "m_reference": "Reference",
    "dlg_convert_lora_title": "Select LoRA to convert.",
    "log_initialization_end": "Initialized: {0:.2f}s.",
    "log_task_start": "Started {0}.",
    "log_task_success": "Completed {0}. {1:.2f}s.",
    "log_task_failed": "Failed {0}. {1:.2f}s.\nEnable [Pause by error] and check the error.",
    "log_ffplay": "Preview seed {0}. You can change ffplay command in EasyPromptAnimeEditor.ini.",
    "log_convert_lora": "Convert LoRA with Dim {0}.\nOriginal LoRA: {1}\nMerge model for extraction: {2}\nConverted LoRA: {3}",
    "err_inv_line": "Invalid line. {0}",
    "err_inv_frame_num": "Invalid frame number. {0}: {1}",
    "err_inv_lora_def": 'Invalid LoRA definition. "{0}" {1}',
    "hlp_prompt": """
# The number of frames + colon (:) + prompt specifies the prompt for the animation keyframe.
# Instead of frame number + colon, "H:", "F:", "N:", and "L:" will set special settings for the entire animation.
# Sharp (#) and after are comments.

H: crowds, akihabara
# Lines starting with "H:" or "h:" specify header prompts, which are added at the beginning of the keyframe prompts in the animation.

 0: standing, upset
10: waving at viewer, surprised
20: waving at viewer, smile
# Use the prompts "standing, upset" at frame 0 of the animation, "having at viewer, surprised" at frame 10, and "having at viewer, smile" at frame 20.
# 10 images are displayed per second (10 frames per second), with interpolation between key frames.

F: 1girl, maid outfit
# Lines that start with "F:" or "f:" specify footer prompts, which are added to the end of the keyframe prompts in the animation.

# When generated for 3 seconds (30 frames) with the above specifications, the keyframe prompt will be as follows.
#  0 frame "crowds, akihabara, standing, upset, 1girl, maid outfit"
# 10 frame "crowds, akihabara, waving at viewer, surprised, 1girl, maid outfit"
# 20 frame "crowds, akihabara, waving at viewer, smile, 1girl, maid outfit"
# 30 frame "crowds, akihabara, standing, upset, 1girl, maid outfit"

# You do not need to set keyframes in detail, just put a word that expresses movement, such as "dancing," in frame 0, and the AI will move the image on its own.

N:(worst quality, low quality:1.4)
# Lines beginning with "N:" or "n:" specify negative prompts to be used for all frames of the animation.

# L:explosion:-0.2 # The # at the beginning of the line is a comment. If you use LoRA, please remove the # at the beginning.
# Lines beginning with "L:" or "l:" may contain multiple LoRA file names + colon (:) + intensity, separated by commas (,).
# If you want to use LoRA, please put LoRA in *.safetensors format in the menu [Folder - Prompt travel - LoRA].
# The available LoRA is the normal LierLa format. C3Lier(Locon) format can be converted to LierLa format using the menu [Tools - Convert LoRA].
""",
}
