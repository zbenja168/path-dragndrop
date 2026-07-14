BRICK = {
    "brick_num": 29,
    "brick_title": "Molecular Basis of Neoplasia: Oncogenes, Tumor Suppressor Genes, and Neoplastic Progression (Part 2 of 2)",
    "games": [
        {
            "slug": "tumor_predisposition_syndromes",
            "title": "Tumor Predisposition Syndromes",
            "subtitle": "Match each hereditary cancer syndrome to its mutated gene, disrupted pathway, and hallmark clinical feature",
            "categories": ["Mutated Gene", "Pathway / Mechanism Disrupted", "Hallmark Clinical Feature"],
            "data": {
                "Retinoblastoma syndrome": {
                    "Mutated Gene": "RB1",
                    "Pathway / Mechanism Disrupted": "Loss of pRB lets cells pass the G1/S checkpoint",
                    "Hallmark Clinical Feature": "Leukocoria in infancy; predisposition to sarcomas"
                },
                "Li-Fraumeni syndrome": {
                    "Mutated Gene": "TP53",
                    "Pathway / Mechanism Disrupted": "Loss of p53, the 'guardian of the genome'",
                    "Hallmark Clinical Feature": "Early breast carcinoma and osteosarcoma"
                },
                "Familial adenomatous polyposis": {
                    "Mutated Gene": "APC",
                    "Pathway / Mechanism Disrupted": "Uninhibited beta-catenin in the WNT pathway",
                    "Hallmark Clinical Feature": "Hundreds of colonic polyps; ~100% cancer risk by age 45"
                },
                "Neurofibromatosis type 1": {
                    "Mutated Gene": "NF1",
                    "Pathway / Mechanism Disrupted": "Unchecked Ras signaling from lost GTPase activation",
                    "Hallmark Clinical Feature": "Cafe-au-lait macules and neurofibromas"
                }
            }
        },
        {
            "slug": "p53_pathway_players",
            "title": "The p53 Pathway",
            "subtitle": "Match each molecule to its identity, activating context, and action within the p53 pathway",
            "categories": ["Molecular Identity", "Trigger / Context", "Action in the p53 Pathway"],
            "data": {
                "MDM2": {
                    "Molecular Identity": "E3 ubiquitin ligase",
                    "Trigger / Context": "Active in unstressed, healthy cells",
                    "Action in the p53 Pathway": "Tags p53 for proteasomal degradation"
                },
                "ATM": {
                    "Molecular Identity": "Serine/threonine protein kinase",
                    "Trigger / Context": "DNA double-strand breaks",
                    "Action in the p53 Pathway": "Activates Chk2 to phosphorylate p53 off MDM2"
                },
                "p14/ARF (CDKN2A)": {
                    "Molecular Identity": "Tumor suppressor protein",
                    "Trigger / Context": "Oncogenic stress such as unchecked Ras",
                    "Action in the p53 Pathway": "Binds MDM2 to stabilize and raise p53"
                },
                "BAX": {
                    "Molecular Identity": "Pro-apoptotic BCL-2 family protein",
                    "Trigger / Context": "Irreversible DNA damage",
                    "Action in the p53 Pathway": "Executes intrinsic (mitochondrial) apoptosis"
                },
                "p53 tetramer": {
                    "Molecular Identity": "Active transcription factor",
                    "Trigger / Context": "Cellular stress that stabilizes p53",
                    "Action in the p53 Pathway": "Blocks the cell from entering S phase"
                }
            }
        },
        {
            "slug": "adenoma_carcinoma_sequence",
            "title": "Colonic Adenoma-Carcinoma Sequence",
            "subtitle": "Order the classic colon cancer pathway by matching each step to its gene event, signaling consequence, and tissue result",
            "categories": ["Gene / Molecular Event", "Signaling Consequence", "Tissue / Gross Result"],
            "data": {
                "Step 1 - Initiation": {
                    "Gene / Molecular Event": "Both APC alleles knocked out (first and second hit)",
                    "Signaling Consequence": "Uninhibited beta-catenin / TCF-LEF proliferation",
                    "Tissue / Gross Result": "Small, benign, non-invasive adenoma forms"
                },
                "Step 2 - Growth": {
                    "Gene / Molecular Event": "Oncogenic KRAS mutation acquired",
                    "Signaling Consequence": "Enhanced proliferation with resistance to apoptosis",
                    "Tissue / Gross Result": "Adenoma enlarges into a grossly visible polyp"
                },
                "Step 3 - Progression": {
                    "Gene / Molecular Event": "Loss of TP53 function",
                    "Signaling Consequence": "Failed cell-cycle arrest and DNA repair",
                    "Tissue / Gross Result": "Chromosomal instability; further mutations accumulate"
                },
                "Step 4 - Malignancy": {
                    "Gene / Molecular Event": "Altered telomere function and additional hits",
                    "Signaling Consequence": "Replicative immortality and tissue invasion",
                    "Tissue / Gross Result": "Invasive, metastatic adenocarcinoma"
                }
            }
        },
        {
            "slug": "epigenetics_in_cancer",
            "title": "Epigenetic Changes in Cancer",
            "subtitle": "Match each epigenetic mechanism to its molecular action and effect in carcinogenesis",
            "categories": ["Epigenetic Mechanism", "Molecular Action", "Effect in Cancer"],
            "data": {
                "DNA hypermethylation": {
                    "Epigenetic Mechanism": "Adds methyl groups at promoter CpG islands",
                    "Molecular Action": "Silences the gene's promoter region",
                    "Effect in Cancer": "Silences a tumor suppressor gene"
                },
                "DNA hypomethylation": {
                    "Epigenetic Mechanism": "Removes methyl groups from DNA",
                    "Molecular Action": "De-represses a normally silenced promoter",
                    "Effect in Cancer": "Permits aberrant oncogene expression"
                },
                "Histone modification": {
                    "Epigenetic Mechanism": "Chemically alters DNA-binding histone proteins",
                    "Molecular Action": "Controls chromatin accessibility",
                    "Effect in Cancer": "Shifts expression of cancer hallmark genes"
                },
                "microRNA binding": {
                    "Epigenetic Mechanism": "Binds complementary mRNA transcripts",
                    "Molecular Action": "Blocks translation of the message",
                    "Effect in Cancer": "Silences mRNA needed for protein synthesis"
                }
            }
        }
    ]
}
