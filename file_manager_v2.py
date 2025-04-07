import os
import shutil

class FileManagerV2:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "file_path": ("STRING", {"multiline": False}),
                "operation": (
                    ["move", "copy", "delete"],
                    {"default": "move"}
                ),
                "target_path": ("STRING", {"multiline": False}),
            },
            "optional": {
                "in_data": ("*",),  # 任意输入类型
            },
        }

    RETURN_TYPES = ("*",)
    RETURN_NAMES = ("out_data",)

    FUNCTION = "process"
    CATEGORY = "utils/FileManager"

    def process(self, file_path, operation, target_path, in_data=None):
        result_message = ""
        try:
            if not os.path.exists(file_path):
                result_message = f"File not found: {file_path}. Skipping operation."
                return (result_message,)

            if operation == "move":
                shutil.move(file_path, target_path)
                result_message = f"Moved '{file_path}' → '{target_path}'"
            elif operation == "copy":
                shutil.copy(file_path, target_path)
                result_message = f"Copied '{file_path}' → '{target_path}'"
            elif operation == "delete":
                os.remove(file_path)
                result_message = f"Deleted '{file_path}'"
            else:
                result_message = f"Unsupported operation: {operation}"

        except Exception as e:
            result_message = f"Error: {str(e)}"

        return (result_message,)

NODE_CLASS_MAPPINGS = {
    "FileManagerV2": FileManagerV2,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FileManagerV2": "File Manager v2",
}
