#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 13:00:05 2018

@author: ankith
"""


import os
import cv2
from lxml import etree
import xml.etree.cElementTree as ET


def write_xml(folder, imgPath, imgName, objects, tl, br, savedir):
    if not os.path.isdir(savedir):
        os.mkdir(savedir)

    image = cv2.imread(imgPath)
    height, width, depth = image.shape

    annotation = ET.Element('annotation')
    ET.SubElement(annotation, 'folder').text = folder
    ET.SubElement(annotation, 'filename').text = imgName
    source = ET.SubElement(annotation, 'source')
    ET.SubElement(source, 'database').text = 'Unknown'
    size = ET.SubElement(annotation, 'size')
    ET.SubElement(size, 'width').text = str(width)
    ET.SubElement(size, 'height').text = str(height)
    ET.SubElement(size, 'depth').text = str(depth)
    ET.SubElement(annotation, 'segmented').text = '0'
    for obj, topl, botr in zip(objects, tl, br):
        ob = ET.SubElement(annotation, 'object')
        ET.SubElement(ob, 'name').text = obj
        ET.SubElement(ob, 'pose').text = 'Unspecified'
        ET.SubElement(ob, 'truncated').text = '0'
        ET.SubElement(ob, 'difficult').text = '0'
        bbox = ET.SubElement(ob, 'bndbox')
        ET.SubElement(bbox, 'xmin').text = str(tl[0])
        ET.SubElement(bbox, 'ymin').text = str(tl[1])
        ET.SubElement(bbox, 'xmax').text = str(br[0])
        ET.SubElement(bbox, 'ymax').text = str(br[1])

    xml_str = ET.tostring(annotation)
    root = etree.fromstring(xml_str)
    xml_str = etree.tostring(root, pretty_print=True)
    save_path = os.path.join(savedir, imgName.replace('jpg', 'xml'))
    with open(save_path, 'wb') as temp_xml:
        temp_xml.write(xml_str)

