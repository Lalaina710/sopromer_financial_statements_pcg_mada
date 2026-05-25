# Changelog

All notable changes to this module will be documented in this file.

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
