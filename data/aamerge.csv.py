import glob
import os
import pandas as pd

# 1. Grab all CSV files in the current directory
csv_files = glob.glob("*.csv")

# Exclude the output file if it already exists from a previous run
output_filename = "AAAmaster_combined_data.csv"
if output_filename in csv_files:
    csv_files.remove(output_filename)

combined_data = []

# 2. Loop through and read each CSV file
for file in csv_files:
    print(f"Processing: {file}")
    df = pd.read_csv(file)

    # Standardize column headers to lowercase to fix case-sensitivity mismatches
    df.columns = df.columns.str.strip().str.lower()

    combined_data.append(df)

# 3. Stack all data frames vertically
if combined_data:
    master_df = pd.concat(combined_data, ignore_index=True)

    # 4. Remove completely identical duplicate rows
    initial_rows = len(master_df)
    master_df.drop_duplicates(inplace=True)
    print(f"Removed {initial_rows - len(master_df)} duplicate rows.")

    # 🆕 Add the new 'Instruction' column (fills with empty values by default)
    master_df['instruction'] = ""

    # 5. Format headers back to your preferred capitalized style safely
    preferred_headers = [
        "Name",
        "Address",
        "Website",
        "Phone_number",
        "Reviews_count",
        "Reviews_average",
        "Place_Type",
        "Opens_at",
        "Instruction"  # Added your new column here
    ]
    
    # Safely map names to avoid crashing if there are unexpected extra columns
    new_columns = preferred_headers + [
        f"Extra_Column_{i+1}" for i in range(len(master_df.columns) - len(preferred_headers))
    ]
    master_df.columns = new_columns[:len(master_df.columns)]

    # 6. Save the final merged dataset
    master_df.to_csv(output_filename, index=False)
    print(f"\n🎉 Success! All files merged into: '{output_filename}'")
else:
    print("No CSV files found in this folder.")
