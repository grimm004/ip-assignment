import cv2
import glob
import os

##############################################################

# These parameter values are indicative. You should choose your own
# according to properties of the method you want to demonstrate

h = 5
template_window_size = 7
#search_window_size = 21

##############################################################

for image_file in glob.glob(".\\images\\*.png"):
    img = cv2.imread(image_file)

    dst = cv2.fastNlMeansDenoisingColored(img, None, h, h, template_window_size, 21)

    path = ".\\processed_h%d_t%d" % (h, template_window_size)
    if not os.path.exists(path):
        os.mkdir(path)
    cv2.imwrite("%s\\%s" % (path, image_file.split("\\")[-1]), dst)
