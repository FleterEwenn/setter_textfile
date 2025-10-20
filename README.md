# Setter_textfile

## But du projet

Setter_textfile permet de realiser des tâches répetitives sur des fichiers de traitement de texte (pour l'instant .txt et .docx).  
Ces tâches sont :
* remplacer en mot par un autre (dans le tout fichier)
* mettre en majuscule un mot
* ou le mettre le minuscule

Ensuite elles sont sauvegardées dans un fichier de sortie de la même extension que le fichier d'entrée.

## Téléchargement du repository

Il suffit de le cloner et d'installer les dépendancesc:  
```
git clone https://github.com/FleterEwenn/setter_textfile.git
pip install -r requirements.txt
```

## Execution du code

### Exécution

Setter_textfile est en CLI, ainsi main.py s'éxécute dans un terminale et le code parse les arguments.  
Voici le schéma d'éxécution avec les arguments :  
>chemin_vers_main\main.py -i chemin_vers_le_fichier_de_sortie\nomdufichier.txt -o idem_pour_le_fichier_de_sortie.txt -p commandes_à_éxécuter

Voici un exemple d'éxécution du code où on considére être dans le dossier ou se trouve main.py :  
`main.py -i C:\Users\Desktop\input.txt -o C:\Users\Desktop\output.txt -p replace:bonjour:bonsoir`

### Commandes disponible dans le pipeline

***Attention :*** **l'odre dans lequel les commandes sont écrites est très important.**

* `replace:old:new` : remplace tous les mots "old" rencontrés dans le fichier par le "new"
* `upper:word` : met en majuscule tout les mots "word" rencontrés dans le fichier
* `lower:word` : met en minuscule tout les mots "word" rencontrés dans le fichier
