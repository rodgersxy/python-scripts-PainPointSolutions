import cv2
import numpy as np

# Load the image
img = cv2.imread("veidz.jpg")

# Define alpha (contrast) and beta (brightness) values
alpha = 2.0  # Simple contrast control (>1 increases contrast)
beta = -160  # Simple brightness control (<0 decreases brightness)

# Adjust contrast and brightness
new = alpha * img + beta
new = np.clip(new, 0, 255).astype(np.uint8)  # Ensure pixel values are within 0-255

# Save the adjusted image
cv2.imwrite("cleaned.png", new)
