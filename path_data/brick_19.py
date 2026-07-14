BRICK = {
    "brick_num": 19,
    "brick_title": "Infections, Immunity, and Evading Host Defense",
    "games": [
        {
            "slug": "innate_immunodeficiencies",
            "title": "Primary Immunodeficiencies of Innate Immunity",
            "subtitle": "Match each inherited innate-immunity syndrome to its defective component and hallmark finding",
            "categories": ["Defective Component / Gene", "Mechanism of Defect", "Hallmark Finding"],
            "data": {
                "Severe congenital neutropenia": {
                    "Defective Component / Gene": "Inherited severe reduction in neutrophil counts",
                    "Mechanism of Defect": "Too few neutrophils to mount a purulent inflammatory response",
                    "Hallmark Finding": "Recurrent bacterial infections with characteristically absent pus"
                },
                "Chronic granulomatous disease": {
                    "Defective Component / Gene": "NADPH oxidase in the phagolysosome",
                    "Mechanism of Defect": "Impaired reactive-oxygen-species production blocks intracellular killing",
                    "Hallmark Finding": "Granulomatous inflammation; pneumonia, liver abscess, osteomyelitis"
                },
                "Primary myeloperoxidase deficiency": {
                    "Defective Component / Gene": "Myeloperoxidase in neutrophil granules and lysosomes",
                    "Mechanism of Defect": "Cannot convert hydrogen peroxide to hypochlorous acid",
                    "Hallmark Finding": "Usually asymptomatic; severe Candida albicans infection in diabetics"
                },
                "Chediak-Higashi syndrome": {
                    "Defective Component / Gene": "LYST lysosomal trafficking regulator protein",
                    "Mechanism of Defect": "Giant granules cannot release cytotoxic contents",
                    "Hallmark Finding": "Partial albinism, neurologic defects, bleeding, recurrent infection"
                },
                "Leukocyte adhesion deficiency": {
                    "Defective Component / Gene": "Integrins on the leukocyte surface",
                    "Mechanism of Defect": "Impaired adhesion prevents leukocyte migration across endothelium",
                    "Hallmark Finding": "Recurrent infections with impaired pus formation"
                },
                "Complement deficiency": {
                    "Defective Component / Gene": "Complement cascade proteins",
                    "Mechanism of Defect": "Impaired opsonization and membrane-attack-complex formation",
                    "Hallmark Finding": "Susceptibility to infection from reduced microbial coating and lysis"
                }
            }
        },
        {
            "slug": "innate_defenses",
            "title": "Components of Innate Immunity",
            "subtitle": "Match each innate defense to its class and its action against microbes",
            "categories": ["Innate Defense", "Class", "Action"],
            "data": {
                "Cilia": {
                    "Innate Defense": "Cilia",
                    "Class": "Physical barrier",
                    "Action": "Mechanically expel pathogens from the airways"
                },
                "Lysozyme": {
                    "Innate Defense": "Lysozyme",
                    "Class": "Antimicrobial substance",
                    "Action": "Digests bacterial cell walls"
                },
                "Defensins": {
                    "Innate Defense": "Defensins",
                    "Class": "Antimicrobial substance",
                    "Action": "Disrupt bacterial membranes"
                },
                "Complement (MAC)": {
                    "Innate Defense": "Complement membrane attack complex",
                    "Class": "Plasma protein cascade",
                    "Action": "Forms a transmembrane pore that lyses the target microbe"
                },
                "Toll-like receptors": {
                    "Innate Defense": "Toll-like receptors",
                    "Class": "Pattern-recognition receptors",
                    "Action": "Recognize PAMPs and trigger cytokine and chemokine release"
                },
                "Natural killer cells": {
                    "Innate Defense": "Natural killer cells",
                    "Class": "Lymphocyte",
                    "Action": "Kill cells lacking MHC class I via perforin and granzymes"
                }
            }
        },
        {
            "slug": "evading_innate",
            "title": "Pathogen Strategies Against Innate Immunity",
            "subtitle": "Match each pathogen to the evasion strategy it uses and the result",
            "categories": ["Pathogen", "Evasion Strategy", "Result"],
            "data": {
                "Streptococcus pneumoniae": {
                    "Pathogen": "Streptococcus pneumoniae",
                    "Evasion Strategy": "Polysaccharide capsule blocks complement deposition and opsonization",
                    "Result": "Resists phagocytosis by neutrophils and macrophages"
                },
                "Cryptococcus neoformans": {
                    "Pathogen": "Cryptococcus neoformans (fungus)",
                    "Evasion Strategy": "Secretes polysaccharide capsule material",
                    "Result": "Inhibits immune attack against the fungus"
                },
                "Mycobacteria": {
                    "Pathogen": "Mycobacteria",
                    "Evasion Strategy": "Inhibits phagolysosome formation",
                    "Result": "Survives inside the macrophage"
                },
                "Histoplasma capsulatum": {
                    "Pathogen": "Histoplasma capsulatum (fungus)",
                    "Evasion Strategy": "Modulates phagolysosomal pH",
                    "Result": "Survives within the phagolysosome"
                },
                "Listeria monocytogenes": {
                    "Pathogen": "Listeria monocytogenes",
                    "Evasion Strategy": "Listeriolysin O ruptures the phagosome; ActA drives actin-based motility",
                    "Result": "Escapes into cytoplasm and spreads cell-to-cell"
                },
                "Adenovirus": {
                    "Pathogen": "Adenovirus",
                    "Evasion Strategy": "E1B-19K protein mimics anti-apoptotic BCL-2",
                    "Result": "Resists host-cell apoptosis"
                }
            }
        },
        {
            "slug": "evading_adaptive",
            "title": "Pathogen Strategies Against Adaptive Immunity",
            "subtitle": "Match each pathogen to its mechanism of evading adaptive immunity and the consequence",
            "categories": ["Pathogen", "Evasion Mechanism", "Consequence"],
            "data": {
                "Staphylococcus aureus": {
                    "Pathogen": "Staphylococcus aureus",
                    "Evasion Mechanism": "Protein A binds the Fc portion of IgG",
                    "Consequence": "Blocks IgG from engaging phagocyte Fc receptors, preventing phagocytosis"
                },
                "Neisseria (pilin)": {
                    "Pathogen": "Neisseria spp. (pilin gene)",
                    "Evasion Mechanism": "Homologous recombination swaps in a new pilin variant",
                    "Consequence": "Antigenic variation escapes existing antibodies"
                },
                "Neisseria (OPA)": {
                    "Pathogen": "Neisseria spp. (OPA gene)",
                    "Evasion Mechanism": "Five-nucleotide repeats prone to deletions and duplications alter OPA proteins",
                    "Consequence": "New surface epitopes avoid antibody detection"
                },
                "HIV": {
                    "Pathogen": "Human immunodeficiency virus",
                    "Evasion Mechanism": "gp120 binds CD4 with CCR5/CXCR4 co-receptors",
                    "Consequence": "Infects and destroys helper T cells, causing immunosuppression"
                },
                "HSV-1": {
                    "Pathogen": "Herpes simplex virus 1",
                    "Evasion Mechanism": "Blocks peptide loading onto MHC class I and its surface expression",
                    "Consequence": "Evades detection by circulating cytotoxic T cells"
                },
                "Trypanosoma brucei": {
                    "Pathogen": "Trypanosoma brucei",
                    "Evasion Mechanism": "Activates polyclonal B cells to make non-specific antibodies",
                    "Consequence": "Distracts and exhausts the antibody response (African sleeping sickness)"
                }
            }
        }
    ]
}
