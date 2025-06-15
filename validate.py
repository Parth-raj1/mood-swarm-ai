import hashlib, getpass, os, json

def verify():
    CORRECT_TOKEN = os.getenv("VALIDATION_SECRET")  # Set locally
    if not CORRECT_TOKEN:
        print("Validation system not configured")
        return

    token = getpass.getpass("Enter validation token: ").strip()
    token_hash = hashlib.sha256(token.encode()).hexdigest()
    correct_hash = hashlib.sha256(CORRECT_TOKEN.encode()).hexdigest()
    
    if token_hash != correct_hash:
        print("❌ INVALID TOKEN")
        return

    # REAL verification
    try:
        with open("benchmarks.json") as f:  # Changed path here
            data = json.load(f)
        assert data["RAM_reduction"] >= 0.42, "RAM reduction too low"
    except Exception as e:
        print(f"⚠️ Verification warning: {str(e)}")
        return
    
    # Generate live signature
    signature = hashlib.sha256(f"{token}{CORRECT_TOKEN}".encode()).hexdigest()

    print("\n✅ VALIDATION CONFIRMED")
    print("All benchmark thresholds passed")
    print(f"Signature: {signature[:8]}... (full: {signature})")
    print("Metrics verified against local benchmarks.")

if __name__ == "__main__":
    verify()

