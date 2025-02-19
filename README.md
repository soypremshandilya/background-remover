# Background Remover

A simple Python application with a GUI to remove the background from images using the `rembg` library. This tool allows users to select an image, remove its background, and save the output as a transparent PNG.

## Features
✅ Select an image using a file dialog  
✅ Display a preview of the selected image  
✅ Remove the background using `rembg`  
✅ Save the output as a transparent PNG  
✅ Show success/error messages  

## Installation
### Prerequisites
Ensure you have Python installed on your system. Then, install the required dependencies:
```sh
pip install rembg pillow tkinterdnd2 onnxruntime
```
If you have a GPU, you can install the GPU version for faster processing:
```sh
pip install onnxruntime-gpu
```

## Usage
Run the script to launch the GUI:
```sh
python background_remover.py
```
### Steps:
1. Click on the **Browse** button to select an image.
2. The selected image will be displayed in the UI.
3. Click **Remove Background** to process the image.
4. The background-removed image will be saved as a transparent PNG in the same directory.

## Contributing
Feel free to fork this repository and submit pull requests with improvements.

## License
This project is licensed under the MIT License.

## Author
Developed by **Prem Shandilya**  
GitHub: [soypremshandilya](https://github.com/soypremshandilya)

