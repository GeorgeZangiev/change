import os
import sys
import psutil



print ("Лучшая программа за последнюю тысячу лет")
print ("Привет Програмист!")
name = input("Ваше имя:")
print (name,", добро пожаловать в мир Python!")

answer = input ("Давайте поработаем?(Y/N)")

if answer == 'Y':
	print ("Отлично, хозяин!")
	print ("Вот что я умею:")
	print ("[1] - выведу список файлов")
	print ("[2] - выведу информацию о системе")
	print ("[3] - выведу список процессов")
	artur = int(input("Укажи номер действия: "))
	
    if artur == 1:
		print (os.listdir())
	elif artur == 2:
		print (sys.platform())
		print (sys.getfilesystemencoding())
		try:
			res = int(os.environ['NUMBER_OF_PROCESSORS'])
			if res > 0:
				return res
		except (KeyError, ValueError):
			pass	
	elif artur == 3:
		print (psutil.pids())
	else:
		pass
	
elif answer == 'N':
	print ("До свидания!")	
else:
	print ("Неизвестный ответ")
	