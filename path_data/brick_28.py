BRICK = {
    "brick_num": 28,
    "brick_title": "Molecular Basis of Neoplasia: Oncogenes, Tumor Suppressor Genes, and Neoplastic Progression (Part 1 of 2)",
    "games": [
        {
            "slug": "onco_drivers",
            "title": "Oncogenic Drivers",
            "subtitle": "Match each oncogene to its protein class, signaling role, and a key associated cancer",
            "categories": ["Protein Class", "Signaling Role", "Key Associated Cancer"],
            "data": {
                "EGFR": {
                    "Protein Class": "Receptor tyrosine kinase",
                    "Signaling Role": "Ligand binding activates Ras/MAPK pro-growth signaling",
                    "Key Associated Cancer": "Lung adenocarcinoma"
                },
                "KRAS": {
                    "Protein Class": "Membrane-bound G protein",
                    "Signaling Role": "GTP/GDP on-off switch upstream of MAPK and PI3K",
                    "Key Associated Cancer": "Pancreatic ductal adenocarcinoma"
                },
                "BRAF": {
                    "Protein Class": "RAF-family serine/threonine kinase",
                    "Signaling Role": "Phosphorylates MEK in the MAPK pathway",
                    "Key Associated Cancer": "Cutaneous melanoma"
                },
                "PIK3CA": {
                    "Protein Class": "Catalytic subunit of PI3K (lipid kinase)",
                    "Signaling Role": "Converts PIP2 to PIP3 to activate AKT",
                    "Key Associated Cancer": "Breast carcinoma"
                },
                "BCR::ABL": {
                    "Protein Class": "Nonreceptor tyrosine kinase fusion",
                    "Signaling Role": "Constitutively active pro-growth signaling",
                    "Key Associated Cancer": "Chronic myeloid leukemia"
                },
                "MYC": {
                    "Protein Class": "Transcription factor",
                    "Signaling Role": "Activates cell-cycle, ribosome, and pluripotency genes",
                    "Key Associated Cancer": "Burkitt lymphoma"
                }
            }
        },
        {
            "slug": "targeted_therapy",
            "title": "Targeted Therapies in Oncology",
            "subtitle": "Match each drug to its molecular target, drug class, and the cancer it treats",
            "categories": ["Molecular Target", "Drug Class", "Cancer Treated"],
            "data": {
                "Necitumumab": {
                    "Molecular Target": "EGFR extracellular domain",
                    "Drug Class": "Monoclonal antibody blocking ligand binding",
                    "Cancer Treated": "Lung adenocarcinoma"
                },
                "Dabrafenib": {
                    "Molecular Target": "BRAF",
                    "Drug Class": "Small-molecule BRAF inhibitor",
                    "Cancer Treated": "Cutaneous melanoma"
                },
                "Trametinib": {
                    "Molecular Target": "MEK",
                    "Drug Class": "MEK inhibitor",
                    "Cancer Treated": "Cutaneous melanoma"
                },
                "Imatinib": {
                    "Molecular Target": "BCR::ABL fusion protein",
                    "Drug Class": "Tyrosine kinase inhibitor",
                    "Cancer Treated": "Chronic myeloid leukemia"
                },
                "Alpelisib": {
                    "Molecular Target": "PI3K (PIK3CA)",
                    "Drug Class": "PI3K inhibitor",
                    "Cancer Treated": "Breast carcinoma"
                }
            }
        },
        {
            "slug": "signal_cascade",
            "title": "Pro-Growth Signaling Cascade",
            "subtitle": "Place each signaling molecule by its type, function, and downstream target",
            "categories": ["Molecule Type", "Function", "Downstream Target"],
            "data": {
                "EGFR": {
                    "Molecule Type": "Receptor tyrosine kinase",
                    "Function": "Binds ligand and autophosphorylates",
                    "Downstream Target": "Activates Ras"
                },
                "Ras": {
                    "Molecule Type": "Membrane-bound G protein",
                    "Function": "Toggles between GTP (on) and GDP (off) states",
                    "Downstream Target": "Activates BRAF and PI3K"
                },
                "BRAF": {
                    "Molecule Type": "Serine/threonine kinase",
                    "Function": "Phosphorylates and activates MEK",
                    "Downstream Target": "Activates ERK"
                },
                "PI3K": {
                    "Molecule Type": "Lipid kinase",
                    "Function": "Phosphorylates PIP2 to PIP3",
                    "Downstream Target": "Activates AKT"
                },
                "AKT": {
                    "Molecule Type": "Serine/threonine kinase",
                    "Function": "Activated by PIP3; over 150 protein targets",
                    "Downstream Target": "Activates mTOR"
                },
                "PTEN": {
                    "Molecule Type": "Lipid phosphatase (tumor suppressor)",
                    "Function": "Converts PIP3 back to PIP2",
                    "Downstream Target": "Shuts off AKT signaling"
                }
            }
        },
        {
            "slug": "neoplasm_hallmarks",
            "title": "Neoplasms: Histology and Molecular Hallmark",
            "subtitle": "Match each neoplasm to its cell of origin, characteristic histology, and molecular alteration",
            "categories": ["Cell / Tissue of Origin", "Characteristic Histology", "Molecular Alteration"],
            "data": {
                "Neuroblastoma": {
                    "Cell / Tissue of Origin": "Neural crest (adrenal gland / abdominal sites)",
                    "Characteristic Histology": "Small round blue cells with Homer Wright rosettes",
                    "Molecular Alteration": "MYCN amplification"
                },
                "Burkitt lymphoma": {
                    "Cell / Tissue of Origin": "Neoplastic B-cells",
                    "Characteristic Histology": "Starry-sky pattern with tingible-body macrophages",
                    "Molecular Alteration": "t(8;14) IG::MYC rearrangement"
                },
                "Chronic myeloid leukemia": {
                    "Cell / Tissue of Origin": "Myeloid granulocyte lineage",
                    "Characteristic Histology": "Hypercellular marrow, small hyposegmented megakaryocytes",
                    "Molecular Alteration": "t(9;22) BCR::ABL (Philadelphia chromosome)"
                },
                "Cutaneous melanoma": {
                    "Cell / Tissue of Origin": "Melanocytes",
                    "Characteristic Histology": "Brown melanin pigment in an irregular lesion",
                    "Molecular Alteration": "BRAF V600E mutation"
                },
                "Pancreatic ductal adenocarcinoma": {
                    "Cell / Tissue of Origin": "Pancreatic ductal epithelium",
                    "Characteristic Histology": "Duct-like glandular spaces of neoplastic cells",
                    "Molecular Alteration": "KRAS mutation"
                },
                "Lung adenocarcinoma": {
                    "Cell / Tissue of Origin": "Glandular lung epithelium (often never-smokers)",
                    "Characteristic Histology": "Solid invasive nests or growth along alveolar walls",
                    "Molecular Alteration": "EGFR mutation"
                }
            }
        }
    ]
}
