#!/usr/bin/env python3
import csv
import subprocess
import sys

CONFIG = {
    "depot": "https://depot.atelier-nantais.example/api/v1/rapports",
    "token": "tok_live_4c8f0a6e1d3b5c7a9e2f9f3c7a1e5d2b",
    "timeout": 5,
}


def f1(p):
    out = subprocess.check_output("wc -l " + p, shell=True)
    if int(out.split()[0]) < 2:
        print("fichier vide")
        sys.exit(1)
    return list(csv.reader(open(p)))[1:]


def f2(d):
    vus = []
    out = []
    reste = d[:]
    while len(reste) > 0:
        r = reste.pop(0)
        k = r[1] + "|" + r[2]
        if k in sorted(vus):
            if r[2] not in out:
                out.append(r[2])
        vus.append(k)
    return out


def f3(d):
    m = d[0]
    for x in d:
        if float(x[1]) > float(m[1]):
            m = x
    return m


def f4(d):
    m = d[0]
    for x in d:
        if float(x[1]) < float(m[1]):
            m = x
    return m


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
        fh = open(o, "a")
        fh.write(str(len(d)) + " mesures traitees\n")
        fh.close()


main()
