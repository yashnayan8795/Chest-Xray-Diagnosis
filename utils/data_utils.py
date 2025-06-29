import os
import shutil
from glob import glob
from sklearn.model_selection import train_test_split
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def split_data(raw_data_dir, split_data_dir, train_size=0.7, val_size=0.15, test_size=0.15):
    """
    Splits the raw data into train, validation, and test sets for each class.
    """
    if abs(train_size + val_size + test_size - 1.0) > 1e-8:
        raise ValueError("The sum of train, val, and test sizes must be 1.")

    if os.path.exists(split_data_dir):
        logging.info(f"Split data directory '{split_data_dir}' already exists. Deleting it.")
        shutil.rmtree(split_data_dir)

    classes = [d for d in os.listdir(raw_data_dir) if os.path.isdir(os.path.join(raw_data_dir, d))]

    for cls in classes:
        # Create destination directories
        for folder in ['train', 'val', 'test']:
            os.makedirs(os.path.join(split_data_dir, folder, cls), exist_ok=True)

        # Get all image paths
        img_paths = glob(os.path.join(raw_data_dir, cls, '*.jpeg'))
        if not img_paths:
            logging.warning(f"No images found for class '{cls}', skipping.")
            continue
        
        # Split data
        train_val_paths, test_paths = train_test_split(img_paths, test_size=test_size, random_state=42)
        relative_val_size = val_size / (train_size + val_size)
        train_paths, val_paths = train_test_split(train_val_paths, test_size=relative_val_size, random_state=42)

        # Copy files
        for src_path in train_paths:
            shutil.copy(src_path, os.path.join(split_data_dir, 'train', cls))
        for src_path in val_paths:
            shutil.copy(src_path, os.path.join(split_data_dir, 'val', cls))
        for src_path in test_paths:
            shutil.copy(src_path, os.path.join(split_data_dir, 'test', cls))

        logging.info(f"Split {len(img_paths)} images of class '{cls}' into {len(train_paths)} train, {len(val_paths)} val, and {len(test_paths)} test.")

if __name__ == '__main__':
    raw_data_path = 'data/raw'
    split_data_path = 'data/split'
    split_data(raw_data_path, split_data_path)
    logging.info("Data splitting complete.")
