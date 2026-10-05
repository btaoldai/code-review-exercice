# Démarrage de releve-cli

Guide pas à pas pour un premier rapport. Pour la liste des réglages, voir [`reglages.md`](reglages.md).

Prérequis : Python 3, Git, un fichier de relevés au format CSV (voir `reglages.md`, section « Format
du fichier de relevés »).

1. Cloner le dépôt et se placer dans le dossier du projet :

   ```
   git clone https://github.com/btaoldai/code-review-exercice.git
   cd code-review-exercice
   ```

2. Copier `config.example.txt` sous le nom `config.txt` :

   ```
   cp config.example.txt config.txt
   ```

3. Ouvrir `config.txt` et inscrire le chemin du fichier de relevés dans `CHEMIN_RELEVES`
   (par défaut `exemples/releves.csv`, qui convient pour un premier essai).

4. Lancer l'outil :

   ```
   python3 releve.py --config config.txt
   ```

Résultat attendu : un rapport de synthèse s'affiche (nombre de mesures, moyenne, maximum,
minimum, postes en doublon), un fichier de rapport apparaît dans `rapports/`, et
`git status` ne propose ni `config.txt` ni `rapports/` : les deux sont exclus par `.gitignore`.

En cas d'échec : `FileNotFoundError` signale un chemin de relevés incorrect dans `config.txt` ;
`PermissionError` sur `rapports/` signale un dossier non inscriptible — le créer ou changer
`DOSSIER_RAPPORT`.
