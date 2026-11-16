import subprocess
import time
import re
import os  # Added to check file paths

# Read all search queries from the file
with open("queries.txt", "r", encoding="utf-8") as f:
    queries = [line.strip() for line in f if line.strip()]

# Ensure the data directory exists before starting
os.makedirs("data", exist_ok=True)

for idx, query in enumerate(queries, 1):
    # Automatically clean up the query to create a safe filename
    clean_name = re.sub(r'[^a-zA-Z0-9]', '', query)
    output_file = f"data/{clean_name}.csv"

    # ⏭️ SKIP CHECK: If the file already exists, print a message and move to the next query
    if os.path.exists(output_file):
        print(f"[{idx}/{len(queries)}] ⏭️ Skipping (Already exists): {output_file}")
        continue

    print(f"[{idx}/{len(queries)}] 🚀 Processing: {query}...")

    # Build the command arguments exactly like your original lines
    cmd = [
        "python3", "main.py",
        "-s", query,
        "-t", "20",
        "-o", output_file,
        "--append"
    ]

    try:
        # run() executes sequentially and waits until it finishes
        result = subprocess.run(cmd, check=True, text=True, capture_output=True)
        print(f"   ✅ Successfully saved to {output_file}")

    except subprocess.CalledProcessError as e:
        print(f"   ❌ Command failed at line {idx} ({query})!")
        print(f"   Error Output: {e.stderr}")
        continue 

    # IMPORTANT: Add a short pause between scripts to avoid getting IP-blocked
    time.sleep(2) 
