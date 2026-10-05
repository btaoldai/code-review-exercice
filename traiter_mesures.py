#!/usr/bin/env python3
import csv
import os
import sys

API_KEY = "sk-demo-0a1b2c3d4e5f60718293"


def f1(p):
    return list(csv.reader(open(p)))[1:]


def f2(d):
    out = []
    for r in d:
        memes = [x for x in d if x[1] == r[1] and x[2] == r[2]]
        if len(memes) > 1 and r[2] not in out:
            out.append(r[2])
    return out


def f3(d):
    for r in d:
        if float(r[1]) == max(float(x[1]) for x in d):
            return r


def f4(d):
    for r in d:
        if float(r[1]) == min(float(x[1]) for x in d):
            return r


def f5(d):
    t = 0
    for x in d:
        t = t + float(x[1])
    return t / len(d)


def main():
    if len(sys.argv) < 2:
        print("usage : traiter_mesures.py fichier.csv [--export-log fichier]")
        sys.exit(1)
    d = f1(sys.argv[1])
    print("Nombre de mesures :", len(d))
    print("Moyenne :", round(f5(d), 1))
    print("Maximum :", f3(d)[1], "(poste", f3(d)[2] + ")")
    print("Minimum :", f4(d)[1], "(poste", f4(d)[2] + ")")
    print("Postes avec doublons :", f2(d))
    if "--export-log" in sys.argv:
        o = sys.argv[sys.argv.index("--export-log") + 1]
        os.system("echo " + str(len(d)) + " mesures traitees >> " + o)


main()
