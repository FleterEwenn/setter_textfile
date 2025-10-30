import argparse
import os
import string
from pipeline_commands import Upper, Lower, Replace
from split_text import File_text

parser = argparse.ArgumentParser(prog="textpipe", description="Moteur de traitement de texte programmable ")

parser.add_argument('-o', '--output', help='fichier de sortie')
parser.add_argument('-i', '--input', help="fichier d'entrée")
parser.add_argument('-p', '--pipeline', help='pipeline de commande replace:old:new/lower:word/upper:word/stats/capitalize:word ...')

args = parser.parse_args()

if not args.input:
	raise Exception("il manque un fichier d'entrée")

elif not os.path.isfile(args.input):
	raise Exception(f"le fichier d'entrée {args.input} mis en paramètre n'existe pas")

current_file = File_text(str(args.input).lower())

if args.pipeline:

	cmds = [cmd for cmd in args.pipeline.split('/')]

	for cmd in cmds:

		if cmd.startswith('stats'):
			len_word = 0
			len_punctuation = 0
			if current_file.isdocx or current_file.isodt:
				for para in current_file.current_words:
					for elt in para:
						if elt.isalpha():
							len_word += 1
						elif elt in string.punctuation:
							len_punctuation += 1
			else:
				for elt in current_file.current_words:
					if elt.isalpha():
						len_word += 1
					elif elt in string.punctuation:
						len_punctuation += 1
			
			print("words : " + str(len_word))
			print("punctuation : " + str(len_punctuation))
		
		elif cmd.startswith('wordcount'):
			try:
				current_cmd, word_to_count = cmd.split(':')
			except:
				raise Exception(f"la commande {cmd} ne correspond pas au schéma wordcount:word")
			
			word_iteration = 0
			if current_file.isodt or current_file.isdocx:
				for para in current_file.current_words:
					for elt in para:
						if elt == word_to_count:
							word_iteration += 1
			else:
				for elt in current_file.current_words:
					if elt == word_to_count:
						word_iteration += 1
			
			print('word ' + '"' + word_to_count+ '"' + ' : ' + str(word_iteration))

		elif cmd.startswith('replace'):

			try:
				current_cmd, old, new = cmd.split(':')
			except:
				raise Exception(f"la commande {cmd} ne correspond pas au schéma replace:old:new")

			if current_file.isdocx or current_file.isodt:
				for i in range(len(current_file.current_words)):
					current_file.current_words[i] = Replace(old, new, current_file.current_words[i])

			else:
				current_file.current_words = Replace(old, new, current_file.current_words)

		elif cmd.startswith('upper'):

			if len(cmd.split(':')) == 2:
				current_cmd, word_to_upper = cmd.split(':')
				
				if current_file.isdocx or current_file.isodt:
					for i in range(len(current_file.current_words)):
						current_file.current_words[i] = Upper(current_file.current_words[i], word_to_upper)
				else:
					current_file.current_words = Upper(current_file.current_words, word_to_upper)

			elif len(cmd.split(':')) == 3:
				current_cmd, word_target, letter_to_upper = cmd.split(':')

				if current_file.isdocx or current_file.isodt:
					for i in range(len(current_file.current_words)):
						current_file.current_words[i] = Upper(current_file.current_words[i], word_target, letter=letter_to_upper)
				else:
					current_file.current_words = Upper(current_file.current_words, word_target, letter=letter_to_upper)

		elif cmd.startswith('lower'):

			if len(cmd.spit(':')) == 2:
				current_cmd, word_to_lower = cmd.split(':')
				if current_file.isdocx or current_file.isodt:
					for i in range(len(current_file.current_words)):
						current_file.current_words[i] = Lower(current_file.current_words[i], word_to_lower)
				else:
					current_file.current_words = Lower(current_file.current_words, word_to_lower)

			elif len(cmd.split(':')) == 3:
				current_cmd, word_target, letter_to_upper = cmd.split(':')
				if current_file.isdocx or current_file.isodt:
					for i in range(len(current_file.current_words)):
						current_file.current_words[i] = Lower(current_file.current_words[i], word_target, letter=letter_to_upper)
				else:
					current_file.current_words = Lower(current_file.current_words, word_target, letter=letter_to_upper)
		
		elif cmd.startswith('capitalize'):

			try:
				current_cmd, word_to_capitalize = cmd.split(':')
			except:
				raise Exception(f"la commande {cmd} ne correspond pas au schéma capitalize:word")

			if args.input.lower().endswith('.docx'):
				for i in range(len(current_file.current_words)):
					current_file.current_words[i] = Upper(current_file.current_words[i], word_to_capitalize, letter=word_to_capitalize[0])
			else:
				current_file.current_words = Upper(current_file.current_words, word_to_capitalize, letter=word_to_capitalize[0])

		else:
			raise Exception(f"la commande {cmd} n'exite pas")

current_file.save(args.output)