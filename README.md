# QuMail: Quantum Key Distribution (QKD) Secure Messaging

QuMail is a specialized secure communication system inspired by **ISRO's SAQTI mission**. It leverages the laws of quantum mechanics to ensure that encryption keys are shared with absolute security. If an eavesdropper attempts to intercept the key, the quantum state collapses, and the system automatically aborts the transmission.



##  Key Features
- **Quantum Handshake:** Uses IBM's **Qiskit** to simulate the BB84 protocol for key generation.
- **Unbreakable Encryption:** Implements **One-Time Pad (OTP)** via XOR cipher, mathematically secure against quantum computer attacks.
- **Eavesdropper Detection:** Real-time calculation of **Quantum Bit Error Rate (QBER)** to detect hackers (Eve).
- **Cross-Platform Support:** Adaptive terminal handling for Windows (CMD/PowerShell), Linux, and macOS.
- **Auto-Bootstrapper:** Automatically detects and installs missing dependencies (Qiskit, Numpy) on launch.

## 🛠️ Project Structure
```text
QuMail/
├── main.py               # Orchestrator & UI (The Control Center)
├── quantum_engine.py     # Qiskit-based BB84 Simulation
├── encryption.py         # OTP XOR Cipher Logic
├── sync_timing.py        # NavIC-inspired timestamping
└── README.md             # Documentation
