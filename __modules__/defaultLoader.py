#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: dmytrenko.o
"""
import sys
stdOutput = open("outlog.log", "w")
sys.stderr = stdOutput
sys.stdout = stdOutput

import codecs, csv, json

def load_int_value(configPath, key):
    try:
        with open(configPath+"/config.json", "r") as configFile:
            jsonConfig = json.load(configFile)
            value = int(jsonConfig[key])
            configFile.close()    
    except:
        print ("Error! Int value can't be reading! Please, check a key {0} in config.json".format(key))
        value = 15
    return value

def load_templateshashmap(templatesDir):
    templatesUkr = []
    templatesRus = []
    with codecs.open(templatesDir+'UKR_RUS_Recall.csv', encoding='utf-8') as f:
        templates = csv.reader(f, delimiter=':')
        for (tu,tr,weight) in templates:
            templatesUkr.append((tu, float(weight)))
            templatesRus.append((tr, float(weight)))
    return {"uk" : templatesUkr, "ru" : templatesRus}


def load_lang_models_config(configPath):
    try:
        with open(configPath+"/config.json", "r") as configFile:
            jsonConfig = json.load(configFile)
            try:
                modelsHashMap = {list(langModel.keys())[0] : langModel[list(langModel.keys())[0]]
                                for langModel in jsonConfig["langModels"]}
            except AttributeError:
                pass
            configFile.close()
    except:
        modelsHashMap = {"uk":"vosk-model-uk-v3", "ru":"vosk-model-ru-0.22"}
    return modelsHashMap

