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
                "in_data": ("*",),  # 支持任意输入类型
            },
        }

    # 增加返回一个字符串信息
    RETURN_TYPES = ("*", "STRING",)
    RETURN_NAMES = ("out_data", "result_msg",)

    FUNCTION = "process"
    CATEGORY = "file-image-utils/FileManager"

    def is_path_folder(self, path: str) -> bool:
        return (
            path.endswith(("/", "\\")) or
            not os.path.splitext(path)[1]  # 没有扩展名 = 文件夹
        )

    def process(self, file_path, operation, target_path, in_data=None):
        result_message = ""
        try:
            if not os.path.exists(file_path):
                result_message = f"[FileManagerV2] ❌ File not found: {file_path}. Skipping operation."
                print(result_message)
                return (in_data, result_message)

            # 判断 target_path 是否为目录
            is_dir = self.is_path_folder(target_path)

            if is_dir:
                os.makedirs(target_path, exist_ok=True)
                target_file = os.path.join(target_path, os.path.basename(file_path))
            else:
                os.makedirs(os.path.dirname(target_path), exist_ok=True)
                target_file = target_path

            # 文件操作
            if operation == "move":
                shutil.move(file_path, target_file)
                result_message = f"[FileManagerV2] ✅ Moved '{file_path}' to '{target_file}'"
            elif operation == "copy":
                shutil.copy(file_path, target_file)
                result_message = f"[FileManagerV2] ✅ Copied '{file_path}' to '{target_file}'"
            elif operation == "delete":
                os.remove(file_path)
                result_message = f"[FileManagerV2] ✅ Deleted '{file_path}'"
            else:
                result_message = f"[FileManagerV2] ❌ Unsupported operation: {operation}"

        except Exception as e:
            result_message = f"[FileManagerV2] ❌ Error: {str(e)}"

        print(result_message)
        return (in_data, result_message)

NODE_CLASS_MAPPINGS = {
    "FileManagerV2": FileManagerV2,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FileManagerV2": "File Manager v2",
}
