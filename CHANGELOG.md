# Changelog

All notable changes to this module will be documented in this file.

## [18.0.10.0.0] - 2026-05-25

### Added - Phase B7 : Template Declaration TVA Madagascar

- **7eme template mis_builder** : `DECLARATION TVA MADAGASCAR` structuree en
  4 sections officielles :
  - **A. CHIFFRE D AFFAIRES HT** : Ventes taxables 20%, Exports 0%, Exoneres
  - **B. TVA COLLECTEE** (a reverser) : sur ventes 20% + autres prestations
  - **C. TVA DEDUCTIBLE** : biens & services 20% + immobilisations 20% +
    credit TVA reportable exercice precedent
  - **D. CALCUL TVA A DECAISSER** : B - C (positif = a decaisser, negatif =
    credit TVA reportable)
- **Instance pre-configuree** avec 2 periodes mensuelles dynamiques :
  - Mois courant (offset 0, type m, duration 1)
  - Mois precedent (offset -1, type m, duration 1)
- **Mapping comptes** SOPROMER PCG Mada verifies sur SOPROMER-REST220526 :
  - CA HT : 70710-70840 (marchandises, produits transformes, prestations)
  - TVA collectee : 44571* (generique + 20% ventes), 44572*-44576*
  - TVA deductible biens/services : 44561*, 44562100, 44563*, 44564*, 44566*
  - TVA deductible immo : 44562000, 44564100, 44565*
  - Credit TVA report : 44550*, 44552*, 44567*
- **14 KPIs** au total : 4 sous-totaux sections + 7 details + 3 rappels
  section D + 1 resultat final (en style `SFS_CR_Final` fond orange).

### Notes

- Module `softeam_l10n_mg` installe au prealable apporte le plan de comptes
  FRANCAIS (country FR id=75) et non un plan Madagascar. Les `tax_tags`
  format `A1-F9` (typologie declaration TVA FR) ne sont PAS exploites :
  filtre uniquement par codes comptes 44* PCG Mada deja en place dans
  SOPROMER (bascule TVA realisee 29/04, projet_bascule_tva_43).
- Sections `ca_export` et `ca_exonere` placeholders a 0 : pas de compte 707
  dedie identifie permettant distinction automatique export vs taxable.
  Pour exploitation : creer comptes 70710E (export), 70710X (exonere) ou
  utiliser modules complementaires l10n_mg.

## [18.0.4.0.0] - 2026-05-25

### Changed - Vague 1 : Periodes dynamiques + sous-titres en haut de section

- **Periodes dynamiques** : remplacement des dates hardcodees (2026-01-01 ->
  2026-12-31, 2025-01-01 -> 2025-12-31) par mode `relative` type `y` :
  - Periode 1 "Exercice courant" : offset=0 (annee du pivot_date = today)
  - Periode 2 "Exercice N-1" : offset=-1
  - Suppression date_from/date_to de l'instance, activation comparison_mode=True
  - Effet : le rapport se cale automatiquement sur l'annee courante chaque
    annee sans intervention manuelle.
- **Sous-titres en haut de section** : restructuration cascade KPIs pour
  matcher visuel PDF MEDICAL INTERNATIONAL. Headers (MARGE COMMERCIALE,
  I - PRODUCTION DE L'EXERCICE, II - CONSO INTERMEDIAIRES, V - RESULTAT
  OPERATIONNEL, VI - RESULTAT FINANCIER, VII - RAI, VIII - RNAO, RESULTAT
  EXTRAORDINAIRE) deplaces AU DESSUS de leurs lignes de detail :
  ```
  MARGE COMMERCIALE :          [valeur calculee]
    Ventes de marchandises     [detail]
    Cout d'achat               [detail]
    Variation de Stocks        [detail]
  I - PRODUCTION DE L EXERCICE [valeur calculee]
    Production vendue          [detail]
    Production stockee         [detail]
  ...
  ```
- **Forward-reference** : exploite le mecanisme natif mis_builder
  `compute_queue` + `recompute_queue` (cf models/mis_report.py) qui retry
  les KPIs avec NameError au pass suivant. Permet d'afficher le sous-total
  AVANT ses composantes en sequence.
- Sequences KPI renumerotees : 10, 20, ..., 300 (par pas de 10) reflechies
  pour ordre visuel cascade.

### Validation
- Periodes : pivot_date=today => 2026 + 2025
- Forward-ref : NameError au 1er pass => recompute_queue => OK 2eme pass
- Marge commerciale, I, II, III, V, VI, VII, VIII en haut de chaque section

## [18.0.3.0.0] - 2026-05-25

### Fixed - Phase B1.1 : bugs rendu PDF (suite review Herve)

- **Signes expressions mis_builder** : ajout prefixe `-` sur toutes les expressions
  referencant les classes de produits (7XX, 75, 76, 77, 781, 785, 702, 706, 713)
  pour convention CR officielle (produits affiches positifs, charges negatives).
  bal[X] = debit - credit ; pour produits naturellement crediteurs, -bal devient
  positif. KPIs corriges : 010 (ventes_march), 050 (prod_vendue), 060 (prod_stockee),
  150 (aut_prod_exp), 160 (reprises_prov), 210 (prod_fin), 270 (prod_extra) - 7 KPIs.
  Cascade sous-totaux (marge_commerciale, valeur_ajoutee, ebe, res_operationnel,
  res_avant_impots, rn_act_ord, resultat_net) inchangee : somme algebrique directe.
- **Titre dupliqué QWeb** : suppression de la date du `name` instance
  ("COMPTE DE RESULTAT PAR NATURE AU 31/12/2025" -> "COMPTE DE RESULTAT PAR NATURE").
  Le QWeb ajoute dynamiquement "AU date_to" via `o.date_to.strftime('%d/%m/%y')`.
- **Periodes corrigees** : Exercice 2026 YTD (2026-01-01 -> 2026-12-31, data
  disponible REST220526) + Exercice 2025 (N-1, sera vide sur snapshot test mais
  cadre normal). date_from/date_to instance alignes 2026.

### Validation
- Ventes marchandises : positif (avant : negatif)
- Marge commerciale : positive (avant : negative)
- Resultat net : signe coherent avec activite (avant : faussement negatif)

## [18.0.2.0.0] - 2026-05-25

### Added - Phase B1 : QWeb pixel-perfect MEDICAL-style

- Override QWeb `mis_builder.report_mis_report_instance` (priority=100) avec
  en-tete societe complet style MEDICAL INTERNATIONAL
- En-tete : logo societe (si present), nom societe gras 16pt, ville gras 11pt,
  bloc adresse + telephone + email + identifiants legaux
- Placeholders gris pour champs manquants (RC, NIF/STAT, website, capital social)
  invitant Hervé à completer via Settings > Companies
- Titre rapport : dynamique "<NOM INSTANCE> AU DD/MM/YY" (date_to)
- CSS MEDICAL injecte : lignes alternees #FAFAFA, header colonnes gris E8E8E8,
  police monospace chiffres, bordures MEDICAL, padding optimise
- Renforcement sous-totaux et resultat final via styles mis_builder existants
  (SFS_CR_Subtotal, SFS_CR_Result, SFS_CR_Final conserves)
- Limitation documentee : format FR espace/virgule (separateur milliers) depend
  de la configuration des KPI styles cote mis_builder, pas modifiable en QWeb pur

### Changed
- Version bumped 18.0.1.0.0 → 18.0.2.0.0
- Summary module mis a jour

## [18.0.1.0.0] - 2026-05-25

### Added - Phase A : Compte de Resultat par Nature
- Module initial scaffold conforme conventions SOPROMER + OCA
- Template MIS Builder "COMPTE DE RESULTAT PAR NATURE" - cascade officielle
  PCG 2005 Madagascar en 8 etapes
- 30 KPIs avec expressions `balp[...]` referencant les classes 6 et 7
  (cascade Marge Commerciale -> Production -> Conso -> VA -> EBE -> RO ->
  RF -> RAI -> RN ordinaires -> Extraordinaire -> RN exercice)
- 4 styles dedies : CR_Detail, CR_Subtotal, CR_Result, CR_Final
- Instance pre-configuree avec 2 colonnes (exercice 2025 + 2024 N-1)
- Paper format A4 portrait dedie (margins custom)
- QWeb inherit minimaliste : en-tete societe (nom + ville) sur impression PDF
- Traductions francaises completes (libellés rubriques + technique)

### Dependencies
- `mis_builder` >=18.0.1.8.1 (OCA/mis-builder)
- `mis_template_financial_report` >=18.0.2.0.0 (OCA/account-financial-reporting)

### Notes
- Source des donnees : SOPROMER-REST220526 template id=4 + instance id=2,
  exportes via SQL et regenerees en XML data avec xml_id stables.
- Devise / company / dates sont parametrables via UI sans modifier le module.
