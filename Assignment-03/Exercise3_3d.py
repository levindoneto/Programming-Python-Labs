# ASCII art
# each character = single Pixel
# multiple lines in which some pixels are filled and some not
# make an image
# D and H shown in ASCII art

# single line 20 characters long (line width)
# dot. for an empty pixel
# # for a full pixel

linewidth = 20
empty = "."
full = "#"


def rect(x,y,z):
    for i in range (0,linewidth):
        s = ""
        for n in range (0, linewidth):
            if (i >= y) & (i < (x + y)):
                if (n >= z) & (n < (x + z)):
                    s = s + full
                else:
                    s = s + empty
            else:
                s = s + empty          
        print(s)

rect(4,6,3)

