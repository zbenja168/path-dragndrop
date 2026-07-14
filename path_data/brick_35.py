BRICK = {
    "brick_num": 35,
    "brick_title": "Cancer Staging and Grading",
    "games": [
        {
            "slug": "tnm_components",
            "title": "The TNM Staging System",
            "subtitle": "Match each TNM element to what it describes, what a higher value means, and its prognostic impact",
            "categories": ["What It Describes", "Higher Value Indicates", "Prognostic Impact"],
            "data": {
                "T category": {
                    "What It Describes": "Size and local extent of the primary tumor",
                    "Higher Value Indicates": "Larger tumor or deeper invasion into local tissue",
                    "Prognostic Impact": "Larger, more invasive tumors carry worse outcomes"
                },
                "N category": {
                    "What It Describes": "Involvement of regional lymph nodes",
                    "Higher Value Indicates": "More numerous or more distant nodes involved",
                    "Prognostic Impact": "Nodal spread substantially worsens prognosis"
                },
                "M category": {
                    "What It Describes": "Presence of distant metastatic disease",
                    "Higher Value Indicates": "M1 = distant metastases are present",
                    "Prognostic Impact": "Single most adverse factor; defines Stage IV"
                },
                "Stage 0 (Tis)": {
                    "What It Describes": "Carcinoma in situ, no invasion through basement membrane",
                    "Higher Value Indicates": "Disease confined above the basement membrane",
                    "Prognostic Impact": "Excellent prognosis; often curable by excision"
                },
                "Stage IV": {
                    "What It Describes": "Distant metastatic (widely disseminated) disease",
                    "Higher Value Indicates": "Spread to distant organs or sites",
                    "Prognostic Impact": "Poorest prognosis; usually not curable"
                }
            }
        },
        {
            "slug": "histologic_grading",
            "title": "Histologic Grading of Tumors",
            "subtitle": "Match each grade or feature to its degree of differentiation, cellular appearance, and behavior",
            "categories": ["Degree of Differentiation", "Cellular Features", "Clinical Behavior"],
            "data": {
                "Grade 1 (low)": {
                    "Degree of Differentiation": "Well differentiated",
                    "Cellular Features": "Cells closely resemble normal tissue; few mitoses",
                    "Clinical Behavior": "Slow-growing; generally better prognosis"
                },
                "Grade 2 (intermediate)": {
                    "Degree of Differentiation": "Moderately differentiated",
                    "Cellular Features": "Some atypia; increased but moderate mitotic activity",
                    "Clinical Behavior": "Intermediate aggressiveness and outcome"
                },
                "Grade 3-4 (high)": {
                    "Degree of Differentiation": "Poorly differentiated to undifferentiated",
                    "Cellular Features": "Marked pleomorphism, high mitotic rate, atypia",
                    "Clinical Behavior": "Aggressive; worse prognosis"
                },
                "Anaplasia": {
                    "Degree of Differentiation": "Complete lack of differentiation",
                    "Cellular Features": "Giant cells, bizarre nuclei, abnormal mitotic figures",
                    "Clinical Behavior": "Hallmark of malignancy; highly aggressive"
                }
            }
        },
        {
            "slug": "treatment_response",
            "title": "Remission, Response, and Cure",
            "subtitle": "Match each response category to its definition, detectable-disease status, and key point",
            "categories": ["Definition", "Detectable Disease?", "Key Point"],
            "data": {
                "Complete remission": {
                    "Definition": "Disappearance of all detectable tumor",
                    "Detectable Disease?": "None on clinical exam or imaging",
                    "Key Point": "Not the same as cure; microscopic disease may persist"
                },
                "Partial remission": {
                    "Definition": "At least 30% reduction in measurable tumor burden",
                    "Detectable Disease?": "Reduced but still present",
                    "Key Point": "A meaningful response, but disease remains"
                },
                "Stable disease": {
                    "Definition": "Neither significant shrinkage nor growth",
                    "Detectable Disease?": "Present and essentially unchanged",
                    "Key Point": "Not a response, but not progression"
                },
                "Progressive disease": {
                    "Definition": "Tumor growth or appearance of new lesions",
                    "Detectable Disease?": "Increasing amount detectable",
                    "Key Point": "Indicates treatment failure"
                },
                "Cure": {
                    "Definition": "No evidence of disease long-term, recurrence risk near baseline",
                    "Detectable Disease?": "None over prolonged follow-up",
                    "Key Point": "Implies eradication; can only be stated in retrospect"
                }
            }
        },
        {
            "slug": "prognostic_factors",
            "title": "Prognostic Statistics and Factors",
            "subtitle": "Match each prognostic measure or factor to its meaning, what a higher value implies, and a note",
            "categories": ["Meaning", "Higher Value Implies", "Note"],
            "data": {
                "5-year survival rate": {
                    "Meaning": "Percentage of patients alive 5 years after diagnosis",
                    "Higher Value Implies": "Better overall prognosis",
                    "Note": "Standard benchmark for comparing cancers"
                },
                "Disease-free survival": {
                    "Meaning": "Time without detectable disease after treatment",
                    "Higher Value Implies": "More durable treatment response",
                    "Note": "Measures how long remission lasts"
                },
                "Overall survival": {
                    "Meaning": "Time from diagnosis to death from any cause",
                    "Higher Value Implies": "Longer life expectancy",
                    "Note": "Considered the gold-standard endpoint"
                },
                "Tumor stage": {
                    "Meaning": "Anatomic extent of spread (TNM)",
                    "Higher Value Implies": "More advanced, worse-prognosis disease",
                    "Note": "Usually the strongest predictor in solid tumors"
                },
                "Tumor grade": {
                    "Meaning": "Degree of histologic differentiation",
                    "Higher Value Implies": "More poorly differentiated, aggressive tumor",
                    "Note": "Complements stage as a prognostic factor"
                },
                "Performance status": {
                    "Meaning": "Patient's functional / activity level",
                    "Higher Value Implies": "Better ability to tolerate therapy",
                    "Note": "Guides treatment eligibility and predicts outcome"
                }
            }
        }
    ]
}
