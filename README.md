# 565-ransomware-simulaton
Final project for 565 Hardware and System Secuirty which simulates a basic ransomware attack on a simualted Windows 11 file system following ranowmare behavior from the paper "Ransomware: Recent advances, analysis, challenges and future research directions" found here: https://www.sciencedirect.com/science/article/pii/S016740482100314X

# README — Simulated Ransomware Framework

## Project Overview

This project implements a safe and isolated ransomware simulation environment designed for cybersecurity education and entropy based ransomware analysis. The framework generates a realistic Windows-style simulated filesystem, calculates baseline Shannon entropy measurements, performs AES-based ransomware encryption on selected files, and reevaluates entropy after the simulated attack.

The project was developed strictly for educational and research purposes and must only be executed within an isolated virtual machine environment.

Do to ethical reasons, I still not be adding the ransomware script to this GitHub. If it is needed for grading (e.g. you are the professor or TA) please contact me via canvas or via email at  kevin.hofmann@rutgers.edu.

---

# Important Safety Notice

This project simulates ransomware behavior and performs real file encryption operations within the provided sandbox directory.

* DO NOT run this project on a real filesystem
* DO NOT target personal directories or production systems
* ONLY execute within an isolated virtual machine
* This project is intended solely for educational cybersecurity research

---

# System Requirements

## Hardware Requirements

* Minimum 8 GB RAM
* At least 25 GB free storage
* Virtualization enabled in BIOS

---

# Software Requirements

## Required Software

* [Oracle VirtualBox](https://www.virtualbox.org)
* [Windows 11 ISO Download](https://www.microsoft.com/software-download/windows11)
* [Python 3.11](https://www.python.org/downloads)
* [Visual Studio Code](https://code.visualstudio.com)

---

# Python Dependencies

Install required packages:

```bash id="0yq57m"
pip install cryptography
```

---

# Project Directory Structure

Example directory layout:

```text id="wmz7kk"
term_project/
│
├── code/
│   ├── generate_file_system.py
│   ├── entropy_analysis.py
│   └── ransomware_sim.py
│
├── sample_files/
│   ├── audio/
│   ├── code/
│   ├── config/
│   ├── database/
│   ├── docs/
│   ├── executables/
│   ├── images/
│   └── videos/
│
├── sandbox/
│
├── entropy_report.csv
├── encryption_key.txt
└── README.md
```

---

# Step 1 — Create the Virtual Machine

## 1. Install VirtualBox

Install Oracle VirtualBox from:

[VirtualBox Download Page](https://www.virtualbox.org/wiki/Downloads.com)

---

## 2. Download Windows 11 ISO

Download the Windows 11 installation ISO from:

[Windows 11 ISO Download](https://www.microsoft.com/software-download/windows11.com)

---

## 3. Create the VM

Recommended VM configuration:

| Setting   | Recommended Value |
| --------- | ----------------- |
| OS        | Windows 11        |
| RAM       | 6 GB              |
| CPU Cores | 4                 |
| Storage   | 25 GB             |

---

## 4. Install Windows 11

Install Windows 11 normally inside the VM.

---

# Step 2 — Set Up the Project Environment

## 1. Install Python

Install Python 3.11 inside the VM:

[Python Downloads](https://www.python.org/downloads.com)

Verify installation:

```bash id="zivg3h"
python --version
```

---

## 2. Install Visual Studio Code

[VS Code Download](https://code.visualstudio.com)

---

## 3. Clone or Copy the Project

Place the project in a working directory such as:

```text id="f1xqfr"
C:\Users\<username>\Documents\term_project
```

Avoid cloud-synced folders such as OneDrive.

---

# Step 3 — Acquire Sample Files

## 1. Download Sample Files

Download representative sample files from:

[FileSamples.com](https://filesamples.com)

Recommended file categories:

* Documents
* Images
* Videos
* Audio
* Source Code
* Databases
* Configuration Files
* Executables

---

## 2. Organize Files

Place downloaded files into:

```text id="7vdg5m"
sample_files/
```

Example:

```text id="7g0ht4"
sample_files/docs/
sample_files/images/
sample_files/audio/
sample_files/videos/
sample_files/code/
sample_files/config/
sample_files/database/
sample_files/executables/
```

Use valid, openable files rather than randomly generated dummy files.

---

# Step 4 — Generate the Simulated File System

Run:

```bash id="1t7e5k"
python generate_file_system.py
```

This script:

* Creates a Windows-style filesystem
* Generates realistic user directories
* Distributes sample files logically
* Creates the sandbox environment

Generated structure example:

```text id="4mu5s3"
sandbox/
└── Users/
    └── Kevin/
        ├── Desktop/
        ├── Documents/
        ├── Downloads/
        ├── Music/
        ├── Pictures/
        ├── Projects/
        └── Videos/
```

---

# Step 5 — Calculate Baseline Entropy

Run:

```bash id="zjlwm4"
python entropy_analysis.py
```

This script calculates:

* Directory-level Shannon entropy
* System-wide entropy averages
* File-level entropy values

Output:

```text id="4tv4zu"
entropy_report.csv
```

Save this CSV as the baseline (clean filesystem) result.

---

# Step 6 — Execute the Ransomware Simulation

Run:

```bash id="9p4k4k"
python ransomware_sim.py
```

The ransomware simulation will:

* Traverse the simulated filesystem
* Encrypt selected file types using AES-256
* Rename encrypted files
* Generate ransom notes
* Store the encryption key externally

Generated outputs include:

* `.encrypted` files
* `README_RESTORE_FILES.txt`
* `encryption_key.txt`

---

# Step 7 — Recalculate Entropy After Encryption

Run the entropy analysis again:

```bash id="ic9m77"
python entropy_analysis.py
```

Compare the new entropy values against the baseline results.

Expected observations:

* Significant entropy increase in encrypted directories
* Increased system-wide entropy
* Loss of file readability and accessibility

---

# Step 8 — Verify the Results

Successful execution should demonstrate:

## 1. File Encryption

Targeted files renamed with:

```text id="q0qr6q"
.encrypted
```

---

## 2. Ransom Note Generation

Example:

```text id="aj3m1f"
README_RESTORE_FILES.txt
```

---

## 3. Entropy Increase

Expected entropy behavior:

| State           | Typical Entropy |
| --------------- | --------------- |
| Plaintext Files | Lower           |
| Encrypted Files | Near Maximum    |

---

# Reproducing the Evaluation Results

To fully reproduce the experiment:

1. Generate the clean filesystem
2. Record baseline entropy
3. Execute ransomware simulation
4. Recalculate entropy
5. Compare before/after results

The attack success rate should reach 100% for all targeted file extensions.

---

# Ethical Considerations

This project was designed exclusively for:

* cybersecurity education
* malware analysis research
* entropy-based ransomware evaluation

Safety precautions include:

* isolated VM execution
* dedicated sandbox filesystem
* no interaction with host files
* explicit educational disclaimers in ransom notes

This project must not be modified or deployed for malicious purposes.

---

# References

[1] *Ransomware: Recent advances, analysis, challenges and future research directions*

[2] *Machine Learning Based File Entropy Analysis for Ransomware Detection in Backup Systems*, IEEE Access, 2019.
