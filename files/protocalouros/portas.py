# -*- coding: utf-8 -*-

import time

#delay: espera entre os textos. Para adicionar drama.
delay = 1.578

print("\n\n\nBEM VINDO AS PORTAS DA ESPERANÇA!\n\n")
print("A sua frente estão 4 portas. Escolha uma.")
porta = int(raw_input("Qual porta você escolhe? Digite um número entre 1 e 4.\n"))

if porta == 1:
	print("Atrás da porta número 1 está:")
	time.sleep(delay)
	print("...")
	time.sleep(delay)
	print("NADA!")
	time.sleep(delay)
	print("PARABÉNS! :)")
	time.sleep(delay)
elif porta == 2:
	print("Um bode sai de trás da porta número dois e começa a te perseguir.")
elif porta == 3:
	print("Atrás da porta número 3 está...")
	time.sleep(delay)
	print("Um saco de batatas")
elif porta == 4:
	print("Atrás da porta número 4 está...")
	time.sleep(delay)
	print("10 REAIS!")
	time.sleep(delay)
	print(":D")
else:
	print("Isso deveria significar algo?")
