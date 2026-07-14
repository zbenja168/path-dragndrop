BRICK = {
    "brick_num": 31,
    "brick_title": "Hallmarks of Neoplasia: Genomic Instability",
    "games": [
        {
            "slug": "repair_pathways",
            "title": "DNA Repair Pathways",
            "subtitle": "Match each DNA repair mechanism to the lesion it fixes, how it works, and the disorder caused by its defect",
            "categories": ["Lesion Corrected", "Key Mechanism", "Disorder When Defective"],
            "data": {
                "Nucleotide excision repair (NER)": {
                    "Lesion Corrected": "Helix-distorting single-strand lesions, e.g. UV pyrimidine dimers",
                    "Key Mechanism": "Endonucleases and helicase remove and replace an oligonucleotide containing the lesion",
                    "Disorder When Defective": "Xeroderma pigmentosum"
                },
                "Mismatch repair (MMR)": {
                    "Lesion Corrected": "Base-base mismatches from DNA replication errors",
                    "Key Mechanism": "Mut-class proteins recognize and excise the mismatched oligonucleotide, mainly in S phase",
                    "Disorder When Defective": "Lynch syndrome"
                },
                "Homologous recombination (HR)": {
                    "Lesion Corrected": "Double-strand breaks, repaired accurately",
                    "Key Mechanism": "Uses a homologous chromosome as a template with no loss of nucleotides",
                    "Disorder When Defective": "BRCA1/2 cancers and Fanconi anemia"
                },
                "Nonhomologous end joining (NHEJ)": {
                    "Lesion Corrected": "Double-strand breaks, repaired error-prone",
                    "Key Mechanism": "Ligase complex directly fuses the two DNA ends without requiring homology",
                    "Disorder When Defective": "SCID and ataxia telangiectasia"
                }
            }
        },
        {
            "slug": "predisposition_syndromes",
            "title": "Cancer Predisposition Syndromes",
            "subtitle": "Match each inherited syndrome to its defective repair pathway, cancer risk, and distinctive feature",
            "categories": ["Defective Repair Pathway", "Cancer Risk", "Distinctive Feature"],
            "data": {
                "Xeroderma pigmentosum": {
                    "Defective Repair Pathway": "Nucleotide excision repair",
                    "Cancer Risk": "Skin cancer (squamous cell, basal cell, melanoma)",
                    "Distinctive Feature": "Extreme photosensitivity; freckling in sun-exposed face and neck, sparing shoulders"
                },
                "Lynch syndrome": {
                    "Defective Repair Pathway": "Mismatch repair",
                    "Cancer Risk": "Colorectal cancer of cecum/proximal colon and endometrial cancer",
                    "Distinctive Feature": "Microsatellite instability; loss of MLH1/PMS2 on immunohistochemistry"
                },
                "Hereditary breast/ovarian cancer (BRCA1)": {
                    "Defective Repair Pathway": "Homologous recombination",
                    "Cancer Risk": "Breast and ovarian cancer",
                    "Distinctive Feature": "Over 60% lifetime breast cancer risk versus 13% in the general population"
                },
                "Fanconi anemia": {
                    "Defective Repair Pathway": "Homologous recombination (DNA cross-link repair)",
                    "Cancer Risk": "Leukemia and bone marrow failure (aplasia)",
                    "Distinctive Feature": "Autosomal recessive; short stature and skeletal abnormalities"
                },
                "Ataxia telangiectasia": {
                    "Defective Repair Pathway": "Nonhomologous end joining",
                    "Cancer Risk": "Leukemia and lymphoma",
                    "Distinctive Feature": "Telangiectasias of skin and eyes with ataxia beginning before age 5"
                }
            }
        },
        {
            "slug": "mismatch_repair_lynch",
            "title": "Mismatch Repair and Lynch Syndrome",
            "subtitle": "Match each component or concept to what it is, its function, and its key clinical fact",
            "categories": ["What It Is", "Function", "Key Clinical Fact"],
            "data": {
                "MSH2-MSH6 complex": {
                    "What It Is": "A heterodimer of Mut-class mismatch repair proteins",
                    "Function": "Identifies mismatch errors in newly synthesized DNA",
                    "Key Clinical Fact": "Intact expression shows normal brown nuclear staining on immunohistochemistry"
                },
                "MLH1-PMS2 complex": {
                    "What It Is": "A heterodimer of Mut-class mismatch repair proteins",
                    "Function": "Excises the incorrect base after the mismatch is recognized",
                    "Key Clinical Fact": "Loss of MLH1 destabilizes PMS2, so both are typically lost together"
                },
                "Microsatellite": {
                    "What It Is": "A tandem repeat of 1-6 nucleotides found throughout the genome",
                    "Function": "Length stays constant in people with functional mismatch repair",
                    "Key Clinical Fact": "Becomes unstable in length (microsatellite instability) when repair is defective"
                },
                "Lynch syndrome": {
                    "What It Is": "An autosomal dominant cancer predisposition syndrome",
                    "Function": "Caused by a germline mutation in MLH1, MSH2, MSH6, or PMS2",
                    "Key Clinical Fact": "Most common inherited colorectal cancer syndrome, about 3% of new colorectal cancers"
                }
            }
        },
        {
            "slug": "core_concepts",
            "title": "Genomic Instability Core Concepts",
            "subtitle": "Match each term to its definition, its cause or trigger, and its board-relevant significance",
            "categories": ["Definition", "Cause or Trigger", "Significance"],
            "data": {
                "DNA lesion": {
                    "Definition": "Any site of damage within a polynucleotide",
                    "Cause or Trigger": "Chemical damage occurring roughly 70,000 times per cell per day",
                    "Significance": "Becomes a mutation if it is not corrected"
                },
                "Mutation": {
                    "Definition": "A change in the DNA base sequence",
                    "Cause or Trigger": "An uncorrected DNA lesion",
                    "Significance": "Retained in all subsequent generations of the cell lineage"
                },
                "Genomic instability": {
                    "Definition": "Increased propensity for genomic mutations",
                    "Cause or Trigger": "Deficient DNA repair or heavy exposure to genetic damage",
                    "Significance": "A mutator phenotype and a hallmark of neoplasia"
                },
                "Cell cycle checkpoint": {
                    "Definition": "A global assessment of the genome for DNA lesions",
                    "Cause or Trigger": "Established before and after S-phase DNA replication",
                    "Significance": "Halts division to allow repair, or triggers apoptosis if damage is excessive"
                },
                "Pyrimidine dimer": {
                    "Definition": "A covalent lesion linking adjacent pyrimidines",
                    "Cause or Trigger": "Ultraviolet (UV) light exposure",
                    "Significance": "Repaired by NER because humans lack photolyase"
                }
            }
        }
    ]
}
