BRICK = {
    "brick_num": 15,
    "brick_title": "Introduction to Infection",
    "games": [
        {
            "slug": "points_of_entry",
            "title": "Points of Entry",
            "subtitle": "Match each portal of entry to its main defense and clinical example",
            "categories": ["Main Barrier / Defense", "How Pathogens Enter", "Clinical Example"],
            "data": {
                "Skin": {
                    "Main Barrier / Defense": "Keratinized squamous epithelium, fatty acids, defensins",
                    "How Pathogens Enter": "Breaks from wounds, burns, bites, or IV catheters",
                    "Clinical Example": "Skin-flora endocarditis after IV drug use"
                },
                "Gastrointestinal Tract": {
                    "Main Barrier / Defense": "Gastric acid, peristalsis, IgA, and gut microbiota",
                    "How Pathogens Enter": "Ingestion of food or water contaminated by feces",
                    "Clinical Example": "C. difficile colitis after antibiotics deplete flora"
                },
                "Respiratory Tract": {
                    "Main Barrier / Defense": "Mucociliary clearance trapping and sweeping particles",
                    "How Pathogens Enter": "Inhalation of aerosolized particles into airways",
                    "Clinical Example": "Small particles reach alveoli and are phagocytosed"
                },
                "Urogenital Tract": {
                    "Main Barrier / Defense": "Flushing flow of urine through the urethra",
                    "How Pathogens Enter": "Ascension of organisms up the urethra",
                    "Clinical Example": "Urinary obstruction raises infection susceptibility"
                },
                "Placenta (Vertical)": {
                    "Main Barrier / Defense": "Placental barrier separating maternal and fetal blood",
                    "How Pathogens Enter": "Transplacental passage from mother to fetus",
                    "Clinical Example": "TORCH agents (Toxoplasma, syphilis, Rubella, CMV, HSV)"
                }
            }
        },
        {
            "slug": "person_to_person",
            "title": "Person-to-Person Transmission",
            "subtitle": "Match each mode of transmission to how it spreads and a typical pathogen",
            "categories": ["How It Spreads", "Example Pathogen", "Key Feature"],
            "data": {
                "Fecal-Oral": {
                    "How It Spreads": "Feces contaminate ingested food or water",
                    "Example Pathogen": "Hepatitis A virus",
                    "Key Feature": "Poor sanitation and fecal contamination drive spread"
                },
                "Respiratory Droplet": {
                    "How It Spreads": "Coughing and sneezing release aerosolized droplets",
                    "Example Pathogen": "SARS-CoV-2 (COVID-19)",
                    "Key Feature": "Small droplets can travel beyond six feet and linger"
                },
                "Sexual Contact": {
                    "How It Spreads": "Direct mucosal contact during intercourse",
                    "Example Pathogen": "Neisseria gonorrhoeae",
                    "Key Feature": "Presents with painful urination and discharge"
                },
                "Vector-Borne": {
                    "How It Spreads": "Bite of an infected insect or animal",
                    "Example Pathogen": "Rabies virus from a raccoon bite",
                    "Key Feature": "Pathogen introduced through the animal bite wound"
                },
                "Vertical": {
                    "How It Spreads": "Mother to infant via placenta or birth canal",
                    "Example Pathogen": "N. gonorrhoeae causing neonatal conjunctivitis",
                    "Key Feature": "Maternal symptoms are often mild or absent"
                },
                "Contact / Fomites": {
                    "How It Spreads": "Hardy forms persist on surfaces and hands",
                    "Example Pathogen": "C. difficile spores",
                    "Key Feature": "Spores resist alcohol, requiring soap-and-water washing"
                }
            }
        },
        {
            "slug": "histologic_patterns",
            "title": "Histologic Patterns of Reaction",
            "subtitle": "Match each tissue reaction to its dominant feature and a classic cause",
            "categories": ["Dominant Feature", "Classic Cause", "Key Detail"],
            "data": {
                "Suppurative Inflammation": {
                    "Dominant Feature": "Neutrophils forming pus and abscesses",
                    "Classic Cause": "Pyogenic bacteria causing bronchopneumonia",
                    "Key Detail": "Abscess is a localized collection of pus"
                },
                "Granulomatous Inflammation": {
                    "Dominant Feature": "Epithelioid macrophages and giant cells",
                    "Classic Cause": "Tuberculosis and sarcoidosis",
                    "Key Detail": "Central caseating necrosis is typical of TB"
                },
                "Mononuclear (Lymphocytic)": {
                    "Dominant Feature": "Diffuse lymphocytic infiltrate",
                    "Classic Cause": "Spirochetes such as Treponema pallidum",
                    "Key Detail": "Also seen with intracellular bacteria and parasites"
                },
                "Cytopathic-Cytoproliferative": {
                    "Dominant Feature": "Inclusion bodies, cell lysis, and proliferation",
                    "Classic Cause": "Viruses such as CMV and HPV",
                    "Key Detail": "HPV produces proliferative warts"
                },
                "Tissue Necrosis": {
                    "Dominant Feature": "Cell death with pseudomembrane formation",
                    "Classic Cause": "Corynebacterium diphtheriae toxin",
                    "Key Detail": "Gray pharyngeal pseudomembrane can block the airway"
                },
                "Chronic Inflammation and Scarring": {
                    "Dominant Feature": "Dense fibrosis from unresolved insult",
                    "Classic Cause": "Chronic hepatitis B infection",
                    "Key Detail": "Liver fibrosis progresses to cirrhosis"
                }
            }
        },
        {
            "slug": "toxins_and_damage",
            "title": "Toxins and Cellular Damage",
            "subtitle": "Match each toxin to its mechanism and clinical effect",
            "categories": ["Mechanism", "Clinical Effect", "Source Clue"],
            "data": {
                "Endotoxin (LPS)": {
                    "Mechanism": "Lipid A of gram-negative outer membrane activates macrophages",
                    "Clinical Effect": "Cytokine surge with hypotension and shock",
                    "Source Clue": "Structural component of gram-negative bacteria"
                },
                "Diphtheria Toxin": {
                    "Mechanism": "A-B toxin whose A subunit halts protein synthesis",
                    "Clinical Effect": "Cell death, pseudomembrane, and myocarditis",
                    "Source Clue": "Produced by Corynebacterium diphtheriae"
                },
                "Exfoliative Toxin": {
                    "Mechanism": "Cleaves desmoglein-1 anchoring keratinocytes",
                    "Clinical Effect": "Staphylococcal scalded skin syndrome with blistering",
                    "Source Clue": "Made by S. aureus, affecting young children"
                },
                "Staphylococcal Enterotoxin": {
                    "Mechanism": "Heat-stable superantigen acting on the GI tract",
                    "Clinical Effect": "Rapid vomiting and non-bloody diarrhea",
                    "Source Clue": "Preformed in foods like custards and potato salad"
                },
                "Toxic Shock Syndrome Toxin": {
                    "Mechanism": "Superantigen driving nonspecific cytokine release",
                    "Clinical Effect": "Toxic shock syndrome with hypotension",
                    "Source Clue": "From S. aureus or Streptococcus pyogenes"
                }
            }
        }
    ]
}
