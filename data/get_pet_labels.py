#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED:                                  
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains the following item:
         index 0 = pet image label (string)
    """
    # Creates list of files in directory
    in_files = listdir(image_dir)
    
    # Creates empty dictionary for the results (pet labels, etc.)
    results_dic = dict()
   
    # Processes through each file in the directory, extracting the pet image label
    for idx in range(0, len(in_files), 1):
       
      
       if in_files[idx][0] != ".":
           
           # Creates temporary label variable to hold pet label name extracted 
           pet_label = ""

           # TODO 2a: Extract the pet label from the filename
           # Split filename by underscore and take the first part as the label
           pet_label_parts = in_files[idx].lower().split('_')[:-1]  # Exclude file number part
           pet_label = ' '.join(pet_label_parts).lower().strip()  # Join and format label

           # If filename doesn't already exist in dictionary, add it and its pet label
           if in_files[idx] not in results_dic:
              results_dic[in_files[idx]] = [pet_label]
           else:
               print("** Warning: Duplicate files exist in directory:", 
                     in_files[idx])
 
    # TODO 2b: Return the dictionary with the pet labels

    return results_dic
