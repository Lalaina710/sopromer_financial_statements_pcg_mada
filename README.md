# SOPROMER Financial Statements - PCG Madagascar 2005

Module Odoo 18 fournissant des etats financiers configurables conformes au
**Plan Comptable General 2005 Madagascar**, batis sur le framework OCA
`mis_builder`.

## Statut Phase A (v18.0.1.0.0)

- [x] Compte de Resultat par Nature (cascade officielle 8 etapes)
- [x] 30 KPIs avec expressions `balp[...]` referencant les classes PCG Mada
- [x] 4 styles dedies (detail, sous-total, resultat, final)
- [x] Instance pre-configuree N et N-1
- [x] Paper format A4 portrait dedie
- [x] En-tete societe (nom + ville) sur impression PDF
- [x] Traductions FR completes

## Phases ulterieures

- [ ] **Phase B** : Bilan Actif/Passif PCG 2005, CR par Fonction (10 etapes)
- [ ] **Phase C** : Tableau Flux de Tresorerie (methode indirecte),
      Variation Capitaux Propres
- [ ] En-tete PDF pixel-perfect avec RC + NIF + capital
- [ ] Formatage chiffres locale FR (espace milliers, virgule decimale)

## Dependances

| Module | Version | Source |
|---|---|---|
| `mis_builder` | >=18.0.1.8.1 | OCA/mis-builder |
| `mis_template_financial_report` | >=18.0.2.0.0 | OCA/account-financial-reporting |

## Installation

1. Cloner ce repo dans le `addons_path` :
   ```bash
   cd /opt/odoo18/custom_addons/dev/
   git clone https://github.com/Lalaina710/sopromer_financial_statements_pcg_mada.git
   ```
2. Installer les dependances OCA si pas deja fait :
   - `mis_builder` (OCA/mis-builder branche 18.0)
   - `mis_template_financial_report` (OCA/account-financial-reporting branche 18.0)
3. Update Apps List puis installer le module via UI Settings > Apps
   (chercher "SOPROMER Financial Statements")

## Usage

### Acceder au rapport
1. Aller dans **Accounting > Reports > MIS Reports**
2. Ouvrir l'instance "CR par Nature - PCG Madagascar (exemple)"
3. Ajuster les dates (par defaut 2024 et 2025)
4. Cliquer "Preview" pour visualiser ou "Export PDF / XLSX"

### Personnaliser
- **Modifier les rubriques** : Settings > Accounting > MIS Reporting > Templates
  -> "COMPTE DE RESULTAT PAR NATURE" -> modifier les KPIs
- **Ajouter colonnes** : sur l'instance, onglet Periods -> ajouter periode
  comparative (Variation N/N-1, etc.)
- **Changer style** : Settings > Accounting > MIS Reporting > Styles

## Formules KPI (rappel cascade PCG 2005)

```
I.    MARGE COMMERCIALE          = 707* + 702* - 601* - 607* - 6031*
I.    PRODUCTION DE L'EXERCICE   = 706* + 713*
II.   CONSO INTERMEDIAIRES       = 602* + 606* + 61* + 62*
III.  VALEUR AJOUTEE             = I + Production - Conso
IV.   EBE                        = VA + 74* - 63* - 64*
V.    RESULTAT OPERATIONNEL      = EBE + 75* + 781*/785* - 65* - 681* - 685*/686*
VI.   RESULTAT FINANCIER         = 76* - 66*
VII.  RAI                        = V + VI
VIII. RN ACTIVITES ORDINAIRES    = RAI - 695*
      RESULTAT NET EXERCICE      = VIII + (77* - 67*)
```

## Compatibilite

- Odoo 18 Community ou Enterprise
- PCG Madagascar 2005 (classes 6 et 7 conformes)
- Adaptable aux autres referentiels (PCG France, SYSCOHADA, IFRS) en
  clonant le template via UI

## Licence

LGPL-3.0 or later

## Auteur

SOPROMER - https://github.com/Lalaina710
