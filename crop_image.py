from PIL import Image
from time import sleep

def crop_image(input_image, output_image, start_x, start_y, width, height):
    input_img = Image.open(input_image)
    box = (start_x, start_y, start_x + width, start_y + height)
    output_img = input_img.crop(box)
    output_img.save(output_image +".png")

def main():
    file_name = "forest1.png" #file name 
    im = Image.open(file_name)
    i_width, i_height = im.size
    h_limit = i_height - 101
    w_limit = i_width - 101
	
    for a in range(0,h_limit,10):
        for b in range(0,w_limit, 10):
            crop_image(file_name,"cropped"+str(a)+"-"+str(b), b,a,100,100)
            sleep(0.1)
        sleep(2)
    


if __name__ == '__main__': main()
