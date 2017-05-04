#!/usr/bin/env python

import sys
ImportPath = '/data/DeepLearningForTraining/UMDFaces/umdfaces2VOC2007-master'
sys.path.append(ImportPath)

from tool_csv import loadCSVFile
from tool_lxml import createXML
import cv2
import os
from skimage import data_dir,io,transform,color
import numpy as np


number_file = 3
base_number = [0,3000000,3167878,3286085]
FILEDIR = "/data/DeepLearningForTraining/UMDFaces/umdfaces_batch%s/"%number_file         #
IMGSTORE = "/data/DeepLearningForTraining/UMDFaces/VOC2007/JPEGImages/"
FILENAME = "umdfaces_batch%s_ultraface.csv"%number_file               #
ANNOTATIONDIR ='/data/DeepLearningForTraining/UMDFaces/VOC2007/Annotations/'


if __name__ == "__main__":
    csv_content = loadCSVFile( FILEDIR + FILENAME)
    cvs_content_part = csv_content[1:,1:10]
    i=1
    base=base_number[number_file]                                         #
    limit = 1000000                                       #
    Wrong_Pic = []
#    info = cvs_content_part[0]
    for info in cvs_content_part:
        try:
            if i==limit:
                print "Reach Limit, Stop..."
                break
    
            print "Process No." + str(i) + " Data...."
    
            str_splite = '/'
            str_spilte_list = str(info[0]).split(str_splite)
    
            jpg_path = info[0]
            #jpg_file = str_spilte_list[len(str_spilte_list)-1]
            jpg_file = str(base+i)+'.jpg'
            # os.system('cp '+ FILEDIR+jpg_path + ' ' + IMGSTORE+jpg_file)
            
            img = cv2.imread(FILEDIR+jpg_path)
            cv2.imwrite(IMGSTORE+jpg_file,img,[int(cv2.IMWRITE_JPEG_QUALITY),95])
            sp = img.shape
            #print sp
            height = sp[0]                 #height(rows) of image
            width = sp[1]                  #width(colums) of image
            depth = sp[2]                  #the pixels value is made up of three primary colors
            #print 'width: %d \nheight: %d \nnumber: %d' %(width,height,depth)
    
            xmin = int(float(info[3]))
            ymin = int(float(info[4]))
            xmax = int(float(info[3])+float(info[5]))
            ymax = int(float(info[4])+float(info[6]))
            #print 'xmin: %d \nymin: %d \nxmax: %d \nymax: %d' %(xmin,ymin,xmax,ymax)
    
            transf = dict()
            transf['folder'] = "FACE2016"
            transf['filename'] = jpg_file
            transf['width'] = str(width)
            transf['height'] = str(height)
            transf['depth'] = str(depth)
            transf['xmin'] = str(xmin)
            transf['ymin'] = str(ymin)
            transf['xmax'] = str(xmax)
            transf['ymax'] = str(ymax)
    
            print "Create No." + str(base+i) + " XML...."
            createXML(transf,ANNOTATIONDIR)
            i = i + 1
            #print jpg_path, jpg_file
            #jpg
            
        except:
            if i==limit:
                print "Reach Limit, Stop..."
                break
    
            print "Process No." + str(base+i) + " Data...."
    
            str_splite = '/'
            str_spilte_list = str(info[0]).split(str_splite)
    
            jpg_path = info[0]
            #jpg_file = str_spilte_list[len(str_spilte_list)-1]
    
            Wrong_Pic.append(FILEDIR+jpg_path)
            i = i + 1
    print "Done..."

    