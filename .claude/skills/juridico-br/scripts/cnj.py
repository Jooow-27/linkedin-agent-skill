#!/usr/bin/env python3
"""Valida (ou completa) número de processo no padrão CNJ (Res. CNJ 65/2008).

Formato: NNNNNNN-DD.AAAA.J.TR.OOOO  — DD calculado pelo módulo 97 (ISO 7064).

  python3 cnj.py 0001234-56.2025.8.26.0100     # valida
  python3 cnj.py 0001234-??.2025.8.26.0100     # calcula o dígito
  python3 cnj.py 00012345620258260100          # aceita só dígitos

Número VÁLIDO não significa processo EXISTENTE: só prova que não foi digitado
errado. A existência deve ser conferida na consulta pública do tribunal.
"""
import re
import sys

J = {"1": "STF", "2": "CNJ", "3": "STJ", "4": "Justiça Federal", "5": "Justiça do Trabalho",
     "6": "Justiça Eleitoral", "7": "Justiça Militar da União", "8": "Justiça Estadual",
     "9": "Justiça Militar Estadual"}


def dv(n, a, j, tr, o):
    return 98 - (int(f"{n}{a}{j}{tr}{o}00") % 97)


def main(arg):
    s = arg.strip()
    m = re.fullmatch(r"(\d{1,7})-(\d{2}|\?\?)\.(\d{4})\.(\d)\.(\d{2})\.(\d{4})", s)
    if not m:
        dig = re.sub(r"\D", "", s)
        if len(dig) != 20:
            print(f"FORMATO INVÁLIDO: {s}")
            return 2
        m = (dig[:7], dig[7:9], dig[9:13], dig[13], dig[14:16], dig[16:])
    else:
        m = m.groups()
    n, d, a, j, tr, o = m
    n = n.zfill(7)
    calc = dv(n, a, j, tr, o)
    fmt = f"{n}-{calc:02d}.{a}.{j}.{tr}.{o}"
    seg = J.get(j, "segmento desconhecido")
    if d == "??":
        print(f"DÍGITO CALCULADO: {fmt}  ({seg}, TR {tr}, origem {o})")
        return 0
    if int(d) == calc:
        print(f"VÁLIDO: {fmt}  ({seg}, TR {tr}, origem {o})")
        return 0
    print(f"INVÁLIDO: dígito informado {d}, esperado {calc:02d} -> {fmt}")
    return 1


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(max(main(x) for x in sys.argv[1:]))
