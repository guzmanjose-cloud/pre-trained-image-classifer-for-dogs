from os import listdir


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
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    #Creates list of files in directory
    results_dic = dict()

    files = listdir(image_dir)




    # Iterates through files and leaves only letters
    for file in files:
        if file[0] != ".":
           pet_label = file
        if pet_label[-4:] == '.jpg':
            pet_label = pet_label[:-4]
        pet_label = pet_label.strip('_0123456789')
        pet_label = pet_label.replace('_', ' ')
        pet_label = pet_label.lower()
        results_dic[file] = [pet_label]
        # prints the key and values of results_dic
        print('\nfilename = ', file, '    pet label = ', pet_label)
        #results_dic = dict(filename = x, label = a )
       
        
       
      
    return results_dic
    
#if __name__ == '__main__':
#    get_pet_labels('./pet_images')