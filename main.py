"""
	Вариант 20.
	Натуральные числа, состоящие из четных и нечетных чередующихся цифр. 
 	Для каждого числа минимальную и максимальную цифру вывести прописью.
"""

import re 

numbersDict = {
	1: 'один',
	2: 'два',
	3: 'три',
	4: 'четрые',
	5: 'пять',
	6: 'шесть',
	7: 'семь',
	8: 'восемь',
	9: 'девять'
}

with open("numbersList.txt") as file:
	stringNumbers = [line.strip() for line in file if line.strip()]


def convertNumbersToInt(numbers):
	intNumbers = []

	try:
		for num in numbers:
			intNumbers.append(int(num))

		return intNumbers
	except ValueError as err:
		print(f"Error cast to int, element: {i}", err)

def isValid(number):
	strNumber = str(number)

	isInteger = bool(re.fullmatch(r"\d+", strNumber))
	if not isInteger: return False

	hasZero = bool(re.search(r"0", strNumber))
	if hasZero: return False

	hasNegativeNumber = bool(re.search(r"-\d", strNumber))
	if hasNegativeNumber: return False

	return True

def isAlternatingNumber(number):
	isEven = False

	valid = isValid(number)

	if not valid:
		return False

	strNumber = str(number)

	isEven = int(strNumber[0]) % 2 == 0 # True - чётное; False - нечётное

	for figure in strNumber[1:]:
		isFigureEven = int(figure) % 2 == 0

		if isFigureEven == isEven:
			return False

		isEven = isFigureEven

	return True

def showAlternatingNumbers(numbers):
	try:
		for number in numbers:
			strNum = str(number)
			min = int(strNum[0])
			max = int(strNum[0])

			if not isAlternatingNumber(number):
				continue

			for figure in strNum:
				intFig = int(figure)
				if intFig > max:
					max = intFig
				elif intFig < min:
					min = intFig

			print("Number", number)
			print("MIN:", numbersDict[min])
			print("MAX:", numbersDict[max])
	except Exception as err:
		print("Error:", err)

def main():
	splitedNubmers = stringNumbers[0].split()
	numbers = convertNumbersToInt(splitedNubmers)
	showAlternatingNumbers(numbers)


if __name__ == "__main__":
	main()
