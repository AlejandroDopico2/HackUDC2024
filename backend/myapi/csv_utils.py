import os
import hashlib
import pandas as pd

# Function to calculate the hash of a file
def calculate_file_hash(file_path):
    hasher = hashlib.sha256()
    
    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):
            hasher.update(chunk)

    return hasher.hexdigest()

# Function to check if the CSV file already exists
def is_duplicate(input_file_path, existing_file_path):
    input_file_hash = calculate_file_hash(input_file_path)
    existing_file_hash = calculate_file_hash(existing_file_path)
    
    return input_file_hash == existing_file_hash

def concatenate_csv(existing_file_path, new_file_path):
    existing_data = pd.read_csv(existing_file_path)
    new_data = pd.read_csv(new_file_path)
    
    concatenated_data = pd.concat([existing_data, new_data], ignore_index=True)
    
    concatenated_data.to_csv(existing_file_path, index=False)