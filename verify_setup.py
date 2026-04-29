import os
import sys
import subprocess

def check_dependencies():
    print("[1/3] Checking dependencies...")
    try:
        import torch
        import transformers
        import fastapi
        import pandas
        print("  - Core libraries found.")
    except ImportError as e:
        print(f"  - [ERR] Missing library: {e}")
        return False
    return True

def check_models():
    print("[2/3] Checking model files...")
    model_path = os.path.join("models", "model_v2", "model.bin")
    if os.path.exists(model_path):
        size = os.path.getsize(model_path) / (1024 * 1024)
        print(f"  - model_v2 found ({size:.1f} MB)")
        return True
    else:
        print("  - [ERR] models/model_v2/model.bin not found!")
        return False

def check_gpu():
    print("[3/3] Checking Hardware Acceleration...")
    try:
        import torch
        if torch.cuda.is_available():
            print(f"  - GPU detected: {torch.cuda.get_device_name(0)}")
        else:
            print("  - No GPU found (falling back to CPU)")
    except:
        pass
    return True

if __name__ == "__main__":
    print("="*40)
    print("PII Detection System - Setup Verification")
    print("="*40)
    
    deps = check_dependencies()
    models = check_models()
    gpu = check_gpu()
    
    print("="*40)
    if deps and models:
        print("SUCCESS: System is ready to run!")
        print("Start with: python -m src.main")
    else:
        print("FAILURE: Please fix the errors above before running.")
    print("="*40)
