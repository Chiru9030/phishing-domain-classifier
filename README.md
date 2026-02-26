# Phishing Domain Classifier (Deep Learning)

A PyTorch-based neural network architecture designed to detect zero-day phishing domains.

## Overview
Traditional phishing detection relies on blocklists which fail against newly registered domains. This project treats domain names as sequences of characters, utilizing an `Embedding` layer coupled with an `LSTM` (Long Short-Term Memory) Recurrent Neural Network.

The model analyzes the lexical composition of the Uniform Resource Locator (URL) to flag deceptive naming conventions mathematically (e.g., `sec-update-paypa1.com`).

## Setup
```bash
pip install -r requirements.txt
python classifier.py
```
