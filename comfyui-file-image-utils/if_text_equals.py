class IfTextEquals:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text_a": ("STRING", {}),
                "text_b": ("STRING", {}),
            },
        }

    RETURN_TYPES = ("BOOLEAN",)
    RETURN_NAMES = ("is_equal",)
    FUNCTION = "compare"
    CATEGORY = "logic"

    def compare(self, text_a, text_b):
        return (text_a.strip() == text_b.strip(),)

NODE_CLASS_MAPPINGS = {
    "IfTextEquals": IfTextEquals,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "IfTextEquals": "If Text Equals",
}
