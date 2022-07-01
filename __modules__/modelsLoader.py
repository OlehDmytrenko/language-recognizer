#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: dmytrenko.o
"""

import os, io, tempfile, zipfile, requests
from vosk import Model

def append_lang(lang, model, defaultLangs, modelsHashMap):
    try:
        defaultLangs.append(lang)
        with io.open("defaultLangs.csv", "a", encoding="utf-8") as file:
            file.write(lang+'\n')
            file.close()
    except:
        print ('¯\_(ツ)_/¯ Unexpected Error while adding new languade to default list!')
    try:
        modelsHashMap.append(lang)
        with io.open("defaultLangs.csv", "a", encoding="utf-8") as file:
            file.write(lang+'\n')
            file.close()
    except:
        print ('Unexpected Error while adding new languade to default list!')
    return


def download_model(model):
    try:
        response = requests.get("https://alphacephei.com/vosk/models/{0}.zip".format(model))
        file = tempfile.TemporaryFile()
        file.write(response.content)
        fzip = zipfile.ZipFile(file)
        fzip.extractall('models')
        file.close()
        fzip.close()
        print ("{0} model was downloaded, unpacked and installed successfuly!".format(model))
    except:
        print ("Please download the {0} from https://alphacephei.com/vosk/models and unpack as {0} in the 'models' folder. Then press <Enter>.".format(model))   
        input()
    return

def load_models(modelsDir, defaultLangs, modelsHashMap):
    if not os.path.exists(modelsDir):
        os.mkdir(modelsDir)
    voskModels = dict()
    #checking if list is empty
    if defaultLangs:
        for lang in defaultLangs:
            try:
                voskModels[lang] = Model(modelsDir+modelsHashMap[lang])
            except:
                download_model(modelsHashMap[lang])
                voskModels[lang] = Model(modelsDir+modelsHashMap[lang])
                print ('{0} Vosk model {1} was downloaded successfully!'.format(lang, modelsHashMap[lang]))   
                continue
              
    else:
        print('The <defaultLangs> list is empty!')
        print ("""Please, enter below at least one language and Vosk model 
               in forrmat: 'uk:vosk-model-uk-v3' or 'ru:vosk-model-ru-0.22'} and press <Enter>!
               Vosk models availible at https://alphacephei.com/vosk/models .""")
        lang, model = input().split(":")
        append_lang(lang, model, defaultLangs, modelsHashMap)
        load_models(modelsHashMap[lang])
    return voskModels