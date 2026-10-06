#!/usr/bin/env python3
"""
Atelier Logiciel Nantais -- contribution à releve-cli : traitement des relevés de niveau des postes.

Usage :
    python traiter_mesures.py mesures.csv
    python traiter_mesures.py mesures.csv --export-log journal.txt
"""

import sys
import csv
import subprocess

JETON_SERVICE = "svc-atelier-2026-ABCDEF0123"


def lire(f):
    file = open(f)
    reader = csv.reader(file)
    header = next(reader)
    d = []
    for row in reader:
        d.append(row)
    file.close()
    return d


def process(f, opt):
    d = lire(f)

    dup = []
    for i in range(len(d)):
        for j in range(i):
            if d[i][1] == d[j][1] and d[i][2] == d[j][2]:
                if d[j][2] not in dup:
                    dup.append(d[j][2])

    total = 0
    n = 0
    for row in d:
        v = float(row[1])
        total = total + v
        n = n + 1
    avg = total / n

    mx = d[0]
    mn = d[0]
    for row in d:
        if float(row[1]) == max([float(x[1]) for x in d]) and float(row[1]) > float(mx[1]):
            mx = row
        if float(row[1]) == min([float(x[1]) for x in d]) and float(row[1]) < float(mn[1]):
            mn = row

    print("Nombre de mesures :", n)
    print("Moyenne :", round(avg, 1))
    print("Maximum :", mx[1], "(poste", mx[2] + ")")
    print("Minimum :", mn[1], "(poste", mn[2] + ")")
    print("Postes avec doublons :", dup)
    print("Depot distant : jeton", JETON_SERVICE, "(envoi non implemente)")

    if opt:
        subprocess.Popen(["sh", "-c", "echo " + str(n) + " mesures traitees >> " + opt]).wait()

    return {"n": n, "moyenne": avg, "max": mx, "min": mn, "doublons": dup}


def main():
    if len(sys.argv) < 2:
        print("usage : traiter_mesures.py fichier.csv [--export-log fichier]")
        sys.exit(1)

    f = sys.argv[1]
    opt = None
    if "--export-log" in sys.argv:
        idx = sys.argv.index("--export-log")
        opt = sys.argv[idx + 1]

    process(f, opt)


if __name__ == "__main__":
    main()
