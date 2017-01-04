
from PIL import Image

if __name__=="__main__":
    #used docs here: https://pillow.readthedocs.io/en/4.0.x/reference/Image.html
    #and example here: https://en.wikibooks.org/wiki/Python_Imaging_Library/Editing_Pixels

    #here we load the random nums in "random_nums.txt"
    with open("random_nums.txt", "r") as f:
        lines = f.read()
        lines = lines.split("\n")
        #print(lines)
        lines.pop()

    #I realize that a set would be more efficient here as we don't have a need for order as a list gives us
    #However, I had some technical difficulties putting all of the elements in a set, and since popping elements
    #from a list is O(1) and this is a timed exercise, I decided to stick with it

    lines = [int(i) for i in lines]

    img = Image.new('RGB', (128,128), "black") #just initalize the Image
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r = lines.pop()
            g = lines.pop()
            b = lines.pop()
            pixels[i,j] = (r,g,b)

    img.save('pic.bmp')
