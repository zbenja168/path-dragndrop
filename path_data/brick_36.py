BRICK = {
    "brick_num": 36,
    "brick_title": "Cancer Medications Overview",
    "games": [
        {
            "slug": "cytotoxic_mechanisms",
            "title": "Cytotoxic Chemotherapy: Mechanisms",
            "subtitle": "Match each agent to its drug class, mechanism of action, and cell cycle target",
            "categories": ["Drug Class", "Mechanism of Action", "Cell Cycle Target"],
            "data": {
                "Methotrexate": {
                    "Drug Class": "Antimetabolite",
                    "Mechanism of Action": "Inhibits dihydrofolate reductase and thymidylate synthetase",
                    "Cell Cycle Target": "S phase"
                },
                "Cytarabine": {
                    "Drug Class": "Antimetabolite",
                    "Mechanism of Action": "Pyrimidine analog that inhibits DNA polymerase",
                    "Cell Cycle Target": "S phase"
                },
                "Irinotecan": {
                    "Drug Class": "Topoisomerase inhibitor",
                    "Mechanism of Action": "Binds topoisomerase I-DNA complex, blocking strand relegation",
                    "Cell Cycle Target": "S and G phases"
                },
                "Bleomycin": {
                    "Drug Class": "Antitumor antibiotic",
                    "Mechanism of Action": "Binds DNA causing single- and double-strand breaks",
                    "Cell Cycle Target": "G2 phase"
                },
                "Vinca alkaloids": {
                    "Drug Class": "Microtubule inhibitor",
                    "Mechanism of Action": "Bind tubulin, inhibit microtubule formation, arrest metaphase",
                    "Cell Cycle Target": "M phase"
                },
                "Cyclophosphamide": {
                    "Drug Class": "Alkylating agent",
                    "Mechanism of Action": "Cross-links DNA chains, inhibiting replication and transcription",
                    "Cell Cycle Target": "Cell cycle-independent"
                }
            }
        },
        {
            "slug": "signature_toxicities",
            "title": "ChemoMan: Signature Toxicities",
            "subtitle": "Match each agent to its drug class, signature adverse effect, and cell cycle phase",
            "categories": ["Drug Class", "Signature Toxicity", "Cell Cycle Phase"],
            "data": {
                "Doxorubicin": {
                    "Drug Class": "Anthracycline / alkylating agent",
                    "Signature Toxicity": "Cardiotoxicity",
                    "Cell Cycle Phase": "Cell cycle-independent"
                },
                "Bleomycin": {
                    "Drug Class": "Antitumor antibiotic",
                    "Signature Toxicity": "Pulmonary fibrosis",
                    "Cell Cycle Phase": "G2 phase"
                },
                "Vincristine": {
                    "Drug Class": "Vinca alkaloid",
                    "Signature Toxicity": "Peripheral neuropathy",
                    "Cell Cycle Phase": "M phase"
                },
                "Cyclophosphamide": {
                    "Drug Class": "Alkylating agent",
                    "Signature Toxicity": "Hemorrhagic cystitis",
                    "Cell Cycle Phase": "Cell cycle-independent"
                },
                "Cytarabine": {
                    "Drug Class": "Antimetabolite",
                    "Signature Toxicity": "Keratitis and conjunctivitis",
                    "Cell Cycle Phase": "S phase"
                },
                "Irinotecan": {
                    "Drug Class": "Topoisomerase I inhibitor",
                    "Signature Toxicity": "Severe acute and delayed diarrhea",
                    "Cell Cycle Phase": "S and G phases"
                }
            }
        },
        {
            "slug": "targeted_therapy",
            "title": "Targeted Therapy & Immunotherapy",
            "subtitle": "Match each agent to its molecular target, effect, and clinical use",
            "categories": ["Molecular Target", "Effect", "Clinical Use"],
            "data": {
                "Rituximab": {
                    "Molecular Target": "CD20 on B cells",
                    "Effect": "Makes B cells susceptible to immune attack",
                    "Clinical Use": "Non-Hodgkin lymphoma and chronic lymphocytic leukemia"
                },
                "Bevacizumab": {
                    "Molecular Target": "Vascular endothelial growth factor (VEGF)",
                    "Effect": "Inhibits angiogenesis, starving the tumor of blood supply",
                    "Clinical Use": "Solid tumors dependent on angiogenesis"
                },
                "Trastuzumab": {
                    "Molecular Target": "HER2 receptor on tumor cells",
                    "Effect": "Blocks growth signaling and marks cells for immune destruction",
                    "Clinical Use": "HER2-positive breast cancer"
                },
                "CAR-T cells": {
                    "Molecular Target": "Cancer antigen via chimeric receptor",
                    "Effect": "Modified autologous T cells directly recognize tumor cells",
                    "Clinical Use": "Adoptive cell therapy for cancer"
                }
            }
        },
        {
            "slug": "cell_cycle_targets",
            "title": "Cell Cycle Phases & Drug Targets",
            "subtitle": "Match each phase to its key event, the chemo class acting there, and an example agent",
            "categories": ["Key Event", "Chemo Class Acting Here", "Example Agent"],
            "data": {
                "G0 phase": {
                    "Key Event": "Quiescent, nondividing cell (neurons, skeletal muscle)",
                    "Chemo Class Acting Here": "None; not targeted by chemotherapy",
                    "Example Agent": "None (minimal malignant potential)"
                },
                "G1 phase": {
                    "Key Event": "Synthesizes mRNA and proteins needed for the cycle",
                    "Chemo Class Acting Here": "Antimetabolites block the G1 to S transition",
                    "Example Agent": "Methotrexate"
                },
                "S phase": {
                    "Key Event": "Chromosomal DNA is replicated",
                    "Chemo Class Acting Here": "Antimetabolites and topoisomerase inhibitors",
                    "Example Agent": "Cytarabine"
                },
                "G2 phase": {
                    "Key Event": "Synthesizes microtubule protein for the mitotic spindle",
                    "Chemo Class Acting Here": "DNA strand-breaking agent",
                    "Example Agent": "Bleomycin"
                },
                "M phase": {
                    "Key Event": "Mitosis; mitotic spindle separates chromosomes",
                    "Chemo Class Acting Here": "Microtubule inhibitors",
                    "Example Agent": "Vinca alkaloids"
                }
            }
        }
    ]
}
