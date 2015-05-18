#!/usr/bin/python
'''Resize a group of images to a predefined or custom resolution'''

from PIL import Image
import os
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


def pic_parameters(infolder, outfolder):
    '''Select Picture Resolution Parameters'''

    # for 'sizes' only need the width as we will calculate the
    # height based on a percentage to keep the proper aspect ratio when
    # resizing
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
          (T)humbnail''')

    size = raw_input('>: ')

    if size in sizes.keys():
        resize(
            infolder + '/', outfolder + '/', sizes[size]
            )

    else:
        print 'Invalid entry, try again...'
        pic_parameters(infolder, outfolder)


def main():
    '''Select working folders'''

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
        print('Which folders would you like to use? Do not Include the \
              trailing "/"')
        infolder = raw_input('Source folder:> ')
        outfolder = raw_input('Destination folder:> ')

    pic_parameters(infolder, outfolder)


if __name__ == '__main__':
    main()
