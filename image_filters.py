# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 20:09:26 2015

@author: neal
"""

from PIL import Image, ImageColor
import os.path

def make_lowres_img():
    img = Image.open("./doges.jpg")
    
    pixel_map = img.load()
    #img = img.convert('1')  #convert to b/w via PIL; uncomment for super-poor quality.
    
    for i in range(img.size[0]):    #threshold each pixel to b/w, no gray
        for j in range(img.size[1]):
            pixel_rgb_sum = pixel_map[i,j][0] + pixel_map[i,j][1] + pixel_map[i,j][2]
            pixel_rgb_sum = pixel_rgb_sum / 3
            pixel_map[i,j] = (pixel_rgb_sum,pixel_rgb_sum,pixel_rgb_sum)
                
    img.save("./gray_doges.jpg")


#make_lowres_img()


"""
kernel = [[-.125, -.125, -.125],
          [-.125, 1.00, -.125],
          [-.125, -.125, -.125]]
"""
k = 5
kernel = [[k/-8., k/-8., k/-8.],
          [k/-8., k+1.,  k/-8.],
          [k/-8., k/-8., k/-8.]]


"""
kernel = [[.125, .125, .125],
          [.125, 1.00, .125],
          [.125, .125, .125]]
"""


"""
kernel = [[0,0,0],
          [0,1,0],
          [0,0,-1]]
"""


"""
kernel = [[1,1,1],
          [1,8,1],
          [1,1,1]]
"""




#kernel_rows = len(kernel)
#kernel_cols = len(kernel[0])

def convolve_image():
    img = Image.open("./doges.jpg")
    
    input_pixel_map = img.load()
    
    output_img = Image.new("RGB", img.size, "black")            
    output_pixel_map = output_img.load()
    
    #print new_pixel_map[100,100]
    
    width, height = img.size
    
    for r in range(2, width):    
        for c in range(2, height):
            for k in range(len(kernel)):
                for j in range(len(kernel[0])):
                                   
                    convoled_pixel = int(output_pixel_map[r,c][0] + kernel[j][k] * input_pixel_map[r-k,c-j][0])
                    if convoled_pixel < 0:
                        convoled_pixel = 0
                    elif convoled_pixel > 255:
                        convoled_pixel = 255
    
                    output_pixel_map[r,c] = convoled_pixel, convoled_pixel, convoled_pixel
                    
                    
    #width, height = img.size            
    output_img.save("./test.jpg")

convolve_image()
#45, 85, 95 is a nice color
