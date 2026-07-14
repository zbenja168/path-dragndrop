BRICK = {
    "brick_num": 5,
    "brick_title": "Introduction to Anatomic Pathology for Patient Care",
    "games": [
        {
            "slug": "specimen_procedures",
            "title": "Tissue Procurement Procedures",
            "subtitle": "Match each surgical procedure to its definition, diagnostic role, and key example",
            "categories": ["Definition", "Diagnostic Role", "Example / Feature"],
            "data": {
                "Incisional biopsy": {
                    "Definition": "Incises and removes a portion of abnormal tissue",
                    "Diagnostic Role": "Diagnostic sampling of the lesion only",
                    "Example / Feature": "Samples part of a lesion to reach a diagnosis"
                },
                "Punch biopsy": {
                    "Definition": "Removes tissue with a cylindric blade",
                    "Diagnostic Role": "Diagnostic small-tissue sample",
                    "Example / Feature": "Commonly used for skin lesions"
                },
                "Core biopsy": {
                    "Definition": "Uses a needle to obtain a core of tissue",
                    "Diagnostic Role": "Diagnostic needle sample of a deeper lesion",
                    "Example / Feature": "Radiologist samples a lung nodule to check for cancer"
                },
                "Excisional biopsy": {
                    "Definition": "Removes the entirety of the abnormal tissue",
                    "Diagnostic Role": "Both diagnostic and therapeutic",
                    "Example / Feature": "Removes a suspicious lump; less extensive than a resection"
                },
                "Resection": {
                    "Definition": "Removes part or all of an organ",
                    "Diagnostic Role": "Therapeutic, often for malignancy",
                    "Example / Feature": "Major surgery named for the organ removed"
                }
            }
        },
        {
            "slug": "resection_terminology",
            "title": "Resection Terminology",
            "subtitle": "Match each resection to the organ removed, its body region, and a common indication",
            "categories": ["Organ Removed", "Body Region", "Common Indication"],
            "data": {
                "Colectomy": {
                    "Organ Removed": "Colon",
                    "Body Region": "Lower gastrointestinal tract",
                    "Common Indication": "Colon cancer or advanced bowel disease"
                },
                "Gastrectomy": {
                    "Organ Removed": "Stomach",
                    "Body Region": "Upper gastrointestinal tract",
                    "Common Indication": "Gastric (stomach) cancer"
                },
                "Hepatectomy": {
                    "Organ Removed": "Liver",
                    "Body Region": "Hepatobiliary system",
                    "Common Indication": "Liver tumor or metastasis"
                },
                "Mastectomy": {
                    "Organ Removed": "Breast",
                    "Body Region": "Chest wall / breast",
                    "Common Indication": "Breast cancer"
                }
            }
        },
        {
            "slug": "stains_and_tissue_tests",
            "title": "Stains and Tissue Tests",
            "subtitle": "Match each stain or test to its target, its color result, and its clinical use",
            "categories": ["Target", "Color / Result", "Clinical Use"],
            "data": {
                "Hematoxylin": {
                    "Target": "Nucleus and nuclear material",
                    "Color / Result": "Dark blue to purple",
                    "Clinical Use": "Routine H&E stain; highlights nuclei"
                },
                "Eosin": {
                    "Target": "Cytoplasmic components",
                    "Color / Result": "Pink",
                    "Clinical Use": "Routine H&E stain; highlights cytoplasm"
                },
                "GMS (methenamine silver)": {
                    "Target": "Fungal organisms",
                    "Color / Result": "Gray to black",
                    "Clinical Use": "Special stain for suspected fungal infection"
                },
                "Masson trichrome": {
                    "Target": "Collagen / connective tissue",
                    "Color / Result": "Highlights fibrosis",
                    "Clinical Use": "Special stain to visualize fibrosis"
                },
                "Immunohistochemistry": {
                    "Target": "A specific molecular antigen (e.g. cytokeratin)",
                    "Color / Result": "Usually brown",
                    "Clinical Use": "Confirms tumor origin, such as carcinoma"
                }
            }
        },
        {
            "slug": "surgical_report_sections",
            "title": "Surgical Pathology Report Sections",
            "subtitle": "Match each report section to its content, a representative detail, and its distinguishing point",
            "categories": ["Content", "Representative Detail", "Distinguishing Point"],
            "data": {
                "Final Diagnosis": {
                    "Content": "The 'top line' diagnostic line naming the disease",
                    "Representative Detail": "e.g. 'papillary thyroid carcinoma'",
                    "Distinguishing Point": "May summarize findings if the diagnosis is equivocal"
                },
                "Gross Description": {
                    "Content": "Physical description and processing of the specimen",
                    "Representative Detail": "The measured size of a tumor (the T stage)",
                    "Distinguishing Point": "Where a tumor's measured size is found"
                },
                "Microscopic Description": {
                    "Content": "What is seen under the microscope",
                    "Representative Detail": "Nuclear enlargement, overlap, and clearing",
                    "Distinguishing Point": "Optional; often folded into the comment"
                },
                "Comment": {
                    "Content": "The pathologist's opinion on the case",
                    "Representative Detail": "Immunohistochemistry and special stain results",
                    "Distinguishing Point": "May recommend additional testing or clinical correlation"
                },
                "Addendum": {
                    "Content": "A minor addition after the report is signed out",
                    "Representative Detail": "A test result not previously available",
                    "Distinguishing Point": "Does not change the diagnosis"
                },
                "Amendment": {
                    "Content": "A major change made after finalization",
                    "Representative Detail": "A change in the diagnosis itself",
                    "Distinguishing Point": "Required whenever the diagnosis changes"
                }
            }
        }
    ]
}
