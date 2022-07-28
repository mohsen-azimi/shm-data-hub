import glob
import os
import shutil
import glob
import subprocess
import cv2
import glob
import numpy as np

# ----------------------------------------------------------------------------------------------------------------------
download = False  # skip this step if you already have the dataset
fix = True  # skip this step if you already have the dataset
convert = True  # skip this step if you already have the dataset
# ----------------------------------------------------------------------------------------------------------------------
for DIR in ['../../../datasets/ozgenel/panoptic', '../../../datasets/ozgenel/annotations']:
    if os.path.exists(DIR) and os.path.isdir(DIR):
        shutil.rmtree(DIR)
    if not os.path.exists(DIR):  # make empty folders
        os.makedirs(DIR)
# ----------------------------------------------------------------------------------------------------------------------
if download:
    print("Downloading the dataset...")
    subprocess.call(["bash", "download_dataset.sh"])
    print("Downloaded the dataset!")
# #######################################################################################################################
# Fix file name issues
if fix:

    PATH = "../../../datasets/ozgenel/"
    # fix naming issues
    for DIR in [PATH + 'BW/', PATH + 'rgb/']:
        files = os.listdir(DIR)  # find out the file name which u want to rename using indexing
        for src in files:
            dst = src[:-3] + 'jpg'
            os.rename(DIR + src, DIR + dst)  # rename it

    # remove extra files without annotations
    for file in os.listdir(PATH + 'BW/'):
        if not os.path.exists(PATH + 'rgb/' + file):
            os.remove(PATH + 'BW/' + file)

    # check if the total number of files matches
    index = 0
    for directory in ['BW', 'rgb']:
        i = 0
        for file in glob.glob(PATH + directory + '/*.jpg'):
            i += 1
        print(f'Total files in {directory}: ', i)

# #######################################################################################################################
# Convert JPG to PNG
if convert:

    PATH = "../../../datasets/ozgenel/"

    index = 0
    for file in glob.glob(PATH + 'BW/' + '/*.jpg'):
        index += 1
        grayImage = cv2.imread(file, cv2.IMREAD_GRAYSCALE)  # read in grayscale mode
        thresh = 127
        mask = cv2.threshold(grayImage, thresh, 255, cv2.THRESH_BINARY)[1]

        cv2.imwrite(PATH+'BW_png/'+file.split(".jpg")[0][-3:] + ".png", mask)
        os.system('clear')
        print(f'{index}/{len(glob.glob(PATH + "BW/*.jpg"))}')


print("Files are ready!")
