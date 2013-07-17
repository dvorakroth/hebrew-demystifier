#!/usr/bin/env python3
#Hebrew Demystifier by Alex Dvořák-Roth -- Licensed under the WTFPLv2 -- http://www.wtfpl.net/txt/copying/
#Questions, complaints and comments to my github/e-mail plox.

from unicodedata import normalize
import argparse

def parse_arguments():
	parser = argparse.ArgumentParser(description='Demystify garbled Hebrew text')
	parser.add_argument('--mac_archive', dest='mac_archive', action='store_const',
		const=('mac_roman', 'cp856'), default=('cp1252', 'cp1255'),
		help='Parse Latin as mac_roman, and encode Hebrew with CP856 (how OSX sometimes extracts Hebrew archives)')
	args = parser.parse_args()
	return {"in_encoding": args.mac_archive[0], "out_encoding": args.mac_archive[1]}

def main(in_encoding, out_encoding):
	try:
		while True:
			original = normalize('NFC', input("Enter garbled Hebrew: ")) #We normalize because combining chars are a bitch
			try:
				asbytes = original.encode(in_encoding) #Read the garbled string
				print(str(asbytes, encoding=out_encoding)) #And output the demystified one.
				#(It's really that simple. I don't why OSs don't have this kind of shit built into the file manager or something)
			except UnicodeEncodeError:
				print("Invalid input string!")
			except UnicodeDecodeError:
				print("Does not result in a valid Hebrew string!")
	except KeyboardInterrupt:
		print("")
		return 0
	except EOFError:
		print("")
		return 0

if __name__ == "__main__":
	import sys
	sys.exit(main(**parse_arguments()))
