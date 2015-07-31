#!/usr/bin/python
'''Resize a group of images to a predefined or custom resolution'''

from PIL import Image, ImageEnhance
import os
import sys
from os.path import expanduser


def dir_list(indir):
    '''Return a list of files as strings'''
    return os.listdir(indir)


def resize(indir, outdir, new_width):
    '''resize images based on parameters using the PILLOW library'''

    images = dir_list(indir)
    i = 1
    numpics = len(images)
    img_quality = 95
    for image in images:
        image_object = Image.open(indir + image)
        new_width = int(new_width)
        size_percentage = (new_width / float(image_object.size[0]))
        new_height = int(
            (float(image_object.size[1]) * float(size_percentage))
            )
        new_image = image_object.resize(
            (new_width, new_height), Image.ANTIALIAS
            )
        new_image.save(outdir + image, quality=img_quality)
        print('Processed {} - {} of {}'.format(image, i, numpics))
        i += 1

    print "\nFinished. \nAnything else?\n"


def apply_filter_contrast(indir, outdir):

    print "Amount of contrast change (0-10)" \
              "<1: lower contrast, >1: increase contrast."

    while True:

        contrast_modifier = raw_input('>: ')

        if float(contrast_modifier) < 0 or float(contrast_modifier) > 10:
            print "enter number in range"
        else:
            break


    picture_list = dir_list(indir)
    counter_processed = 1
    img_quality = 95
    numpics = len(picture_list)

    for current_file_name in picture_list:
        image_object = Image.open(indir + current_file_name)
        contrast_object = ImageEnhance.Contrast(image_object)
        contrast_object.enhance(float(contrast_modifier)).save(outdir + current_file_name, quality=img_quality)
        print('Processed {} - {} of {}'.format(current_file_name, counter_processed, numpics))
        counter_processed += 1

    print "\nFinished. \nAnything else?\n"




def filter_switch_function(case, indir, outdir):
    return {
        'E': apply_filter_contrast(indir, outdir),
    }



def filter_images(indir, outdir):

    while True:

        print('''Choose filter:
          (E)nhance contrast,
          (T)ile to mosaic,
          (B)lack and white,
          (D)ramaticize,
          (A)dd black frame,
          (R)ETURN TO MENU''')

        filter_choice = raw_input('>: ')

        if filter_choice == 'r' or filter_choice == 'R':
            break

        list_of_choices = {'E','e','T','t','B','b','D','d','A','a'}

        if filter_choice not in list_of_choices:
            print 'Invalid entry, try again...'
            continue
        else:
            filter_switch_function(filter_choice, indir + '/', outdir + '/',)
            break














def resize_images(infolder, outfolder):
    while True:
        sizes = {
        'P': '2376',
        'L': '1024',
        'W': '800',
        'E': '640',
        'S': '250',
        'T': '128',
        'p': '2376',
        'l': '1024',
        'w': '800',
        'e': '640',
        's': '250',
        't': '128'
        }

        print('''Resize for:
          (P)rinting,
          (L)arge Format,
          (W)eb,
          (E)mail,
          (S)mall,
          (T)humbnail
          (R)ETURN TO MENU''')

        size = raw_input('>: ')

        if size == 'r' or size == 'R':
            break

        if size in sizes.keys():

            resize(
                infolder + '/', outfolder + '/', sizes[size]
                )
        else:
            print 'Invalid entry, try again...'

        pic_parameters(infolder, outfolder)
        break




def pic_parameters(infolder, outfolder):
    '''Select Picture Resolution Parameters'''

    # for 'sizes' only need the width as we will calculate the
    # height based on a percentage to keep the proper aspect ratio when
    # resizing
    while True:

        print('(R)esize, (A)dd Filter or (q)uit?')
        pic_operation = raw_input('>: ')
        possible_inputs = {'R','r','A','a'}

        if pic_operation == 'Q' or pic_operation == 'q':
            print "quit."
            break

        if pic_operation not in possible_inputs:
            print 'Invalid entry, try again...'
            continue

        if pic_operation == 'r' or pic_operation == 'R':
            resize_images(infolder, outfolder)
            break
        else:
            filter_images(infolder, outfolder)









def main():
    '''Select working folders'''
    operating_system = sys.platform

    operating_system = sys.platform
    if operating_system == 'win32':
        os.system('cls')
        homedir = expanduser('~') + '\Pictures\\'
    else:
        os.system('clear')
        homedir = expanduser('~') + '/Pictures/'


    print('Your Pictures folder is {}'.format(homedir))
    print('')
    confirm = raw_input('Do you want to work in this folder? (Y/N)')

    if 'Y' in confirm or 'y' in confirm:
        source_folder = raw_input('Source folder in {}'.format(homedir))
        dest_folder = raw_input('Destination folder in {}'.format(homedir))
        infolder = homedir + source_folder
        outfolder = homedir + dest_folder
    else:
        if operating_system == 'win32':
            print('Which folders would you like to use? Do not Include the trailing "\\"')
        else:
            print('Which folders would you like to use? Do not Include the \
                trailing "/"')

        infolder = raw_input('Source folder:> ')
        outfolder = raw_input('Destination folder (s for same):> ')
    if 'S' in outfolder or 's' in outfolder:
        outfolder = infolder

    pic_parameters(infolder, outfolder)



if __name__ == '__main__':
    main()
