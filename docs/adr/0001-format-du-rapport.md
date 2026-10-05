# 0001 — Produire le rapport en texte tabulaire, pas en JSON

Statut : accepté — 6 octobre 2026

## Contexte

Le rapport est lu par des humains dans un terminal, chaque semaine, par le membre de l'atelier qui
tient le tableau de suivi. Le service de dépôt accepte aussi le JSON, mais l'atelier n'a aucun
outil de visualisation pour lire un rapport JSON, et personne ne souhaite en maintenir un.

## Options examinées

1. Rapport en JSON : lisible par machine, directement accepté par le service de dépôt ; illisible
   dans un terminal sans outil supplémentaire.
2. Rapport en texte tabulaire, converti en JSON au moment du dépôt : lisible immédiatement ;
   une conversion de plus à maintenir dans releve-cli.

## Décision

Option 2. Critère retenu : le premier lecteur du rapport est un humain devant un terminal.

## Conséquences

- Facile : vérifier un rapport à l'œil, sans outil ; relire un rapport ancien dans `rapports/`.
- Difficile : le dépôt vers le service demande une conversion, donc du code et des tests de plus.
- À surveiller : documenter le format exact des colonnes du rapport dans `docs/reglages.md` dès
  qu'il change ; cette fiche sera remplacée, pas réécrite, si le lecteur principal change.
