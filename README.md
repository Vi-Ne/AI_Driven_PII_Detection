# PII Detection System - Context-Aware ML Framework

AI-Driven PII (Personally Identifiable Information) Detection Framework using **Dual-Head ContextualBERT** models. The system scans CSV/Excel files to identify sensitive data columns like names, emails, phone numbers, Aadhaar numbers, and more.

The system achieves high precision by evaluating data alongside the domain and schema of the dataset, effectively distinguishing between PII and Non-PII even with identical data values.

## Features

- **Context-Aware Architecture**: Uses a Dual-Head ContextualBERT model (Model V2) to distinguish PII based on domain and schema.
- **High Performance**: Reaches 99.9% F1-score on a multi-domain dataset with ~80k examples.
- **Binary Gating**: Implements a dedicated "Is-PII" gate layer to drastically reduce false positives in public datasets.
- **Smart Redaction**: Type-aware redaction (email masking, phone masking, ID masking, etc.)
- **Web Interface**: FastAPI-based web UI for uploading and scanning files with real-time feedback.
- **Audit Logging**: Tracks all scan operations with timestamps for compliance auditing.

## Detailed Project Structure

```text
PIIDetection/
├── src/                # [CORE] Application Logic
│   ├── main.py         # Entry point: FastAPI server and API endpoints
│   ├── model_loader.py # Logic for loading Dual-Head BERT models & tokenizers
│   ├── pii_processor.py# The "Brain": Handles context construction and prediction pipeline
│   └── utils.py        # Shared utility functions
├── models/             # [WEIGHTS] Serialized Model Artifacts (Git LFS)
│   ├── model_v2/       # The active ContextualBERT engine (recommended)
│   ├── model1/         # Legacy baseline model
│   └── ...             # model_v2 includes model.bin, config.json, and vocab.txt
├── training/           # [TRAINING] Scripts for model evolution
│   ├── train_context_model.py      # Main Model V2 training script (PyTorch)
│   ├── generate_synthetic_data.py  # Advanced generator for multi-domain training data
│   └── training_code_model_v2.py   # Alternative training experimental scripts
├── tests/              # [QUALITY] Validation and Benchmarking
│   ├── test_industry.py# Comprehensive situation-based testing (30+ scenarios)
│   └── test_context_deep.py        # Deep-dive context sensitivity verification
├── static/             # [UI] Frontend CSS and JavaScript assets
├── templates/          # [UI] HTML Jinja2 templates for the dashboard
├── docs/               # [DOCS] Technical Documentation
│   ├── ARCHITECTURE.md # High-level design and data flow diagrams
│   └── DEPLOYMENT.md   # Extensive step-by-step installation guide
├── Demenstration Video/    # [DEMO] Full system walkthrough video
├── KLE Monthly Connect PPT/# [REPORTS] Monthly progress and review presentations
├── Archicture Diagram.png  # [DOCS] High-level system architecture visualization
├── training_data/      # [DATA] Locally generated synthetic datasets (CSV/Parquet)
├── verify_setup.py     # Diagnostic tool to check environment & model integrity
├── run_app.bat         # One-click Windows launcher
├── requirements.txt    # List of required Python libraries
└── pyproject.toml      # Project metadata and configuration
```

## Quick Start

### 1. Prerequisites (Crucial)

This system uses **Git LFS** (Large File Storage) for model weights.

```bash
# Install Git LFS (if not already installed)
git lfs install

# Pull the model files after cloning
git lfs pull
```

### 2. Install Dependencies

```bash
# Using uv (recommended)
uv sync

# Or using pip
pip install -r requirements.txt
```

### 3. Quick Start

**Step 1: Verify environment**
```bash
python verify_setup.py
```

**Step 2: Run the Web Server**
- **Option A: One-click (Windows)**: Double-click `run_app.bat`
- **Option B: Manual**: `python -m src.main`

Open `http://127.0.0.1:8000` in your browser.

### 4. Test via CLI

```bash
python tests/test_industry.py
```

## Supported PII Types (29+)

| PII Category | Description / Examples |
| :--- | :--- |
| **NAME** | Full name, First name, Last name |
| **EMAIL** | personal@gmail.com, official@corp.com |
| **PHONE_NUMBER** | +91-9876543210, (555) 123-4567 |
| **DATE_OF_BIRTH** | 15/01/1990, 1990-01-15 |
| **AADHAAR_NUMBER** | 1234 5678 9012 (Indian UID) |
| **PAN_NUMBER** | ABCDE1234F (Permanent Account Number) |
| **VOTER_ID** | EPIC/Election ID numbers |
| **PASSPORT_NUMBER** | Global Passport identifiers |
| **DRIVERS_LICENSE** | State-issued driving licenses |
| **ADDRESS** | Residential and Shipping addresses |
| **PIN_CODE** | Postal codes, Zip codes |
| **BANK_ACCOUNT** | Savings/Current account numbers |
| **IFSC_CODE** | Bank branch identifiers |
| **CREDIT_CARD** | Visa, Mastercard, Amex numbers |
| **CVV** | 3-4 digit card security codes |
| **UPI_ID** | user@upi, name@okaxis |
| **SSN** | US Social Security Numbers |
| **MEDICAL_CONDITION** | Diagnoses (e.g., Diabetes, Asthma) |
| **MRN** | Medical Record Numbers |
| **BLOOD_GROUP** | A+, O-, AB+, etc. |
| **GENDER / AGE** | Demographic indicators |
| **NATIONALITY** | Citizenship info |
| **IP_ADDRESS** | IPv4 and IPv6 addresses |
| **GPS_COORDINATES** | Latitude and Longitude pairs |
| **VEHICLE_REG** | License plate numbers (MH-01-AX...) |
| **SALARY / INCOME** | Financial compensation details |
| **USERNAME** | Account login handles |
| **PASSWORD** | Plaintext or hashed credentials |
| **NON_PII** | Optimized to ignore public/safe data |

## Troubleshooting

- **"Model not found"**: Ensure you have installed Git LFS and run `git lfs pull`. Check if `models/model_v2/model.bin` exists and is ~400MB.
- **Port already in use**: If port 8000 is taken, the app will fail to start. You can change the port in `src/main.py`.
- **Memory Error**: BERT models require ~8GB RAM. Close other heavy applications if you encounter crashes.

## License

MIT
