# SHM-data-hub: Crack Detection Datasets
Semantic Segmentation



Özgenel, Çağlar Fırat (2019), “Concrete Crack Segmentation Dataset”, Mendeley Data, V1, doi: 10.17632/jwsn7tfbrp.1

## 1. Concrete Crack Segmentation Dataset

Published: 3 April 2019|Version 1|DOI:10.17632/jwsn7tfbrp.1

Contributor: Çağlar Fırat Özgenel

`wget https://md-datasets-cache-zipfiles-prod.s3.eu-west-1.amazonaws.com/jwsn7tfbrp-1.zip`

#### Description

The dataset includes 458 hi-res images together with their alpha maps (BW) indicating the crack presence. The ground truth for semantic segmentation has two classes to conduct binary pixelwise classification. The photos are captured in various buildings located in Middle East Technical University.  You can access a larger dataset containing images with 227x227 px dimensions for classification which are produced from this dataset from  http://dx.doi.org/10.17632/5y9wdsg2zt.1 . 



# fix issues with the jpg and JPG names
`import os`
`for PATH in ["../../datasets/crack/train/", "../../datasets/crack/val/"]:`
  `files = os.listdir(PATH)   #find out the file name which u want to rename using indexing`
  `for src in files:`
    `dst = src[:-3]+'jpg'`
    `os.rename(PATH+src, PATH+dst)     #rename it`



1. 