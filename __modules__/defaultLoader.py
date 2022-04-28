#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 3 10:12:31 2022
Edited on Sat Mar 5 05:02:22 2022
@author: dmytrenko.o
"""
import sys
stdOutput = open("outlog.log", "w")
sys.stderr = stdOutput
sys.stdout = stdOutput

import os, io, tempfile, zipfile, requests, codecs, csv
from vosk import Model

def load_default_templateshashmap(templatesDir):
    templatesUkr = []
    templatesRus = []
    with codecs.open(templatesDir+'UKR_RUS_Recall.csv', encoding='utf-8') as f:
        templates = csv.reader(f, delimiter=':')
        for (tu,tr,weight) in templates:
            templatesUkr.append((tu, float(weight)))
            templatesRus.append((tr, float(weight)))
    return {"uk" : templatesUkr, "ru" : templatesRus}

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

def load_default_models(modelsDir, defaultLangs, modelsHashMap):
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
        load_default_models(modelsHashMap[lang])
    return voskModels

def load_default_modelshashmap(defaultModalsHashMapDir):
    try:
        modelsHashMap = dict(line.split(":") for line in (io.open(defaultModalsHashMapDir+"defaultModelsHashMap.csv", 'r', encoding="utf-8").read()).split())
    except:
        modelsHashMap = {"uk":"vosk-model-uk-v3", "ru":"vosk-model-ru-0.22"}
    return modelsHashMap

def load_except_languages(defaultExcLangsDir):
    try:
        exceptedLangs = (io.open(defaultExcLangsDir+"exceptedLangs.csv", 'r', encoding="utf-8").read()).split()
    except:
        exceptedLangs = []
    return exceptedLangs

def load_default_languages(defaultLangsDir):
    try:
        defaultLangs = (io.open(defaultLangsDir+"defaultLangs.csv", 'r', encoding="utf-8").read()).split()
    except:
        defaultLangs = ['uk', 'ru']
    return defaultLangs
