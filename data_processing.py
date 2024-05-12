import pandas as pd
import numpy as np
import re


# Apply the function to each row in the 'High_dimensional_embeddings' column
def load_data(file_path):
    data = pd.read_csv(file_path)
    data['High_dimensional_embeddings'] = data['High_dimensional_embeddings'].apply(convert_embedding)
    return data

# Convert from stringified list to actual numpy array
def convert_embedding(row):
  # If the embedding is stored as a string of numbers, convert it directly
    if isinstance(row, str):
        # Clean the string to ensure it's in a simple list format or directly convertible
        clean_row = re.sub(r'\s+', '', row.strip('[]'))
        # Convert the cleaned string to a numpy array
        return np.fromstring(clean_row, sep=',')
    return row