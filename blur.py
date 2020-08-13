from PIL import Image
import argparse
import sys
import math
import time

parser = argparse.ArgumentParser(description = 'Program to blur your images')
parser.add_argument('-b', '--blur_factor', metavar='', default=2, type=int, help='How blurred you want your image to be (default: 2).')
parser.add_argument('-o', '--output_path', metavar='', default='output.jpg', type=str, help='Output path of the blurred image (default: output.jpg).')
parser.add_argument('-p', '--progress', default='False', action='store_true', help='Show progress (default: False).')
args, unknown = parser.parse_known_args()


blur_factor = args.blur_factor
output_path = args.output_path
start_time = time.time()
 
try:
        image_path = unknown[-1]
except:
        print("Input image not especified.")
        sys.exit()

try:
        image = Image.open(image_path)
except:
        print("Image %s doesn't exist." % image_path)
        sys.exit()
        
tam = image.size
output = Image.new('RGB', image.size)

length = 2 * blur_factor + 1
length_squared = length ** 2

for y in range(image.size[1]):
        cache_red_sum = 0
        cache_green_sum = 0
        cache_blue_sum = 0
        
        ay = y - blur_factor
        
        for x in range(image.size[0]):
                ax = x - blur_factor

                first_row_red_sum = 0
                first_row_green_sum = 0
                first_row_blue_sum = 0
        
                last_row_red_sum = 0
                last_row_green_sum = 0
                last_row_blue_sum = 0

                for by in range(0, length):
                        try:
                                temp_color = image.getpixel((ax + length - 1, ay + by))
                        except:
                                temp_color = image.getpixel((x, y))
                                
                        last_row_red_sum += temp_color[0]
                        last_row_green_sum += temp_color[1]
                        last_row_blue_sum += temp_color[2]
                
                if x == 0:
                        for bx in range(0, length - 1):
                                for by in range(0, length):
                                        try:
                                                temp_color = image.getpixel((ax + bx, ay + by))
                                        except:
                                                temp_color = image.getpixel((x, y))
                                        
                                        cache_red_sum += temp_color[0]
                                        cache_green_sum += temp_color[1]
                                        cache_blue_sum += temp_color[2]
                                        
                else:
                        for by in range(0, length):
                                try:
                                        temp_color = image.getpixel((ax, ay + by))
                                except:
                                        temp_color = image.getpixel((x, y))
                                                
                                first_row_red_sum += temp_color[0]
                                first_row_green_sum += temp_color[1]
                                first_row_blue_sum += temp_color[2]

                        cache_red_sum += last_row_red_sum - first_row_red_sum
                        cache_green_sum += last_row_green_sum - first_row_green_sum
                        cache_blue_sum += last_row_blue_sum - first_row_blue_sum
                
                
                red_medium = round((cache_red_sum + last_row_red_sum) / length_squared)
                green_medium = round((cache_green_sum + last_row_green_sum) / length_squared)
                blue_medium = round((cache_blue_sum + last_row_blue_sum) / length_squared)
                
                rgb_medium = (red_medium, green_medium, blue_medium)
                
                output.putpixel((x,y), rgb_medium)
                
                if args.progress == True:
                        print('Completed %s' % str(100*i/(image.size[0]*image.size[1])), '%', end="\r")
        
if args.progress == True:
        print('                                ', end="\r")
        print('Completed 100%. ', end="")
        
output.save(output_path)

end_time = time.time()
print("Took %s seconds" % str(int(end_time)-int(start_time)))
