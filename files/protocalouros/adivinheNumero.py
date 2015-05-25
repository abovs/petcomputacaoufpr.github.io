# -*- coding: utf-8 -*-

"""
	1. O programa sorteia um número aleatório
	2. O usuaŕio entra com um palpite
		2a. Se o palpite estiver correto, o programa acaba
		2b. Se não, diga se o número sorteado é maior ou menor que o palpite
	3. Repete o passo dois
"""

import random

numero = random.randint(0,10000)

palpite = int(raw_input("Digite o seu palpite: (0-100)"))

while palpite != numero:
	if palpite > numero:
		print "O número é menor."
	else:
		print "O número é maior."
	
	palpite = int(raw_input("Digite o seu palpite: (0-100)"))

print "ACERTOU!!!!!!!!!"
