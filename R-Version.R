# Function to read amino acids data from a file
read_amino_acids <- function(filename) {
  amino_acids <- read.table(filename, header = TRUE, sep = "\t", stringsAsFactors = FALSE)
  setNames(amino_acids$Formula, amino_acids$Abbrev)
}

# Function to generate tripeptides with formulas
generate_tripeptides_with_formulas <- function(amino_acids) {
  abbreviations <- names(amino_acids)
  tripeptides_with_formulas <- vector("list", length = length(abbreviations)^3)
  names(tripeptides_with_formulas) <- rep("", length(tripeptides_with_formulas))

  idx <- 1
  for (first in abbreviations) {
    for (second in abbreviations) {
      for (third in abbreviations) {
        # Ensure the generated sequence follows the specified rules
        if (first != second && second != third && third != first) {
          tripeptide_name <- paste(c(first, second, third), collapse = "-")
          tripeptide_formula <- paste(c(amino_acids[[first]], amino_acids[[second]], amino_acids[[third]]), collapse = "-")
          tripeptides_with_formulas[[idx]] <- list(tripeptide_name = tripeptide_name, tripeptide_formula = tripeptide_formula)
          idx <- idx + 1
        }
      }
    }
  }

  tripeptides_with_formulas <- tripeptides_with_formulas[1:(idx - 1)]
  tripeptides_with_formulas
}

# Function to write tripeptides and formulas to a file
write_tripeptides_to_file <- function(tripeptides, output_filename) {
  tripeptides_df <- do.call(rbind.data.frame, tripeptides)
  colnames(tripeptides_df) <- c("Tripeptide Name", "Combined Formula")
  write.table(tripeptides_df, output_filename, sep = "\t", quote = FALSE, row.names = FALSE)
  cat("Tripeptides and formulas computed and written to '", output_filename, "'\n", sep = "")
}

# Read amino acids data from the file
amino_acids_data <- read_amino_acids("amino_acids.txt")

# Generate all possible tripeptide combinations with formulas
all_tripeptides_with_formulas <- generate_tripeptides_with_formulas(amino_acids_data)

# Write the tripeptides and formulas to a new text file
write_tripeptides_to_file(all_tripeptides_with_formulas, "tripeptides_with_formulas.txt")
