from PIL import Image
import numpy as np
import os

class LoadImageFromPath:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image_path": ("STRING", {"default": "", "multiline": False}),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = "load_image"
    CATEGORY = "utils/Image"

    def load_image(self, image_path):
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image path not found: {image_path}")
        img = Image.open(image_path).convert("RGB")
        img = np.array(img).astype(np.float32) / 255.0
        return (img,)

NODE_CLASS_MAPPINGS = {
    "LoadImageFromPath": LoadImageFromPath,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LoadImageFromPath": "Load Image From Path",
}
