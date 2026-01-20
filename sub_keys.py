import hashlib
import secrets
import json
from ecdsa import SigningKey, SECP256k1

private_key_bytes = secrets.token_bytes(32)
pvt_key = SigningKey.from_string(private_key_bytes, curve=SECP256k1)

pub_key = pvt_key.verifying_key


GITHUB_HANDLE = "SakshamSinghal20"
message = f"SOB-2026-{GITHUB_HANDLE}".encode()

signature = pvt_key.sign(
    message,
    hashfunc=hashlib.sha256,
)


public_key_hex = pub_key.to_string("compressed").hex()

signature_hex = signature.hex()
output = {
    "handle": GITHUB_HANDLE,
    "public_key": public_key_hex,
    "signature": signature_hex
}


with open(f"submission/{GITHUB_HANDLE}.json", "w") as f:
    json.dump(output, f, indent=2)
print("Submission file created successfully.")
