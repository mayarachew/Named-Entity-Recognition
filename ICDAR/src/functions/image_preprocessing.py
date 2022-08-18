"""Apply preprocessing method."""
import numpy as np
import cv2 # type: ignore

def image_preprocessing(image: np.uint8) -> np.uint8:
    """Add preprocessing step to images
    Args:
        image: image to be preprocessed
    Returns:
        image_preprocessed
    """

    # Transform grayscale image in binary image using an adaptive gaussian threshold
    image_preprocessed = cv2.adaptiveThreshold(src=image, 
                                     maxValue=170, 
                                     adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                     thresholdType=cv2.THRESH_BINARY, 
                                     blockSize=35, 
                                     C=40)

    return image_preprocessed