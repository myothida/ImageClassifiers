#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#                                                                             
# PROGRAMMER:
# DATE CREATED:                                  
# REVISED DATE: 
# PURPOSE: Create a function calculates_results_stats that calculates the 
#          statistics of the results of the programrun using the classifier's model 
#          architecture to classify the images. This function will use the 
#          results in the results dictionary to calculate these statistics. 
#          This function will then put the results statistics in a dictionary
#          (results_stats_dic) that's created and returned by this function.
#          This will allow the user of the program to determine the 'best' 
#          model for classifying the images. The statistics that are calculated
#          will be counts and percentages. Please see "Intro to Python - Project
#          classifying Images - xx Calculating Results" for details on the 
#          how to calculate the counts and percentages for this function.    
#         This function inputs:
#            -The results dictionary as results_dic within calculates_results_stats 
#             function and results for the function call within main.
#         This function creates and returns the Results Statistics Dictionary -
#          results_stats_dic. This dictionary contains the results statistics 
#          (either a percentage or a count) where the key is the statistic's 
#           name (starting with 'pct' for percentage or 'n' for count) and value 
#          is the statistic's value.  This dictionary should contain the 
#          following keys:
#            n_images - number of images
#            n_dogs_img - number of dog images
#            n_notdogs_img - number of NON-dog images
#            n_match - number of matches between pet & classifier labels
#            n_correct_dogs - number of correctly classified dog images
#            n_correct_notdogs - number of correctly classified NON-dog images
#            n_correct_breed - number of correctly classified dog breeds
#            pct_match - percentage of correct matches
#            pct_correct_dogs - percentage of correctly classified dogs
#            pct_correct_breed - percentage of correctly classified dog breeds
#            pct_correct_notdogs - percentage of correctly classified NON-dogs
#
##
# TODO 5: Define calculates_results_stats function below, please be certain to replace None
#       in the return statement with the results_stats_dic dictionary that you create 
#       with this function
# 
def calculates_results_stats(results_dic):
    """
    Calculates statistics of the results of the program run using classifier's model 
    architecture to classifying pet images. Then puts the results statistics in a 
    dictionary (results_stats_dic) so that it's returned for printing to help
    the user to determine the 'best' model for classifying images. Note that 
    the statistics calculated as the results are either percentages or counts.
    
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
    
    Returns:
     results_stats_dic - Dictionary that contains the results statistics (either
                    a percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value.
    """
    
    # Initialize counters for the statistics
    n_images = len(results_dic)  # Total number of images processed
    n_dogs = 0  # Number of dog images
    n_notdogs = 0  # Number of non-dog images
    n_correct = 0  # Number of correct classifications
    n_correct_dogs = 0  # Number of correct dog classifications
    n_correct_notdogs = 0  # Number of correct non-dog classifications
    n_correct_breed = 0
    

    # Loop through results_dic to accumulate the counts
    for key in results_dic:
        pet_is_dog = results_dic[key][3]  # 1 if pet is a dog, 0 if not
        classifier_is_dog = results_dic[key][4]  # 1 if classifier says it's a dog, 0 if not
        match = results_dic[key][2]  # 1 if labels match, 0 if not

        # Count the number of dog and non-dog images
        if pet_is_dog == 1:
            n_dogs += 1
        else:
            n_notdogs += 1
        
        # Count the number of correct classifications
        if match == 1:
            n_correct += 1
        
        # Count correct dog classifications
        if pet_is_dog == 1 and classifier_is_dog == 1:
            n_correct_dogs += 1
        
        # Count correct non-dog classifications
        if pet_is_dog == 0 and classifier_is_dog == 0:
            n_correct_notdogs += 1

        if pet_is_dog ==1 and match == 1:
            n_correct_breed +=1

    # Calculate the statistics
    pct_correct = (n_correct / n_images) * 100 if n_images > 0 else 0
    pct_correct_dogs = (n_correct_dogs / n_dogs) * 100 if n_dogs > 0 else 0
    pct_correct_breed = (n_correct_breed / n_dogs) * 100 if n_dogs > 0 else 0
    pct_correct_notdogs = (n_correct_notdogs / n_notdogs) * 100 if n_notdogs > 0 else 0

    # Create a dictionary for the results statistics
    results_stats_dic = {
        'n_images': n_images,
        'n_dogs_img': n_dogs,
        'n_notdogs_img': n_notdogs,
        'n_match': n_correct,
        'n_correct_dogs': n_correct_dogs,
        'n_correct_notdogs': n_correct_notdogs,
        'pct_match': pct_correct,
        'pct_correct_breed': pct_correct_breed,
        'pct_correct_dogs': pct_correct_dogs,
        'pct_correct_notdogs': pct_correct_notdogs
    }

    return results_stats_dic
