# Setter_textfile

## But du projet

Setter_textfile permet de realiser des tâches répetitives sur des fichiers de traitement de texte (pour l'instant .txt, .docx et .odt).  
Ces tâches sont :
* remplacer en mot par un autre
* mettre en majuscule un mot
* ou le mettre le minuscule
* afficher les statistiques
* mettre en capitale un mot

Ensuite elles sont sauvegardées dans un fichier de sortie (mis en paramètre au non) de la même extension que le fichier d'entrée.

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
* `upper` :
   * `upper:word` : met en majuscule tout les mots "word" rencontrés dans le fichier
   * `upper:word:letter` : met en majuscule toutes les lettres "letter" dans les mots "word" rencontrés dans le fichier 
* `lower` :
  * `lower:word` : idem que "upper" mais en minuscule
  * `lower:word:letter` : idem que "upper" mais en minuscule
* `stats` : donne les statistiques du fichier
* `capitalize:word` : capitalise le mot "word"
