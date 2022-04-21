import numpy as np
import cv2
from skimage.filters import threshold_local
import math
from scipy import ndimage

class Scanner:

    def __init__(self, img):
        self.img = img

    def Scan_View(self):
        print("Scanned")
        image = cv2.imread(self.img) # read the original image
        original = image.copy() # copy the image

        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # converts the image to greyscale
        thr = threshold_local(image, 11, offset = 10, method = 'gaussian') # threshold
        image = (image > thr).astype("uint8") * 255 #apply threshold

        # # show the original image and the edge detected image
        # cv2.imshow("original", original)
        # cv2.imshow("Scanned", image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        # print(np.shape(original), np.shape(image))

        # B&W image
        cv2.imwrite("Part_scan_view.png", image)
        return image

if __name__=="__main__":
    # Defining the image name
    img = "33333.jpeg"

    # Calling the scanner class
    scan = Scanner(img)

    # Scanning the image - B&W scheme
    scanned_im = scan.Scan_View()