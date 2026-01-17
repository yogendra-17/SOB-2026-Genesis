# SOB-2026-Genesis

## The Assignment: "The Proof of Identity PR"

Welcome to the School of Bitcoin 2026 Genesis assignment!

### Objective
Prove that you have successfully generated a keypair and understand the Git workflow.

### Instructions

1.  **Fork & Clone**: Fork this `SOB-2026-Genesis` repository and clone it to your local machine.

2.  **Generate Keys**: Write a script in **Python or TypeScript** to:
    *   Generate a random 256-bit Private Key.
    *   Derive the Secp256k1 Public Key.
    *   **Sign** the message: `"SOB-2026-[GitHub-Handle]"` (UTF-8 encoded).

3.  **Submit**: Create a file `participants/[your-handle].json` with the following content:

    ```json
    {
      "handle": "your-github-username",
      "public_key": "the_hex_of_your_pubkey",
      "signature": "the_hex_of_your_signature"
    }
    ```

    *   **handle**: Your exact GitHub username.
    *   **public_key**: The hexadecimal representation of your public key.
    *   **signature**: The hexadecimal representation of your DER-encoded signature (or simplified concatenation if using a library that supports it, but standard DER is safest for cross-language).

4.  **The PR**: Commit your file and submit a Pull Request to this repository.

### Verification
A "Gatekeeper" script will automatically run on your PR. It checks:
*   If your Public Key is valid.
*   If your **Signature** successfully verifies the message `"SOB-2026-[handle]"` against your Public Key.

Good luck!
