from PIL import Image
import numpy as np
import os
import torch

class LoadImageFromPath:
    @classmethod
    def INPUT_TYPES(cls):
        return {"required": {"image_path": ("STRING", {"default": ""})}}

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "load_image"
    CATEGORY = "file-image-utils/Image"

    def load_image(self, image_path):
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image not found: {image_path}")

        image = Image.open(image_path).convert("RGB")  # 强制转换为 RGB
        image = np.array(image).astype(np.float32) / 255.0  # 转为 float32，标准化
        image = torch.from_numpy(image)[None,]  # 加 batch 维度 -> (1, H, W, 3)
        return (image,)

NODE_CLASS_MAPPINGS = {
    "LoadImageFromPath": LoadImageFromPath,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LoadImageFromPath": "Load Image From Path",
}
