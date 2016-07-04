#!/usr/bin/python2
# coding:utf-8

# by ins3c7
# 3 july 2016

import random, os, threading, time
from requests import get

os.system('clear')

alpha = 'abcdefghijklmnopqrstuvwxyz'

full = []

with open('texto.txt', 'r') as f:
	f_ = f.readlines()

texto = ''.join(f_).lower().split()

def tres():
	while 8:
		pre = []
		for l in range(3):
			pre.append(random.choice(alpha))

		word = ''.join(pre)
		
		if word in texto:
			# print word[0].upper() + word[1:] + '.'
			if word not in full:
				full.append(word)
			return

def quatro():
	while 8:
		pre = []
		for l in range(4):
			pre.append(random.choice(alpha))

		word = ''.join(pre)
		
		if word in texto:
			# print word[0].upper() + word[1:] + '.'
			if word not in full:
				full.append(word)
			tres()
			return


def cinco():
	while 8:
		pre = []
		for l in range(5):
			pre.append(random.choice(alpha))

		word = ''.join(pre)

		if word in texto:
			# print word[0].upper() + word[1:] + '.'
			if word not in full:
				full.append(word)
			quatro()

def seis():
	while 8:
		pre = []
		for l in range(6):
			pre.append(random.choice(alpha))

		word = ''.join(pre)
		
		if word in texto:
			# print word[0].upper() + word[1:] + '.'
			if word not in full:
				full.append(word)


cinco_ = threading.Thread(target=cinco)
cinco_.start()

while True:
	frase = []
	try:
		for fr in range(random.choice(range(0, len(full)))):
			frase.append(random.choice(full))
	except Exception, e:
		pass

	frase = ' '.join(set(frase))
	
	if len(frase):
		print frase[0].upper() + frase[1:] + '.'

	if len(full) > 10:
		random.shuffle(full)
		print ' '.join(full)
		full = []
	
	time.sleep(1)
