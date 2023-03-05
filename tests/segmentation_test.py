# Importing Necessary Libraries

import matplotlib.pyplot as plt
from skimage import io
from skimage.color import rgb2gray


test_image = io.imread('../test_images/1_Princess-Parkway-1.jpg')
gray_test = rgb2gray(test_image)

# Setting the plot size to 15,15
plt.figure(figsize=(15, 15))

for i in range(10):
    binarized_gray = (gray_test > i * 0.1) * 1
    plt.subplot(5, 2, i + 1)

    # Rounding of the threshold
    # value to 1 decimal point
    plt.title("Threshold: >" + str(round(i * 0.1, 1)))

    # Displaying the binarized image
    # of various thresholds
    plt.imshow(binarized_gray, cmap='gray')

plt.tight_layout()
plt.show()
