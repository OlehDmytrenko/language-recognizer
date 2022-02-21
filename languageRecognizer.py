# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 10:57:26 2021

@author: dmytr
"""

import moviepy.editor as mp
from vosk import Model, KaldiRecognizer
import os
import wave
from scipy.io import wavfile
import csv
import codecs
import re
import time as tm
t0 = tm.time()

def weightedTemplates(fName):
    templatesUkr = []
    templatesRus = []
    with codecs.open(os.getcwd()+'/templates/'+fName, encoding='utf-8') as f:
        templates = csv.reader(f, delimiter=':')
        for (tu,tr,weight) in templates:
            templatesUkr.append((tu, float(weight)))
            templatesRus.append((tr, float(weight)))
    return templatesUkr, templatesRus


def video2parts(minutes):
    in_dir = os.getcwd()+'/audios/full_audios/'
    out_dir = os.getcwd()+'/audios/part_audios/'
    name = 0
    for file_ in os.listdir(in_dir):
        samplerate, data = wavfile.read(in_dir+file_)
        print ('Samplerate {0}'.format(samplerate))
        totalSize = len(data)
        ChunkSize = samplerate*minutes*15 #60 sec in 1 minute
        amountChunk = int(totalSize/ChunkSize)
        
        for i in range(amountChunk):
            chunkData = data[i*ChunkSize:i*ChunkSize+ChunkSize]
            name += 1
            wavfile.write(out_dir+str(name)+'.wav', samplerate ,chunkData)

def video2wav():
    videos_dir = os.getcwd()+'/videos/'
    tests_dir = os.getcwd()+'/audios/full_audios/'
    for file_ in os.listdir(videos_dir):
        clip = mp.VideoFileClip(videos_dir+file_)
        clip.audio.write_audiofile(tests_dir+os.path.splitext(file_)[0].lower()+'.wav',  fps=44100, nbytes=2,  ffmpeg_params=["-ac", "1"])    #fps=1000, 
        clip.close()
    
def recognizer(file, model, templ):
    wf = wave.open(os.getcwd()+'/audios/part_audios/'+file, "rb")   
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
    
    countTemplates = 0
    tamlateFreq = dict()
    for i, weight in templ: #
        countTemplate = (text.count(i))#*weight
        tamlateFreq[i] = countTemplate
        countTemplates += countTemplate
    tamlateFreq = sorted(tamlateFreq.items(), key=lambda kv: kv[1], reverse=1)
    print (tamlateFreq)
    out_results.write(str(tamlateFreq)+'\n')
    print ('Number of templates: {0}'.format(countTemplates))
    out_results.write('Number of templates: {0}'.format(countTemplates)+'\n')
    return countTemplates, tamlateFreq, text

video2wav()
video2parts(1)

templ_ukr, templ_rus = weightedTemplates('UKR_RUS_Recall.csv')

ukrCount = 0
rusCount = 0
anotherCount = 0
model_ukr = Model("models/model_ukr")
model_rus = Model("models/model_ru")

out_results = open(os.getcwd()+'/results/results.txt', 'a', encoding='utf-8')
for file in os.listdir(os.getcwd()+'/audios/part_audios/'):
    print ('Recognition of: {0}'.format(file))
    out_results.write('Recognition of: {0}'.format(file)+'\n')
    countUkrTemplates, UkrTamlateFreq, text = recognizer(file, model_ukr, templ_ukr)
    out_text = open(os.getcwd()+'/results/UKR_model/'+os.path.splitext(file)[0].lower()+'.txt', 'w', encoding='utf-8')
    out_text.write(text)
    out_text.close()
    countRusTemplates, RusTamlateFreq, text = recognizer(file, model_rus, templ_rus)
    out_text = open(os.getcwd()+'/results/RUS_model/'+os.path.splitext(file)[0].lower()+'.txt', 'w', encoding='utf-8')
    out_text.write(text)
    out_text.close()
    
    if countUkrTemplates>countRusTemplates:
        print ('-----Ukrainian language-----\n')
        out_results.write('-----Ukrainian language-----\n\n')
        ukrCount += 1
    elif countRusTemplates>countUkrTemplates:
        print ('-----Russian language-----\n')
        out_results.write('-----Russian language-----\n\n')
        rusCount += 1
    else:
        print ('-----Mixed language-----\n')
        out_results.write('-----Mixed language-----\n\n')
        anotherCount += 1

print ('Ukrainian {0}'.format(ukrCount))
print ('Russian {0}'.format(rusCount))
print ('Mixed {0}'.format(anotherCount))

out_results.close()
print ('Time: '+str(tm.time()-t0))
print