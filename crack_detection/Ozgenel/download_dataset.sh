#!/bin/sh
mkdir -p ../../../datasets/ozgenel/panoptic
mkdir -p ../../../datasets/ozgenel/annotations
cd ../../../datasets/ozgenel


wget https://md-datasets-cache-zipfiles-prod.s3.eu-west-1.amazonaws.com/jwsn7tfbrp-1.zip -O data.zip
unzip 'data.zip'
unrar x "concreteCrackSegmentationDataset.rar"
#rm -rf concreteCrackSegmentationDataset.rar
#rm data.zip

cd ../../shm-data-hub/crack_detection/Ozgenel/




