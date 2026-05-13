import os
import shutil
import random

# CONFIG
SOURCE_DIR = r"C:\Users\kevin\OneDrive\RutgersSpring-2026\Hardware Secuirty\term_project\sample_files"
TARGET_ROOT = r"C:\Users\kevin\OneDrive\RutgersSpring-2026\Hardware Secuirty\term_project\sandbox"

random.seed(42)

# Updated structure (no "compressed")
STRUCTURE = {
    "Users/Kevin/Documents": ["docs", "config"],
    "Users/Kevin/Desktop": ["docs", "images"],
    "Users/Kevin/Downloads": ["executables", "docs"],
    "Users/Kevin/Pictures": ["images"],
    "Users/Kevin/Videos": ["video"],
    "Users/Kevin/Music": ["audio"],
    "Users/Kevin/Projects": ["code", "config"],
}

# Build file pool (each file used once)
def build_file_pool(source_dir):
    pool = {}
    for category in os.listdir(source_dir):
        category_path = os.path.join(source_dir, category)
        if os.path.isdir(category_path):
            files = [
                os.path.join(category_path, f)
                for f in os.listdir(category_path)
                if os.path.isfile(os.path.join(category_path, f))
            ]
            pool[category.lower()] = files
    return pool

# Create directories
def create_structure(root, structure):
    for path in structure:
        full_path = os.path.join(root, path)
        os.makedirs(full_path, exist_ok=True)

# Distribute files WITHOUT duplication
def distribute_files(root, structure, pool):
    # Flatten all files into category buckets
    available_files = {k: v.copy() for k, v in pool.items()}

    for folder, categories in structure.items():
        target_path = os.path.join(root, folder)

        # Shuffle categories for randomness
        random.shuffle(categories)

        for category in categories:
            if category not in available_files:
                continue

            files = available_files[category]

            # Shuffle files to randomize selection
            random.shuffle(files)

            # Move ALL remaining files of that category into valid folders
            while files:
                src = files.pop()  # removes file (prevents reuse)

                base, ext = os.path.splitext(os.path.basename(src))
                new_name = f"{base}_{random.randint(1000,9999)}{ext}"
                dst = os.path.join(target_path, new_name)

                shutil.copy(src, dst)

# Clear sandbox
def clear_sandbox(path):
    if os.path.exists(path):
        shutil.rmtree(path)

# Main
def main():
    clear_sandbox(TARGET_ROOT)

    file_pool = build_file_pool(SOURCE_DIR)

    create_structure(TARGET_ROOT, STRUCTURE)
    distribute_files(TARGET_ROOT, STRUCTURE, file_pool)

    print("Filesystem generated (no duplication).")

if __name__ == "__main__":
    main()