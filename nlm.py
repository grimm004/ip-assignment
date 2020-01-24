import cv2
import glob
import os

##############################################################

# These parameter values are indicative. You should choose your own
# according to properties of the method you want to demonstrate

h = 5
m = 7  # template_window_size
s = 21  # search_window_size

##############################################################

for image_file in glob.glob(".\\images\\*.png"):
    img = cv2.imread(image_file)

    dst = cv2.fastNlMeansDenoisingColored(img, None, h, h, m, s)

    path = ".\\processed_h%d_t%d_m%d" % (h, m, s)
    if not os.path.exists(path):
        os.mkdir(path)
    cv2.imwrite("%s\\%s" % (path, image_file.split("\\")[-1]), dst)
