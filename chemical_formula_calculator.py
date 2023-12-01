# Function to take any amino acids chemical formula and compute the tripeptide formula

def combine_amino_acids(amino_acids):
    # Initialize the combined structure with the first amino acid
    combined_structure = amino_acids[0]

    # Iterate over the remaining amino acids and concatenate their structures with a peptide bond
    for amino_acid in amino_acids[1:]:
        # Remove the terminal groups of the current amino acid (NH2 from N-terminus and COOH from C-terminus)
        amino_acid = amino_acid[6:-4]
        # Combine with a peptide bond
        combined_structure += f"-{amino_acid}"

    return combined_structure

def write_to_file(filename, combined_structure):
    with open(filename, 'w') as file:
        file.write(combined_structure)

# Example usage with Glycine, Serine, and Valine
amino_acids = ["NH2-CH2-COOH", "NH2-CH(OH)-CH2-COOH", "NH2-CH(CH3)-CH2-COOH"]
combined_structure = combine_amino_acids(amino_acids)

# Write the combined structure to a text file
write_to_file("combined_structure.txt", combined_structure)

print("Combined Chemical Structure:")
print(combined_structure)
print("Data written to 'combined_structure.txt'")
