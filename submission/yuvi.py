from ecdsa import SigningKey, SECP256k1
import hashlib
import json

GITHUB_HANDLE = "yuvimittal"

message = f"SOB-2026-{GITHUB_HANDLE}".encode()

sk = SigningKey.generate(curve=SECP256k1)
vk = sk.verifying_key

msg_hash = hashlib.sha256(message).digest()

signature = sk.sign_digest(msg_hash)

public_key_hex = vk.to_string().hex()
signature_hex = signature.hex()

output = {
    "handle": GITHUB_HANDLE,
    "public_key": public_key_hex,
    "signature": signature_hex
}

with open(f"submission/{GITHUB_HANDLE}.json", "w") as f:
    json.dump(output, f, indent=2)

print("Public Key:", public_key_hex)
print("Signature:", signature_hex)
print("Saved submission file.")
