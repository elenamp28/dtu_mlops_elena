import torch
from torchvision.models import resnet152, ResNet152_Weights

model = resnet152(weights=ResNet152_Weights.DEFAULT)
scripted_model = torch.jit.script(model)