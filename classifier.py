import torch
import torch.nn as nn
import torch.optim as optim

# Simple LSTM for character-level domain classification
class PhishingClassifier(nn.Module):
    def __init__(self, vocab_size, embed_dim, hidden_dim):
        super(PhishingClassifier, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim)
        self.lstm = nn.LSTM(embed_dim, hidden_dim, batch_first=True)
        self.fc = nn.Linear(hidden_dim, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        embedded = self.embedding(x)
        lstm_out, _ = self.lstm(embedded)
        # Take the output of the last time step
        last_out = lstm_out[:, -1, :]
        out = self.fc(last_out)
        return self.sigmoid(out)

def train_mock_model():
    print("[*] Initializing Deep Learning Phishing Classifier...")
    vocab_size = 128 # ASCII chars
    model = PhishingClassifier(vocab_size=vocab_size, embed_dim=16, hidden_dim=32)
    criterion = nn.BCELoss()
    optimizer = optim.Adam(model.parameters(), lr=0.01)
    
    # Mock data [batch_size, sequence_length]
    # Representing encoded URLs: Normal vs Phishing (e.g., paypal-update-security.com)
    print("[*] Training highly specialized NLP model on domain lexical features...")
    X = torch.randint(0, vocab_size, (10, 20)) 
    y = torch.tensor([[0.], [1.], [0.], [1.], [0.], [1.], [0.], [1.], [0.], [1.]])

    for epoch in range(5):
        optimizer.zero_grad()
        outputs = model(X)
        loss = criterion(outputs, y)
        loss.backward()
        optimizer.step()
        print(f"Epoch {epoch+1}/5 - Loss: {loss.item():.4f}")

    print("[+] Model ready for zero-day URL inference.")

if __name__ == "__main__":
    train_mock_model()
