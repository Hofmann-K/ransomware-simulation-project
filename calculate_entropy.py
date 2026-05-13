import os
import math
from collections import Counter
import csv

# CONFIG
SANDBOX_ROOT = r"C:\Users\kevin\OneDrive\RutgersSpring-2026\Hardware Secuirty\term_project\sandbox"
KEVIN_ROOT = os.path.join(SANDBOX_ROOT, "Users", "Kevin")

OUTPUT_CSV = r"C:\Users\kevin\OneDrive\RutgersSpring-2026\Hardware Secuirty\term_project\entropy_report_clean.csv"

# Shannon entropy (0–8)
def shannon_entropy(file_path):
    try:
        with open(file_path, "rb") as f:
            data = f.read()

        if not data:
            return 0

        freq = Counter(data)
        probs = [count / len(data) for count in freq.values()]

        entropy = -sum(p * math.log2(p) for p in probs)
        return entropy

    except Exception:
        return None

# Scale entropy to 0–100
def scale_entropy(entropy):
    if entropy is None:
        return None
    return (entropy / 8.0) * 100

# Get all files recursively
def get_all_files(root):
    files = []
    for dirpath, _, filenames in os.walk(root):
        for f in filenames:
            files.append(os.path.join(dirpath, f))
    return files

# Compute directory averages
def compute_directory_averages(base_path):
    results = []

    for item in os.listdir(base_path):
        dir_path = os.path.join(base_path, item)

        if not os.path.isdir(dir_path):
            continue

        entropies = []

        for file_path in get_all_files(dir_path):
            e = shannon_entropy(file_path)
            if e is not None:
                entropies.append(e)

        if entropies:
            avg = sum(entropies) / len(entropies)
            results.append((item, avg, scale_entropy(avg)))

    return results

# Compute system-wide entropy
def compute_system_entropy(root):
    entropies = []

    for file_path in get_all_files(root):
        e = shannon_entropy(file_path)
        if e is not None:
            entropies.append(e)

    avg = sum(entropies) / len(entropies)
    return avg, scale_entropy(avg)

# Compute per-file entropy for specific folders
def compute_file_details(folder_path):
    results = []

    for file_path in get_all_files(folder_path):
        e = shannon_entropy(file_path)
        if e is not None:
            results.append((file_path, e, scale_entropy(e)))

    return results

# Save everything to CSV
def save_results(dir_avgs, system_avg, file_details_docs, file_details_proj):
    with open(OUTPUT_CSV, "w", newline="") as f:
        writer = csv.writer(f)

        writer.writerow(["Type", "Name/Path", "Entropy (0-8)", "Entropy (0-100)"])

        # Directory averages
        for name, e, s in dir_avgs:
            writer.writerow(["DIRECTORY_AVG", name, f"{e:.4f}", f"{s:.2f}"])

        # System average
        writer.writerow(["SYSTEM_AVG", "ALL_FILES", f"{system_avg[0]:.4f}", f"{system_avg[1]:.2f}"])

        # File-level details (Documents)
        for path, e, s in file_details_docs:
            writer.writerow(["FILE_DETAIL_DOCS", path, f"{e:.4f}", f"{s:.2f}"])

        # File-level details (Projects)
        for path, e, s in file_details_proj:
            writer.writerow(["FILE_DETAIL_PROJECTS", path, f"{e:.4f}", f"{s:.2f}"])

# Main
def main():
    # Directory averages (inside Kevin)
    dir_avgs = compute_directory_averages(KEVIN_ROOT)

    # System-wide entropy
    system_avg = compute_system_entropy(SANDBOX_ROOT)

    # File-level details
    docs_path = os.path.join(KEVIN_ROOT, "Documents")
    proj_path = os.path.join(KEVIN_ROOT, "Projects")

    file_details_docs = compute_file_details(docs_path)
    file_details_proj = compute_file_details(proj_path)

    # Save results
    save_results(dir_avgs, system_avg, file_details_docs, file_details_proj)

    print("Entropy analysis complete.")
    print(f"Report saved to: {OUTPUT_CSV}")

if __name__ == "__main__":
    main()