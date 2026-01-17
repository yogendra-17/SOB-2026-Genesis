import json
import os
import sys
import hashlib
from ecdsa import VerifyingKey, SECP256k1, BadSignatureError

def verify_student_submission(file_path):
    print(f"Verifying {file_path}...")
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print(f"FAILED: {file_path} is not valid JSON.")
        return False
    except Exception as e:
        print(f"FAILED: Could not read {file_path}: {e}")
        return False
    
    # Check for required fields
    required_fields = ['handle', 'public_key', 'signature']
    for field in required_fields:
        if field not in data:
            print(f"FAILED: Missing field '{field}' in {file_path}")
            return False

    # 1. Verify Public Key is a valid point on secp256k1
    try:
        pubkey_hex = data['public_key']
        # ecdsa library expects bytes
        vk = VerifyingKey.from_string(bytes.fromhex(pubkey_hex), curve=SECP256k1)
    except Exception as e:
        print(f"FAILED: Invalid Public Key in {file_path}: {e}")
        return False

    # 2. Verify Digital Signature
    # Reconstruct the challenge string
    handle = data['handle']
    challenge_str = f"SOB-2026-{handle}"
    challenge_bytes = challenge_str.encode('utf-8')
    
    try:
        signature_hex = data['signature']
        signature_bytes = bytes.fromhex(signature_hex)
        
        # Verify the signature
        if vk.verify(signature_bytes, challenge_bytes, hashfunc=hashlib.sha256):
            print(f"SUCCESS: Signature valid for {handle}")
        else:
            print(f"FAILED: Signature invalid for {handle}")
            return False
            
    except KeyError:
        print(f"FAILED: Missing 'signature' field in {file_path}")
        return False
    except BadSignatureError:
        print(f"FAILED: Bad Signature for {handle} in {file_path}")
        return False
    except Exception as e:
        print(f"FAILED: Error verifying signature in {file_path}: {e}")
        return False

    print(f"SUCCESS: {file_path} passes all checks!")
    return True

if __name__ == "__main__":
    participants_dir = "participants"
    if not os.path.exists(participants_dir):
        print(f"Error: Directory '{participants_dir}' not found.")
        sys.exit(1)

    files = [f for f in os.listdir(participants_dir) if f.endswith('.json')]
    if not files:
        print("No participant JSON files found.")
        # We might want to fail if no files, or pass if it's just a setup run. 
        # For now, let's pass but warn.
        sys.exit(0)

    failed_files = []
    for filename in files:
        file_path = os.path.join(participants_dir, filename)
        if not verify_student_submission(file_path):
            failed_files.append(filename)

    if failed_files:
        print(f"\nVerification failed for {len(failed_files)} files: {', '.join(failed_files)}")
        sys.exit(1)
    
    print("\nAll submissions verified successfully!")
    sys.exit(0)
