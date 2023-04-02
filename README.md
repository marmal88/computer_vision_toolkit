# CV Toolkit

# Introduction

This is a series of notebooks to better understand CV tasks using the skin_cancer dataset.
The intention is to have a toolkit to refer to for future CV projects.

## 1. Computer Vision Tasks (torch)
1. Basic Exploratory Data Analysis
2. Transfer learning 
3. Object similarity
4. Unsupervised learning T-SNE

## 2. Working with External tools
1. Uploading to Hugging Face

## 3. Implementations from scratch (Numpy)
1. 

---
# Data

Data was obtained from kaggle and can be accessed [here](https://www.kaggle.com/datasets/kmader/skin-cancer-mnist-ham10000).

- HAM10000 ("Human Against Machine with 10000 training images") dataset.
- Consisting of 10015 dermatoscopic images
- Cases include a representative collection of all important diagnostic categories in the realm of pigmented lesions: 
  - Actinic keratoses and intraepithelial carcinoma / Bowen's disease (akiec)
  - basal cell carcinoma (bcc)
  - benign keratosis-like lesions (solar lentigines / seborrheic keratoses and lichen-planus like keratoses, bkl)
  - dermatofibroma (df)
  - melanoma (mel)
  - melanocytic nevi (nv) 
  - vascular lesions (angiomas, angiokeratomas, pyogenic granulomas and hemorrhage, vasc)

- More than 50% of lesions are confirmed through histopathology (histo), the ground truth for the rest of the cases is either follow-up examination (followup), expert consensus (consensus), or confirmation by in-vivo confocal microscopy (confocal). 
- The dataset includes lesions with multiple images, which can be tracked by the lesionid-column within the HAM10000_metadata file.
---