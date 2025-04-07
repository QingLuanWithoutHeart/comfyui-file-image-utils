from .file_manager_v2 import NODE_CLASS_MAPPINGS as fm_nodes, NODE_DISPLAY_NAME_MAPPINGS as fm_display
from .load_image_from_path import NODE_CLASS_MAPPINGS as li_nodes, NODE_DISPLAY_NAME_MAPPINGS as li_display
from .if_text_equals import NODE_CLASS_MAPPINGS as if_nodes, NODE_DISPLAY_NAME_MAPPINGS as if_display

NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

NODE_CLASS_MAPPINGS.update(fm_nodes)
NODE_CLASS_MAPPINGS.update(li_nodes)
NODE_CLASS_MAPPINGS.update(if_nodes)

NODE_DISPLAY_NAME_MAPPINGS.update(fm_display)
NODE_DISPLAY_NAME_MAPPINGS.update(li_display)
NODE_DISPLAY_NAME_MAPPINGS.update(if_display)
