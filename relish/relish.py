#!/usr/bin/python
'''Resize a group of images to a predefined or custom resolution
Modify image appearance and add a frame and a watermark'''


from PIL import Image, ImageEnhance, ImageFont, ImageDraw
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


def apply_filter_contrast_color_sharpen(indir, outdir, operation):
    '''apply filter and image modification bases on parameter input using the PILLOW library'''
    if operation == 'e':
        print "Amount of contrast change (0-10)" \
              "<1: lower contrast, >1: increase contrast."

    if operation == 'c':
        print "Amount of color change (0-10)" \
              "<1: lower color saturation, >1: increase color saturation."

    if operation == 's':
        print "Amount of sharpness change (0-10)" \
              "<1: lower sharpness, >1: increase sharpness."

    while True:

        modifier_value = raw_input('>: ')

        try:
            float(modifier_value)
        except ValueError:
            print "--please enter a real number--"
            continue

        if float(modifier_value) < 0 or float(modifier_value) > 10:
            print "enter number in range (0-10)"
        else:
            break

    picture_list = dir_list(indir)
    counter_processed = 1
    img_quality = 95
    num_pics = len(picture_list)

    for current_file_name in picture_list:
        image_object = Image.open(indir + current_file_name)

        if operation == 'e':
            modifier_object = ImageEnhance.Contrast(image_object)
        if operation == 'c':
            modifier_object = ImageEnhance.Color(image_object)
        else:
            modifier_object = ImageEnhance.Sharpness(image_object)

        modifier_object.enhance(float(modifier_value)).save(outdir + current_file_name, quality=img_quality)
        print('Processed {} - {} of {}'.format(current_file_name, counter_processed, num_pics))
        counter_processed += 1

    print "\nFinished. \nAnything else?\n"


def apply_filter_watermark(indir , outdir, text_string_watermark):
    '''add water mark to image using PILLOW library'''
    picture_list = dir_list(indir)
    counter_processed = 1
    img_quality = 95
    num_pics = len(picture_list)

    for current_file_name in picture_list:
        image_object = Image.open(indir + current_file_name).convert('RGBA')
        text_image_overlay = Image.new('RGBA', image_object.size, (255,255,255,0))
        font_watermark = ImageFont.load_default()
        draw_object = ImageDraw.Draw(text_image_overlay)
        draw_object.text((10,10), text_string_watermark, font=font_watermark, fill=(255,255,255,128))
        overlay = Image.alpha_composite(image_object, text_image_overlay)
        overlay.save(outdir + current_file_name, quality=img_quality)

        print('Processed {} - {} of {}'.format(current_file_name, counter_processed, num_pics))
        counter_processed += 1

    print "\nFinished. \nAnything else?\n"


def apply_filter_frame(indir, outdir, size_frame):
    '''add frame inside image using PILLOW library'''
    picture_list = dir_list(indir)
    counter_processed = 1
    img_quality = 95
    num_pics = len(picture_list)
    for current_file_name in picture_list:
        image_object = Image.open(indir + current_file_name).convert('RGBA')

        draw = ImageDraw.Draw(image_object)
        draw.line((0,0, image_object.size[0],0), fill=0, width=int(size_frame))
        draw.line((0, image_object.size[1],image_object.size[0], image_object.size[1]), fill=0, width=int(size_frame))
        draw.line((0,0,0,image_object.size[1]), fill=0, width=int(size_frame))
        draw.line((image_object.size[0],0, image_object.size[0], image_object.size[1]), fill=0, width=int(size_frame))

        image_object.save(outdir + current_file_name, quality=img_quality)

        print('Processed {} - {} of {}'.format(current_file_name, counter_processed, num_pics))
        counter_processed += 1

    print "\nFinished. \nAnything else?\n"


def filter_images(indir, outdir):

    while True:

        print('''Choose filter:
            (E)nhance contrast,
            (C)olor saturation,
            (S)harpen,
            (D)raw black frame
            (A)dd watermark text
            (R)ETURN TO MENU''')

        filter_choice = raw_input('>: ')

        if filter_choice == 'r' or filter_choice == 'R':
            break

        list_of_choices = {'E','e','C','c','S','s','D','d','A','a'}

        if filter_choice not in list_of_choices:
            print '--Invalid entry, try again...--'
            continue

        if filter_choice == 'a' or filter_choice == 'A':
            print 'enter text for watermark:'
            text_string_watermark = raw_input('>: ')
            apply_filter_watermark(indir + '/', outdir + '/', text_string_watermark)
            continue

        if filter_choice == 'd' or filter_choice == 'D':
            while True:
                print 'enter width of frame in pixel:'
                size_frame = raw_input('>: ')

                try:
                    float(size_frame)
                except ValueError:
                    print "--please enter a real number--"
                    continue
                else:
                    break

            apply_filter_frame(indir + '/', outdir + '/',size_frame)
            continue

        else:
            apply_filter_contrast_color_sharpen(indir + '/', outdir + '/', filter_choice)
            continue


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
            print '--Invalid entry, try again...--'

        break


def pic_parameters(infolder, outfolder):
    '''Select Picture Resolution Parameters'''

    # for 'sizes' only need the width as we will calculate the
    # height based on a percentage to keep the proper aspect ratio when
    # resizing
    while True:

        print('\nChoose action: \n(R)esize, (A)dd Filter or (Q)UIT?')
        pic_operation = raw_input('>: ')
        possible_inputs = {'R','r','A','a'}

        if pic_operation == 'Q' or pic_operation == 'q':
            print "**** quit ****."
            break

        if pic_operation not in possible_inputs:
            print '--Invalid entry, try again...--'
            continue

        if pic_operation == 'r' or pic_operation == 'R':
            resize_images(infolder, outfolder)

        if pic_operation == 'a' or pic_operation == 'A':
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


    print('\n****Your Pictures folder is {}'.format(homedir))
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
        outfolder = raw_input('Destination folder (type S for same):> ')
    if 'S' in outfolder or 's' in outfolder:
        outfolder = infolder

    pic_parameters(infolder, outfolder)


if __name__ == '__main__':
    main()
