# QuMail: Quantum-Safe Messaging System 🚀

QuMail is a secure communication platform inspired by **ISRO's SAQTI mission**. It uses **Quantum Key Distribution (QKD)** to generate unbreakable encryption keys that are immune to eavesdropping and future quantum computer attacks.

## 🛡️ How it Works
QuMail operates on the principle of **Quantum Mechanics**. Unlike standard email which uses math-based encryption, QuMail uses the **BB84 Protocol** to share a secret key via simulated polarized photons.



### 1. Quantum Handshake (The Start)
When you launch `main.py`, the system initiates a handshake. Alice (the sender) and Bob (the receiver) exchange qubits using **IBM Qiskit**. They only keep the bits where their measurement bases match.

**Expected Output:**
> *Quantum Key Established: 64 bits*
> *Link Secure. QBER: 0.0%*

### 2. XOR Encryption (The Lock)
Once the key is shared, QuMail uses a **One-Time Pad (OTP)** cipher. This transforms your plain text into a binary ciphertext that is mathematically impossible to crack without the quantum key.



### 3. Decryption (The Recovery)
On the receiving end, the same Quantum Key is applied to the ciphertext to perfectly reconstruct the original message.

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- `pip install qiskit qiskit-aer numpy psutil`

### Installation
```bash
git clone [https://github.com/gytdrop/QuMail.git](https://github.com/gytdrop/QuMail.git)
cd QuMail
python main.py
