
# OCR Assignment

## Objective

Develop an Optical Character Recognition (OCR) algorithm capable of detecting and accurately recognizing English text from image inputs. The system should return the recognized text along with the bounding boxes for each detected text segment.

## Requirements

- Python 3.x
- Required Libraries:
  - OpenCV
  - pytesseract
  - json
  - ipyfilechooser
  - ipywidgets

## Installation

1. **Install Python 3.x**: Ensure that Python 3.x is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Required Libraries**: Use pip to install the necessary libraries. Run the following commands:
   ```bash
   pip install opencv-python
   pip install pytesseract
   pip install ipyfilechooser
   pip install ipywidgets
   pip install matplotlib
   ```
   or
   ```bash
   pip install opencv-python pytesseract ipyfilechooser ipywidgets matplotlib
   ```

3. **Tesseract OCR**: Ensure that Tesseract OCR is installed on your system. You can download it from [GitHub](https://github.com/UB-Mannheim/tesseract/wiki) and follow the installation instructions. Make sure to add Tesseract to your system's PATH.

## Usage

1. **Open the Jupyter Notebook**: Open the `OCR_Assignment.ipynb` notebook in Jupyter.

2. **Select Images**: Use the FileChooser widget to select the images you want to process. Ensure that the images are in the `.jpg` format.

3. **Start Processing**: Click the "Start Processing" button to run the OCR algorithm on the selected images. The recognized text and bounding boxes will be saved in a JSON file named `ocr_results.json`.

## File Structure

- **`OCR_Assignment.ipynb`**: The main Jupyter Notebook containing the OCR algorithm and the user interface for selecting images and starting the processing.
- **`ocr_results.json`**: The output JSON file containing the recognized text and bounding boxes for each processed image. This file will be generated after running the notebook.

## Approach

### OCR Algorithm

1. **Image Reading**: The image is read using OpenCV.
2. **Preprocessing**:
   - Convert the image to grayscale.
   - Apply a median blur to remove noise.
   - Binarize the image using Otsu's thresholding.
3. **Text Recognition**: Use Tesseract to recognize text in the image with a custom configuration (`--oem 3 --psm 11`).
4. **Bounding Boxes**: Extract bounding boxes for detected text segments and filter out low-confidence detections.


## Conclusion

The system is capable of accurately recognizing English text from images and outputting the recognized text along with bounding boxes.

For any further questions or issues, please contact [Lakshitha Vimuth](mailto:lakshithavimuth8@gmail.com) or [Website](https://lvimuth.github.io/).
