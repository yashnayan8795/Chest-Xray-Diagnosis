# This is a placeholder for Exploratory Data Analysis 

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import numpy as np

# Define paths
split_data_dir = 'data/split'
train_dir = os.path.join(split_data_dir, 'train')
val_dir = os.path.join(split_data_dir, 'val')
test_dir = os.path.join(split_data_dir, 'test')

# Count images in each set
def count_images(directory):
    counts = {}
    for cls in os.listdir(directory):
        cls_dir = os.path.join(directory, cls)
        if os.path.isdir(cls_dir):
            counts[cls] = len(os.listdir(cls_dir))
    return counts

train_counts = count_images(train_dir)
val_counts = count_images(val_dir)
test_counts = count_images(test_dir)

# Create a DataFrame for plotting
data = {
    'Set': ['Train']*len(train_counts) + ['Validation']*len(val_counts) + ['Test']*len(test_counts),
    'Class': list(train_counts.keys()) + list(val_counts.keys()) + list(test_counts.keys()),
    'Count': list(train_counts.values()) + list(val_counts.values()) + list(test_counts.values())
}
df = pd.DataFrame(data)

# Plot class distribution
plt.figure(figsize=(10, 6))
sns.barplot(x='Set', y='Count', hue='Class', data=df)
plt.title('Class Distribution in Train, Validation, and Test Sets')
plt.show()

# Display sample images
def display_samples(directory, num_samples=3):
    plt.figure(figsize=(12, 8))
    for i, cls in enumerate(os.listdir(directory)):
        cls_dir = os.path.join(directory, cls)
        if os.path.isdir(cls_dir):
            img_names = os.listdir(cls_dir)[:num_samples]
            for j, img_name in enumerate(img_names):
                img_path = os.path.join(cls_dir, img_name)
                img = Image.open(img_path)
                plt.subplot(len(os.listdir(directory)), num_samples, i * num_samples + j + 1)
                plt.imshow(img, cmap='gray')
                plt.title(f'{cls}')
                plt.axis('off')
    plt.tight_layout()
    plt.show()

print("Displaying sample images from the training set:")
display_samples(train_dir) 