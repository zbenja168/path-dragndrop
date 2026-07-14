BRICK = {
    "brick_num": 22,
    "brick_title": "Diseases of the Immune System: Transplantation",
    "games": [
        {
            "slug": "graft_types",
            "title": "Types of Grafts",
            "subtitle": "Match each graft type to its donor-recipient pairing, genetic match, and a clinical example",
            "categories": ["Donor and Recipient", "Genetic Match", "Example"],
            "data": {
                "Autograft": {
                    "Donor and Recipient": "One person is both donor and recipient",
                    "Genetic Match": "Identical (patient's own tissue)",
                    "Example": "Skin moved from the thigh to a burn on the same person"
                },
                "Isograft": {
                    "Donor and Recipient": "Two individuals who are identical twins",
                    "Genetic Match": "Genetically identical, same species",
                    "Example": "Kidney transplanted between identical twins"
                },
                "Allograft": {
                    "Donor and Recipient": "Two different people",
                    "Genetic Match": "Genetically different, same species",
                    "Example": "Most human organ transplants"
                },
                "Xenograft": {
                    "Donor and Recipient": "A human and an animal",
                    "Genetic Match": "Different species",
                    "Example": "Animal tissue or organ implanted into a human"
                }
            }
        },
        {
            "slug": "liver_donor_pathology",
            "title": "Donor Liver Frozen-Section Findings",
            "subtitle": "Match each donor-liver pathology to its appearance, site affected, and transplant implication",
            "categories": ["Definition / Appearance", "Site or Cell Affected", "Transplant Implication"],
            "data": {
                "Steatosis": {
                    "Definition / Appearance": "Fat accumulation within cells (macrovesicular and microvesicular)",
                    "Site or Cell Affected": "Hepatocyte cytoplasm",
                    "Transplant Implication": ">30% macrovesicular is relative, >60% is absolute contraindication"
                },
                "Portal inflammation": {
                    "Definition / Appearance": "Lymphocytic infiltrate seen as numerous blue dots on H&E",
                    "Site or Cell Affected": "Portal tract (portal vein, hepatic artery, bile duct)",
                    "Transplant Implication": "Seen in fatty liver disease; assessed for organ viability"
                },
                "Fibrosis": {
                    "Definition / Appearance": "Deposition of collagen, graded by extent of involvement",
                    "Site or Cell Affected": "Bridging between portal areas (highlighted by trichrome stain)",
                    "Transplant Implication": "Higher fibrosis stage lowers graft suitability"
                },
                "Necrosis": {
                    "Definition / Appearance": "Coagulative necrosis with loss of nuclear detail",
                    "Site or Cell Affected": "Hepatocytes, shrunken with loss of dark-staining nuclei",
                    "Transplant Implication": ">10% necrosis may disqualify transplantation"
                }
            }
        },
        {
            "slug": "kidney_donor_pathology",
            "title": "Donor Kidney Frozen-Section Findings",
            "subtitle": "Match each donor-kidney pathology to the structure affected, histologic change, and a key detail",
            "categories": ["Structure Affected", "Histologic Change", "Grading / Key Detail"],
            "data": {
                "Interstitial fibrosis and inflammation": {
                    "Structure Affected": "Interstitium and tubules",
                    "Histologic Change": "Scarring with an inflammatory cell infiltrate",
                    "Grading / Key Detail": "Assessed on frozen section to gauge viability"
                },
                "Arterial sclerosis": {
                    "Structure Affected": "Arteries (intimal layer)",
                    "Histologic Change": "Collagenous matrix and smooth muscle between endothelium and internal elastic lamina",
                    "Grading / Key Detail": "Intimal thickening graded mild, moderate, or severe"
                },
                "Arteriolar hyalinization": {
                    "Structure Affected": "Arterioles",
                    "Histologic Change": "Wall thickened by homogenous, eosinophilic protein material",
                    "Grading / Key Detail": "Vessel wall takes on a glassy pink appearance"
                },
                "Global glomerulosclerosis": {
                    "Structure Affected": "Glomeruli",
                    "Histologic Change": "Scarring and hyalinization of the glomerular tuft",
                    "Grading / Key Detail": "Involves more than half of the glomerulus"
                }
            }
        },
        {
            "slug": "matching_allocation",
            "title": "Organ Matching and Allocation Systems",
            "subtitle": "Match each system or score to its full name, function, and a key detail",
            "categories": ["Full Name / Definition", "Function", "Key Detail"],
            "data": {
                "OPTN": {
                    "Full Name / Definition": "Organ Procurement and Transplantation Network",
                    "Function": "National system created to share donor organs",
                    "Key Detail": "Established by the U.S. government in 1984"
                },
                "UNOS": {
                    "Full Name / Definition": "United Network for Organ Sharing",
                    "Function": "Runs computerized matching and generates a candidate rank list",
                    "Key Detail": "Matched 46,630 transplants in 2023"
                },
                "MELD score": {
                    "Full Name / Definition": "Model for End-Stage Liver Disease",
                    "Function": "Ranks liver urgency in patients age 12 or older",
                    "Key Detail": "Uses bilirubin, sodium, albumin, creatinine, and INR"
                },
                "PELD score": {
                    "Full Name / Definition": "Pediatric End-Stage Liver Disease",
                    "Function": "Ranks liver urgency in patients younger than 12",
                    "Key Detail": "Uses height, weight, bilirubin, albumin, INR, and creatinine"
                },
                "Status 1 designation": {
                    "Full Name / Definition": "Highest-priority liver listing",
                    "Function": "Overrides the standard MELD/PELD ranking",
                    "Key Detail": "Used for patients in fulminant hepatic failure"
                }
            }
        }
    ]
}
