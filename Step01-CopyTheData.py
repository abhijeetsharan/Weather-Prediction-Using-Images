import os
import random
import shutil

# Function to split data into training and validation sets
def split_data(SOURCE, TRAINING, VALIDATION, SPLIT_SIZE):
    files = []
    
    # Ensure directories exist
    if not os.path.exists(TRAINING):
        os.makedirs(TRAINING)
    if not os.path.exists(VALIDATION):
        os.makedirs(VALIDATION)

    # Collect valid files (non-empty files)
    for filename in os.listdir(SOURCE):
        file = os.path.join(SOURCE, filename)
        if os.path.getsize(file) > 0:
            files.append(filename)
        else:
            print(f"{filename} is an empty file")

    print(f"Total files: {len(files)}")

    # Split data into training and validation sets
    trainLength = int(len(files) * SPLIT_SIZE)
    suffleDataSet = random.sample(files, len(files))
    
    trainingSet = suffleDataSet[:trainLength]
    validSet = suffleDataSet[trainLength:]

    # Copy files to the respective directories
    for filename in trainingSet:
        shutil.copy(os.path.join(SOURCE, filename), os.path.join(TRAINING, filename))

    for filename in validSet:
        shutil.copy(os.path.join(SOURCE, filename), os.path.join(VALIDATION, filename))

# Define source, train, and validation folders
categories = ['cloudy', 'foggy', 'rainy', 'shine', 'sunrise']
base_dir = "C:/Users/devil/OneDrive/Desktop/PROJECTS/Weather Prediction using Images"
source_folder = os.path.join(base_dir, "original-dataset")
train_folder = os.path.join(base_dir, "dataset/Train")
valid_folder = os.path.join(base_dir, "dataset/Validate")

splitSize = 0.85

# Loop through each category and split the data
for category in categories:
    src = os.path.join(source_folder, category)
    train = os.path.join(train_folder, category)
    valid = os.path.join(valid_folder, category)
    split_data(src, train, valid, splitSize)
