#!/usr/bin/python3

import math

			########################################################################
			#         Defining the class formulae. This is the core of the         #
			#	  program, inside which the main functions are defined.        #
			#	  This functions perform the mathematical calculations         #
			#	  in the main function. 	                              # 
			########################################################################

class formulae:
	@staticmethod
	def factorial():
		fact = 1
		num = int(input("\n[\033[34m~\033[0m]Enter the number: "))
		if num == 0:
			print("[\033[34m~\033[0m]Factorial: 0\033[0m")
		else:
			for i in range(1, num + 1):
				fact *= i
			print("[\033[32m+\033[0m]Factorial: " + str(fact) + "\n\033[0m")

	@staticmethod
	def ArCircle():
		print("\n[\033[34m~\033[0m]Press 1 to take pi=3.14 or 2 to take pi=22/7")
		command = input().strip()
		if command == "1":
			radius = eval(input("[\033[34m~\033[0m]Enter the radius of the circle: "))
			area = 3.14
			radius **= 2
			area *= radius
			print("[\033[32m+\033[0m]Area: " + str(area) + "\n\033[0m")
		elif command == "2":
			radius = eval(input("[\033[34m~\033[0m]Enter the radius of the circle: "))
			area = 22/7
			radius **= 2
			area *= radius
			print("[\033[32m+\033[0m]Area: " + str(area) + "\n\033[0m")
		else:
			print("[\033[31m✗\033[0m]Not a valid option.\n\033[0m")

	@staticmethod
	def celsius2F():
		celsius = eval(input("\n[\033[34m~\033[0m]Enter the Celsius: "))
		fahrenheit = (9/5 * celsius + 32)
		print("[\033[32m+\033[0m]Fahrenheit: " + str(fahrenheit) + "\n\033[0m")

	@staticmethod
	def sqrORsqrt():
		num = eval(input("\n[\033[34m~\033[0m]Enter the Number: "))
		print("[\033[34m~\033[0m]Press 1 to show the square root of the number.\n[~]Press 2 to give the square of the number.")
		choice = input("[\033[34m~\033[0m]Choice: ").strip()
		if choice == "1":
			print("[\033[32m+\033[0m]Sq.root: " + str(math.sqrt(num)) + "\n\033[0m")
		elif choice == "2":
			print("[\033[32m+\033[0m]Square: " + str(num * num) + "\n\033[0m")
		else:
			print("[\033[31m✗\033[0m]Not a valid option.\n\033[0m")

	@staticmethod
	def arRect():
		length = eval(input("\n[\033[34m~\033[0m]Enter the length of the Rectangle: "))
		breadth = eval(input("[\033[34m~\033[0m]Enter the breadth of the Rectangle: "))
		print("[\033[32m+\033[0m]Area of the Rectangle: " + str(length * breadth) + "\n\033[0m")

	@staticmethod
	def pRect():
		length = eval(input("\n[\033[34m~\033[0m]Enter the length of the Rectangle: "))
		breadth = eval(input("[\033[34m~\033[0m]Enter the breadth of the Rectsngle: "))
		print("[\033[32m+\033[0m]Perimeter: " + str(2 * (length + breadth)) + "\n\033[0m")

	@staticmethod
	def vSphere():
		radius = eval(input("\n[\033[34m~\033[0m]Enter the radius: "))
		print("[\033[34m~\033[0m]Press 1 to take pi=3.14 or 2 to take pi=22/7")
		command = input().strip()
		if command == "1":
			volume = 4/3 * (3.14 * (radius * radius * radius))
			print("[\033[32m+\033[0m]Volume: " + str(volume) + "\n\033[0m")
		elif command == "2":
			volume = 4/3 * (22/7 * (radius * radius * radius))
			print("[\033[32m+\033[0m]Volume: " + str(volume) + "\n\033[0m")
		else:
			print("[\033[31m✗\033[0m]Not a valid option.\n\033[0m")

	@staticmethod
	def arTriangle():
		height = eval(input("\n[\033[34m~\033[0m]Enter the height of the triangle: "))
		base = eval(input("[\033[34m~\033[0m]Enter the base of the triangle: "))
		area = 1/2 * (base * height)
		print("[\033[32m+\033[0m]Area of the triangle: " + str(area) + "\n\033[0m")

	@staticmethod
	def mulTable():
		num = int(input("\n[\033[34m~\033[0m]Enter the number: "))
		for i in range(1, 21):
			res = num * i
			print(f"{num} x {i} = {res}")
		print("\033[0m")

	@staticmethod
	def sqDetails():
		side = eval(input("\n[\033[34m~\033[0m]Enter the side of the square: "))
		area = side * side
		perimeter = 4 * side
		print(f"\nDetails of the square\n---------------------\n[\033[32m+\033[0m]Area of the square: {area}\n[\033[32m+\033[0m]Perimeter of the square: {perimeter}\n\033[0m")

	@staticmethod
	def BMIcalc():
		height = float(input("\n[\033[34m~\033[0m]Enter your height in meters: "))
		weight = float(input("[\033[34m~\033[0m]Enter your weight in kg: "))
		bmi = weight / (height ** 2)
		if bmi < 18.5:
			print( f"[\033[32m+\033[0m]Underweight (by {bmi} BMI.)\n\033[0m")
		elif bmi == 18.5 or bmi >= 24.9:
			print("[\033[32m+\033[0m]Normal or Healthy.\033[0m")
			print(f"[\033[32m+\033[0m]BMI : {bmi}\n\033[0m")
		elif bmi == 25.0 or bmi >= 29.9:
			print(f"[\033[32m+\033[0m]Overweight (by {bmi} BMI.)\n\033[0m")
		else:
			print(f"[\033[32m+\033[0m]Obesity (by {bmi} BMI.)\n\033[0m")

	@staticmethod
	def exponent():
		base = eval(input("\n[\033[34m~\033[0m]Enter the base(x): "))
		power = eval(input("[\033[34m~\033[0m]Enter the power(e): "))
		ans = base ** power
		print("[\033[32m+\033[0m] " + str(base) + "^" + str(power) + " = " + str(ans))
		print("\033[0m")

	@staticmethod			
	def math13():
		print("\n[\033[34m~\033[0m]Press 1 to convert decimal to binary or 2 to convert decimal to hexadecimal or 3 to convert decimal to octal")
		choice = input().strip()
		if choice == "1":
			dec_num = int(input("\n[\033[34m~\033[0m]Enter the decimal number: "))
			print("[\033[32m+\033[0m]Binary number: " + str(bin(dec_num).lstrip("0b") + "\n"))
		elif choice == "2":
			num = int(input("\n[\033[34m~\033[0m]Enter the decimal number: "))
			print("[\033[32m+\033[0m]Hexadecimal number: " + str(hex(num) + "\n"))
		elif choice == "3":
			num = int(input("\n[\033[34m~\033[0m]Enter the decimal number: "))
			print("[\033[32m+\033[0m]Octal number: " + str(oct(num) + "\n"))
		else:
			print("[\033[31m✗\033[0m]Not a valid option.\n\033[0m")	

	@staticmethod
	def math14():
		print("\n[\033[34m~\033[0m]Press 1 to convert binary to decimal or 2 to convert hexadecimal to decimal or 3 to convert octal to decimal")
		choice = input().strip()
		if choice == "1":
			num = int(input("\n[\033[34m~\033[0m]Enter the binary number: "))
			s = 0
			i = 0 
			while num != 0:
				rem = num % 10
				s = s + rem * pow(2, i)
				num = int(num/10)
				i = i + 1
			print("[\033[32m+\033[0m]Decimal number: " + str(s) + "\n")
		elif choice == "2":
			hex_dec = input("\n[\033[34m~\033[0m]Enter the hexadecimal number: ")	
			dec = int(hex_dec, 16)
			print("[\033[32m+\033[0m]Decimal number: " + str(dec) + "\n")
		elif choice == "3":
			octal = input("\n[\033[34m~\033[0m]Enter the octal number: ")
			decimal = str(int(octal, 8))
			print("[\033[32m+\033[0m]Decimal number: " + str(decimal) + "\n")
		else:
			print("[\033[31m✗\033[0m]Not a valid option.\n\033[0m")

	@staticmethod
	def math15():
		pass

	@staticmethod
	def math16():
		pass

	@staticmethod
	def math17():
		pass

	@staticmethod
	def math18():
		pass

	@staticmethod
	def math19():
		pass

	@staticmethod
	def math20():
		pass

