from huggingface_hub import hf_hub_download
import os

# Create pretrained_model directory
os.makedirs("pretrained_model", exist_ok=True)

# Download pretrained models
model_files = [
    "pretrained_model/model_final.pth",
    "pretrained_model/model_0004999.pth"
]

for model_file in model_files:
    print(f"Downloading {model_file}...")
    hf_hub_download(
        repo_id="ibrahimhamamci/HierarchicalDet",
        filename=model_file,
        local_dir=".",
        local_dir_use_symlinks=False
    ) 