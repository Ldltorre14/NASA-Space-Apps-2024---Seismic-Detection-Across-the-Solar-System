import numpy as np


def createSequences(data, sequence_length):
    sequences = []
    labels = []

    # Assuming the first column is datetime and the second column is the label
    datetime_col = data.iloc[:, 0]  # First column for timestamps
    label_col = data.iloc[:, 1]  # Second column for numeric labels
    
    numeric_data = data.iloc[:, 1:]  # Exclude the datetime column
    numeric_data = numeric_data.astype(float)

    for i in range(len(data) - sequence_length):
        seq = numeric_data.iloc[i:i + sequence_length].values  # Convert to NumPy array
        seq = np.array(seq, dtype=np.float32)
        
        label = label_col.iloc[i + sequence_length]  # Use numeric label instead of datetime
        
        sequences.append(seq)
        labels.append(label)
    
    return np.array(sequences), np.array(labels, dtype=np.float32)