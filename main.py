#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: dmytr
"""
from __modules__ import packagesInstaller
packages = ['sys', 'subprocess', 'os', 'io', 'time', 'tempfile', 'zipfile', 'requests', 'codecs', 'csv', 'json', 'scipy', 'moviepy', 'shutil', 'vosk', 'wave', 're']
packagesInstaller.setup_packeges(packages)

import sys
stdOutput = open("outlog.log", "w")
sys.stderr = stdOutput
sys.stdout = stdOutput

import os, subprocess
subprocess.run('python -m venv '+os.getcwd()+'/modules/', shell=True)
from __modules__ import defaultLoader, modelsLoader, stenogramAnalyser, mediaProcessor

import time
t0 = time.time()

if __name__ == "__main__":
    
    try:
        inputFileDir = sys.argv[1]
    except:
        if not os.path.exists(os.getcwd()+'/videos/'):
            print("Directory './videos/' don't exist") 
            print ("Directory {0} don't exist!".format(os.getcwd()+'/videos/'))
            print ("Creating {0} directory...".format(os.getcwd()+'/videos/'))
            os.mkdir(os.getcwd()+'/videos/')
            print ("Directory {0} was created seccsesfuly!".format(os.getcwd()+'/videos/'))
        inputFileDir =  os.getcwd()+'/videos/'
    
    modelsHashMap = defaultLoader.load_lang_models_config(os.getcwd())
    defaultLangs = list(modelsHashMap.keys())
    templatesHashMap = defaultLoader.load_templateshashmap(os.getcwd()+'/templates/')
    audioDuration = defaultLoader.load_int_value(os.getcwd(), "audioDuration") # sec, audioDuration is part of audios
    
    audiosDir =  os.getcwd()+'/audios/'
    mediaProcessor.video2wav(inputFileDir, audiosDir)
    mediaProcessor.audio2parts(audiosDir, audioDuration)
    
    
    ukrCount = 0
    rusCount = 0
    mixedCount = 0
    
    voskModels = modelsLoader.load_models(os.getcwd()+'/models/', defaultLangs, modelsHashMap)
    
    for audio in os.listdir(audiosDir):
        countTemplates = dict()
        print ('Recognition of: {0}'.format(audio))
        for lang in defaultLangs:
            countTemplates[lang] = stenogramAnalyser.recognizer(audiosDir, audio, voskModels[lang], templatesHashMap[lang])         
        if countTemplates["uk"]>countTemplates["ru"]:
            print ('Ukrainian\n')
            sys.stdout = sys.__stdout__
            print (audio + ' - Ukrainian')
            sys.stdout = stdOutput
            ukrCount += 1
        elif countTemplates["ru"]>countTemplates["uk"]:
            print ('Russian\n')
            sys.stdout = sys.__stdout__
            print (audio + ' - Russian')
            sys.stdout = stdOutput
            rusCount += 1
        else:
            print ('Mixed\n')
            sys.stdout = sys.__stdout__
            print (audio + ' - Mixed')
            sys.stdout = stdOutput
            mixedCount += 1
    
    print ('Ukrainian {0}'.format(ukrCount))
    print ('Russian {0}'.format(rusCount))
    print ('Mixed {0}'.format(mixedCount))
    
    print ('Time {0}'.format(time.time() - t0))
    