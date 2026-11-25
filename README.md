# Phishing Domain Classifier

A Deep Learning model utilizing PyTorch to detect malicious phishing domains based on character-level lexical analysis.

## 📖 Complete Brief
This project uses Natural Language Processing (NLP) techniques applied directly to URLs to prevent users from navigating to malicious sites. While traditional blockers use blacklists (which are easily bypassed by newly registered domains), this project uses a Long Short-Term Memory (LSTM) neural network. The model reads the raw characters of a domain name (e.g., `paypal-security-update.com`) and learns the structural and lexical patterns commonly used by attackers to spoof legitimate brands. This character-level modeling allows it to successfully classify zero-day phishing links on the fly without relying on external databases.

## ✨ Features
- **Deep Learning Architecture:** Employs an LSTM network built with PyTorch, ideal for sequential character data.
- **Zero-Day Detection:** Focuses on lexical properties rather than known blacklists, effectively catching newly minted malicious domains.
- **Self-Contained Training Script:** The provided script initializes the PyTorch model, generates a dummy dataset representing encoded URLs, and executes a full training loop over 5 epochs.

## 🛠 Prerequisites
- Python 3.x
- `torch` (PyTorch)

## 🚀 How to Run

1. **Navigate to the classifier directory:**
   ```bash
   cd ./phishing-domain-classifier/
   ```

2. **Install dependencies:**
   Make sure PyTorch is installed on your system.
   ```bash
   pip3 install -r requirements.txt
   ```

3. **Train the model:**
   ```bash
   python3 classifier.py
   ```

4. **Expected Output:**
   The script creates the neural network, generates a mock batch of character-encoded domains, and trains the model while logging the loss rate decreasing over each epoch:
   ```text
   [*] Initializing Deep Learning Phishing Classifier...
   [*] Training highly specialized NLP model on domain lexical features...
   Epoch 1/5 - Loss: 0.6953
   Epoch 2/5 - Loss: 0.6865
   ...
   Epoch 5/5 - Loss: 0.6698
   [+] Model ready for zero-day URL inference.
   ```
