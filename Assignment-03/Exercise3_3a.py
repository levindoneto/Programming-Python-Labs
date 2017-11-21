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


def fullPixelDiagonal():
    counter = 0
    for i in range (0,linewidth):
        s = ""
        for n in range (0, linewidth):
            if counter == n:
                s = s + full
            else:
                s = s + empty          
        print(s)
        counter = counter + 1

fullPixelDiagonal()


### Exercise: Please write a function
### that produces a diagonal line, from
### top left to bottom right.
    
