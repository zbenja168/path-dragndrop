BRICK = {
    "brick_num": 10,
    "brick_title": "Environmental Disease: Physical and Environmental Injury",
    "games": [
        {
            "slug": "mechanical_injuries",
            "title": "Mechanical Injuries: Wound Patterns",
            "subtitle": "Match each mechanical injury to its mechanism, morphology, and forensic clue",
            "categories": ["Mechanism", "Key Morphologic Feature", "Forensic / Clinical Clue"],
            "data": {
                "Abrasion": {
                    "Mechanism": "Friction scrapes skin against a rough surface",
                    "Key Morphologic Feature": "Superficial loss of epidermis (a graze)",
                    "Forensic / Clinical Clue": "Direction of force read from heaped-up skin tags"
                },
                "Contusion (bruise)": {
                    "Mechanism": "Blunt force ruptures small vessels beneath intact skin",
                    "Key Morphologic Feature": "Hemorrhage into tissue with unbroken skin surface",
                    "Forensic / Clinical Clue": "Evolving color change helps estimate the age of injury"
                },
                "Laceration": {
                    "Mechanism": "Blunt force overstretches and tears the skin",
                    "Key Morphologic Feature": "Irregular jagged edges with intact tissue bridges",
                    "Forensic / Clinical Clue": "Bridging strands across the wound distinguish it from a cut"
                },
                "Incised wound": {
                    "Mechanism": "A sharp edge (knife or glass) cleanly cuts the skin",
                    "Key Morphologic Feature": "Clean straight margins, longer than it is deep, no bridging",
                    "Forensic / Clinical Clue": "Smooth walls point to a sharp-force weapon"
                },
                "Puncture wound": {
                    "Mechanism": "A pointed instrument penetrates into deeper tissue",
                    "Key Morphologic Feature": "Narrow entry that is deeper than it is wide",
                    "Forensic / Clinical Clue": "High risk of occult organ injury and deep infection"
                },
                "Gunshot entrance wound": {
                    "Mechanism": "A projectile perforates skin and underlying tissue",
                    "Key Morphologic Feature": "Round defect ringed by an abrasion collar",
                    "Forensic / Clinical Clue": "Surrounding soot or stippling indicates close range"
                }
            }
        },
        {
            "slug": "burn_depth",
            "title": "Thermal Burns: Depth Classification",
            "subtitle": "Match each burn degree to the tissue involved, its appearance, and pain/healing",
            "categories": ["Tissue Depth", "Appearance", "Pain and Healing"],
            "data": {
                "First-degree (superficial)": {
                    "Tissue Depth": "Epidermis only",
                    "Appearance": "Red and dry with no blisters",
                    "Pain and Healing": "Painful; heals in days with no scarring"
                },
                "Second-degree (partial-thickness)": {
                    "Tissue Depth": "Epidermis plus part of the dermis",
                    "Appearance": "Moist, red-pink, with blisters",
                    "Pain and Healing": "Very painful; may heal with scarring"
                },
                "Third-degree (full-thickness)": {
                    "Tissue Depth": "Entire epidermis and dermis destroyed",
                    "Appearance": "White, charred, and leathery (eschar)",
                    "Pain and Healing": "Painless as nerves are destroyed; needs grafting"
                },
                "Fourth-degree": {
                    "Tissue Depth": "Extends through skin into muscle and bone",
                    "Appearance": "Charred with exposed deep structures",
                    "Pain and Healing": "Painless; requires debridement or amputation"
                }
            }
        },
        {
            "slug": "thermoregulatory_disorders",
            "title": "Systemic Heat and Cold Injury",
            "subtitle": "Match each thermoregulatory disorder to its mechanism, hallmark, and key danger",
            "categories": ["Mechanism", "Hallmark Feature", "Key Danger / Management"],
            "data": {
                "Heat cramps": {
                    "Mechanism": "Electrolyte loss through sweating during exertion",
                    "Hallmark Feature": "Painful muscle cramps with a normal core temperature",
                    "Key Danger / Management": "Benign; treated with salt and fluid replacement"
                },
                "Heat exhaustion": {
                    "Mechanism": "Water and salt depletion causing volume loss",
                    "Hallmark Feature": "Fatigue and dizziness, profuse sweating, temp below 40 C",
                    "Key Danger / Management": "May progress to heat stroke if untreated"
                },
                "Heat stroke": {
                    "Mechanism": "Failure of thermoregulation with core temp above 40 C",
                    "Hallmark Feature": "Hot skin and CNS dysfunction (confusion, coma)",
                    "Key Danger / Management": "Rhabdomyolysis and DIC; emergent rapid cooling"
                },
                "Malignant hyperthermia": {
                    "Mechanism": "RYR1 mutation triggers Ca release after anesthetics",
                    "Hallmark Feature": "Muscle rigidity and rising temperature under anesthesia",
                    "Key Danger / Management": "Life-threatening; reversed with dantrolene"
                },
                "Systemic hypothermia": {
                    "Mechanism": "Prolonged cold exposure lowers the core temperature",
                    "Hallmark Feature": "Bradycardia, confusion, and Osborn (J) waves on ECG",
                    "Key Danger / Management": "Fatal arrhythmia; managed with gradual rewarming"
                },
                "Frostbite": {
                    "Mechanism": "Freezing forms ice crystals and injures local vessels",
                    "Hallmark Feature": "Necrosis of distal extremities such as fingers and toes",
                    "Key Danger / Management": "Gangrene and tissue loss; careful rewarming"
                }
            }
        },
        {
            "slug": "radiation_injury",
            "title": "Ionizing Radiation Injury",
            "subtitle": "Match each radiation effect to its target tissue, mechanism, and clinical outcome",
            "categories": ["Target Tissue", "Mechanism", "Clinical Outcome"],
            "data": {
                "Hematopoietic syndrome": {
                    "Target Tissue": "Bone marrow progenitor cells",
                    "Mechanism": "Killing of rapidly proliferating hematopoietic precursors",
                    "Clinical Outcome": "Pancytopenia with infection and bleeding after weeks"
                },
                "Gastrointestinal syndrome": {
                    "Target Tissue": "Intestinal crypt epithelium",
                    "Mechanism": "Loss of dividing crypt stem cells and mucosal barrier",
                    "Clinical Outcome": "Bloody diarrhea and sepsis, death within days"
                },
                "Cerebrovascular syndrome": {
                    "Target Tissue": "Brain vasculature and neurons",
                    "Mechanism": "Vascular injury and edema at very high doses",
                    "Clinical Outcome": "Seizures, coma, and death within hours"
                },
                "Delayed fibrosis": {
                    "Target Tissue": "Vasculature of previously irradiated tissue",
                    "Mechanism": "Endothelial injury causing chronic ischemia",
                    "Clinical Outcome": "Progressive fibrosis and atrophy of the tissue"
                },
                "Radiation carcinogenesis": {
                    "Target Tissue": "Cellular DNA",
                    "Mechanism": "Double-strand breaks and mutations in surviving cells",
                    "Clinical Outcome": "Leukemia and solid tumors years to decades later"
                }
            }
        }
    ]
}
