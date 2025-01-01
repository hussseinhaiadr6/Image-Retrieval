from datasets import load_dataset
from PIL import Image
import os
import numpy as np
import torchvision.transforms as T
from transformers import AutoImageProcessor, Dinov2Model
import torch
import json


loaded_array = np.load('./Dataset.npy')

loaded_list = []
with open('./my_list.txt', 'r') as file:
    for line in file:
        # Convert each line to the appropriate data type (e.g., integer, string)
        # Assuming the list originally had integers and strings only
        line = line.strip()
        if line.isdigit():
            loaded_list.append(int(line))
        else:
            loaded_list.append(line)


extractor = AutoImageProcessor.from_pretrained("facebook/dinov2-base")
model = Dinov2Model.from_pretrained("facebook/dinov2-base")
hidden_dim = model.config.hidden_size

transformation_chain = T.Compose(
    [
        # We first resize the input image to 256x256 and then we take center crop.
        T.Resize(int((256 / 224) * extractor.size["shortest_edge"])),
        T.CenterCrop(extractor.size["shortest_edge"]),
        T.ToTensor(),
        T.Normalize(mean=extractor.image_mean, std=extractor.image_std),
    ])
all_candidate_embeddings = torch.from_numpy(loaded_array)
def compute_scores(emb_one, emb_two):
    """Computes cosine similarity between two vectors."""

    scores = torch.nn.functional.cosine_similarity(emb_one, emb_two)
    return scores.numpy().tolist()
def fetch_similar(image, top_k=3):
    """Fetches the `top_k` similar images with `image` as the query."""
    # Prepare the input query image for embedding computation.
    image_transformed = transformation_chain(image).unsqueeze(0)


    new_batch = {"pixel_values": image_transformed.to(device)}

    # Comute the embedding.
    with torch.no_grad():
        query_embeddings = model(**new_batch).last_hidden_state.cpu()
        query_embeddings = query_embeddings.mean(dim=1)
        #print((query_embeddings.shape))
    # Compute similarity scores with all the candidate images at one go.
    # We also create a mapping between the candidate image identifiers
    # and their similarity scores with the query image.
    sim_scores = compute_scores(all_candidate_embeddings, query_embeddings)
    similarity_mapping = dict(zip(loaded_list, sim_scores))

    # Sort the mapping dictionary and return `top_k` candidates.
    similarity_mapping_sorted = dict(
        sorted(similarity_mapping.items(), key=lambda x: x[1], reverse=True)
    )
    id_entries = list(similarity_mapping_sorted.keys())[:top_k]

    ids = list(map(lambda x: int(x.split("_")[0]), id_entries))

    labels = list(map(lambda x: str(x), id_entries))
    return ids, labels

device = "cpu"

def get_similar_images(Dir_path):
    image_dict = {}
    for filename in os.listdir(Dir_path):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):  # Check for valid image extensions
            image_path = os.path.join(Dir_path, filename)
            test_sample=Image.open(image_path).convert('RGB')
            sim_ids, sim_labels = fetch_similar(test_sample)
            image_dict[filename] = sim_labels  # Store the result in the dictionary

    # Print the resulting dictionary

    output_file = f'{Dir_path.split("/")[-1]}.txt'

    # Write the dictionary to a text file

    with open(output_file, 'w') as f:
        json.dump(image_dict, f)

    # Load the dictionary back from the text file
    with open(output_file, 'r') as f:
        loaded_image_dict = json.load(f)




