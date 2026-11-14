# Prazos

Rode `scripts/prazo.py` para obter a data. Este arquivo diz **qual prazo** e
**de quando conta**. O script só conhece feriados nacionais: peça ou procure
o calendário do tribunal (feriados locais, portarias, indisponibilidade).

## Regras de contagem

| Regime | Base | Recesso 20/12–20/01 | Dispositivo |
|---|---|---|---|
| Cível (CPC) | Dias úteis | Suspende | CPC 219, 220, 224 |
| Juizados (JEC/JEF/JEFP) | Dias úteis | Suspende | Lei 9.099, 12-A; CPC 220 |
| Trabalhista | Dias úteis | Suspende | CLT 775, 775-A |
| Penal | Dias corridos; início postergado se a intimação for em dia sem expediente (Súm. 310/STF); vencimento prorroga | Não suspende (salvo ato do tribunal) | CPP 798 |
| Material (prescrição/decadência) | Dias corridos / meses / anos | Não suspende | CC 132; leis específicas |

- **Prazo em dobro:** Fazenda Pública (CPC 183), MP (180), Defensoria (186),
  litisconsortes com advogados diferentes de escritórios distintos **só em
  autos físicos** (229, §2º). Não se aplica quando a lei fixa prazo próprio
  para o ente (ex.: MS, JEF/JEFP — Lei 10.259, art. 9º; Lei 12.153, art. 7º).
  No processo do trabalho, Fazenda tem prazo em dobro para recurso (DL
  779/69) e 30 dias para embargos à execução (Lei 9.494, art. 1º-B).
- **Prazo não fixado em lei ou pelo juiz:** 5 dias (CPC 218, §3º).
- **Ato prematuro é tempestivo** (CPC 218, §4º).

## Marco inicial (CPC 231 e comunicação eletrônica)

| Forma | Começa a contar | Base |
|---|---|---|
| Publicação no DJEN/DJe | Disponibilização no dia D → publicação em D+1 útil → prazo começa no 1º útil seguinte | Lei 11.419, art. 4º, §§3º–4º; CPC 224, §§2º–3º |
| Intimação pelo portal/sistema (consulta) | Dia da consulta; se não consultar em 10 dias corridos, considera-se feita no 10º (ciência ficta) | Lei 11.419, art. 5º, §3º |
| Citação por meio eletrônico (CPC 246) | 5º dia útil seguinte à confirmação do recebimento | CPC 231, IX |
| Citação eletrônica sem confirmação em 3 dias úteis | Não vale: faz-se por outro meio, e o réu explica a omissão (multa por ato atentatório) | CPC 246, §§1º-A a 1º-C |
| Correio | Juntada do AR | CPC 231, I |
| Oficial de justiça | Juntada do mandado | CPC 231, II |
| Edital | Fim da dilação fixada pelo juiz | CPC 231, IV |

**Domicílio Judicial Eletrônico (Res. CNJ 455/2022 e alterações):**
obrigatório para PJs públicas e privadas (exceto ME/EPP com cadastro na
REDESIM, que podem optar); facultativo para pessoas físicas. Quando o mesmo
ato é publicado no DJEN e enviado ao Domicílio, a regra de prevalência foi
objeto de ajustes normativos e de jurisprudência. ⚠ **Conferir a redação
vigente da resolução e o entendimento do tribunal** antes de afirmar o termo
inicial; na dúvida, aconselhe contar pelo marco **mais cedo**.

## Prazos mais usados

### Cível
| Ato | Prazo |
|---|---|
| Contestação (procedimento comum) | 15 dias úteis (CPC 335) |
| Réplica | 15 (CPC 350–351) |
| Embargos de declaração | 5 (CPC 1.023) |
| Apelação, contrarrazões | 15 (CPC 1.003, §5º) |
| Agravo de instrumento | 15 |
| Agravo interno | 15 (CPC 1.021) |
| REsp / RE | 15 |
| Agravo em REsp/RE (1.042) | 15 |
| Embargos à execução | 15 da juntada do mandado de citação (CPC 915) |
| Cumprimento de sentença: pagamento | 15 (CPC 523) — multa 10% + honorários 10% |
| Impugnação ao cumprimento | 15 após o prazo de pagamento (CPC 525) |
| Embargos monitórios | 15 (CPC 701–702) |
| Ação rescisória | 2 anos do trânsito (CPC 975) — decadencial |
| Mandado de segurança | 120 dias corridos da ciência do ato (Lei 12.016, art. 23) — decadencial |

### Juizados
| Ato | Prazo |
|---|---|
| Recurso inominado (JEC) | 10 dias úteis (Lei 9.099, art. 42) — preparo em 48h |
| ED no JEC | 5 (art. 49) |
| Contestação | Até a audiência de instrução (JEC) |

### Trabalhista
| Ato | Prazo |
|---|---|
| Defesa | Em audiência (CLT 847); no PJe, até a audiência |
| Recurso ordinário, RR, AIRR, agravo de petição, embargos à SDI | 8 dias úteis (Lei 5.584/70, art. 6º) |
| ED | 5 (CLT 897-A) |
| Embargos à execução / impugnação | 5 após garantia do juízo (CLT 884) |
| Prescrição | 5 anos durante o contrato, limitado a 2 anos após a extinção (CF 7º, XXIX); intercorrente 2 anos (CLT 11-A) |

### Penal
| Ato | Prazo |
|---|---|
| Resposta à acusação | 10 dias (CPP 396) |
| Apelação | 5 dias para interpor + 8 para razões (CPP 593, 600) |
| RESE | 5 dias (CPP 586) + 2 para razões (588) |
| ED | 2 dias (CPP 619) |
| Embargos infringentes e de nulidade | 10 dias (CPP 609, p.ú.) |
| Apelação no JECrim | 10 dias, com razões (Lei 9.099, art. 82, §1º) |
| REsp / RE criminal | 15 dias corridos (Lei 8.038/90 c/c CPP) — ⚠ conferir |
| Agravo em execução | 5 dias (Súm. 700/STF) |
| HC / revisão criminal | Sem prazo |
| Queixa-crime / representação | 6 meses do conhecimento da autoria (CP 103; CPP 38) — decadencial |

## Preparo

Preparo comprovado no ato de interposição (CPC 1.007); insuficiência → 5 dias
para complementar (§2º); ausência total → recolhimento em dobro (§4º). Isentos:
beneficiário da gratuidade, Fazenda, MP. Trabalhista: custas + depósito
recursal (CLT 899) — valores ⚠ voláteis (tabela anual do TST); isenções e
reduções do §§9º–10 do art. 899.

## Checklist ao informar prazo ao usuário

1. Qual o ato e o regime?
2. Qual o marco inicial (DJEN? Domicílio? juntada?) e sua data?
3. Há prazo em dobro?
4. Rodou o script? Inclua feriados locais informados.
5. Escreva: "**Vencimento estimado: dd/mm/aaaa** — confira o calendário do
   [tribunal] e eventuais suspensões."
6. Se faltarem menos de 3 dias úteis, destaque a urgência no topo.
