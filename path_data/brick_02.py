BRICK = {
    "brick_num": 2,
    "brick_title": "Cancer Staging and Grading",
    "games": [
        {
            "slug": "measuring_survival",
            "title": "Measuring Survival",
            "subtitle": "Match each survival statistic to its definition, its death/recurrence rule, and its time anchor",
            "categories": ["Definition", "Deaths / Events Counted", "Measured From"],
            "data": {
                "Cancer-specific survival": {
                    "Definition": "Percent of patients not dead from that specific cancer",
                    "Deaths / Events Counted": "Only deaths caused by the cancer count",
                    "Measured From": "The time of cancer diagnosis"
                },
                "Overall survival": {
                    "Definition": "Percent of patients not dead from any cause",
                    "Deaths / Events Counted": "Death from any cause counts",
                    "Measured From": "The time of cancer diagnosis"
                },
                "Disease-free survival": {
                    "Definition": "Percent of patients with no signs of cancer",
                    "Deaths / Events Counted": "Tracks cancer recurrence, not death",
                    "Measured From": "Completion of treatment"
                },
                "Relative survival": {
                    "Definition": "Percent alive compared with cancer-free peers",
                    "Deaths / Events Counted": "Compared against a matched cancer-free population",
                    "Measured From": "The time of cancer diagnosis"
                }
            }
        },
        {
            "slug": "tnm_staging",
            "title": "The TNM Staging System",
            "subtitle": "Match each staging component to what its letter means, what it assesses, and its scale and prognostic weight",
            "categories": ["Letter Stands For", "What It Assesses", "Scale and Weight"],
            "data": {
                "T": {
                    "Letter Stands For": "Tumor",
                    "What It Assesses": "Size or depth of invasion of the primary tumor",
                    "Scale and Weight": "1 to 4, with 1 smallest and 4 largest"
                },
                "N": {
                    "Letter Stands For": "Node",
                    "What It Assesses": "Spread to nearby lymph nodes",
                    "Scale and Weight": "0 to 3; second most important after metastasis"
                },
                "M": {
                    "Letter Stands For": "Metastasis",
                    "What It Assesses": "Spread to distant organs in the body",
                    "Scale and Weight": "0 or 1; the single most important component"
                },
                "Overall stage": {
                    "Letter Stands For": "Combined TNM stage",
                    "What It Assesses": "Overall size of the tumor and how far it has spread",
                    "Scale and Weight": "0 to 4; the most important prognostic factor for survival"
                }
            }
        },
        {
            "slug": "tumor_markers",
            "title": "Tumor Markers and Their Cancers",
            "subtitle": "Match each tumor marker to the cancer it is associated with and a distinguishing clinical note",
            "categories": ["Associated Cancer", "Clinical Note"],
            "data": {
                "CA19-9": {
                    "Associated Cancer": "Colon cancer and pancreatic cancer",
                    "Clinical Note": "Rises with two gastrointestinal cancers"
                },
                "CEA": {
                    "Associated Cancer": "Colorectal carcinoma",
                    "Clinical Note": "Nonspecific serum biomarker seen in several tumors"
                },
                "Alpha-fetoprotein (AFP)": {
                    "Associated Cancer": "Hepatocellular carcinoma (HCC)",
                    "Clinical Note": "Abbreviated AFP"
                },
                "Chromogranin": {
                    "Associated Cancer": "Neuroendocrine tumors",
                    "Clinical Note": "Points to a neuroendocrine origin"
                },
                "PSA": {
                    "Associated Cancer": "Prostate cancer",
                    "Clinical Note": "Varies with age; low sensitivity and specificity, not for screening"
                },
                "CA-125": {
                    "Associated Cancer": "Ovarian cancer",
                    "Clinical Note": "Follows ovarian tumor burden"
                }
            }
        },
        {
            "slug": "prognostic_drivers",
            "title": "What Drives the Prognosis",
            "subtitle": "Match each prognostic factor to what it describes, how it is measured, and its effect on prognosis",
            "categories": ["What It Describes", "How It Is Measured", "Effect on Prognosis"],
            "data": {
                "Stage": {
                    "What It Describes": "Tumor size and how far the cancer has spread",
                    "How It Is Measured": "The TNM system, on a scale of 0 to 4",
                    "Effect on Prognosis": "The most important single prognostic factor"
                },
                "Grade": {
                    "What It Describes": "Histologic differentiation and number of mitoses",
                    "How It Is Measured": "Microscopic exam of the tumor cells",
                    "Effect on Prognosis": "High grade is worse, but weighs less than stage"
                },
                "Patient age": {
                    "What It Describes": "The patient's age and general health",
                    "How It Is Measured": "Clinical assessment of the patient",
                    "Effect on Prognosis": "Elderly or immunosuppressed patients fare worse"
                },
                "Tumor markers": {
                    "What It Describes": "Tumor substances raised in the blood or urine",
                    "How It Is Measured": "Serum or urine assay over time",
                    "Effect on Prognosis": "Track treatment response and recurrence, not diagnosis"
                },
                "Estrogen receptor status": {
                    "What It Describes": "Estrogen receptor expression in breast cancer",
                    "How It Is Measured": "Receptor testing for estrogen receptor",
                    "Effect on Prognosis": "Receptor-positive tumors carry a better prognosis"
                },
                "HER2/Neu status": {
                    "What It Describes": "HER2/Neu expression in breast cancer",
                    "How It Is Measured": "Testing for HER2/Neu overexpression",
                    "Effect on Prognosis": "HER2/Neu-negative tumors carry a better prognosis"
                }
            }
        }
    ]
}
