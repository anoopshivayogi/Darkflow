import os
from os import walk
from PIL import Image
from shutil import copyfile
from xml_makerAnk import write_xml

inputpath = "license_plate2"
outpath = "annotations"
cls_id = 0
mypath = "/home/ankith/XMLMaker/license_plate2/"
# Get files in the inputpath
txt_name_list = []
for (dirpath, dirnames, filenames) in walk(mypath):
    txt_name_list.extend(filenames)
    break
for txt_name in txt_name_list:
    txt_path = mypath + txt_name
    txt_file = open(txt_path, "r")
    
    lines = txt_file.read().split('\n') 
    
    t = int(lines[0]) # t contains how many bounding boxes in an image
    
    if len(lines) != 2:
           
        """ Open output text files """
        txt_outpath = outpath + txt_name
        print("Output:" + txt_outpath)
     
        for i in range(1,t+1):
            line = lines[i].split(" ")
            xmin = line[0]
            xmax = line[2]
            ymax = line[1]
            ymin = line[3]
            img_name = os.path.splitext(txt_name)[0] + ".jpg"
            img_path = "/home/ankith/XMLMaker/Images/" + img_name
            
            #img_path = [im for im in os.scandir('Images/001')][i]
             
            print('Path image ' ,img_path)
            #img=Image.open(img_path)
            #img =  [im for im in os.scandir('Images/001')][i]
            #w= int(im.size[0])
            #h= int(im.size[1])
            #print(w, h)
            tl = (xmin,ymax)
            br = (xmax,ymin)
            objects = ['plate']
            write_xml(inputpath, img_path, img_name, objects, tl, br, outpath)
            #txt_outfile.write(" ".join(tl)+" "+" ".join(br)+" "+img_path)
        
        
        #dst_path = "/home/ankith/Downloads/BBox-Label-Tool-master/Images/001_new/" + os.path.splitext(txt_name)[0] + ".jpg"
        #copyfile(img_path, dst_path )
