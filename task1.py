import os
import pyttsx3

print()
print("\t\t\t\t========================================")
print("\t\t\t\t||  Tell me, what can I do for you?   ||")
print("\t\t\t\t========================================")
pyttsx3.speak("Tell me, what can I do for you?")
global y

def my():
	if ("run" in x):
		pyttsx3.speak("running " + y)
	elif ("launch" in x):
		pyttsx3.speak("launching " + y)
	elif ("open" in x):
		pyttsx3.speak("opening " + y)
	else:
		print("Nothing")

print()

print("Sample Input : 'run notepad' or 'open paint' or 'launch chrome'")
while True:
	x = input(" Enter the program to launch: ").lower()
	if ((("run" in x) or ("open" in x) or ("launch" in x)) and (("notepad" in x) or ("editor" in x))):
		y = "notepad"
		my()
		os.system(y)
		print(" ------------------------------------")
	elif ((("run" in x) or ("open" in x) or ("launch" in x)) and (("explorer" in x) or ("fileexplorer" in x))):
		y = "file explorer"
		my()
		os.system("explorer")
		print(" ------------------------------------")
	elif ((("run" in x) or ("open" in x) or ("launch" in x)) and ("chrome" in x)):
		y = "chrome"
		my()
		os.system(y)
		print(" ------------------------------------")
	elif ((("run" in x) or ("open" in x) or ("launch" in x)) and (("ppt" in x) or ("powerpnt" in x) or ("powerpoint" in x))):
		y = "powerpoint"
		my()
		os.system("powerpoint")
		print(" ------------------------------------")
	elif ((("run" in x) or ("open" in x) or ("launch" in x)) and (("winword" in x) or ("word" in x) or ("msword" in x))):
		y = "MS Word"
		my()
		os.system("winword")
		print(" ------------------------------------")
	elif ((("run" in x) or ("open" in x) or ("launch" in x)) and (("excel" in x) or ("msexcel" in x))):
		y = "MS excel"
		my()
		os.system("excel")
		print(" ------------------------------------")
	elif ((("run" in x) or ("open" in x) or ("launch" in x)) and (("paint" in x) or ("mspaint" in x))):
		y = "MS paint"
		my()
		os.system("mspaint")
		print(" ------------------------------------")
	elif (("exit" in x) or ("close" in x) or ("terminate" in x)):
		print("\n :) See you next time!")
		pyttsx3.speak("See you next time")
		break
	else:
		print(" :( Wrong Input!")
		pyttsx3.speak("Wrong Input, try again")
		print(" ------------------------------------")
print()