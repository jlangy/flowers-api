import json
import numpy as np
import torch
from torchvision import transforms, datasets, models
from network import Network
import PIL
from PIL import Image
from validate import validation
from torch import nn, optim
from network import make_network

print('hi')

data_transforms = transforms.Compose([transforms.Resize(256), transforms.CenterCrop(224), transforms.ToTensor(), transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])])   
#Import pretrained model
checkpoint = torch.load('checkpoint.pth', map_location=lambda storage, loc: storage)



with open('cat_to_name.json', 'r') as f:
    cat_to_name = json.load(f)

model = make_network(checkpoint['arch'], checkpoint['hidden_units'])
model.load_state_dict(checkpoint['model_state_dict'])
class_to_idx = checkpoint['class_to_idx']

print('hi')

def process_image(image):
    image = Image.open(image)
    image = data_transforms(image)
    return image.numpy()

def predict(image_path, model, topk=3):
    model.eval()
    image = process_image(image_path)
    image = torch.from_numpy(image)
    image.unsqueeze_(0)
    output = model.forward(image)
    output = output.exp()
    probs,classes = output.topk(topk)    
    classes = classes.cpu().numpy()[0]
    probs = probs.detach().cpu().numpy()[0]
    idx_to_class = {_class: index for index, _class in class_to_idx.items()}
    classes = list(map(lambda x : idx_to_class[x], classes ))
    return probs, classes

def predict_results(image):
    probs, classes = predict(image, model, 3)
    name_classes = list(map(lambda x: cat_to_name[x], classes))
    results = {}
    for i in range(3):
      results[i] = {"name": name_classes[i], "prob": str(probs[i])}
    return results
    
    # print(' Predicted species is {} with {:.2f}% confidence. \n '.format(name_classes[0], probs[0]*100))
    # for num in range(1,3):
    #     print('{} most likely species is {}'.format(num+1, name_classes[num]))

    



