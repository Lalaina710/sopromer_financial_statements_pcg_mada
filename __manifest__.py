# Copyright 2026 SOPROMER
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).
{
    "name": "SOPROMER Financial Statements - PCG Madagascar 2005",
    "version": "18.0.10.0.0",
    "category": "Accounting/Reporting",
    "summary": "Etats financiers configurables PCG 2005 Madagascar via OCA mis_builder "
               "(CR Nature + BILAN ACTIF/PASSIF + CR FONCTION + TFT + VARIATION CP + DECLARATION TVA)",
    "description": """
SOPROMER Financial Statements - PCG Madagascar 2005
====================================================

Module Odoo 18 transportable fournissant les etats financiers conformes au
Plan Comptable General 2005 Madagascar, construits sur le framework OCA
mis_builder.

Phase A (v18.0.1.0.0)
---------------------
* Compte de Resultat par Nature - cascade officielle 8 etapes (Marge
  Commerciale, Production, Consommations Intermediaires, Valeur Ajoutee,
  EBE, Resultat Operationnel, Resultat Financier, Resultat Net).
* Instance pre-configuree avec 2 colonnes (exercice N + N-1).
* 4 styles dedies (CR_Detail, CR_Subtotal, CR_Result, CR_Final).
* Paper format A4 portrait dedie.
* En-tete societe sur impression PDF.
* Traductions FR completes.

Phases ulterieures
------------------
* Phase B : Bilan Actif/Passif PCG 2005, CR par Fonction (10 etapes).
* Phase C : Tableau de Flux de Tresorerie (methode indirecte), Etat de
  Variation des Capitaux Propres.

Dependances
-----------
* mis_builder (OCA) v18.0.1.8.1+
* mis_template_financial_report (OCA) v18.0.2.0.0+
""",
    "author": "SOPROMER",
    "website": "https://github.com/Lalaina710/sopromer_financial_statements_pcg_mada",
    "license": "LGPL-3",
    "depends": [
        "mis_builder",
        "mis_template_financial_report",
    ],
    "data": [
        "data/mis_report_styles.xml",
        "data/mis_report_cr_par_nature_template.xml",
        "data/mis_report_cr_par_nature_instance.xml",
        "data/mis_report_bilan_actif_template.xml",
        "data/mis_report_bilan_actif_instance.xml",
        "data/mis_report_bilan_passif_template.xml",
        "data/mis_report_bilan_passif_instance.xml",
        "data/mis_report_cr_par_fonction_template.xml",
        "data/mis_report_cr_par_fonction_instance.xml",
        "data/mis_report_tft_indirecte_template.xml",
        "data/mis_report_tft_indirecte_instance.xml",
        "data/mis_report_variation_cp_template.xml",
        "data/mis_report_variation_cp_instance.xml",
        "data/mis_report_declaration_tva_template.xml",
        "data/mis_report_declaration_tva_instance.xml",
        "reports/paper_format_mada.xml",
        "reports/mis_report_qweb_inherit.xml",
    ],
    "installable": True,
    "application": False,
    "auto_install": False,
}
