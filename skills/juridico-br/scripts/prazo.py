#!/usr/bin/env python3
"""Calculadora de prazos processuais brasileiros (sem dependências).

Uso:
  python3 prazo.py 2026-03-02 15                    # CPC, dias úteis
  python3 prazo.py 2026-03-02 8 --regime clt
  python3 prazo.py 2026-03-02 5 --regime cpp       # dias corridos
  python3 prazo.py 2026-03-02 15 --dobro            # Fazenda/MP/Defensoria
  python3 prazo.py 2026-03-02 15 --feriado 2026-03-19 --feriado 2026-04-23
  python3 prazo.py 2026-03-02 15 --suspensao 2026-03-10:2026-03-12

A data informada é a do EVENTO que deflagra o prazo (ex.: intimação/publicação
considerada). O dia do começo é excluído e o do vencimento incluído (CPC 224).
Para DJEN/DJe, informe a data da PUBLICAÇÃO (o 1º dia útil seguinte à
disponibilização) — veja references/prazos.md.

Regimes:
  cpc  dias úteis; suspensão de 20/12 a 20/01 (CPC 220)
  clt  dias úteis; suspensão de 20/12 a 20/01 (CLT 775-A)
  jec  dias úteis (Lei 9.099/95, art. 12-A); recesso de 20/12 a 20/01
  cpp  dias corridos (CPP 798); se vencer em dia não útil, prorroga (798, §3º);
       não há suspensão no recesso
  material  dias corridos, sem prorrogação (prescrição/decadência: conferir regra
       específica — ex.: CC 132, §1º prorroga só quando a lei manda)

LIMITES: considera só feriados NACIONAIS (Lei 662/49, Lei 6.802/80, Lei
14.759/2023), Carnaval (segunda e terça), Sexta-feira Santa e Corpus Christi
(dias sem expediente forense na maioria dos tribunais). A Quarta-feira de
Cinzas (expediente a partir das 12h) é contada como útil; use --cinzas para
excluí-la quando o tribunal suspender os prazos. Feriados estaduais e
municipais, portarias de suspensão e indisponibilidade do sistema devem ser
informados com --feriado / --suspensao. Sempre confira o calendário do tribunal.
"""
import argparse
import datetime as dt
import sys


def pascoa(ano: int) -> dt.date:
    a = ano % 19
    b, c = divmod(ano, 100)
    d, e = divmod(b, 4)
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i, k = divmod(c, 4)
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    mes = (h + l - 7 * m + 114) // 31
    dia = ((h + l - 7 * m + 114) % 31) + 1
    return dt.date(ano, mes, dia)


def feriados(ano: int, cinzas: bool) -> dict:
    p = pascoa(ano)
    f = {
        dt.date(ano, 1, 1): "Confraternização Universal",
        dt.date(ano, 4, 21): "Tiradentes",
        dt.date(ano, 5, 1): "Dia do Trabalho",
        dt.date(ano, 9, 7): "Independência",
        dt.date(ano, 10, 12): "N. Sra. Aparecida",
        dt.date(ano, 11, 2): "Finados",
        dt.date(ano, 11, 15): "Proclamação da República",
        dt.date(ano, 12, 25): "Natal",
        p - dt.timedelta(days=48): "Carnaval (segunda)",
        p - dt.timedelta(days=47): "Carnaval (terça)",
        p - dt.timedelta(days=2): "Sexta-feira Santa",
        p + dt.timedelta(days=60): "Corpus Christi",
    }
    if ano >= 2024:
        f[dt.date(ano, 11, 20)] = "Zumbi e Consciência Negra (Lei 14.759/2023)"
    # Lei 5.010/66, art. 62: feriados da Justiça Federal (11/08, 01/11, 08/12,
    # Semana Santa de quarta a domingo) — ative com --federal.
    if cinzas:
        f[p - dt.timedelta(days=46)] = "Quarta-feira de Cinzas"
    return f


def parse(s: str) -> dt.date:
    return dt.date.fromisoformat(s)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("inicio", help="data do evento (AAAA-MM-DD)")
    ap.add_argument("dias", type=int)
    ap.add_argument("--regime", choices=["cpc", "clt", "jec", "cpp", "material"], default="cpc")
    ap.add_argument("--dobro", action="store_true", help="CPC 180/183/186/229")
    ap.add_argument("--feriado", action="append", default=[], help="AAAA-MM-DD (repetível)")
    ap.add_argument("--suspensao", action="append", default=[], help="AAAA-MM-DD:AAAA-MM-DD (repetível)")
    ap.add_argument("--cinzas", action="store_true", help="tratar Quarta de Cinzas como não útil")
    ap.add_argument("--federal", action="store_true", help="incluir feriados da Lei 5.010/66 (JF/JT/TRFs)")
    ap.add_argument("--verbose", "-v", action="store_true")
    a = ap.parse_args()

    inicio = parse(a.inicio)
    dias = a.dias * (2 if a.dobro else 1)
    extra = {parse(x): "informado pelo usuário" for x in a.feriado}
    susp = []
    for s in a.suspensao:
        x, y = s.split(":")
        susp.append((parse(x), parse(y)))

    cache = {}

    def fer(d):
        if d.year not in cache:
            f = feriados(d.year, a.cinzas)
            if a.federal:
                p = pascoa(d.year)
                for k in range(4):  # quarta a sábado santo
                    f.setdefault(p - dt.timedelta(days=4 - k), "Semana Santa (Lei 5.010/66)")
                f.setdefault(dt.date(d.year, 8, 11), "Dia do Advogado/Cursos Jurídicos (Lei 5.010/66)")
                f.setdefault(dt.date(d.year, 11, 1), "Todos os Santos (Lei 5.010/66)")
                f.setdefault(dt.date(d.year, 12, 8), "Dia da Justiça (Lei 5.010/66)")
            cache[d.year] = f
        return cache[d.year].get(d) or extra.get(d)

    def recesso(d):
        return (d.month == 12 and d.day >= 20) or (d.month == 1 and d.day <= 20)

    def suspenso(d):
        if a.regime in ("cpc", "clt", "jec") and recesso(d):
            return "suspensão 20/12–20/01"
        for x, y in susp:
            if x <= d <= y:
                return "suspensão informada"
        return None

    def util(d):
        return d.weekday() < 5 and not fer(d)

    log = []
    d = inicio
    if a.regime in ("cpc", "clt", "jec"):
        n = 0
        while n < dias:
            d += dt.timedelta(days=1)
            motivo = suspenso(d) or (None if util(d) else (fer(d) or "fim de semana"))
            if motivo:
                log.append(f"  {d}  pula: {motivo}")
                continue
            n += 1
            log.append(f"  {d}  dia {n}")
    else:
        # corridos: começa no 1º dia seguinte; no CPP, início em dia não útil
        # posterga o início (Súmula 310/STF) e vencimento em dia não útil prorroga.
        if a.regime == "cpp":
            while True:
                nxt = d + dt.timedelta(days=1)
                if util(nxt) and not suspenso(nxt):
                    break
                log.append(f"  {nxt}  início postergado: {fer(nxt) or suspenso(nxt) or 'fim de semana'}")
                d = nxt
        d += dt.timedelta(days=dias)
        if a.regime == "cpp":
            while not util(d) or suspenso(d):
                log.append(f"  {d}  vencimento prorrogado: {fer(d) or suspenso(d) or 'fim de semana'}")
                d += dt.timedelta(days=1)

    if a.verbose:
        print("\n".join(log))
    print(f"Regime: {a.regime.upper()}  |  Prazo: {dias} dias{' (em dobro)' if a.dobro else ''}")
    print(f"Evento: {inicio:%d/%m/%Y}  ->  VENCIMENTO: {d:%d/%m/%Y} ({['seg','ter','qua','qui','sex','sáb','dom'][d.weekday()]})")
    print("Aviso: confira feriados locais, portarias do tribunal e indisponibilidades do sistema.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
