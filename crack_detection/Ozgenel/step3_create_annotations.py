import glob
import json
import os
import shutil
import glob
from sklearn.model_selection import train_test_split
from src import CreateCocoFormatInstances as COCO
import subprocess

# ----------------------------------------------------------------------------------------------------------------------
split = True
# ----------------------------------------------------------------------------------------------------------------------
all_files = glob.glob(os.path.join('../../../datasets/ozgenel/BW_png/', "*.png"))
if split:
    train_files, val_files = train_test_split(all_files, train_size=0.8, random_state=66, shuffle=True)
else:
    train_files = all_files
    val_files = []
# ----------------------------------------------------------------------------------------------------------------------

for subset, files in {"train": train_files, "val": val_files}.items():
    ##############################################################################
    my_coco = COCO()  # create an instance of the class CreateCocoFormat()
    my_coco.load_categories()  # load categories from images_info.json


    for mask_image in files:
        my_coco.create_annotations(mask_image)  # create annotations from masks
        my_coco.cache_image_id += 1
        os.system('clear')
        print(my_coco.cache_image_id,"/",len(files))
    ##############################################################################
    with open(f"../../../datasets/ozgenel/annotations/instances_{subset}.json", 'w') as f:
        json.dump(my_coco.coco_instance, f)
    with open(f"../../../datasets/ozgenel/annotations/panoptic_{subset}.json", 'w') as f:
        json.dump(my_coco.coco_panoptic, f)

        print("Created %d annotations for '%s' images in folder" % (my_coco.cache_image_id, subset))
        if my_coco.cache_image_id == 0:
            print("No annotations created!")
