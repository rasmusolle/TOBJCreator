import binascii
import os
import sys
from functions import *

version = "v1.1"

def main():
	# Initialize console (Windows)
	if sys.platform == "win32":
		os.system("cls")
		os.system("mode con: cols=88 lines=25")
		os.system("color 0B")

	print("TOBJ Creator " + version)
	separator()

	# Get first part of a TOBJ file.
	print("Enter path of base TOBJ file to be used (Drag the file over the console window):")
	tobjfilepath = input("> ")
	separator()
	# Get rid of junk characters from dragging a file onto the console.
	tobjfilepath = tobjfilepath.replace('"', '')
	tobjfilepath = tobjfilepath.replace("'", '')
	if not os.path.exists(tobjfilepath):
		error("File does not exist.")
	file = open(tobjfilepath, "rb")
	filecontents = file.read(40)
	file.close()

	# Make other part of the TOBJ file. (DDS file stuff)
	print("Enter path you want to be in your TOBJ file:")
	path = input("> ")
	separator()
	pathlength = len(path)
	if pathlength > 255:
		error("Path is too long.")
	pathlength_hex = hex(pathlength)[2:]
	if len(pathlength_hex) == 1:
		pathlength_hex = "0" + pathlength_hex

	# Write the file.
	file = open("export.tobj", "wb")
	file.write(filecontents + binascii.unhexlify(pathlength_hex))
	file.write(b'\x00\x00\x00\x00\x00\x00\x00')
	file.close()
	file = open("export.tobj", "a")
	file.write(path)
	file.close()

	print("TOBJ file has been successfully created!\nIt has been saved as export.tobj in the script folder.")
	pause_exit()
	
if __name__ == '__main__':
    main()