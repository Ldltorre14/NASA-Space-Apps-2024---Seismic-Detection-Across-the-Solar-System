import torch.optim as optim
import pandas as pd
import numpy as np
import torch
import torch.nn as nn
from models.RNN_Model import RNNModel



def training(input_size, hidden_size, num_layers, lr, epochs, num_batches, inputs, labels):
    model = RNNModel(input_size=input_size, hidden_size=hidden_size, num_layers=num_layers)
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=lr)
    
    for epoch in range(epochs):
        for i in range(num_batches):
            batch_inputs = inputs[i]
            batch_labels = labels[i]

            outputs = model(batch_inputs)
            loss = criterion(outputs, batch_labels)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        
        print(f'Epoch [{epoch + 1}/{epochs}], Loss: {loss.item():.4f}')  


