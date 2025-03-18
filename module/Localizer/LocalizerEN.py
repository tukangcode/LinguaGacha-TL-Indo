from module.Localizer.LocalizerBase import LocalizerBase

class LocalizerEN(LocalizerBase):

    # 保留
    switch_language: str = (
        "请选择应用语言，新的语言设置将在下次启动时生效！"
        "\n"
        "Select application language, changes will take effect on restart!"
    )
    switch_language_toast: str = (
        "应用语言切换成功，请重启应用生效 ..."
        "\n"
        "Language switched successfully, please restart the application for changes to take effect ..."
    )

    # 通用
    add: str = "Add"
    edit: str = "Edit"
    none: str = "None"
    stop: str = "Stop"
    start: str = "Start"
    close: str = "Close"
    alert: str = "Alert"
    warning: str = "Warning"
    confirm: str = "Confirm"
    cancel: str = "Cancel"
    enable: str = "Enable"
    disable: str = "Disable"
    auto: str = "Auto"
    wiki: str = "Wiki"
    inject: str = "Inject"
    alert_no_data: str = "No valid data"
    alert_reset_translation: str = "Reset unfinished translations and start new task?"
    select_file: str = "Select File"
    select_file_type: str = "Support Format (*.json *.xlsx)"
    table_delete_row: str = "Delete Row"
    table_insert_row: str = "Insert Row"

    # 主页面
    app_close_message_box: str = "Are you sure you want to exit the application ... ?"
    app_close_message_box_msg: str = "The main window is closed, the application will automatically exit later ..."
    app_new_version: str = "Download New Version!"
    app_new_version_toast: str = "New version found, version number is {VERSION}, tap the button at the lower left to download ..."
    app_theme_btn: str = "Theme"
    app_language_btn: str = "Language"
    app_settings_page: str = "App Settings"
    app_platform_page: str = "API"
    app_project_page: str = "Project Settings"
    app_translation_page: str = "Start Translation"
    app_basic_settings_page: str = "Basic Settings"
    app_advance_Feature_page: str = "Advanced Features"
    app_glossary_page: str = "Glossary"
    app_pre_translation_replacement_page: str = "Pre-Translation Replacement"
    app_post_translation_replacement_page: str = "Post-Translation Replacement"
    app_custom_prompt_navigation_item: str = "Custom Prompts"
    app_custom_prompt_zh_page: str = "Chinese Prompts"
    app_custom_prompt_en_page: str = "English Prompts"
    app_tool_box_page: str = "Tool Box"

    # 路径
    path_bilingual: str = "bilingual"
    path_glossary_export = "export_glossary"
    path_pre_translation_replacement_export = "export_pre_translation_replacement"
    path_post_translation_replacement_export = "export_post_translation_replacement"
    path_result_check_kana = "result_check_residual_kana.json"
    path_result_check_hangeul = "result_check_residual_hangeul.json"
    path_result_check_code = "result_check_incorrect_code.json"
    path_result_check_similarity = "result_check_high_similarity.json"
    path_result_check_glossary = "result_check_incorrect_glossary.json"
    path_result_name_injection_file = "result.xlsx"
    path_result_name_injection_folder = "name_injection"

    # 日志
    log_debug_mode: str = "Debug mode enabled ..."
    log_config_file_not_exist: str = "Configuration file not found ..."
    log_api_test_fail: str = "API test failed ... "
    log_task_fail: str = "Translation task failed ..."
    log_read_file_fail: str = "File reading failed ..."
    log_write_file_fail: str = "File writing failed ..."
    log_read_cache_file_fail: str = "Failed to read cached data from file ..."
    log_write_cache_file_fail: str = "Failed to write cached data to file ..."
    log_load_llama_cpp_slots_num_fail: str = "Failed to get response data from [green]llama.cpp[/] ..."
    log_crash: str = "A critical error has occurred, program will now exit. Error detail has been saved to the log file ..."
    translator_max_round: str = "Max rounds"
    translator_current_round: str = "Current round"
    translator_api_url: str = "API URL"
    translator_name: str = "API Name"
    translator_model: str = "Model Name"
    translator_proxy_url: str = "Active Network Proxy"
    translator_prompt: str = "The following prompt will be used for this task:\n{PROMPT}\n"
    translator_begin: str = "Translation task is about to start, estimated total tasks: {TASKS}, concurrent tasks: {BATCH_SIZE}. Please ensure network connection ..."
    translator_writing: str = "Writing translation data, please wait ..."
    translator_done: str = "All texts are translated, translation task finished ..."
    translator_fail: str = "Maximum translation rounds reached, some texts are still untranslated. Please check the translation results ..."
    translator_stop: str = "Translation task stopped ..."
    translator_write: str = "Translation result saved to {PATH} directory ..."
    translator_generate_task: str = "Generate tasks"
    translator_rule_filter: str = "Rule filtering completed, {COUNT} entries not requiring translation filtered out ..."
    translator_mtool_filter: str = "MToolOptimizer preprocessing completed, {COUNT} entries containing duplicate clauses filtered out ..."
    translator_language_filter: str = "Language filtering completed, {COUNT} entries not containing target language filtered out ..."
    translator_task_response_think: str = "Model thinking:\n"
    translator_task_response_result: str = "Model response:\n"
    translator_response_check_fail: str = "Translated text failed check, will automatically retry in the next round of translation"
    translator_response_check_fail_part: str = "Partial translated text failed check, will automatically retry in the next round of translation"
    translator_task_success: str = "Task time {TIME} seconds, {LINES} lines of text, input tokens {PT}, output tokens {CT}"
    translator_too_many_task: str = "Too many real-time tasks. Details hidden for performance ...."
    translator_no_items: str = "No translatable data was found. Please check that the input file and project settings are correct ..."
    translator_running: str = "Task is running, please try again later ..."
    file_checker_kana: str = "Kana residue check complete, no issues found ..."
    file_checker_kana_full: str = "Kana residue check complete, {COUNT} issues found, {PERCENT}%, results written to [green]{TARGET}[/] ..."
    file_checker_hangeul: str = "Hangeul residue check complete, no issues found ..."
    file_checker_hangeul_full: str = "Hangeul residue check complete, {COUNT} issues found, {PERCENT}%, results written to [green]{TARGET}[/] ..."
    file_checker_code: str = "Code check complete, no issues found ..."
    file_checker_code_full: str = "Code check complete, {COUNT} issues found, {PERCENT}%, results written to [green]{TARGET}[/] ..."
    file_checker_code_alert_key: str = "____ALERT____"
    file_checker_code_alert_value: str = "This file lists entries with *potential* code issues. Please verify in context!"
    file_checker_similarity: str = "Similarity check complete, no issues found ..."
    file_checker_similarity_full: str = "Similarity check complete, {COUNT} potential issues found, {PERCENT}%, results written to [green]{TARGET}[/] ..."
    file_checker_similarity_alert_key: str = "____ALERT____"
    file_checker_similarity_alert_value: str = "This file lists entries with *potentially* high similarity. Please verify in context!"
    file_checker_glossary: str = "Glossary check complete, no issues found ..."
    file_checker_glossary_full: str = "Glossary check complete, {COUNT} issues found, {PERCENT}%, results written to [green]{TARGET}[/] ..."
    platofrm_tester_key: str = "Testing API Key"
    platofrm_tester_proxy: str = "Network proxy enabled, proxy address: "
    platofrm_tester_messages: str = "Sending prompts"
    platofrm_tester_response_think: str = "Model thinking"
    platofrm_tester_response_result: str = "Model response"
    platofrm_tester_result: str = "Tested {COUNT} APIs in total, {SUCCESS} successful, {FAILURE} failed ..."
    platofrm_tester_running: str = "Task is running, please try again later ..."
    response_checker_unknown: str = "Unknown"
    response_checker_fail_data: str = "Response error (data structure)"
    response_checker_fail_line: str = "Response error (number of data lines)"
    response_checker_similarity: str = "Similar response detected"
    response_checker_degradation: str = "Degraded response detected"
    response_decoder_glossary_by_json: str = "Glossary data [bright_blue]->[/] deserialization, total {COUNT} entries"
    response_decoder_glossary_by_rule: str = "Glossary data [bright_blue]->[/] rule parsing after split, total {COUNT} entries"
    response_decoder_translation_by_json: str = "Translation data [bright_blue]->[/] deserialization, total {COUNT} entries"
    response_decoder_translation_by_rule: str = "Translation data [bright_blue]->[/] rule parsing after split, total {COUNT} entries"

    # 应用设置
    app_settings_page_proxy_url = "Please enter network proxy address ..."
    app_settings_page_proxy_url_title = "Network Proxy"
    app_settings_page_proxy_url_content = "When enabled, requests will be sent to the API using the set proxy address, e.g., http://127.0.0.1:7890"
    app_settings_page_font_hinting_title = "Font Optimization"
    app_settings_page_font_hinting_content = "When enabled, app ui font edge rendering will be smoother (will take effect after app restart)"
    app_settings_page_debug_title = "Debug Mode"
    app_settings_page_debug_content = "When enabled, the app will display additional debug information"
    app_settings_page_scale_factor_title = "Global Scale Factor"
    app_settings_page_scale_factor_content = "When enabled, the app interface will be scaled according to the selected ratio (will take effect after app restart)"

    # 接口管理
    platform_page_api_test_result: str = "API test result: {SUCCESS} successful, {FAILURE} failed ..."
    platform_page_api_activate: str = "Activate API"
    platform_page_api_edit: str = "Edit API"
    platform_page_api_args: str = "Edit Arguments"
    platform_page_api_test: str = "Test API"
    platform_page_api_delete: str = "Delete API"
    platform_page_widget_add_title: str = "API List"
    platform_page_widget_add_content: str = "Add and manage any LLM API compatible with OpenAI and Anthropic formats here"

    # 接口编辑
    platform_edit_page_name: str = "Please enter API name ..."
    platform_edit_page_name_title: str = "API Name"
    platform_edit_page_name_content: str = "Please enter API name, only for display within the app, no practical effect"
    platform_edit_page_api_url: str = "Please enter API URL ..."
    platform_edit_page_api_url_title: str = "API URL"
    platform_edit_page_api_url_content: str = "Please enter API URL, pay attention to whether /v1 needs to be added at the end"
    platform_edit_page_api_key: str = "Please enter API Key ..."
    platform_edit_page_api_key_title: str = "API Key"
    platform_edit_page_api_key_content: str = "Please enter API Key, e.g., sk-d0daba12345678fd8eb7b8d31c123456. Multiple keys can be entered for polling, one key per line"
    platform_edit_page_thinking_title: str = "Use Thinking Mode First"
    platform_edit_page_thinking_content: str = "Prefer thinking mode for models that offer both thinking and normal modes. Currently, only Claude Sonnet 3.7 supports this."
    platform_edit_page_model: str = "Please enter Model Name ..."
    platform_edit_page_model_title: str = "Model Name"
    platform_edit_page_model_content: str = "Current model in use: {MODEL}"
    platform_edit_page_model_edit: str = "Manual Input"
    platform_edit_page_model_sync: str = "Fetch Online"

    # 参数编辑
    args_edit_page_top_p_title: str = "top_p"
    args_edit_page_top_p_content: str = "Please set with caution, incorrect values may cause abnormal results or request errors"
    args_edit_page_temperature_title: str = "temperature"
    args_edit_page_temperature_content: str = "Please set with caution, incorrect values may cause abnormal results or request errors"
    args_edit_page_presence_penalty_title: str = "presence_penalty"
    args_edit_page_presence_penalty_content: str = "Please set with caution, incorrect values may cause abnormal results or request errors"
    args_edit_page_frequency_penalty_title: str = "frequency_penalty"
    args_edit_page_frequency_penalty_content: str = "Please set with caution, incorrect values may cause abnormal results or request errors"
    args_edit_page_document_link: str = "Click to view documentation"

    # 模型列表
    model_list_page_title: str = "Available Model List"
    model_list_page_content: str = "Click to select the model to use"
    model_list_page_fail: str = "Failed to get model list, please check API configuration ..."

    # 项目设置
    project_page_source_language_title: str = "Source Language"
    project_page_source_language_content: str = "Set the language of the source text used in the current translation project"
    project_page_source_language_items: str = "Chinese,English,Japanese,Korean,Russian,German,French,Spanish,Italian,Portuguese,Thai,Indonesian,Vietnamese"
    project_page_target_language_title: str = "Target Language"
    project_page_target_language_content: str = "Set the language of the translated text used in the current translation project"
    project_page_target_language_items: str = "Chinese,English,Japanese,Korean,Russian,German,French,Spanish,Italian,Portuguese,Thai,Indonesian,Vietnamese"
    project_page_input_folder_title: str = "Input Folder"
    project_page_input_folder_content: str = "Current input folder is"
    project_page_input_folder_btn: str = "Select Folder"
    project_page_output_folder_title: str = "Output Folder (cannot be the same as input folder)"
    project_page_output_folder_content: str = "Current output folder is"
    project_page_output_folder_btn: str = "Select Folder"
    project_page_traditional_chinese_title: str = "Output Chinese in Traditional Characters"
    project_page_traditional_chinese_content: str = "When enabled, if the target language is set to Chinese, Chinese text will be output in Traditional Chinese characters"

    # 开始翻译
    translation_page_status_idle = "Idle"
    translation_page_status_testing = "Testing"
    translation_page_status_translating = "Translating"
    translation_page_status_stopping = "Stopping"
    translation_page_indeterminate_saving = "Saving cache file ..."
    translation_page_indeterminate_stoping = "Stopping translation task ..."
    translation_page_card_time = "Elapsed Time"
    translation_page_card_remaining_time = "Remaining Time"
    translation_page_card_line = "Translated Lines"
    translation_page_card_remaining_line = "Remaining Lines"
    translation_page_card_speed = "Average Speed"
    translation_page_card_token = "Total Tokens"
    translation_page_card_task = "Real Time Tasks"
    translation_page_alert_pause = "Stopped translation tasks can be resumed at any time. Confirm to stop the task ... ?"
    translation_page_continue = "Continue Translation"
    translation_page_export = "Export Translation Data"
    translation_page_export_toast = "Translation files have been generated in the output folder based on the current translation data ..."

    # 基础设置
    basic_settings_page_batch_size_title = "Concurrent Tasks"
    basic_settings_page_batch_size_content = (
        "Maximum number of translation tasks executed simultaneously."
        "\n"
        "Setting appropriately can greatly increase translation speed. Please refer to the API platform's limits for settings."
    )
    basic_settings_page_task_token_limit_title = "Task Length Threshold"
    basic_settings_page_task_token_limit_content = "Maximum text length sent to the model at once for each translation task, unit is Token."
    basic_settings_page_request_timeout_title = "Request Timeout"
    basic_settings_page_request_timeout_content = (
        "Timeout duration for a model's response to a translation request."
        "\n"
        "If the model doesn't respond in time, the translation task will fail, unit is Seconds. Not applicable to Google models."
    )
    basic_settings_page_max_round_title = "Maximum Translation Rounds"
    basic_settings_page_max_round_content = "After one translation round, if entries are still untranslated, restart translation until finished or the round limit is reached."

    # 高级功能
    advance_feature_page_auto_glossary_enable = "Auto Complete Glossary (Experimental feature, SakuraLLM model not supported)"
    advance_feature_page_auto_glossary_enable_desc = (
        "When enabled, this feature analyzes text during translation to automatically fill in missing proper noun entries in the glossary."
        "<br>"
        "This feature is designed to only identify and fill in gaps, and cannot replace manually glossaries. It only works when <font color='darkgoldenrod'><b>Glossary</b></font> is enabled."
        "<br>"
        "May cause <font color='darkgoldenrod'><b>negative effects</b></font> or <font color='darkgoldenrod'><b>translation anomalies</b></font>. Theoretically, it only has positive effects on powerful models at the DeepSeek R1 level."
        "<br>"
        "Please <font color='darkgoldenrod'><b>judge for yourself</b></font> whether to enable it."
    )
    advance_feature_page_mtool_optimizer_enable = "MTool Optimizer"
    advance_feature_page_mtool_optimizer_enable_desc = (
        "When enabled, this feature can reduce translation time and token consumption by up to 40% when translating MTool text."
        "<br>"
        "May cause issues such as <font color='darkgoldenrod'><b>residual original text</b></font> or <font color='darkgoldenrod'><b>incoherent sentences</b></font>."
        "<br>"
        "Please <font color='darkgoldenrod'><b>judge for yourself</b></font> whether to enable it, and it should only be enabled when <font color='darkgoldenrod'><b>translating MTool text</b></font>."
    )

    # 术语表
    glossary_page_head_title = "Glossary"
    glossary_page_head_content = "By building a glossary in the prompt to guide model translation, unified translation and correction of personal pronouns can be achieved"
    glossary_page_table_row_01 = "Original Text"
    glossary_page_table_row_02 = "Translated Text"
    glossary_page_table_row_03 = "Description"
    glossary_page_import = "Import"
    glossary_page_import_toast = "Data imported ..."
    glossary_page_export = "Export"
    glossary_page_export_toast = "Data exported to application root directory ..."
    glossary_page_add = "Add"
    glossary_page_add_toast = "New row added ..."
    glossary_page_save = "Save"
    glossary_page_save_toast = "Data saved ..."
    glossary_page_reset = "Reset"
    glossary_page_reset_toast = "Data reset ..."
    glossary_page_reset_alert = "Confirm reset to default data ... ?"
    glossary_page_kg = "One-Click Tools"

    # 译前替换
    pre_translation_replacement_page_head_title = "Pre-translation Replacement"
    pre_translation_replacement_page_head_content = "Before translation starts, replace the matched parts in the original text with the specified text, the execution order is from top to bottom."
    pre_translation_replacement_page_table_row_01 = "Original Text"
    pre_translation_replacement_page_table_row_02 = "Replacement"
    pre_translation_replacement_page_import = "Import"
    pre_translation_replacement_page_import_toast = "Data imported ..."
    pre_translation_replacement_page_export = "Export"
    pre_translation_replacement_page_export_toast = "Data exported to application root directory ..."
    pre_translation_replacement_page_add = "Add"
    pre_translation_replacement_page_add_toast = "New row added ..."
    pre_translation_replacement_page_save = "Save"
    pre_translation_replacement_page_save_toast = "Data saved ..."
    pre_translation_replacement_page_reset = "Reset"
    pre_translation_replacement_page_reset_toast = "Data reset ..."
    pre_translation_replacement_page_reset_alert = "Confirm reset to default data ... ?"

    # 译后替换
    post_translation_replacement_page_head_title = "Post-translation Replacement"
    post_translation_replacement_page_head_content = "After translation is completed, replace the matched parts in the translated text with the specified text, the execution order is from top to bottom"
    post_translation_replacement_page_table_row_01 = "Original Text"
    post_translation_replacement_page_table_row_02 = "Replacement"
    post_translation_replacement_page_import = "Import"
    post_translation_replacement_page_import_toast = "Data imported ..."
    post_translation_replacement_page_export = "Export"
    post_translation_replacement_page_export_toast = "Data exported to application root directory ..."
    post_translation_replacement_page_add = "Add"
    post_translation_replacement_page_add_toast = "New row added ..."
    post_translation_replacement_page_save = "Save"
    post_translation_replacement_page_save_toast = "Data saved ..."
    post_translation_replacement_page_reset = "Reset"
    post_translation_replacement_page_reset_toast = "Data reset ..."
    post_translation_replacement_page_reset_alert = "Confirm reset to default data ... ?"

    # 自定义提示词 - 中文
    custom_prompt_zh_page_head = "Custom prompt used when target language is set to Chinese (SakuraLLM model not supported)"
    custom_prompt_zh_page_head_desc = (
        "Add extra translation requirements such as story settings and writing styles via custom prompts."
        "<br>"
        "Note: The prefix and suffix are fixed and cannot be modified."
        "<br>"
        "The custom prompts on this page will only be used when the <font color='darkgoldenrod'><b>translation language is set to Chinese</b></font>."
    )
    custom_prompt_zh_page_save = "Save"
    custom_prompt_zh_page_save_toast = "Data saved ..."
    custom_prompt_zh_page_reset = "Reset"
    custom_prompt_zh_page_reset_toast = "Data reset ..."
    custom_prompt_zh_page_reset_alert = "Confirm reset to default data ... ?"

    # 自定义提示词 - 英文
    custom_prompt_en_page_head = "Custom prompt used when target language is set to non-Chinese languages (SakuraLLM model not supported)"
    custom_prompt_en_page_head_desc = (
        "Add extra translation requirements such as story settings and writing styles via custom prompts."
        "<br>"
        "Note: The prefix and suffix are fixed and cannot be modified."
        "<br>"
        "The custom prompts on this page will only be used when the <font color='darkgoldenrod'><b>translation language is set to non-Chinese</b></font>."
    )
    custom_prompt_en_page_save = "Save"
    custom_prompt_en_page_save_toast = "Data saved ..."
    custom_prompt_en_page_reset = "Reset"
    custom_prompt_en_page_reset_toast = "Data reset ..."
    custom_prompt_en_page_reset_alert = "Confirm reset to default data ... ?"

    # 百宝箱
    tool_box_page_re_translation = "Partial Re-Translation"
    tool_box_page_re_translation_desc = "Re-translate parts of already translated text based on set filters, mainly for content updates or error correction."
    tool_box_page_name_injection = "Name Injection"
    tool_box_page_name_injection_desc = "Extract, deduplicate, translate, and inject name fields from <font color='darkgoldenrod'><b>RenPy</b></font> and <font color='darkgoldenrod'><b>GalGame</b></font> game texts for consistent naming."

    # 百宝箱 - 部分重翻
    re_translation_page = "Partial Re-Translation"
    re_translation_page_desc = (
        "Will filter the text in the <font color='darkgoldenrod'><b>Input Folder</b></font> based on the set filter conditions, and then retranslate the text that meets the conditions."
        "<br>"
        "Workflow:"
        "<br>"
        "• Load the original and translated texts from the <font color='darkgoldenrod'><b>src</b></font> and <font color='darkgoldenrod'><b>dst</b></font> subdirectories of the <font color='darkgoldenrod'><b>Input Folder</b></font>."
        "<br>"
        "• The filenames and file contents of the original and translated files must correspond strictly one-to-one."
        "<br>"
        "• Filter out the text that needs to be retranslated according to the settings on this page, translate it according to the normal process."
    )
    re_translation_page_white_list = "Keywords - Whitelist"
    re_translation_page_white_list_desc = (
        "Text containing these keywords will be retranslated. You can enter multiple keywords, one per line."
        "\n"
        "Hitting one of them is enough to determine that the text needs to be retranslated."
    )
    re_translation_page_white_list_placeholder = "Please enter keywords ..."
    re_translation_page_alert_not_equal = "The number of lines in the original and translated texts does not match ..."

    # 百宝箱 - 角色姓名注入
    name_injection_page = "Name Injection"
    name_injection_page_desc = (
        "Extract, translate, and inject name fields from eligible files in the <font color='darkgoldenrod'><b>Input Folder</b></font>."
        "<br>"
        "Supported formats: RenPy export game text (.rpy), VNTextPatch or SExtractor export game text with name field (.json)"
    )
    name_injection_page_step_01 = "Step 1 - Extract & Translate"
    name_injection_page_step_01_desc = (
        "Extract name fields and related context, then translate."
        "<br>"
        "The translated data will be in <font color='darkgoldenrod'><b>Output Folder/name_injection/result.xlsx</b></font>."
    )
    name_injection_page_step_02 = "Step 2 - Organize & Inject"
    name_injection_page_step_02_desc = (
        "Check and correct the translated name data in the result file, <font color='darkgoldenrod'><b>close</b></font> it, and start injection."
        "<br>"
        "Note:"
        "<br>"
        "• Only text <font color='darkgoldenrod'><b>wrapped in 【】 will be injected</b></font>."
        "<br>"
        "• Game text for injection is read from <font color='darkgoldenrod'><b>Input Folder</b></font>, and the injected text is saved in <font color='darkgoldenrod'><b>Output Folder</b></font>."
    )
    name_injection_page_success = "Name data injected successfully ..."