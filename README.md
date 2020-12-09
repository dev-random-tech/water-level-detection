# water-level-detection
Detecting the water level with image segmentation

# Tutorial

# Running inference on image and predicting segment mask
1. Download the code with trained model weight from [Here](https://drive.google.com/file/d/1AtZFRyKAiEk9Pfip636_c7tZJjT0xUOP/view?usp=sharing) or [here](https://drive.google.com/file/d/1E9oABPr84FOVTbaF2CnLm8qq9tbV4yY6/view?usp=sharing). or train the model yourself using the instructions of the Training section.
2. Open the RunPredictionOnFolder.py script.
3. Set the path to the folder where the images are stored to the: InputDir parameter (all the images in the input folder should be in .jpg or .png format)
4. Set the output folder where the output will be stored to the: OutDir parameter.
5. Run script. 
6. Output: predicted region for each input image and class would appear in the OutDir folder.

Note: RunPredictionOnFolder.py should run out of the box (as is) using the sample images and [trained model](https://drive.google.com/file/d/1AtZFRyKAiEk9Pfip636_c7tZJjT0xUOP/view?usp=sharing) provided.
  ## Additional parameters:
* If you train the net yourself, set the path to your  trained model  in the Trained_model_path parameter
*  If you have a Nvidia GPU and Cuda installed, set the UseGPU parameter to True (this will allow the net to achieve a much faster running time).
* Changing FreezeBatchNormStatistics parameter from False to True might change the segmentation quality for better or worst (and so does changing the image size)

## Additional Running scripts:
* RunPredictionOnVideo.py script: receive an Input video in InputVideo apply prediction overlay the prediction on the image  and save it to video files.

* RunPredictionWebCam.py script: Take image from web come run prediction overlay the prediction on the image  and display on screen

# Training general
There are two training options: one is to train using only with LabPics dataset, this is faster, simpler. The second training option is to use a combination of the LabPics dataset and Vessels classes from the [COCO panoptic dataset](http://cocodataset.org/#download) (Such as bottles/glasses/jars..). This option is more complex to train and gives lower accuracy on the test set but gives a more robust net that work under a wider set of conditions. 


# Training simple (only LabPics)
1. Download the LabPics data set from [Here](https://drive.google.com/file/d/1TZao7JDzxcJr_hMqYHLRcV2N0UHoH2c1/view?usp=sharing) or [here](https://drive.google.com/file/d/1gfaM_6eZjtg7dkFShGl1gIfsXzj1KjIX/view?usp=sharing)
2. Open the Train.py script
3. Set the path to the LabPics dataset main folder to the TrainFolderPath parameter.
4. Run the script 
5. Output trained model will appear in the /log subfolder or any folder set in Trained model Path



## Training second option (With LabPics dataset and Vessels from  the COCO panoptic dataset)
### Downloading datasets
1. Download the LabPics data set from [Here](https://drive.google.com/file/d/1TZao7JDzxcJr_hMqYHLRcV2N0UHoH2c1/view?usp=sharing) or [here](https://drive.google.com/file/d/1gfaM_6eZjtg7dkFShGl1gIfsXzj1KjIX/view?usp=sharing)


2. Download the [COCO panoptic dataset](http://cocodataset.org/#download) annotation and train images.
### Converting COCO dataset into training data
3. Open script TrainingDataGenerationCOCO/RunDataGeneration.py
4. Set the COCO dataset image folder to the ImageDir parameter.
5. Set the COCO panoptic annotation folder to the AnnotationDir parameter.
6. Set the COCO panoptic .json file to the DataFile parameter.
7. Set the output folder (where the generated data will be saved) to the OutDir parameter.
8. Run script. 
### Training
9. Open the COCO_Train.py script
10. Set the path to the LabPics dataset main folder to the LabPicsTrainFolderPath parameters.
11. Set the path to the COCO generated data (OutDir, step 7)  to the COCO_TrainDir paramter.
12. Run the script 
13. Output trained model will appear in the /log_COCO subfolder or any folder set in Trained model Path





# Code file structure
RunPredictionOnFolder.py: Run prediction on image using pre-trained image

Train.py: Training the net of the [LabPics](https://drive.google.com/file/d/1TZao7JDzxcJr_hMqYHLRcV2N0UHoH2c1/view?usp=sharing) dataset

ChemReader.py: File reader for the LabPics dataset (used by the Train.py script)

FCN_NetModel.py: The class containing the neural net model.

Evaluator.py: Evaluate the net performance during training (Used by Train.py)

CategoryDictionary.py: List of classes and subclasses used by the net and LabPics dataset.

Logs folder: Folder where the trained models and training logs are stored.

InputImages Folder: Example input images for the net.

### For second training mode (with COCO)

COCO_TRAIN.py:  Training script for second training mode (with COCO).

CocoReader.py: Reader for the converted COCO data.

TrainingDataGenerationCOCO folder: Convert COCO dataset for training data.



# Notes/Thanks
The images for the [LabPics dataset](https://drive.google.com/file/d/1TZao7JDzxcJr_hMqYHLRcV2N0UHoH2c1/view?usp=sharing)    were taken from Youtube channels such as [NileRide](https://www.youtube.com/user/TheRedNile), [NurdRage](https://www.youtube.com/user/NurdRage), and [Chemplayer](https://www.youtube.com/channel/UCsJHe4uMbquncMpe1PiLa2A), [douglas lab](https://www.youtube.com/channel/UCR3CEAL-y3CoMf4oJOJgtEw), [Koen2All](https://www.youtube.com/user/koen2all) and from Instagram channels such as Chemistrylife, organic Chemistry lab, Chemistry and me, Ministry Of Chemistry , vacuum distillation, Cocktail.

Work was done in the Matter Lab (Alan Aspuru Guzik group) and the Vector institute Toronto.

The [LabPics dataset](https://drive.google.com/file/d/1gfaM_6eZjtg7dkFShGl1gIfsXzj1KjIX/view?usp=sharing) was made by Mor Bismuth.

# Links
LabPics dataset for annotated images of liquid, solid and foam materials in mostly transperent vessels in Lab setting and general everyday setting can be download from [here](https://drive.google.com/file/d/1TZao7JDzxcJr_hMqYHLRcV2N0UHoH2c1/view?usp=sharing) or [here](https://drive.google.com/file/d/1gfaM_6eZjtg7dkFShGl1gIfsXzj1KjIX/view?usp=sharing)

Train model for this net can be download from [here](https://drive.google.com/file/d/1AtZFRyKAiEk9Pfip636_c7tZJjT0xUOP/view?usp=sharing) or [here](https://drive.google.com/file/d/1E9oABPr84FOVTbaF2CnLm8qq9tbV4yY6/view?usp=sharing).

