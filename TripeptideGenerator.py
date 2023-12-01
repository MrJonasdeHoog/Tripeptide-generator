def read_amino_acids(filename):
    amino_acids = {}
    with open(filename, 'r') as file:
        # Skip the header line
        next(file)
        for line in file:
            abbrev, formula = line.strip().split('\t')
            amino_acids[abbrev] = formula
    return amino_acids

def generate_tripeptides_with_formulas(amino_acids):
    tripeptides_with_formulas = []
    abbreviations = list(amino_acids.keys())

    for first in abbreviations:
        for second in abbreviations:
            for third in abbreviations:
                # Ensure the generated sequence follows the specified rules
                if first != second and second != third and third != first:
                    tripeptide_name = f"{first}-{second}-{third}"
                    tripeptide_formula = f"{amino_acids[first]}-{amino_acids[second]}-{amino_acids[third]}"
                    tripeptides_with_formulas.append((tripeptide_name, tripeptide_formula))

    return tripeptides_with_formulas

def write_tripeptides_to_file(tripeptides, output_filename):
    with open(output_filename, 'w') as file:
        for tripeptide in tripeptides:
            file.write(tripeptide + '\n')

if __name__ == "__main__":
    # Read amino acids data from the file
    amino_acids_data = read_amino_acids("amino_acids.txt")

    # Generate all possible tripeptide combinations with formulas
    all_tripeptides_with_formulas = generate_tripeptides_with_formulas(amino_acids_data)

    # Write the tripeptides and formulas to a new text file
    with open("tripeptides_with_formulas.txt", 'w') as file:
        file.write("{:<20}\t{}\n".format("Tripeptide Name", "Combined Formula"))
        for tripeptide, formula in all_tripeptides_with_formulas:
            file.write("{:<20}\t{}\n".format(tripeptide, formula))

    print("Tripeptides and formulas computed and written to 'tripeptides_with_formulas.txt'")
    
