BRICK = {
    "brick_num": 34,
    "brick_title": "Pathogen-associated Neoplasms",
    "games": [
        {
            "slug": "pathogen_to_neoplasm",
            "title": "Pathogens and Their Neoplasms",
            "subtitle": "Match each oncogenic pathogen to its type, associated neoplasm, and oncogenic mechanism",
            "categories": ["Pathogen Type", "Key Associated Neoplasm", "Oncogenic Mechanism"],
            "data": {
                "Epstein-Barr virus (EBV)": {
                    "Pathogen Type": "Herpesvirus (human herpesvirus 4)",
                    "Key Associated Neoplasm": "Hodgkin & Burkitt lymphoma, nasopharyngeal carcinoma",
                    "Oncogenic Mechanism": "LMP-1 and EBNA-2 viral oncogenes drive B-cell proliferation"
                },
                "Human herpesvirus 8 (HHV-8)": {
                    "Pathogen Type": "Herpesvirus (Kaposi sarcoma-associated)",
                    "Key Associated Neoplasm": "Kaposi sarcoma and primary effusion lymphoma",
                    "Oncogenic Mechanism": "Altered VEGF regulation driving angiogenesis"
                },
                "High-risk HPV": {
                    "Pathogen Type": "DNA papillomavirus",
                    "Key Associated Neoplasm": "Cervical squamous cell carcinoma",
                    "Oncogenic Mechanism": "E6 inactivates p53 and E7 inactivates Rb"
                },
                "HTLV-1": {
                    "Pathogen Type": "Retrovirus (like HIV)",
                    "Key Associated Neoplasm": "Adult T-cell leukemia/lymphoma (ATLL)",
                    "Oncogenic Mechanism": "Tax and HBZ proteins drive CD4+ T-cell proliferation"
                },
                "Helicobacter pylori": {
                    "Pathogen Type": "Curved gram-negative bacterium",
                    "Key Associated Neoplasm": "Gastric adenocarcinoma and MALT lymphoma",
                    "Oncogenic Mechanism": "Chronic inflammation from longstanding gastritis"
                },
                "Schistosoma haematobium": {
                    "Pathogen Type": "Parasitic flatworm (helminth)",
                    "Key Associated Neoplasm": "Squamous cell carcinoma of the bladder",
                    "Oncogenic Mechanism": "Chronic inflammation from bladder egg deposition"
                }
            }
        },
        {
            "slug": "histologic_hallmarks",
            "title": "Histologic Hallmarks",
            "subtitle": "Match each neoplasm to its classic histologic finding and the associated pathogen",
            "categories": ["Neoplasm", "Histologic Hallmark", "Associated Pathogen"],
            "data": {
                "Classic Hodgkin lymphoma": {
                    "Neoplasm": "Malignancy of supradiaphragmatic lymph nodes",
                    "Histologic Hallmark": "Bilobed 'owl eye' Reed-Sternberg cell with eosinophilic nucleoli",
                    "Associated Pathogen": "EBV (~50% of cases)"
                },
                "Burkitt lymphoma": {
                    "Neoplasm": "Non-Hodgkin B-cell lymphoma",
                    "Histologic Hallmark": "'Starry sky' with tingible body macrophages",
                    "Associated Pathogen": "EBV (>90% of endemic cases)"
                },
                "Adult T-cell leukemia/lymphoma": {
                    "Neoplasm": "Malignancy of CD4+ T cells",
                    "Histologic Hallmark": "Multi-lobated 'flower' nucleus in acute phase",
                    "Associated Pathogen": "HTLV-1"
                },
                "Hepatocellular carcinoma": {
                    "Neoplasm": "Malignant neoplasm of hepatocyte origin",
                    "Histologic Hallmark": "Plump, eosinophilic polygonal cells with nuclear atypia",
                    "Associated Pathogen": "HBV and HCV"
                },
                "Gastric intestinal metaplasia": {
                    "Neoplasm": "Pre-neoplastic change of gastric mucosa",
                    "Histologic Hallmark": "Goblet cells and Paneth cells with red granules",
                    "Associated Pathogen": "Helicobacter pylori"
                },
                "Kaposi sarcoma": {
                    "Neoplasm": "Vascular neoplasm of endothelial origin",
                    "Histologic Hallmark": "Neoplastic vascular channels in skin lesions",
                    "Associated Pathogen": "HHV-8"
                }
            }
        },
        {
            "slug": "tumorigenesis_mechanisms",
            "title": "Mechanisms of Tumorigenesis",
            "subtitle": "Match each pathogen to its key molecular player and the resulting effect",
            "categories": ["Pathogen", "Key Molecular Player", "Result"],
            "data": {
                "High-risk HPV": {
                    "Pathogen": "Serotypes 16, 18, 31, and 33",
                    "Key Molecular Player": "E6 and E7 oncoproteins inactivate p53 and Rb",
                    "Result": "Loss of the G1-to-S checkpoint and uncontrolled proliferation"
                },
                "HHV-8": {
                    "Pathogen": "Kaposi sarcoma-associated herpesvirus",
                    "Key Molecular Player": "Altered vascular endothelial growth factor (VEGF)",
                    "Result": "Angiogenesis forming a vascular sarcoma"
                },
                "EBV": {
                    "Pathogen": "Targets B lymphocytes via the CD21 marker",
                    "Key Molecular Player": "LMP-1 and EBNA-2 viral oncogenes",
                    "Result": "B-cell proliferation and survival with acquired mutations"
                },
                "HTLV-1": {
                    "Pathogen": "Retrovirus with tropism for CD4+ T cells",
                    "Key Molecular Player": "Tax and HBZ viral proteins",
                    "Result": "T-cell proliferation with inhibited apoptosis"
                },
                "Helicobacter pylori": {
                    "Pathogen": "Curved gram-negative rod expressing CagA",
                    "Key Molecular Player": "Pro-inflammatory cytokines and chronic inflammation",
                    "Result": "Gastritis to metaplasia to dysplasia to adenocarcinoma"
                },
                "Hepatitis B and C": {
                    "Pathogen": "Hepatotropic viruses causing chronic infection",
                    "Key Molecular Player": "Reactive oxygen species and inflammatory DNA damage",
                    "Result": "Cirrhosis progressing to hepatocellular carcinoma"
                }
            }
        },
        {
            "slug": "transmission_epidemiology",
            "title": "Transmission and Epidemiology",
            "subtitle": "Match each pathogen to its main mode of transmission and the classic at-risk or endemic group",
            "categories": ["Pathogen", "Main Transmission", "Endemic / At-Risk Group"],
            "data": {
                "EBV": {
                    "Pathogen": "Herpesvirus causing mononucleosis",
                    "Main Transmission": "Oral secretions ('kissing disease')",
                    "Endemic / At-Risk Group": "Young adults"
                },
                "HTLV-1": {
                    "Pathogen": "Retrovirus causing ATLL",
                    "Main Transmission": "Mother-to-neonate at birth (most common); breast milk",
                    "Endemic / At-Risk Group": "Japan, the Caribbean, parts of Africa and South America"
                },
                "Hepatitis C virus": {
                    "Pathogen": "Hepatotropic RNA virus",
                    "Main Transmission": "IV drug use and needle-stick injury",
                    "Endemic / At-Risk Group": "60-80% of infections become chronic"
                },
                "Hepatitis B virus": {
                    "Pathogen": "Hepatotropic DNA virus",
                    "Main Transmission": "Sexual contact, IV drug use, and childbirth",
                    "Endemic / At-Risk Group": "Health professionals (vaccine required)"
                },
                "HHV-8": {
                    "Pathogen": "Kaposi sarcoma-associated herpesvirus",
                    "Main Transmission": "Bodily fluids, most commonly salivary contact",
                    "Endemic / At-Risk Group": "Immunosuppressed patients, especially those with AIDS"
                },
                "Schistosoma haematobium": {
                    "Pathogen": "Aquatic parasitic flatworm",
                    "Main Transmission": "Skin penetration in freshwater (snail intermediate host)",
                    "Endemic / At-Risk Group": "Causes bladder cancer; presents with 'swimmer's itch'"
                }
            }
        }
    ]
}
