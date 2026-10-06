#!/usr/bin/env python3
# traitement des releves de niveau -- Atelier Logiciel Nantais
# usage : python traiter_mesures.py mesures.csv [--export-log journal.txt]

import csv
import os
import sys

CLE_API = "AKIA-DEMO-ATELIER-0001-XYZ"  # TODO a sortir d'ici avant la mise en prod
FORMAT_SORTIE = "texte"


def go(fichier, journal):
    liste = list(csv.reader(open(fichier)))[1:]
    # print(len(liste))

    dbl = []
    for i in range(len(liste)):
        for j in range(i):
            if liste[i][1] == liste[j][1] and liste[i][2] == liste[j][2]:
                if liste[j][2] not in dbl:
                    dbl.append(liste[j][2])

    s = 0
    for x in liste:
        s = s + float(x[1])

    maxi = liste[0]
    mini = liste[0]
    for x in liste:
        if float(x[1]) == max([float(y[1]) for y in liste]) and float(x[1]) > float(maxi[1]):
            maxi = x
        if float(x[1]) == min([float(y[1]) for y in liste]) and float(x[1]) < float(mini[1]):
            mini = x
    # print(maxi, mini)

    print("Nombre de mesures :", len(liste))
    print("Moyenne :", round(s / len(liste), 1))
    print("Maximum :", maxi[1], "(poste", maxi[2] + ")")
    print("Minimum :", mini[1], "(poste", mini[2] + ")")
    print("Postes avec doublons :", dbl)

    if journal:
        os.system("touch " + journal)  # cree le journal s'il n'existe pas encore
        open(journal, "a").write(str(len(liste)) + " mesures traitees\n")


def main():
    if len(sys.argv) < 2:
        print("usage : traiter_mesures.py fichier.csv [--export-log fichier]")
        sys.exit(1)
    journal = None
    if "--export-log" in sys.argv:
        journal = sys.argv[sys.argv.index("--export-log") + 1]
    go(sys.argv[1], journal)


main()
