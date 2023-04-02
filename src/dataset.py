import os
from PIL import Image
import pandas as pd
from torch.utils.data import Dataset
from typing import List

class CustomImageDataset(Dataset):
    """ This is the classic torch (map-style) dataset for loading images and corresponding labels from a CSV file.
        This implementation is preferred over other dataset types as we can specify the labels clearly 
        with no need to shuffle the folders. 
    """    
    def __init__(self, annotations_file: pd.DataFrame, transform:List =None):
        """ Initializes a CustomImageDataset instance.
        Args:
            annotations_file (pd.DataFrame): A pandas DataFrame containing the image file paths and corresponding labels.
            transform (List, optional): A list of PyTorch transforms to apply to the images. Defaults to None.
        """        
        self.data = pd.read_csv(os.path.join(os.getcwd(), annotations_file))
        self.img_path = self.data["file_name"].apply(lambda x: os.path.join(os.getcwd(), x))
        self.transform = transform

    def __len__(self)->int:
        """ Returns the number of images in the dataset.
        Returns:
            int: The number of images in the dataset.
        """        
        return len(self.data)

    def __getitem__(self, idx: int)->tuple:
        """ Loads and returns an image and its corresponding label.
        Args:
            idx (int): The index of the image to load.
        Returns:
            tuple: A tuple containing the loaded image and its corresponding label.
        """        
        image = Image.open(os.path.abspath(self.img_path[idx]))
        label = self.data["label"].iloc[idx]
        if self.transform:
            sample = self.transform(image)
        return sample, label

