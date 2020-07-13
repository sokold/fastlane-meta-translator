#if language_is_preset is true, uses the languages defined in preset_langs,else it search the languages from fastlane/metadata directory.
language_is_preset = True
#language codes can be found here https://www.ibabbleon.com/iOS-Language-Codes-ISO-639.html
preset_langs = ["en-US", "fr-FR", "de-DE", "zh-CN", "ko", "ja"]

# if uses_existing_meta is False, all language metadata folder are removed first if any then create from the base_language folder by copying
uses_existing_meta = False
# use google translate to translate from base_language
base_language = "en-US"

# such as 'description.txt','release_notes.txt','keywords.txt',"name.text","subtitle"
metadata_to_translate = ['description.txt','keywords.txt']

need_to_copy_screenshot = False

   


