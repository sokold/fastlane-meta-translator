# fastlane metadata translator

[fastlane](https://fastlane.tools/) is a great tool for iOS building and release automation. especially when you have multiple localizations.
fastlane metadata translator is a tool to help you translate the metadata to other lanuages with Google Translate.

fastlane是用于iOS构建和发布自动化的好工具，特别是有多个本地化版本时。 fastlane metadata translator是一个帮助你使用Google Translate将元数据自动转换为其他语言的工具。

## Requirements:
- install fastlane and make sure you download metadata from app connect. you should see a fastlane folder in your iOS project folder.
- install Python3 and pip
- install googletrans. `pip install googletrans`

## Usage:
- edit config.py to configure the languages and options
- in terminal:
`python meta.py /Users/me/Documents/iOSProject`
the metadata in language folders should be translated and ready to upload to appstore.

here is how config.py looks like:
```
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
```
