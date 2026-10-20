# Python Cryptography & Blockchain Projects

A collection of Python projects exploring cryptographic hashing, blockchain fundamentals, digital signatures, encryption, Merkle trees, and Proof of Work mining.

These projects were created for learning and practicing Python programming, cryptography, and core blockchain concepts.

## 📌 Projects Included

### 1. SHA-256 Hash Generator
**File:** `hash.py`

- Uses Python's `hashlib` library.
- Demonstrates SHA-256 hashing.
- Accepts user input from the terminal.

### 2. Basic Blockchain Using Python
**File:** `Blockchain.py`

- Implements a basic block structure.
- Stores block data, current hash, and previous hash.
- Links blocks using SHA-256 hashes.
- Demonstrates the basic structure of a blockchain.

### 3. AES Encryption & Decryption
**File:** `encryption.py`

- Uses the Python `cryptography` library.
- Demonstrates AES encryption and decryption.
- Uses CBC mode and PKCS7 padding.
- Generates a random encryption key and initialization vector (IV).

### 4. Merkle Tree
**File:** `merkle_tree.py`

- Generates SHA-256 hashes for transactions.
- Combines hashes in pairs to build a Merkle tree.
- Calculates the final Merkle root.
- Demonstrates how transaction data can be represented using hashes.

### 5. RSA Digital Signature
**File:** `Digital_Signature_Using_RSA.py`

- Generates an RSA public-private key pair.
- Signs a message using the private key.
- Verifies the signature using the public key.
- Uses SHA-256 and RSA-PSS padding.

### 6. RSA Digital Signature with Functions
**File:** `digital_signature.py`

- Implements reusable functions for key generation, signing, and verification.
- Uses RSA with a 2048-bit key.
- Uses SHA-256 and PSS padding.
- Handles invalid signatures.

### 7. Elliptic Curve Cryptography (ECC)
**File:** `Elliptic_Curve_Cryptography_ECC.py`

- Generates an elliptic curve key pair using SECP256R1.
- Creates digital signatures using ECDSA.
- Uses SHA-256 for signing and verification.
- Demonstrates public-key cryptography using elliptic curves.

### 8. Blockchain Mining with Proof of Work
**File:** `Mining.py`

- Implements a basic block structure.
- Calculates SHA-256 block hashes.
- Demonstrates nonce-based mining.
- Uses a configurable mining difficulty.
- Links newly mined blocks to the previous block.

## 🛠️ Technologies Used

- **Language:** Python
- **Cryptography:** RSA, ECC, ECDSA, AES
- **Hashing:** SHA-256
- **Concepts:** Blockchain, Merkle Trees, Digital Signatures, Proof of Work
- **Libraries:** `hashlib`, `time`, `os`, `cryptography`

## ⚙️ Installation

### 1. Install Python

Install Python 3 from the official website:

https://www.python.org/downloads/

### 2. Clone the Repository

Replace `YOUR-USERNAME` with your GitHub username.

```bash
git clone https://github.com/YOUR-USERNAME/Python_Cryptography_Blockchain_Projects.git
```

### 3. Open the Project Folder

```bash
cd Python_Cryptography_Blockchain_Projects
```

### 4. Install Dependencies

The hashing, basic blockchain, Merkle tree, and mining examples use Python's built-in libraries.

Install the `cryptography` package for the AES, RSA, and ECC projects:

```bash
python -m pip install cryptography
```

## ▶️ How to Run

Run any project from the terminal using Python.

For example:

```bash
python main.py
```

Run the other scripts by replacing `main.py` with the relevant filename.

## 📚 Learning Objectives

Through these projects, I explored:

- How SHA-256 hashing works in Python.
- How blocks can be linked through hashes.
- How a basic Proof of Work mining loop works.
- How Merkle roots are calculated.
- How symmetric encryption and decryption work.
- How RSA and ECC digital signatures are generated and verified.
- How Python can be used to understand fundamental blockchain concepts.

## ⚠️ Disclaimer

These projects are educational demonstrations and are not production-ready blockchain or security systems.

Some files were reconstructed from screenshots and video recordings of earlier projects. They may not be byte-for-byte copies of the original deleted source files.

- The SHA-256 example in `hash.py` preserves the original screenshot's `.hexdigest` usage; add parentheses to call the method and obtain the actual hash.
- The AES-CBC example is a learning demonstration. It does not package the IV with the ciphertext and should not be used as-is for real-world data protection.
- The basic blockchain and mining examples do not implement a complete, secure, distributed blockchain network.

Always review and test code before using it in real applications.

## 👨‍💻 Author

**Rehan Ansari**

Computer Engineering Student | Python | Blockchain & Cryptography

GitHub: https://github.com/Rehan-Code764

---

If you find these projects useful for learning, feel free to explore the code and experiment with the implementations.
