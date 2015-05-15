from PIL import Image
import time

new_width = '1024'

image_object = Image.open('/home/al/Pictures/in/IMG_5701.JPG')
new_width = int(new_width)
print('New Width - {}'.format(new_width))
size_percentage = (new_width / float(image_object.size[0]))
print('Size percentage {}'.format(size_percentage))
print float(image_object.size[0])
new_height = int((float(image_object.size[1]) * float(size_percentage)))
print('New Height - {}'.format(new_height))
image_object.resize((new_width, new_height), Image.ANTIALIAS)
time.sleep(3)
image_object.save('/home/al/Pictures/out/IMG_5701.JPG')

