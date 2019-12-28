import os
from colorama import Fore, Back, Style
try:
    os.system('clear')
except:
    os.system('cls')
print('calculator v1.0 by Skifi\n')

deistv = str(input(Fore.RED +"Выберите действие (+, -, /, *): " + Fore.RESET))
num_1 = int(input("Напишите первое число: "))
num_2 = int(input("Напишите второе число: "))
name = str("calculator v1.0")
if deistv == '+':
	resh = num_1 + num_2
	print("Ответ:",resh)
elif deistv == '-':
	resh = num_1 - num_2
	print("Ответ:",resh)
elif deistv == '/':
	resh = num_1 / num_2
	print("Ответ:",resh)
elif deistv == '*':
	resh = num_1 * num_2
	print("Ответ:",resh)
else:
	print("Выбрано неверное действие!!!")
if 1:
	start_or_stop = str(input("Выключить калькулятор v1.0? \nНапишите - да или нет: "))
	while start_or_stop == 'да':
		print('выкл')
		break
	while start_or_stop == 'нет':
		deistv = str(input("Выберите действие (+, -, /, *): "))
		num_1 = int(input("Напишите первое число: "))
		num_2 = int(input("Напишите второе число: "))
		name = str("calculator v1.0")
		if deistv == '+':
			resh = num_1 + num_2
			print("Ответ:",resh)
		elif deistv == '-':
			resh = num_1 - num_2
			print("Ответ:",resh)
		elif deistv == '/':
			resh = num_1 / num_2
			print("Ответ:",resh)
		elif deistv == '*':
			resh = num_1 * num_2
			print("Ответ:",resh)
		else:
			print("\nВыбрано неверное действие!!!")
		if 1:
			try:
				os.system('exit')
			except:
				os.system('cls')
		
