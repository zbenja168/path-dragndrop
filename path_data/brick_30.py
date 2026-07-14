BRICK = {
    "brick_num": 30,
    "brick_title": "Cancer Immune Evasion",
    "games": [
        {
            "slug": "evasion_mechanisms",
            "title": "Mechanisms of Immune Evasion",
            "subtitle": "Match each evasion mechanism to its key substance and its result",
            "categories": ["Key Molecule / Substance", "Mechanism", "Result"],
            "data": {
                "Antigen Masking": {
                    "Key Molecule / Substance": "Glycocalyx (excess extracellular matrix)",
                    "Mechanism": "Thick surface coating hides tumor antigens",
                    "Result": "Immune cells cannot target antigens for destruction"
                },
                "Outgrowth of Antigen Variants": {
                    "Key Molecule / Substance": "Lost or downregulated surface antigen",
                    "Mechanism": "Non-immunogenic subclones survive immune selection",
                    "Result": "No antigen remains for immune cells to recognize"
                },
                "Loss of MHC Molecules": {
                    "Key Molecule / Substance": "MHC class I",
                    "Mechanism": "Mutations delete MHC class I from the cell surface",
                    "Result": "Cytotoxic T cells can no longer recognize the tumor cell"
                },
                "Lack of Co-Stimulation": {
                    "Key Molecule / Substance": "Absent co-stimulatory (Signal 2)",
                    "Mechanism": "Tumor presents antigen without a co-stimulatory signal",
                    "Result": "T cells become anergic or undergo apoptosis"
                },
                "Immunosuppression": {
                    "Key Molecule / Substance": "TGF-beta",
                    "Mechanism": "Tumor secretes the cytokine in large quantities",
                    "Result": "Suppresses B cells, T cells, dendritic cells, and macrophages"
                },
                "Checkpoint Engagement": {
                    "Key Molecule / Substance": "PD-L1 / PD-L2",
                    "Mechanism": "Bind the PD-1 receptor on T cells",
                    "Result": "Delivers an inhibitory signal that blocks T cell activation"
                }
            }
        },
        {
            "slug": "receptor_ligand_pairs",
            "title": "Immune Receptors and Their Ligands",
            "subtitle": "Match each molecule to where it acts, its binding partner, and its effect on T cells",
            "categories": ["Location / Cell", "Binding Partner", "Effect on T Cell"],
            "data": {
                "CTLA-4": {
                    "Location / Cell": "Upregulated inhibitory receptor on T cells",
                    "Binding Partner": "B7 (B7-1 / B7-2) on antigen-presenting cells",
                    "Effect on T Cell": "Reduces CD28 engagement and inhibits activation"
                },
                "CD28": {
                    "Location / Cell": "Co-stimulatory receptor on T cells",
                    "Binding Partner": "B7 molecules on antigen-presenting cells",
                    "Effect on T Cell": "Delivers Signal 2 and activates the T cell"
                },
                "PD-1": {
                    "Location / Cell": "Programmed cell death receptor on T cells",
                    "Binding Partner": "PD-L1 / PD-L2 on tumor cells",
                    "Effect on T Cell": "Inhibitory signal that suppresses the T cell"
                },
                "FasL": {
                    "Location / Cell": "Tumor cell surface (melanoma, hepatocellular carcinoma)",
                    "Binding Partner": "Fas receptor on cytotoxic T cells",
                    "Effect on T Cell": "Triggers extrinsic-pathway apoptosis of the T cell"
                },
                "MHC Class I": {
                    "Location / Cell": "All nucleated cells",
                    "Binding Partner": "Receptor of the cytotoxic (CD8) T cell",
                    "Effect on T Cell": "Displays antigen so the T cell can recognize the cell"
                }
            }
        },
        {
            "slug": "immunotherapies",
            "title": "Cancer Immunotherapies",
            "subtitle": "Match each therapy to its target, mechanism, and clinical use",
            "categories": ["Target", "Mechanism", "Clinical Use"],
            "data": {
                "Pembrolizumab (Keytruda)": {
                    "Target": "PD-1 receptor on T cells",
                    "Mechanism": "Antibody blocks PD-1 from binding PD-L1 on cancer cells",
                    "Clinical Use": "Advanced-stage solid tumors such as lung cancer"
                },
                "Anti-CTLA-4 Antibody": {
                    "Target": "CTLA-4 inhibitory receptor",
                    "Mechanism": "Blocks CTLA-4/B7 binding to restore CD28 co-stimulation",
                    "Clinical Use": "Advanced-stage solid tumors"
                },
                "Anti-PD-L1 Antibody": {
                    "Target": "PD-L1 ligand on tumor cells",
                    "Mechanism": "Prevents the PD-L1/PD-1 inhibitory signal on T cells",
                    "Clinical Use": "Advanced solid tumors and some forms of lymphoma"
                },
                "CAR-T Cell Therapy": {
                    "Target": "CD19 antigen on B cells",
                    "Mechanism": "Patient T cells engineered to recognize a specific antigen",
                    "Clinical Use": "B-cell malignancies (diffuse large B-cell lymphoma, B-lymphoblastic leukemia/lymphoma)"
                }
            }
        },
        {
            "slug": "t_cell_fate",
            "title": "T Cell Fate and Cytokines",
            "subtitle": "Match each trigger to its pathway and the resulting outcome",
            "categories": ["Trigger", "Pathway", "Outcome"],
            "data": {
                "Missing Co-Stimulation": {
                    "Trigger": "Signal 1 (antigen) delivered without Signal 2",
                    "Pathway": "Anergy induction",
                    "Outcome": "Unresponsive (anergic) or apoptotic T cells"
                },
                "FasL-Fas Engagement": {
                    "Trigger": "Tumor FasL binds Fas on the T cell",
                    "Pathway": "Extrinsic apoptosis pathway",
                    "Outcome": "Apoptosis of cytotoxic T cells"
                },
                "TGF-beta Secretion": {
                    "Trigger": "Tumor secretes TGF-beta in large amounts",
                    "Pathway": "Cytokine-mediated immunosuppression",
                    "Outcome": "Suppressed B cells, T cells, dendritic cells, and macrophages"
                },
                "TNF-alpha Activity": {
                    "Trigger": "Cytokine released during malignancy",
                    "Pathway": "Systemic catabolism and leukocyte recruitment",
                    "Outcome": "Cachexia and white blood cell recruitment"
                },
                "PD-1 Activation": {
                    "Trigger": "PD-L1 / PD-L2 bind PD-1 on the T cell",
                    "Pathway": "Inhibitory immune checkpoint",
                    "Outcome": "Suppressed T cell activation"
                }
            }
        }
    ]
}
