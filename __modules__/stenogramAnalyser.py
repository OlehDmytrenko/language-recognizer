#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 16:24:46 2022

@author: dmytrenko.o
"""
import sys
stdOutput = open("outlog.log", "w")
sys.stderr = stdOutput
sys.stdout = stdOutput

import wave, re
from vosk import KaldiRecognizer

def recognizer(partsAudioDir, audio, model, templ):
    wf = wave.open(partsAudioDir+audio, "rb")
    rec = KaldiRecognizer(model, wf.getframerate()) 
    text = []
    fulltext = ''
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            fulltext += rec.Result()
    fulltext += rec.FinalResult()
    textarray = re.findall('"text" : "(.+?)"', fulltext)
    text = ''
    for part in textarray:
        text += part+' '
    
    print (text)
    
    countTemplates = 0
    tamlateFreq = dict()
    for i, weight in templ: #
        countTemplate = (text.count(i))#*weight
        tamlateFreq[i] = countTemplate
        countTemplates += countTemplate
    tamlateFreq = sorted(tamlateFreq.items(), key=lambda kv: kv[1], reverse=1)
    print (tamlateFreq)
    print ('Number of templates: {0}'.format(countTemplates))
    return countTemplates
  