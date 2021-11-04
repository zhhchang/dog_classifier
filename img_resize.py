import argparse
import glob
import os.path

import numpy as np
from PIL import Image


parser = argparse.ArgumentParser(description = "Process images to targe resolution")  
parser.add_argument('--width', type=int, default=128, help="output_image_weight") 
parser.add_argument('--length', type=int, default=128, help="output_image_height") 
parser.add_argument('--imgnum', type=int, default=0, help="total_processed_numbers") 
parser.add_argument('--oridir', type=str, default="../data/affenpinscher", help="imput_image_dir") 
parser.add_argument('--outdir', type=str, default="../data_final/affenpinscher", help="output_image_dir")  
 
args = parser.parse_args()
args.graynum = 0
args.imgnum = 0

def convertjpg(jpgfile, outdir, width, length):


    img = Image.open(jpgfile) 
    print(img.mode)

    # if img.mode == 'L':
    #     img = np.stack((np.array(img),)*3, axis=-1)
    #     img = Image.fromarray(img)
    #     args.graynum = args.graynum + 1
        
    try:
        new_img = img.resize((width, length), Image.BILINEAR)
        new_img.save(os.path.join(outdir, os.path.basename(jpgfile))) 
    except Exception as e:
        print(e)


for jpgfile in glob.glob(args.oridir + "/*.jpg"):         
    convertjpg(jpgfile, args.outdir, args.width, args.length)         
    args.imgnum = args.imgnum + 1

print("\n==================================")
print("number of resized images [%d]]" % (args.imgnum))
print("==================================\n")





