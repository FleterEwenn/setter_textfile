import argparse
import os

parser = argparse.ArgumentParser(prog="textpipe", description="Moteur de traitement de texte programmable ")

parser.add_argument('-o', '--output', help='fichier de sortie')
parser.add_argument('-i', '--input', help="fichier d'entrée")
parser.add_argument('-p', '--pipeline', help='pipeline de commande replace:old:new / ...')

args = parser.parse_args()

if not args.input or not args.output:
	raise Exception("il manque un fichier d'entrée ou de sortie")
elif not os.path.isfile(args.input) or not os.path.isfile(args.output):
	raise Exception("les fichiers mis en paramètre n'existent pas")

if args.pipeline:

	cmds = [cmd for cmd in args.pipeline.split('/')]

	for cmd in cmds:

		if cmd.startswith('replace'):

			current_cmd, old, new = cmd.split(':')
			with open(args.input, 'r') as file:
				text = file.read()
				words = text.split(' ')
				for i in range(len(words)):
					if words[i] == old:
						words[i]  = new
				file.close()
				
			with open(args.output, 'w') as file:
				for word in words:
					file.write(word + ' ')