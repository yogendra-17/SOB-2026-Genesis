#!/usr/bin/env python3
"""
SOB-2026-Genesis Challenge Solution
Generates Secp256k1 keypair and signs challenge message
"""

import hashlib
import json
import os
from ecdsa import SigningKey, SECP256k1


def main():
    # Configuration
    github_handle = "Sumit-ai-dev"
    
    # Generate Secp256k1 keypair
    private_key = SigningKey.generate(curve=SECP256k1)
    public_key = private_key.get_verifying_key()
    
    # Create and sign the challenge message
    message = f"SOB-2026-{github_handle}"
    signature = private_key.sign(
        message.encode('utf-8'),
        hashfunc=hashlib.sha256
    )
    
    # Convert to hex format
    public_key_hex = public_key.to_string("compressed").hex()
    signature_hex = signature.hex()
    
    # Prepare submission data
    submission = {
        "handle": github_handle,
        "public_key": public_key_hex,
        "signature": signature_hex
    }
    
    # Save to JSON file
    output_dir = "submission"
    os.makedirs(output_dir, exist_ok=True)
    
    output_path = os.path.join(output_dir, f"{github_handle}.json")
    with open(output_path, 'w') as f:
        json.dump(submission, f, indent=2)
    
    print(f"✓ Submission created: {output_path}")
    print(f"✓ Handle: {github_handle}")
    print(f"✓ Public Key: {public_key_hex[:32]}...")
    print(f"✓ Signature: {signature_hex[:32]}...")


if __name__ == "__main__":
    main()
