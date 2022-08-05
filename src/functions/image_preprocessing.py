"""Apply preprocessing method."""
import numpy as np
import cv2 # type: ignore
import pytesseract
import imutils

def image_preprocessing(image: np.uint8) -> np.uint8:
    """Add preprocessing step to images
    Args:
        image: image to be preprocessed
    Returns:
        image_preprocessed
    """

    # Transform grayscale image in binary image using an adaptive gaussian threshold
    image_binary = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 33, 20)

    # Get text orientation (angles) 
    # informations_obj = pytesseract.image_to_osd(image_binary, output_type=pytesseract.Output.DICT)

    # Rotate the image to correct the orientation
    # image_rotated = imutils.rotate_bound(image_binary, angle=informations_obj['orientation_conf'])

    # Find image contours
    contours = cv2.findContours(image_binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = contours[0] if len(contours) == 2 else contours[1]

    # Fill a mask with the contour
    mask = np.zeros(image_binary.shape, dtype=np.uint8)
    mask = cv2.fillPoly(mask, contours, [255,255,255])
    mask = np.invert(mask)

    # OR operation bitwise
    bitwise = cv2.bitwise_or(image_binary, mask)

    image_preprocessed = bitwise

    return image_preprocessed