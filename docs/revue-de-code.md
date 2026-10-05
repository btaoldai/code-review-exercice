# Exercice de revue de code — traiter_mesures.py

Un script Python est proposé comme contribution à releve-cli : il traite les relevés de niveau
déposés par les postes de l'atelier et affiche un résumé pour le tableau de suivi.

Ce dépôt est **le même pour tout le monde**. Il ne s'agit pas de votre production, mais d'un
code fourni, à relire comme vous relieriez la contribution d'un collègue.

## Organisation

- `main` ne contient pas le script.
- Une branche par relecteur, `feature/traiter-mesures-01` à `feature/traiter-mesures-18`, ajoute
  le script ; une **pull request** est ouverte pour chacune, de la branche vers `main`. Les scripts
  ne sont pas tous identiques. Vous relisez **votre** pull request, dont le numéro est annoncé en
  séance ; vous pouvez lire celles des autres, pas y déposer de revue.

| Fichier | Rôle |
|---|---|
| `traiter_mesures.py` | Le script à relire (présent sur les branches `feature/…`) |
| `exemples/releves.csv` | Un jeu de données d'exemple, 8 lignes |
| `exemples/releves-5000.csv` | Un jeu de 5 000 lignes, qui rend mesurable le défaut de performance |

## Exécuter le script

Si Python 3 est disponible sur votre poste (sinon, la lecture dans l'onglet *Files changed* suffit ;
l'exécution est projetée en séance) :

```bash
git clone https://github.com/btaoldai/code-review-exercice.git
cd code-review-exercice
git switch feature/traiter-mesures-07          # votre numéro
python3 traiter_mesures.py exemples/releves.csv
python3 traiter_mesures.py exemples/releves-5000.csv --export-log journal.txt
```

Résultat attendu : cinq lignes de résumé (nombre, moyenne, maximum, minimum, postes avec
doublons) ; sur 5 000 lignes, un temps d'exécution nettement plus long. Le fichier `journal.txt`
est exclu par `.gitignore`.

Une revue de code commence toujours par vérifier que ce qui est proposé fonctionne réellement.
N'exécutez pas de charge destructive pour « tester » un défaut : le lire et décrire sa conséquence
suffit.

## Ce qui est attendu de votre relecture

Ouvrez votre pull request et déposez vos commentaires **ancrés à la ligne concernée**
dans `traiter_mesures.py`, selon trois axes, l'axe indiqué dans le texte de chaque commentaire :

- **[lisibilité]** — noms de variables et de fonctions, longueur et responsabilité des fonctions,
  commentaires utiles ;
- **[performance]** — boucles répétées inutilement, opérations coûteuses réexécutées à chaque
  itération ;
- **[sécurité]** — valeurs sensibles écrites en dur, entrées utilisateur transmises sans
  validation à une commande système.

Un commentaire de ligne n'a pas de statut propre. Une fois vos commentaires déposés, soumettez
**une revue** (bouton *Review changes*) avec l'un des trois statuts :

- **Approve** — rien ne s'oppose à la fusion.
- **Request changes** — la fusion attend une correction.
- **Comment** — des remarques, sans prise de position sur la fusion.

Dans un projet réel, l'auteur pousse ensuite ses corrections et une nouvelle revue est soumise,
jusqu'à obtenir Approve : c'est la convergence vers un merge de qualité. Ici vous ne corrigez pas
ce code : vous conduisez la revue, le premier tour de cette boucle.
