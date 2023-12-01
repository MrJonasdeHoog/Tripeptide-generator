#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <iomanip>

std::map<std::string, std::string> read_amino_acids(const std::string& filename) {
    std::map<std::string, std::string> amino_acids;

    std::ifstream file(filename);
    if (file.is_open()) {
        // Skip the header line
        std::string line;
        std::getline(file, line);

        while (std::getline(file, line)) {
            std::istringstream iss(line);
            std::string abbrev, formula;
            if (std::getline(iss, abbrev, '\t') && std::getline(iss, formula, '\t')) {
                amino_acids[abbrev] = formula;
            }
        }

        file.close();
    } else {
        std::cerr << "Error opening file: " << filename << std::endl;
    }

    return amino_acids;
}

std::vector<std::pair<std::string, std::string>> generate_tripeptides_with_formulas(const std::map<std::string, std::string>& amino_acids) {
    std::vector<std::pair<std::string, std::string>> tripeptides_with_formulas;
    std::vector<std::string> abbreviations;

    for (const auto& entry : amino_acids) {
        abbreviations.push_back(entry.first);
    }

    for (const auto& first : abbreviations) {
        for (const auto& second : abbreviations) {
            for (const auto& third : abbreviations) {
                // Ensure the generated sequence follows the specified rules
                if (first != second && second != third && third != first) {
                    std::string tripeptide_name = first + "-" + second + "-" + third;
                    std::string tripeptide_formula = amino_acids.at(first) + "-" + amino_acids.at(second) + "-" + amino_acids.at(third);
                    tripeptides_with_formulas.push_back(std::make_pair(tripeptide_name, tripeptide_formula));
                }
            }
        }
    }

    return tripeptides_with_formulas;
}

void write_tripeptides_to_file(const std::vector<std::pair<std::string, std::string>>& tripeptides, const std::string& output_filename) {
    std::ofstream file(output_filename);
    if (file.is_open()) {
        file << std::left << std::setw(20) << "Tripeptide Name" << "\t" << "Combined Formula" << "\n";
        for (const auto& tripeptide : tripeptides) {
            file << std::left << std::setw(20) << tripeptide.first << "\t" << tripeptide.second << "\n";
        }

        file.close();
        std::cout << "Tripeptides and formulas computed and written to '" << output_filename << "'" << std::endl;
    } else {
        std::cerr << "Error opening file: " << output_filename << std::endl;
    }
}

int main() {
    // Read amino acids data from the file
    std::map<std::string, std::string> amino_acids_data = read_amino_acids("amino_acids.txt");

    // Generate all possible tripeptide combinations with formulas
    std::vector<std::pair<std::string, std::string>> all_tripeptides_with_formulas = generate_tripeptides_with_formulas(amino_acids_data);

    // Write the tripeptides and formulas to a new text file
    write_tripeptides_to_file(all_tripeptides_with_formulas, "tripeptides_with_formulas.txt");

    return 0;
}
