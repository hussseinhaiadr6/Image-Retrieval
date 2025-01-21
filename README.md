# Image Similarity Retrieval System

This project implements an **image similarity retrieval system** using **DinoV2** for feature extraction and an embedding model for similarity computation. The system takes an input query image, processes it through a pre-trained model, and retrieves the most similar image from a specified folder based on cosine similarity.

## Features
- **Efficient Feature Extraction**: Utilizes DinoV2 for generating high-quality image embeddings.
- **Similarity Search**: Computes similarity between the query image and images in a specified directory using embedding models.
- **Folder-based Retrieval**: The system supports batch image comparison by scanning an entire folder.
- **Customizable Architecture**: Easily replace the embedding model or similarity metric.

## Workflow
1. **Image Input**: Place the query image in the designated folder.
2. **Embedding Generation**: Extract features from images using DinoV2.
3. **Similarity Computation**: Calculate the similarity between the query image and images in the folder.
4. **Image Retrieval**: Return the most similar image along with its similarity score.

## Requirements
To run this project, make sure you have the following dependencies installed:
- `Python 3.8+`
- `torch`
- `torchvision`
- `timm` (for DinoV2 pre-trained model)
- `numpy`
- `Pillow`
- `scikit-learn`

Install dependencies using:
```bash
pip install -r requirements.txt
```

## File Structure
- Pipeline.py: Main script to execute the image similarity retrieval process.
- Loader.py: Helper functions to load images and preprocess them.
- image_similarity_my_implementation.ipynb: Jupyter notebook for development and visualization.
- requirements.txt: List of required Python packages.
- Excel_Image_Extractor.py and Excel_image_writer.py: Utility scripts for handling image data stored in Excel files.
- Gamme ESSENTIELLE BUT - Electros.xlsx and Gamme ESSENTIELLE - Sanitaires.xlsx: Sample Excel files with associated image data.
## How to Run
Clone the repository:

```bash
git clone https://github.com/hussseinhaiadr6/image_similarity_project.git
cd image_similarity_project
```
Add your dataset images to a folder (e.g., images/).
Specify the path to your query image and dataset folder in Pipeline.py.
Run the script:
```bash 
python Pipeline.py
```
The system will output the most similar image along with its similarity score.

##Results
The retrieved image is displayed with the similarity score in the console or notebook.
For further analysis, intermediate results (e.g., embeddings) can be visualized using the notebook.

## Applications
Content-based Image Retrieval: Useful for finding similar images in large datasets.
Duplicate Image Detection: Identify duplicates in datasets.
Visual Search: Integrate with web applications for visual search functionalities.
## License
This project is open-source and available under the MIT License.
