import binascii
import os
import sys
import tempfile
from functions import *

version = "v1.1"

def main(tobjfilepath = False,path = False,tobjoutpath = False):
	successful = False
	selected = False

	# Initialize console (Windows)
	if sys.platform == "win32" and len(sys.argv) < 4 and not tobjfilepath:
		os.system("cls")
		os.system("mode con: cols=88 lines=25")
		os.system("color 0B")

	print("TOBJ Creator " + version)
	separator()

	# Get first part of a TOBJ file.
	if not tobjfilepath:
		while not successful:
			print("Enter path of base TOBJ file to be used (Drag the file over the console window):")
			tobjfilepath = input("> ")
			separator()
			# Get rid of junk characters from dragging a file onto the console.
			tobjfilepath = stripquotes(tobjfilepath)
			if not os.path.exists(tobjfilepath):
				error("File does not exist.")
			else:
				successful = True
	else:
		if not os.path.exists(tobjfilepath):
			error("File does not exist.")
	file = open(tobjfilepath, "rb")
	filecontents = file.read(40)
	file.close()
	successful = False

	# Make other part of the TOBJ file. (DDS file stuff)
	if not path:
		while not successful:
			print("Enter path you want to be in your TOBJ file:")
			path = input("> ")
			separator()
			pathlength = len(path)
			if pathlength > 255:
				error("Path is too long.")
			else:
				successful = True
	else:
		pathlength = len(path)
		if pathlength > 255:
			error("Path is too long.")
	pathlength_hex = hex(pathlength)[2:]
	if len(pathlength_hex) == 1:
		pathlength_hex = "0" + pathlength_hex
	successful = False

	# Input destination of TOBJ file.
	if not tobjoutpath:
		while not successful:
			print("Enter destination of TOBJ file:")
			tobjoutpath = input("> ")
			separator()
			# Get rid of junk characters from dragging a file onto the console.
			tobjoutpath = stripquotes(tobjoutpath)
			if os.path.exists(tobjoutpath):
				while not selected:
					print("Destination already exists. Overwrite? [Y/N]")
					overwrite = input("> ")
					if overwrite == "y" or overwrite == "Y":
						selected = True
						successful = True
					if overwrite == "n" or overwrite == "N":
						selected = True
					separator()
				selected = False
			else:
				successful = True

	# Write the file.
	file = open(tobjoutpath, "wb")
	file.write(filecontents + binascii.unhexlify(pathlength_hex))
	file.write(b'\x00\x00\x00\x00\x00\x00\x00')
	file.close()
	file = open(tobjoutpath, "a")
	file.write(path)
	file.close()

	print("TOBJ file has been successfully created!")
	if len(sys.argv) < 4 and __name__ == '__main__':
		pause_exit()


if __name__ == '__main__':
	if len(sys.argv) < 4:
		main()
	else:
		main(sys.argv[1],sys.argv[2],sys.argv[3])
