import os
import sys

def separator():
	print("=======================================================================================")

def error(message):
	print("Error - " + message)

def pause_exit():
	if sys.platform == "linux" or sys.platform == "linux2":
		sys.exit(0)
	elif sys.platform == "win32":
		print("Press any key to exit the program...")
		os.system("pause >nul")
		sys.exit(0)
	else:
		sys.exit(0)