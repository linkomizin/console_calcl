print('Привет, это калькулятор')



def argument_1():

	while 1:
		arg_1 = input('Введите число:  ')
		try:
			if ',' in str(arg_1):
				arg_1 = str(arg_1.replace(',','.'))
			else:
				pass
			arg_1 = float(arg_1)
			break
		except (AttributeError, ValueError):
			print('Неверно. Введите число! ')
			continue

	return arg_1

def operator(a, b):
	number = (1,2,3,4)
	while 1:
		index = input()
		try:
			index = int(index)
			if index in number:
				if index == 1 :
					rez = a + b
					return rez
				elif index == 2 :
					rez = a - b
					return rez
				elif index == 3 :
					rez = a * b
					return rez
				elif index == 4 :
					rez = a / b
					return rez
			break
		except ValueError:
			print('Vvedite 1, 2, 3, 4')
			continue

def main():
	while True:
		a = argument_1()
		b = argument_1()

		print('Введено: {}, {}'.format(a, b))

		print('Какой знак выберешь?: \n 1: +\n 2: -\n 3: *\n 4: / ')
		operation = operator(a,b)
		print('Результат: ', operation)


main()