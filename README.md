# SOPROMER Financial Statements - PCG Madagascar 2005

Module Odoo 18 fournissant un set complet d'**etats financiers configurables**
conformes au **Plan Comptable General 2005 Madagascar** (decret n°2004-272 du
18 fevrier 2004), batis sur le framework OCA `mis_builder`.

Modele de reference visuel : **MEDICAL INTERNATIONAL SARL** (Annexe I PCG 2005).

- **Version** : 18.0.10.1.0
- **License** : LGPL-3
- **Auteur** : SOPROMER
- **Repo** : https://github.com/Lalaina710/sopromer_financial_statements_pcg_mada

## Templates livres (7)

| # | Template | Cascade | KPIs |
|---|---|---|---|
| 1 | **Compte de Resultat par Nature** | 8 etapes (Marge Comm → Production → Conso → VA → EBE → RE → RF → RAI → RN) | 30 |
| 2 | **Bilan Actif** | Non Courants (immo incorp/corp/financ + impots differes) + Courants (stocks, creances, CCA, tresorerie) | 49 |
| 3 | **Bilan Passif** | Capitaux Propres + Passifs Non Courants (emprunts LT, provisions) + Passifs Courants (fournisseurs, personnel, etat, CCA) | 35 |
| 4 | **Compte de Resultat par Fonction** | 10 etapes officielles (Production → Conso → VA → EBE → Operationnel → Financier → Avt impots → Net Activites → Extraordinaire → Net) | 28 |
| 5 | **Tableau Flux de Tresorerie** (methode indirecte) | A. Activite + B. Investissement + C. Financement + Variation tresorerie | 27 |
| 6 | **Etat de Variation des Capitaux Propres** | 4 colonnes (Capital / Reserves / Ecart eval / Resultat+RAN) - format simplifie | 6 |
| 7 | **Declaration TVA Madagascar** | 4 sections (A. CA HT / B. TVA collectee / C. TVA deductible / D. Calcul TVA a decaisser) | 14 |

## Fonctionnalites

- Cascade officielle PCG 2005 avec sous-titres en haut de section (style MEDICAL)
- Expressions `mis_builder` referencant les classes PCG Madagascar
- Periodes **dynamiques** (mode `relative` year/month, exercice courant + N-1 auto)
- Styles dedies : Detail, Sous-total (gras), Resultat (gras + fond jaune),
  Final (gras + fond orange)
- Paper format A4 portrait dedie (marges 25/20/15/15, dpi 90)
- En-tete PDF MEDICAL-style : logo societe + nom + ville + adresse +
  contacts + RC + NIF
- Titre dynamique : `<NOM RAPPORT> AU <date_to>` calcule a l'execution
- Traductions FR completes (32 strings)
- Multi-company aware (`company_ids`, `target_move='posted'`)
- Multi-currency (conversion automatique en devise societe)
- Convention de signe respectee :
  - Produits (classe 7) : `-balp[X%]` -> affichage positif
  - Charges (classe 6) : `balp[X%]` -> affichage positif (deduit dans cascade)
  - Classe 9 (analytique/ecarts) exclue de tous les etats officiels

## Dependances

| Module | Version | Source |
|---|---|---|
| `mis_builder` | >=18.0.1.8.1 | [OCA/mis-builder](https://github.com/OCA/mis-builder) |
| `mis_template_financial_report` | >=18.0.2.0.0 | [OCA/account-financial-reporting](https://github.com/OCA/account-financial-reporting) |

Optionnel (recommande pour matrialisation BI) :
- [`mis_kpi_snapshot`](https://github.com/Lalaina710/mis_kpi_snapshot)
  pour exposer les KPI calcules a Metabase / Superset / PowerBI via SQL JOIN.

## Installation

1. Cloner les depots OCA prerequis dans le `addons_path` :
   ```bash
   cd /opt/odoo18/custom_addons/dev/
   git clone -b 18.0 https://github.com/OCA/mis-builder.git
   git clone -b 18.0 https://github.com/OCA/account-financial-reporting.git
   ```
2. Cloner ce repo :
   ```bash
   git clone https://github.com/Lalaina710/sopromer_financial_statements_pcg_mada.git
   ```
3. Update Apps List puis installer le module via UI Settings > Apps
   (chercher "SOPROMER Financial Statements").

## Usage

### Acceder aux 7 rapports

`Accounting > Reports > MIS Reporting > MIS Reports` -> ouvrir l'instance
souhaitee (ex: "COMPTE DE RESULTAT PAR NATURE", "BILAN ACTIF", etc.).

Boutons disponibles :
- **Preview** : visualisation HTML interactive
- **Print** : export PDF (format A4 portrait MEDICAL-style)
- **Export XLSX** : export Excel pour expert-comptable

### Personnaliser via UI

| Action | Chemin Odoo |
|---|---|
| Modifier rubriques | `Accounting > Configuration > MIS Report Templates` |
| Changer periodes / dates | `Accounting > Reports > MIS Reports` > onglet `Periods` |
| Changer styles (gras, couleur) | `Accounting > Configuration > MIS Report Styles` |
| Ajouter colonne comparaison | onglet `Periods` > nouveau period mode `cmpcol` |

Voir le manuel detaille :
`sopromer-rapports/11_manuels/manuel_mis_builder_etats_financiers_v2.html`
(41 chapitres, ~28k mots, pour comptables non-tech).

## Mapping PCG 2005 Madagascar (extrait)

Expressions `mis_builder` typiques :

```
# CR par Nature
I.    MARGE COMMERCIALE          = -balp[707%] - balp[6031%] + balp[601%]
II.   PRODUCTION DE L'EXERCICE   = -balp[706%] - balp[713%]
III.  CONSO INTERMEDIAIRES       = balp[602%] + balp[606%] + balp[61%] + balp[62%]
IV.   VALEUR AJOUTEE             = I + II - III
V.    EBE                        = IV - balp[63%] - balp[64%]
VI.   RESULTAT OPERATIONNEL      = EBE - balp[75%] - balp[781%] + balp[65%] + balp[681%] + balp[685%]/[686%]
VII.  RESULTAT FINANCIER         = -balp[76%] + balp[66%]
VIII. RAI                        = VI - VII (signe selon convention cascade)
      RN ACTIVITES ORDINAIRES    = VIII - balp[695%]
      RN EXERCICE                = RN AO + (-balp[77%] + balp[67%])

# Bilan Actif (a date)
Clients                          = bale[411%]
Tresorerie banques               = bale[512%]
Tresorerie caisses               = bale[53%]

# Declaration TVA Madagascar
TVA collectee 20%                = balp[44571%]
TVA deductible B&S 20%           = -balp[44566%]
TVA deductible immobilisations   = -balp[44562%]
```

## Limitations connues

- **Setup hybride Odoo + ERP comptable externe (Sage 100c chez SOPROMER)** :
  les classes 1 (capitaux propres), 2 (immobilisations), 3 (stocks valorises)
  sont souvent vides dans Odoo car gerees sur l'ERP externe. Le Bilan
  affichera 0 pour ces rubriques. Solution : pipeline import ERP externe
  vers table dediee (skill `odoo-sage-import` a venir).

- **Variation Capitaux Propres** : format simplifie (soldes par composante x
  annee). Le vrai format pivot lignes mouvements x colonnes composantes
  necessite un module custom — limitation `mis_builder` non bloquante.

- **Pixel-perfect identique au PDF MEDICAL INTERNATIONAL** : QWeb `mis_builder`
  proche mais pas identique au template Excel custom MEDICAL. Mise en page
  affinable via override `mis_builder.report_mis_report_instance`.

- **Champ capital social** : pas de champ natif `res.company`. Placeholder
  utilise. Ajouter champ custom `company_capital` si vraiment necessaire.

## Compatibilite

- Odoo 18 Community ou Enterprise
- PostgreSQL >= 14 recommande
- Plan comptable Madagascar 2005 (compatible aussi avec PCG France,
  SYSCOHADA, IFRS en adaptant les prefixes via UI Templates)
- Multi-company, multi-currency

## Roadmap

- [x] **Phase A** v18.0.1.0.0 : Scaffold + CR par Nature
- [x] **Phase B1** v18.0.2.0.0 : QWeb pixel-perfect MEDICAL-style
- [x] **Phase B1.1** v18.0.3.0.0 : Fix signes expressions + periodes
- [x] **Vague 1** v18.0.4.0.0 : Periodes dynamiques + sous-titres en haut
- [x] **Vague 2** v18.0.5-9.0.0 : Bilan Actif/Passif + CR Fonction + TFT + Variation CP
- [x] **Phase B7** v18.0.10.0.0 : Declaration TVA Madagascar
- [ ] **Phase C** : Pipeline import ERP externe (Sage) pour bilan complet
- [ ] **Phase D** : Champ custom `res.company.company_capital` + formatage
      chiffres locale FR via override QWeb

## Licence

LGPL-3.0 or later

## Auteur

SOPROMER - https://github.com/Lalaina710

## Support

Issues : https://github.com/Lalaina710/sopromer_financial_statements_pcg_mada/issues
