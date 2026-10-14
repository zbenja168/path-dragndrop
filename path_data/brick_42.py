BRICK = {
    "brick_num": 42,
    "brick_title": "Cancer Growth, Metastasis, and Medications Overview",
    "games": [
        {
            "slug": "metastasis_steps",
            "title": "The Steps of Metastasis",
            "subtitle": "Match each step of metastasis to what happens and its key mechanism or obstacle",
            "categories": ["What Happens", "Key Mechanism or Obstacle"],
            "data": {
                "Invasion": {
                    "What Happens": "Cells separate and breach basement membrane and ECM",
                    "Key Mechanism or Obstacle": "Loss of E-cadherin/catenins plus protease cleavage of matrix"
                },
                "Intravasation": {
                    "What Happens": "Tumor cells enter the bloodstream or lymphatics",
                    "Key Mechanism or Obstacle": "Most die from shear stress or loss-of-adhesion apoptosis"
                },
                "Survival in circulation": {
                    "What Happens": "Cells travel as multicellular aggregates, bound to platelets",
                    "Key Mechanism or Obstacle": "Large size lodges cells in the first capillary bed"
                },
                "Extravasation": {
                    "What Happens": "Tumor cells exit the vessel into the target tissue",
                    "Key Mechanism or Obstacle": "Destination shaped by drainage, tropism, and dormancy escape"
                },
                "Growth at secondary site": {
                    "What Happens": "Deposit enlarges into a distant metastasis",
                    "Key Mechanism or Obstacle": "Tumor secretions make resident stroma habitable"
                }
            }
        },
        {
            "slug": "routes_of_spread",
            "title": "Routes of Spread: Tumor to Destination",
            "subtitle": "Match each tumor to its route of spread, typical destination, and the reason for that destination",
            "categories": ["Route of Spread", "Typical Destination", "Why There"],
            "data": {
                "Breast carcinoma (upper outer quadrant)": {
                    "Route of Spread": "Lymphatic",
                    "Typical Destination": "Axillary lymph nodes",
                    "Why There": "Nearby lymphatic drainage of that quadrant"
                },
                "Colon adenocarcinoma": {
                    "Route of Spread": "Hematogenous via portal venous blood",
                    "Typical Destination": "Liver",
                    "Why There": "First downstream organ receiving the colon's venous drainage"
                },
                "Bladder or prostate carcinoma": {
                    "Route of Spread": "Hematogenous via systemic veins",
                    "Typical Destination": "Lung",
                    "Why There": "Superior and inferior vena cava blood flows to the lungs"
                },
                "Ovarian carcinoma": {
                    "Route of Spread": "Seeding of a body cavity",
                    "Typical Destination": "Peritoneal cavity and omentum",
                    "Why There": "Open space lets cells be sown like seeds"
                },
                "Glioblastoma": {
                    "Route of Spread": "Seeding along cerebrospinal fluid spaces",
                    "Typical Destination": "Brain and spinal cord",
                    "Why There": "Subarachnoid space provides an open path"
                },
                "Sarcoma": {
                    "Route of Spread": "Hematogenous (mesenchymal tumor pattern)",
                    "Typical Destination": "Distant organs via the circulation",
                    "Why There": "Mesenchymal tumors are associated with blood-borne spread"
                }
            }
        },
        {
            "slug": "cytotoxic_chemo_mechanisms",
            "title": "Cytotoxic Chemotherapy by Cell Cycle Phase",
            "subtitle": "Match each drug to its phase specificity, drug class, and mechanism of action",
            "categories": ["Phase Specificity", "Drug Class", "Mechanism"],
            "data": {
                "Methotrexate": {
                    "Phase Specificity": "S phase",
                    "Drug Class": "Antimetabolite (folate pathway)",
                    "Mechanism": "Inhibits dihydrofolate reductase, blocking reduced folate formation"
                },
                "Irinotecan": {
                    "Phase Specificity": "S/G2 phases",
                    "Drug Class": "Topoisomerase I inhibitor",
                    "Mechanism": "Prevents religation of cleaved DNA, causing double-strand breaks"
                },
                "Bleomycin": {
                    "Phase Specificity": "G2 phase",
                    "Drug Class": "DNA-binding strand breaker",
                    "Mechanism": "Binds DNA, producing single- and double-strand breaks"
                },
                "Vinca alkaloids": {
                    "Phase Specificity": "M phase (arrest at metaphase)",
                    "Drug Class": "Microtubule inhibitor (blocks assembly)",
                    "Mechanism": "Bind tubulin and prevent mitotic spindle formation"
                },
                "Taxanes": {
                    "Phase Specificity": "M phase (mitotic interference)",
                    "Drug Class": "Microtubule inhibitor (blocks disassembly)",
                    "Mechanism": "Stabilize existing microtubules and inhibit their breakdown"
                },
                "Cyclophosphamide / cisplatin": {
                    "Phase Specificity": "Cell cycle independent",
                    "Drug Class": "Alkylating agent / platinum agent",
                    "Mechanism": "Cross-link DNA chains, blocking replication and transcription"
                }
            }
        },
        {
            "slug": "targeted_and_cell_therapy",
            "title": "Targeted Antibodies, Immunotherapy, and Cell Therapy",
            "subtitle": "Match each therapy to its target and its main antitumor effect",
            "categories": ["Target", "Main Effect"],
            "data": {
                "Rituximab": {
                    "Target": "CD20 on B cells",
                    "Main Effect": "Makes malignant B cells more susceptible to immune attack"
                },
                "Bevacizumab": {
                    "Target": "Vascular endothelial growth factor (VEGF)",
                    "Main Effect": "Inhibits tumor angiogenesis, starving cancer cells of blood"
                },
                "Trastuzumab": {
                    "Target": "HER2 receptors on tumor cells",
                    "Main Effect": "Blocks growth signaling and marks cells for immune destruction"
                },
                "Immune checkpoint-targeting drugs": {
                    "Target": "Inhibitory immune checkpoint pathways",
                    "Main Effect": "Prevent tumors from turning off the antitumor immune response"
                },
                "CAR-T cells": {
                    "Target": "Cancer antigen via a chimeric BCR-domain/CD3 receptor",
                    "Main Effect": "Reinfused autologous T cells directly target tumor cells"
                }
            }
        }
    ]
}
