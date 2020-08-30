#!/usr/bin/python3

import os
import banners
from Formulae.formulae import formulae

			#####################################################
			#             Defining the main function            #
			#####################################################
		
menu = """
\033[94m [*]Quit(q) or Exit(0); Clear the terminal(clear); banner(dispaly a cool banner); help(to show the commands.)

\033[36m [1 ]Find out area of a circle.                             [11]BMI Calculator.
 [2 ]Find factorial.			 		    [12]Find x^e
 [3 ]Convert Celsius to Fahrenheit.	 		    [13]Convert decimal to binary, hexadecimal or octal.
 [4 ]Find square or sq.rt of a number.	 		    [14]Convert binary, hexadecimal or octal to decimal.
 [5 ]Find area of a rectangle.		 		    [15]coming soon...
 [6 ]Find Perimeter of a rectangle.			    [16]coming soon...
 [7 ]Find out the volume of a sphere.			    [17]coming soon...
 [8 ]Find area of a triangle.				    [18]coming soon...
 [9 ]Display the multiplication table of a given number.    [19]coming soon...
 [10]Find details of a square(i.e. Area & Perimeter).       [20]coming soon...
"""

def main():
	math = formulae()
	while True:
		cmnd = input("""\033[31m┌─[\033[01mroot\033[93m@\033[0m\033[96mmath-user\033[0m\033[31m]-[\033[92m/\033[31m]\n└──╼ \033[93m#\033[0m\033[37m""").lower().strip()
		if cmnd == "q" or cmnd == "0" or cmnd == "exit" or cmnd == "quit":
			print("\nThank You for using the MATH Shell.\nBye.\n")
			break
		if cmnd == "clear":
			os.system("clear")
		elif cmnd == "help":
			print(menu)
		elif cmnd == "banner":
			print(banners.banner())
		elif cmnd == "":
			continue
		elif cmnd == "1":
			try:
				math.ArCircle()
			except Exception as e:
				print("[\033[31m✗\033[0m]\033[31mERROR\033[0m: " + str(e) + "\n")
		elif cmnd == "2":
			try:
				math.factorial()
			except Exception as e:
				print("[\033[31m✗\033[0m]\033[31mERROR\033[0m: " + str(e) + "\n")
		elif cmnd == "3":
			try:
				math.celsius2F()
			except Exception as e:
				print("[\033[31m✗\033[0m]\033[31mERROR\033[0m: " + str(e) + "\n")
		elif cmnd == "4":
			try:
				math.sqrORsqrt()
			except Exception as e:
				print("[\033[31m✗\033[0m]\033[31mERROR\033[0m: " + str(e) + "\n")
		elif cmnd == "5":
			try:
				math.arRect()
			except Exception as e:
				print("[\033[31m✗\033[0m]\033[31mERROR\033[0m: " + str(e) + "\n")
		elif cmnd == "6":
			try:
				math.pRect()
			except Exception as e:
				print("[\033[31m✗\033[0m]\033[31mERROR\033[0m: " + str(e) + "\n")
		elif cmnd == "7":
			try:
				math.vSphere()
			except Exception as e:
				print("[\033[31m✗\033[0m]\033[31mERROR\033[0m: " + str(e) + "\n")
		elif cmnd == "8":
			try:
				math.arTriangle()
			except Exception as e:
				print("[\033[31m✗\033[0m]\033[31mERROR\033[0m: " + str(e) + "\n")
		elif cmnd == "9":
			try:
				math.mulTable()
			except Exception as e:
				print("[\033[31m✗\033[0m]\033[31mERROR\033[0m: " + str(e) + "\n")
		elif cmnd == "10":
			try:
				math.sqDetails()
			except Exception as e:
				print("[\033[31m✗\033[0m]\033[31mERROR\033[0m: " + str(e) + "\n")
		elif cmnd == "11":
			try:
				math.BMIcalc()
			except Exception as e:
				print("[\033[31m✗\033[0m]\033[31mERROR\033[0m: " + str(e) + "\n")
		elif cmnd == "12":
			try:
				math.exponent()
			except Exception as e:
				print("[\033[31m✗\033[0m]\033[31mERROR\033[0m: " + str(e) + "\n")
		elif cmnd == "13":
			try:
				math.math13()
			except Exception as e:
				print("[\033[31m✗\033[0m]\033[31mERROR\033[0m: " + str(e) + "\n")
		elif cmnd == "14":
			try:
				math.math14()
			except Exception as e:
				print("[\033[31m✗\033[0m]\033[31mERROR\033[0m: " + str(e) + "\n")
		elif cmnd == "15":
			print("coming soon...")
			continue
		elif cmnd == "16":
			print("coming soon...")
			continue
		elif cmnd == "17":
			print("coming soon...")
			continue
		elif cmnd == "18":
			print("coming soon...")
			continue
		elif cmnd == "19":
			print("coming soon...")
			continue
		elif cmnd == "20":
			print("coming soon...")
			continue
		else:
			print("math: " + cmnd + ":" + " command not found")
			#os.system(cmnd)

			########################################################
			#              Handling the main function              #
			########################################################
		
while True:
	try:
		password = input("[math] password for math-user: ")
	except KeyboardInterrupt:
		print()
		exit()
	except EOFError:
		print("\nmath: no password was provided")
		exit()
	if password == "password":
		print(banners.banner(), menu)
		try:
			main()
		except KeyboardInterrupt:
			print("\n\nThank You for using the MATH Shell.\nBye.\n")
		except EOFError:
			print("exit")
			print("\nThank You for using the MATH Shell.\nBye.\n")
			exit()
		except Exception as e:
			print("[\033[31m✗\033[0m]\033[31mERROR\033[0m: " + str(e) + "\n")
		break 
	else:
		print("Sorry, try again.")

