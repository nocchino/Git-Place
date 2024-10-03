from PIL import Image

def check_first_white_px(width, height):
    for y in range(height):
        for x in range(width):
            if pixelMap[x, y] == (255, 255, 255):
                return (x, y)


canvas=Image.open("image.png")

pixelMap=canvas.load()
width, height = canvas.size

print(check_first_white_px(width, height))

'''
the program will tell you the first white pixel to draw like (0,1) or (43,466)
now in the canvas.putpixel right below change the coordinates and the color.
REMEMBER: the coordinates are (x, y) and the color is (r, g, b) 
where r, g, b are the values of the color you want to draw

'''
canvas.putpixel((0,0),(0,0,0))

'''
when you are done with the changes, uncomment the line 
below and run the program again to see the changes on the image.png
'''

#canvas.save("image.png")
        

