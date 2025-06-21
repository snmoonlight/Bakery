import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
from collections import Counter


# --- Настройки ---
item_sequence = [6, 1, 7, 3, 6, 7, 8, 13, 1, 6, 3, 6, 7, 6, 7, 2, 1, 13, 2, 8, 6, 7]
unique_items = list(set(item_sequence))
item_to_idx = {item: idx for idx, item in enumerate(unique_items)}
idx_to_item = {idx: item for item, idx in item_to_idx.items()}

# --- Гиперпараметры ---
input_size = len(unique_items)
hidden_size = 32
num_layers = 3
output_size = len(unique_items)
sequence_length = len(item_sequence)

# --- Подготовка входных данных ---
def encode_sequence(seq):
    indices = [item_to_idx[i] for i in seq]
    one_hot = F.one_hot(torch.tensor(indices), num_classes=input_size).float()
    return one_hot.unsqueeze(0)  # Добавим batch размерность

x = encode_sequence(item_sequence)

# --- RNN-модель ---
class RecommenderRNN(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, output_size):
        super(RecommenderRNN, self).__init__()
        self.rnn = nn.RNN(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        out, _ = self.rnn(x)
        last_output = out[:, -1, :]  # Только последний таймстеп
        prediction = self.fc(last_output)
        return prediction


model = RecommenderRNN(input_size, hidden_size, num_layers, output_size)


# --- Прогон без обучения ---
def give_rec():
    model.eval()
    with torch.no_grad():
        output = model(x)
        probs = torch.softmax(output, dim=1).squeeze()
        top2 = torch.topk(probs, 2).indices.tolist()
        recommendations = [idx_to_item[i] for i in top2]
        #print("Рекомендуемые товары:", recommendations)
        return recommendations
