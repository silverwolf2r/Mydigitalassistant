#!/usr/bin/env python3
# game of Shiritori in English 

import os
import enchant
import random
import re
import requests
from os import system, name
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
options = Options()
from selenium.webdriver.common.keys import Keys
import time
import speech_recognition as sr
import os
import datetime
import random 
import win32com.client as wincl
import winsound


frequency = 2500  # Set Frequency To 2500 Hertz
duration = 100  # Set Duration To 1000 ms == 1 second


def clear():
	system('cls')
	
	
	
def unique(list1): 
  
    # intilize a null list 
    unique_list = [] 
      
    # traverse for all elements 
    for x in list1: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x) 
    # print list 
    for x in unique_list: 
        print (x) 
	


def randomword(char):
	# use char to find a word from the dictionary 
	words = (' ')
	clear()
	print("The computer is attempting to find a word")
	url = "http://www.mieliestronk.com/corncob_lowercase.txt"
	res = requests.get(url)
	text = res.text 
	words = [idx for idx in text.split() if idx.lower()[0] == char.lower()]
	# find all words that start with char
	word = random.choice(words) 
	clear()
	print("The Computers Word: " + word)
	return word





	
	
	
x = 1
# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
	r.adjust_for_ambient_noise(source, duration=1)
	speak = wincl.Dispatch("SAPI.SpVoice")
	speak.Speak("Say a Word")
	winsound.Beep(frequency,duration)
	audio = r.listen(source)
    
#recognize audio and assign it to a variable   
Playerword = str(r.recognize_google(audio))

words_used = []
Computerword = ("")
d = enchant.Dict("en_US")

while Playerword:
	
	words_used.append(Computerword)
	words_used.append(Playerword)
	plast_char = Playerword[-1]
	#search for a word by plast_char and assign it to Computerword
	x = 1
	clear()
	while x == 1:
		Computerword = randomword(plast_char)#input ("Player 2 say a word that starts with " + plast_char + " ")	
		if Computerword not in words_used and Computerword[0] == plast_char and d.check(Computerword) == True:
			speak = wincl.Dispatch("SAPI.SpVoice")
			speak.Speak(str(Computerword))
			x = 2
		else:
			clear()
			#print("Look at the word list and try again")
			#print("word list: ")
			#unique(words_used)
		
		
	clast_char = Computerword[-1]
	words_used.append(Computerword)
	words_used.append(Playerword)
	x = 1
	while x == 1:
		# obtain audio from the microphone
		r = sr.Recognizer()
		with sr.Microphone() as source:
			r.adjust_for_ambient_noise(source, duration=1)
			print("Player 1 say a word that starts with " + clast_char + " ")
			winsound.Beep(frequency,duration)
			audio = r.listen(source)
    
		ad = None
		while ad == None:
			try:
				#recognize audio and assign it to a variable   
				Playerword = str(r.recognize_google(audio))
				ad = str(r.recognize_google(audio))
			except:
				ad = None

		if Playerword not in words_used and Playerword[0] == clast_char and d.check(Playerword) == True:
			x = 2
		else:
			clear()
			print("Look at the word list and try again")
			print("word list: ")
			unique(words_used)
			
			
			
# Check to make sure the word exists 
# Come up with a way for the computer to make a word

		
	









