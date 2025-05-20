#!/bin/bash

# Create pretrained_model directory
mkdir -p pretrained_model

# Download pretrained models from Hugging Face
curl -L https://huggingface.co/ibrahimhamamci/HierarchicalDet/resolve/main/pretrained_model/model_final.pth -o pretrained_model/model_final.pth
curl -L https://huggingface.co/ibrahimhamamci/HierarchicalDet/resolve/main/pretrained_model/model_0004999.pth -o pretrained_model/model_0004999.pth 