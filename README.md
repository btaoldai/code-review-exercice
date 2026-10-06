# releve-cli — Atelier Logiciel Nantais

releve-cli est l'outil en ligne de commande de l'Atelier Logiciel Nantais : il lit un fichier de
relevés au format CSV (une mesure horodatée par ligne, poste par poste) et produit un rapport de
synthèse en texte tabulaire : nombre de mesures, moyenne, maximum, minimum, postes en doublon.
Il s'adresse aux membres de l'atelier qui tiennent le tableau de suivi hebdomadaire.

Ce dépôt est aussi le support de l'**exercice de revue de code** du module *Travail collaboratif
& documentation technique* : voir la section [Exercice de revue de code](#exercice-de-revue-de-code).

## Installation et démarrage

Prérequis : Python 3 installé, Git, un fichier de relevés au format décrit dans
[`docs/reglages.md`](docs/reglages.md).

1. Récupérer le dépôt et se placer dedans :

   ```
   git clone https://github.com/btaoldai/code-review-exercice.git
   cd code-review-exercice
   ```

2. Copier la configuration d'exemple, puis renseigner `CHEMIN_RELEVES` dans `config.txt` :

   ```
   cp config.example.txt config.txt
   ```

3. Lancer l'outil sur le fichier d'exemple :

   ```
   python3 releve.py --config config.txt
   ```

Résultat attendu : le rapport de synthèse s'affiche (nombre de mesures, moyenne, maximum,
minimum, postes en doublon) et `git status` ne montre aucun fichier `config.txt` à ajouter.

Cas d'échec le plus courant : `FileNotFoundError` sur le fichier de relevés — vérifier le chemin
inscrit dans `CHEMIN_RELEVES`, relatif à la racine du dépôt.

## Usage

### Produire le rapport de la semaine

Placer le fichier exporté par les postes dans `exemples/`, renseigner son chemin dans
`config.txt`, lancer la commande du démarrage : le rapport s'affiche et une copie est écrite dans
le dossier `DOSSIER_RAPPORT`.

### Changer le fichier de relevés traité

Modifier la seule ligne `CHEMIN_RELEVES=` de `config.txt`. Aucun autre réglage ne change.

## Architecture

releve-cli lit un fichier local, calcule la synthèse, écrit le rapport dans un dossier local et peut
le transmettre à un service de dépôt extérieur à l'atelier, qui n'est pas maintenu ici.

Schéma détaillé : [`docs/architecture.md`](docs/architecture.md).

## Organisation du dépôt

| Chemin | Contenu |
|---|---|
| `README.md` | Cette page : présentation, installation, usage, architecture. |
| `docs/demarrage.md` | Guide détaillé de démarrage. |
| `docs/reglages.md` | Référence des réglages et format du fichier de relevés. |
| `docs/architecture.md` | Schéma d'architecture, légende, périmètre, date. |
| `docs/adr/` | Fiches de décision technique, numérotées, jamais réécrites. |
| `docs/revue-de-code.md` | Consignes de l'exercice de revue de code. |
| `CHANGELOG.md` | Journal des versions, à destination des utilisateurs. |
| `config.example.txt` | Modèle de configuration, sans valeur réelle. |
| `exemples/` | Fichiers de relevés d'exemple (8 lignes et 5 000 lignes). |
| `releve.py` | Programme principal — en cours d'intégration, voir les pull requests ouvertes. |

## Contribution

- Une branche par sujet, nommée `docs/…`, `feat/…`, `fix/…` ou `chore/…`.
- Un message d'enregistrement préfixé par `feat`, `fix`, `docs` ou `chore` (Conventional Commits).
- Toute modification passe par une pull request décrite en trois parties (contexte, changements,
  impact), relue par une personne qui ne l'a pas écrite : commentaires ancrés aux lignes, puis une
  revue avec un statut unique, Approve, Request changes ou Comment.
- Aucune valeur réelle de configuration n'est enregistrée dans le dépôt : `config.txt` est exclu
  par `.gitignore`.

## Exercice de revue de code

Une contribution `feat: ajouter le traitement des relevés de niveau des postes` est proposée en
pull request, **une par relecteur** (branches `feature/traiter-mesures-01` à `-18`) : chacun réserve une pull request libre par un
premier commentaire, une par personne (travail individuel). Chaque relecteur relit la sienne sur trois axes — lisibilité, performance, sécurité — et
soumet une revue. Consignes complètes : [`docs/revue-de-code.md`](docs/revue-de-code.md).

```
git switch feature/traiter-mesures-07          # la pull request que vous avez réservée
python3 traiter_mesures.py exemples/releves.csv
python3 traiter_mesures.py exemples/releves-5000.csv --export-log journal.txt
```

## Contact

Atelier Logiciel Nantais — pour toute question, ouvrez une issue sur ce dépôt.
