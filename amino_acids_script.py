# Dictionary containing the full names, abbreviations, and chemical formulas for the 20 amino acids
amino_acids_data = {
    "Alanine": {"Abbrev": "Ala", "Formula": "NH2-CH(CH3)-COOH"},
    "Arginine": {"Abbrev": "Arg", "Formula": "NH2-CH(NH2)-COOH"},
    "Asparagine": {"Abbrev": "Asn", "Formula": "NH2-CH(NH2)-COOH"},
    "Aspartic acid": {"Abbrev": "Asp", "Formula": "NH2-CH(COOH)-COOH"},
    "Cysteine": {"Abbrev": "Cys", "Formula": "NH2-CH(SH)-COOH"},
    "Glutamic acid": {"Abbrev": "Glu", "Formula": "NH2-CH(CH2-COOH)-COOH"},
    "Glutamine": {"Abbrev": "Gln", "Formula": "NH2-CH(CH2-COOH)-COOH"},
    "Glycine": {"Abbrev": "Gly", "Formula": "NH2-CH2-COOH"},
    "Histidine": {"Abbrev": "His", "Formula": "NH2-CH(C3H3N2)-COOH"},
    "Isoleucine": {"Abbrev": "Ile", "Formula": "NH2-CH(CH3)-CH2-CH(CH3)-COOH"},
    "Leucine": {"Abbrev": "Leu", "Formula": "NH2-CH(CH3)-CH2-CH(CH2CH3)-COOH"},
    "Lysine": {"Abbrev": "Lys", "Formula": "NH2-CH(CH2CH2NH2)-COOH"},
    "Methionine": {"Abbrev": "Met", "Formula": "NH2-CH2-S-CH3"},
    "Phenylalanine": {"Abbrev": "Phe", "Formula": "NH2-CH(C6H5)-COOH"},
    "Proline": {"Abbrev": "Pro", "Formula": "NH-CH2-CH2-CH(CH2)-COOH"},
    "Serine": {"Abbrev": "Ser", "Formula": "NH2-CH(OH)-CH2-COOH"},
    "Threonine": {"Abbrev": "Thr", "Formula": "NH2-CH(OH)-CH(CH3)-COOH"},
    "Tryptophan": {"Abbrev": "Trp", "Formula": "NH2-CH(C8H6N)-COOH"},
    "Tyrosine": {"Abbrev": "Tyr", "Formula": "NH2-CH(C6H4OH)-COOH"},
    "Valine": {"Abbrev": "Val", "Formula": "NH2-CH(CH3)-CH2-COOH"}
}

# Writing the data to a text file
filename = "amino_acids.txt"

with open(filename, 'w') as file:
    file.write("{:<5}\t{}\n".format("Abbrev", "Chemical Formula"))
    for amino_acid, data in amino_acids_data.items():
        file.write("{:<5}\t{}\n".format(data["Abbrev"], data["Formula"]))

print(f"Data written to '{filename}'")
