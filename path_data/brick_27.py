BRICK = {
    "brick_num": 27,
    "brick_title": "Cancer Growth and Metastasis",
    "games": [
        {
            "slug": "steps_of_metastasis",
            "title": "Steps of the Metastatic Cascade",
            "subtitle": "Match each step of metastasis to what happens, its key mechanism, and the fate of the tumor cells",
            "categories": ["What Happens", "Key Mechanism / Barrier", "Fate of Tumor Cells"],
            "data": {
                "Invasion": {
                    "What Happens": "Tumor cells breach the basement membrane into surrounding stroma",
                    "Key Mechanism / Barrier": "Proteases cleave type IV collagen; loss of E-cadherin",
                    "Fate of Tumor Cells": "Amoeboid migration ratcheting through the extracellular matrix"
                },
                "Intravasation": {
                    "What Happens": "Entry of tumor cells into the bloodstream or lymphatics",
                    "Key Mechanism / Barrier": "Bind platelets and one another to survive shear stress",
                    "Fate of Tumor Cells": "Many die from shear stress or loss-of-adhesion apoptosis"
                },
                "Extravasation": {
                    "What Happens": "Exit from the circulation into a distant tissue",
                    "Key Mechanism / Barrier": "Large tumor cell lodges in the first capillary bed reached",
                    "Fate of Tumor Cells": "Site set by vascular drainage and tissue tropism"
                },
                "Growth at Secondary Site": {
                    "What Happens": "Colonization and outgrowth at the distant organ",
                    "Key Mechanism / Barrier": "Escape from tumor dormancy in a foreign 'soil'",
                    "Fate of Tumor Cells": "Secrete cytokines and growth factors to remodel the stroma"
                }
            }
        },
        {
            "slug": "spread_pathways",
            "title": "Match the Tumor to Its Spread Pattern",
            "subtitle": "Match each tumor to its metastatic route, why it uses that route, and its target site",
            "categories": ["Metastatic Route", "Why This Route", "Target Site / Example"],
            "data": {
                "Breast carcinoma (upper outer quadrant)": {
                    "Metastatic Route": "Lymphatic spread",
                    "Why This Route": "Carcinoma; low-shear lymphatics are easy to enter",
                    "Target Site / Example": "Axillary lymph nodes"
                },
                "Sarcoma": {
                    "Metastatic Route": "Hematogenous spread",
                    "Why This Route": "Mesenchymal-origin tumors favor blood-borne spread",
                    "Target Site / Example": "Lung"
                },
                "Colon carcinoma": {
                    "Metastatic Route": "Hematogenous (portal venous)",
                    "Why This Route": "Portal drainage carries cells to the first downstream organ",
                    "Target Site / Example": "Liver"
                },
                "Ovarian carcinoma": {
                    "Metastatic Route": "Seeding",
                    "Why This Route": "Sheds cells into an open body cavity",
                    "Target Site / Example": "Peritoneal cavity and omentum"
                },
                "Glioblastoma": {
                    "Metastatic Route": "Seeding (via CSF)",
                    "Why This Route": "Spreads through the open subarachnoid space",
                    "Target Site / Example": "Brain and spinal cord"
                }
            }
        },
        {
            "slug": "invasion_molecules",
            "title": "Molecular Players in Invasion",
            "subtitle": "Match each molecule or structure to its role in invasion and what happens when it is altered",
            "categories": ["Role in Invasion / Metastasis", "Consequence When Altered"],
            "data": {
                "E-cadherin": {
                    "Role in Invasion / Metastasis": "Adhesion junction connecting epithelial cells",
                    "Consequence When Altered": "Loss causes detachment and single-file infiltration (lobular carcinoma)"
                },
                "Proteases": {
                    "Role in Invasion / Metastasis": "Cleave the basement membrane and type IV collagen",
                    "Consequence When Altered": "Degrade stroma and release growth-promoting agents"
                },
                "Actin cytoskeleton": {
                    "Role in Invasion / Metastasis": "Drives amoeboid tumor cell migration",
                    "Consequence When Altered": "Enables cells to ratchet through the extracellular matrix"
                },
                "Laminin receptors": {
                    "Role in Invasion / Metastasis": "Bind laminin, a major basement membrane component",
                    "Consequence When Altered": "Overexpression facilitates adhesion, migration, and invasion"
                },
                "Platelets and coagulation factors": {
                    "Role in Invasion / Metastasis": "Coat circulating tumor cells",
                    "Consequence When Altered": "Form emboli that help cells survive bloodstream shear stress"
                }
            }
        },
        {
            "slug": "landing_site_determinants",
            "title": "Determinants of the Metastatic Landing Site",
            "subtitle": "Match each determinant of where tumor cells settle to how it works and a classic illustration",
            "categories": ["How It Works", "Classic Illustration"],
            "data": {
                "Vascular / lymphatic drainage": {
                    "How It Works": "Cells lodge in the first capillary bed or node downstream",
                    "Classic Illustration": "Colon cancer to the liver via the portal vein"
                },
                "Tissue tropism ('seed and soil')": {
                    "How It Works": "Adhesion molecules and chemokine receptors match a target organ",
                    "Classic Illustration": "Cells home to organs providing a favorable soil"
                },
                "Escape from dormancy": {
                    "How It Works": "Tumor secretes cytokines, growth factors, and ECM molecules",
                    "Classic Illustration": "Remodels resident stroma to become habitable"
                },
                "Multicellular aggregation": {
                    "How It Works": "Cells travel as clumps bound to platelets",
                    "Classic Illustration": "Emboli survive the bloodstream better than single cells"
                },
                "Tumor cell size": {
                    "How It Works": "A large tumor cell is trapped at the first capillary bed",
                    "Classic Illustration": "Helps explain lung and liver as common sites"
                }
            }
        }
    ]
}
