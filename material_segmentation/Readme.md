**Structural Material Semantic Segmentation Dataset**

Download (Colab): 


`!wget https://data.lib.vt.edu/ndownloader/articles/16624648/versions/1`

`!unzip 1`

`!unzip 'Material Detection.zip' -d path_to_directory`

The material segmentation dataset comprises 3817 images gathered from the Virginia Department of Transportation (VDOT) Bridge Inspection Reports. There were four classes of material in the dataset: [concrete, steel, metal decking, and background]. The data was randomly sorted into training and testing using a custom script. 10% percent were reserved as the test set, and 90% were used as the training set. Therefore, there were 381 images in the test set and 3436 images in the training set. The original and the rescaled images used for training have been included. The images were resized to 512x512 for training and testing the DeeplabV3+ model. After training with the DeeplabV3+ model (DOI: 10.7294/16628620), we were able to achieve an F1-score of 94.2%. Details of the dataset, training process, and code can be referenced by reading the associated journal article. The GitHub repository information may be found in the journal article.



**Data:** https://data.lib.vt.edu/articles/dataset/Structural_Material_Semantic_Segmentation_Dataset/16624648?file=30914683


**REFERENCES**
https://github.com/beric7/structural_inspection_main
https://doi.org/10.7294/16628620

