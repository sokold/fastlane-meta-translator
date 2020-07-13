#  Created by Ross Chen on 2020/1/11.
#  Copyright © 2020 Ross Chen. All rights reserved.

"""
this script helps to create fastlane meta translations from google translate. 
it requires Python3 and googletrans lib
you can change configrations in config.py
usage: python meta.py /Users/me/Documents/iOSProject 
"""

import sys,os
import shutil
from config import * 

from googletrans import Translator

translator = Translator()



def get_langs():
    if not language_is_preset:
        lst = [name for name in os.listdir(meta_dir) if os.path.isdir(meta_dir+name) and len(name)<7 and not name==base_language]
    else:
        lst = preset_langs
    return lst


def clean_data(target_dir):
    # use len(name)<7 to filter language folders
    lang_folders = [target_dir+name for name in os.listdir(target_dir) if os.path.isdir(target_dir+name) and len(name)<7 and name != base_language]
    for folder in lang_folders:
         shutil.rmtree(folder)

def copy_data(target_dir):
    clean_data(target_dir)
    for lang in langs:
        if lang == base_language:
            continue
        dst_folder = target_dir+lang
        if not os.path.exists(dst_folder):
            os.makedirs(dst_folder)
        src_folder = target_dir+base_language
        for name in os.listdir(src_folder):
            source = src_folder + "/" + name
            dest = dst_folder + "/" + name
            shutil.copy2(source, dest)


def to_google_lang(name):
    excludes = ['zh-CN','zh-TW']
    if name in excludes:
        return name
    return name.split("-")[0]


def translate():
    for lang in langs:
        items = metadata_to_translate
        for item in items:
            srcpath = meta_dir + base_language + "/" + item
            dst_folder = meta_dir + '%s/' % lang
            if not os.path.exists(dst_folder):
                os.makedirs(dst_folder)
            dstpath = dst_folder + item
            content = open(srcpath).read() 
            try:
                content_result = translator.translate(content, dest=to_google_lang(lang), src=to_google_lang(base_language))
                open(dstpath,'w+').write(content_result.text)
                print(lang,item.replace(".txt",''))
            except Exception as e:
                print("trans error ",e, to_google_lang(lang),item)



if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("enter xcode project root path.")
        exit(1)

    arg = sys.argv[1].strip() 
    target_dir = os.path.join(arg, r'fastlane/')
    if not os.path.exists(target_dir):
        print("incorrect fastlane path")
        exit(1)

    meta_dir = os.path.join(target_dir, r'metadata/')  
    screen_dir = os.path.join(target_dir, r'screenshots/')  
    langs = get_langs()
    #print(langs)

    if not uses_existing_meta:
        copy_data(meta_dir)

    if need_to_copy_screenshot:
        copy_data(screen_dir)

    translate()
      



    
