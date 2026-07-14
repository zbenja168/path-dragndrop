BRICK = {
    "brick_num": 4,
    "brick_title": "Cell Death: Apoptosis and Necrosis",
    "games": [
        {
            "slug": "apoptosis_molecular_players",
            "title": "Apoptosis: Molecular Players",
            "subtitle": "Match each protein to its class, pathway, and net effect on cell death",
            "categories": ["Class / Role", "Pathway", "Net Effect"],
            "data": {
                "BCL2": {
                    "Class / Role": "Anti-apoptotic BCL2-family protein",
                    "Pathway": "Intrinsic (mitochondrial)",
                    "Net Effect": "Keeps outer membrane impermeable, blocks cytochrome c release"
                },
                "Cytochrome c": {
                    "Class / Role": "Electron transport chain protein",
                    "Pathway": "Intrinsic (mitochondrial)",
                    "Net Effect": "Forms the apoptosome that activates caspase-9"
                },
                "BAX and BAK": {
                    "Class / Role": "Pro-apoptotic effector proteins",
                    "Pathway": "Intrinsic (mitochondrial)",
                    "Net Effect": "Permeabilize outer membrane so cytochrome c leaks out"
                },
                "BH3-only proteins": {
                    "Class / Role": "Stress sensors upregulated by DNA damage and ER stress",
                    "Pathway": "Intrinsic (mitochondrial)",
                    "Net Effect": "Inhibit BCL2 and stimulate BAX and BAK"
                },
                "Fas and Fas ligand": {
                    "Class / Role": "Death receptor bound by its ligand",
                    "Pathway": "Extrinsic (death receptor)",
                    "Net Effect": "Recruits FADD to activate caspase-8"
                },
                "Caspase-8": {
                    "Class / Role": "Initiator caspase activated via FADD",
                    "Pathway": "Extrinsic (death receptor)",
                    "Net Effect": "Triggers executioner caspases and cleaves BID"
                }
            }
        },
        {
            "slug": "necrosis_patterns",
            "title": "Patterns of Necrosis",
            "subtitle": "Match each necrosis pattern to its appearance, typical cause, and classic example",
            "categories": ["Appearance", "Typical Cause / Location", "Classic Example"],
            "data": {
                "Coagulative necrosis": {
                    "Appearance": "Firm, pale tissue with cell outlines preserved",
                    "Typical Cause / Location": "Ischemia in most solid organs",
                    "Classic Example": "Myocardial infarction"
                },
                "Liquefactive necrosis": {
                    "Appearance": "Dead tissue digested into viscous liquid or pus",
                    "Typical Cause / Location": "Ischemia within the central nervous system",
                    "Classic Example": "Brain infarct after a stroke"
                },
                "Caseous necrosis": {
                    "Appearance": "Friable, cheese-like off-white debris in a granuloma",
                    "Typical Cause / Location": "Granulomatous infection",
                    "Classic Example": "Tuberculosis"
                },
                "Gangrenous necrosis": {
                    "Appearance": "Mummified or rotting tissue crossing tissue planes",
                    "Typical Cause / Location": "Ischemia of a limb or digits",
                    "Classic Example": "Frostbite of the toes"
                },
                "Fat necrosis": {
                    "Appearance": "Chalky-white saponified deposits",
                    "Typical Cause / Location": "Lipases leaking into fat-rich tissue",
                    "Classic Example": "Acute pancreatitis"
                },
                "Fibrinoid necrosis": {
                    "Appearance": "Bright pink fibrin and immune complexes in the vessel wall",
                    "Typical Cause / Location": "Immune-mediated vascular injury",
                    "Classic Example": "Granulomatosis with polyangiitis"
                }
            }
        },
        {
            "slug": "necrosis_vs_apoptosis",
            "title": "Necrosis vs. Apoptosis",
            "subtitle": "Sort each feature into how it appears in necrosis versus apoptosis",
            "categories": ["In Necrosis", "In Apoptosis"],
            "data": {
                "Number of cells affected": {
                    "In Necrosis": "Groups of neighboring cells",
                    "In Apoptosis": "Single cells"
                },
                "Cell size and shape": {
                    "In Necrosis": "Cellular swelling",
                    "In Apoptosis": "Cellular shrinkage"
                },
                "Membrane integrity": {
                    "In Necrosis": "Membrane ruptures and contents spill out",
                    "In Apoptosis": "Maintained; blebs into apoptotic bodies"
                },
                "Inflammatory response": {
                    "In Necrosis": "Significant inflammatory reaction",
                    "In Apoptosis": "No inflammatory reaction"
                },
                "DNA degradation": {
                    "In Necrosis": "Random DNA degradation",
                    "In Apoptosis": "Ordered internucleosomal fragmentation"
                },
                "Regulation": {
                    "In Necrosis": "Always pathologic and uncontrolled",
                    "In Apoptosis": "Programmed; can be physiologic"
                }
            }
        },
        {
            "slug": "cell_death_clinical",
            "title": "Cell Death: Clinical Correlations",
            "subtitle": "Match each finding to its underlying mechanism and clinical association",
            "categories": ["Underlying Mechanism", "Effect on Cell Death", "Clinical Association"],
            "data": {
                "BCL2 overexpression": {
                    "Underlying Mechanism": "t(14;18) places BCL2 under the Ig heavy-chain enhancer",
                    "Effect on Cell Death": "Blocks apoptosis so cells survive abnormally",
                    "Clinical Association": "Follicular lymphoma"
                },
                "PD-L1 on tumor cells": {
                    "Underlying Mechanism": "Binds PD-1 on T cells",
                    "Effect on Cell Death": "Prevents T-cell-driven apoptosis of tumor cells",
                    "Clinical Association": "Immune evasion; target of pembrolizumab and nivolumab"
                },
                "Fas ligand on cytotoxic T cells": {
                    "Underlying Mechanism": "Engages the Fas death receptor on target cells",
                    "Effect on Cell Death": "Triggers extrinsic apoptosis of the target",
                    "Clinical Association": "Removes self-reactive lymphocytes and infected cells"
                },
                "Cardiac troponin release": {
                    "Underlying Mechanism": "Necrotic cardiomyocytes rupture and spill proteins",
                    "Effect on Cell Death": "Reflects uncontrolled necrosis rather than apoptosis",
                    "Clinical Association": "Serum marker of myocardial infarction"
                }
            }
        }
    ]
}
