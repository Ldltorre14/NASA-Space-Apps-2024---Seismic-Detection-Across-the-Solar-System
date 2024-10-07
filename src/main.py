import pandas as pd
import matplotlib.pyplot as plt
import constants.consts as cs
import utils.cleaning_utils
import utils.normalize
import utils.visualize
from utils.preprocessing import preprocessDataFrame
from models.sequental_training_data import createSequences
from models.training_script import training
import torch

# Parameters
sequence_length = 10
input_size = 2  # We are using 'time_rel' and 'velocity' as features
hidden_size = 32
num_layers = 1
lr = 0.001
epochs = 100
batch_size = 32

# Load the dataset
df = pd.read_csv(cs.LUNAR_TRAINING_DATA_DIRECTORY + "/xa.s12.00.mhz.1970-01-19HR00_evid00002.csv")

# Preprocess the dataframe
# Convert 'time_abs' to datetime and clean up missing/duplicate values
processed_df = preprocessDataFrame(df)

# Visualizations (before and after processing)
#utils.visualize.visualizeVelocityOverTime(df)
#utils.visualize.visualizeRollingCorrelationTimeVelocity(df)
#utils.visualize.visualizeVelocityOverTime(processed_df)
#utils.visualize.visualizeRollingCorrelationTimeVelocity(processed_df)

# Create sequences using 'time_rel' and 'velocity'
# This will generate sequences of length 'sequence_length' for training
sequences, labels = createSequences(processed_df[['time_rel', 'velocity']], sequence_length)

# Debugging: Print shape of sequences and labels
print("Shape of sequences:", sequences.shape)  # Expected: (num_samples, sequence_length, 2)
print("Shape of labels:", labels.shape)        # Expected: (num_samples,)

# Convert the sequences and labels into torch tensors
inputs = torch.tensor(sequences, dtype=torch.float32)
labels = torch.tensor(labels, dtype=torch.float32).view(-1, 1)

# Get the number of samples and ensure the batch size is valid
num_samples = inputs.shape[0]
num_batches = num_samples // batch_size

# Trim inputs and labels if necessary to make them divisible by the batch size
inputs = inputs[:num_batches * batch_size]
labels = labels[:num_batches * batch_size]

# Reshape inputs into the desired shape for batching
# New shape: [num_batches, batch_size, sequence_length, input_size]
inputs = inputs.view(num_batches, batch_size, sequence_length, input_size)

# Reshape labels accordingly
# New shape: [num_batches, batch_size, 1]
labels = labels.view(num_batches, batch_size, 1)

# Debugging: Print final shapes of inputs and labels
print("Final shape of inputs:", inputs.shape)  # Should be: [num_batches, batch_size, sequence_length, input_size]
print("Final shape of labels:", labels.shape)  # Should be: [num_batches, batch_size, 1]

# Start the training
training(input_size=input_size, hidden_size=hidden_size, num_layers=num_layers,
         lr=lr, epochs=epochs, num_batches=num_batches, inputs=inputs, labels=labels)