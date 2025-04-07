# ComfyUI File/Image Utils Nodes

This custom node set provides useful utilities for file operations and image loading in ComfyUI.

## Features

- 📂 File Manager v2: Move, copy, or delete a file with feedback.
- 🖼️ Load Image from Path: Load a local image file into ComfyUI workflow.
- 🔁 If Text Equals: Logic node to compare two strings.

## Installation

```bash
git clone https://github.com/QingLuanWithoutHeart/comfyui-file-image-utils.git
```
Then place it into your ComfyUI/custom_nodes/ directory.

Dependencies
Install required libraries:

```bash
pip install -r requirements.txt
```


Nodes
🔹 File Manager v2
Supports move, copy, delete

Outputs status message

Accepts any input/output types

🔹 Load Image from Path
Reads an image from a local path and loads into ComfyUI

🔹 If Text Equals
Compares two strings and returns True or False
