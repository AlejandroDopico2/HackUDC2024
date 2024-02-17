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

    # Function to calculate the hash of a file
def calculate_file_hash(csv1,csv2):
    df1 = pd.Dataframe(csv1)
    df2 = pd.DataFrame(csv2)

    common = df1.index.isin(df2.index)
    


# Function to check if the CSV file already exists
def is_duplicate(input_file_path, existing_file_path):
    df1 = pd.read_csv(input_file_path)
    df2 = pd.read_csv(existing_file_path)

    common = len(df2[~df2.index.isin(df1.index)])

    print(common)

    return common == 0

def concatenate_csv(existing_file_path, new_file_path):
    existing_data = pd.read_csv(existing_file_path)
    new_data = pd.read_csv(new_file_path)
    
    concatenated_data = pd.concat([existing_data, new_data], ignore_index=True)
    
    concatenated_data.to_csv(existing_file_path, index=False)