# Réglages de releve-cli

Référence : ce document se consulte, il ne se lit pas d'un bout à l'autre. Les valeurs réelles se
placent dans `config.txt`, jamais dans ce document ni dans `config.example.txt`.

## Réglages

| Réglage | Valeur par défaut | Valeurs acceptées | Rôle |
|---|---|---|---|
| `CHEMIN_RELEVES` | `exemples/releves.csv` | Chemin de fichier existant, relatif à la racine du dépôt | Fichier de relevés à traiter |
| `DOSSIER_RAPPORT` | `rapports/` | Dossier existant ou créable | Dossier où le rapport de synthèse est écrit |
| `API_KEY` | `cle-d-exemple-a-remplacer` | Jeton fourni par le service de dépôt | Authentification auprès du service de dépôt des rapports ; valeur réelle uniquement dans `config.txt` |
| `INTERVALLE` | `300` | Nombre entier, en secondes | Délai entre deux rapports en mode continu |

## Format du fichier de relevés

Fichier CSV, séparateur virgule, encodage UTF-8, première ligne d'en-tête :

| Colonne | Contenu | Exemple |
|---|---|---|
| `horodatage` | Date et heure ISO 8601 de la mesure | `2026-10-06T06:00:00` |
| `niveau_pct` | Niveau mesuré, en pourcentage, nombre décimal | `71.2` |
| `identifiant_poste` | Identifiant du poste de relevé | `poste-01` |

Deux fichiers d'exemple sont fournis : `exemples/releves.csv` (8 lignes, dont un doublon volontaire
sur `poste-1`) et `exemples/releves-5000.csv` (5 000 lignes, pour mesurer un temps de traitement).
