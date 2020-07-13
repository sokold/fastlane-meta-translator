# fastlane metadata translator

[fastlane](https://fastlane.tools/) is a great tool for iOS build and release automation. especially when you have multiply localizations.
fastlane metadata translator is a tool to help you translate the metadata to other lanuages with Google Translate.

## Requirements:
- install fastlane and make sure you download metadata from app connect. you should see a fastlane folder in your iOS project folder.
- install Python3 and pip
- install googletrans
>> pip install googletrans

## Usage:
- edit config.py to configure the languages and options
- in terminal:
`python meta.py /Users/me/Documents/iOSProject`
the metadata in language folders should be translated and ready to upload to appstore.
