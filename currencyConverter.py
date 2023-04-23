from colorama import Fore, Back, Style
import time as t
import random
welcomeMessage = "Welcome To Currency Converter v1.1\n"
print(welcomeMessage.center(55))
print("—————————————".center(55))

f = open("currencyDetails.txt")
lines = f.readlines()
	
currencyInfo = {}
for line in lines:
	parsed = line.split("\t")
	currencyInfo[parsed[0]] = float(parsed[1])
	
print("\nSome Currencies Are:")
print(Fore.GREEN)
	
	#colours = Fore.GREEN, Style.RESET_ALL
	
for keys in currencyInfo.keys():
	#	print(random.choice(colours))
	print("\n",keys)
		
print(Style.RESET_ALL)



def cC():	
	try:
		print("———————————————————————————————————————————————————————————")
		user = float(input("\nValue In INR: "))
		currencyCon = input("\nCurrency: ")
		print(Fore.YELLOW)
		print("\nCalculating.....")
		print(Style.RESET_ALL)
		t.sleep(4)
		calculation = float(currencyInfo[currencyCon])
		
		currency = f"{user} INR = {user * calculation} {currencyCon}."
		print(Fore.WHITE)	
		print("\n",currency)
		print(Style.RESET_ALL)
	
	except KeyError:
		print("\nInvalid Currency!")
		
	except:
		print("\nSomething Went Wrong!")
		exit()
		
if __name__ == "__main__":	
	cC()
	while(True):
		print("————————————————————————————————————————————————————————————")
		print(Fore.YELLOW)
		uChoice = input("\nWant To Continue With Project? (y For YES | n For NO): ")
		print(Style.RESET_ALL)
		if uChoice == "y":
			cC()
		else:
			print("\nThank You For Using Our System!")
			exit()