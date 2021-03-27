There are following files in this project

FormatDataset.py:
This is the files that will be used to create data set on real time.So you to create a dataset
run this file it will ask for name enter the name and then it will start capturing the face

Preprocess.py
This file will generate 37 new images for each subject using 3 images per subject of front,left and right from images.csv
Total images per subject comes to 40. 

SVMKNN.py 
Run this file it will train the model for SVM and KNN

CNN.py
Run this file it will train the model for CNN

Test.py
This file will be used to recognize faces 

images.csv
This file is used by preprocess.py to preprocess the images from dataset folder.
There are 3 entries for each subject, where each entry is for image from front,left and right portion of face.

images_path.csv
This file is used by cnn.py to input the data.
There are 400 manual entries where there are 40 images per subject.
Total number of subjects are 10, thus 400.

Note: We can use the images.csv and add the image augmentation steps within the cnn file to generate similiar file like this and not do manual entry. We have code available for it but we choose to use this file instead.


student_entry.csv
The entry of each subject is made in this file.
