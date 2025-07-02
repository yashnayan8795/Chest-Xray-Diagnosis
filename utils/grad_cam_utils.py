import torch
from pytorch_grad_cam import GradCAM
from pytorch_grad_cam.utils.image import show_cam_on_image
from torchvision import transforms
import numpy as np

def generate_grad_cam(model, image_pil, target_layer, device):
    model.eval()

    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485], [0.229])
    ])

    image_tensor = transform(image_pil).unsqueeze(0).to(device)

    # ✅ DO NOT include `use_cuda=...` here
    cam = GradCAM(model=model, target_layers=[target_layer])

    grayscale_cam = cam(input_tensor=image_tensor)[0]

    img_np = image_tensor.squeeze().cpu().numpy()
    img_np = np.transpose(img_np, (1, 2, 0))
    img_np = (img_np - img_np.min()) / (img_np.max() - img_np.min())

    cam_image = show_cam_on_image(img_np, grayscale_cam, use_rgb=True)
    return cam_image
