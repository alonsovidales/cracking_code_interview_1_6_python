# Given an image represented by an NxN matrix, where each pixel in the image is 4
# bytes, write a method to rotate the image by 90 degrees. Can you do this in place?

def rorate_img(img):
    new_img = []
    for i in xrange(len(img)):
        new_img.append([0]*len(img))

    for x in xrange(len(img)):
        for y in xrange(len(img)):
            new_img[y][len(img)-x-1] = img[x][y]

    return new_img

# For the implace the same but using 4 vars to store the data and rotate the 4
# at once, iterate only until x/2 and y/2

result = rorate_img([
    [(1, 1, 1), (2, 2, 2), (3, 3, 3), (4, 4, 4)],
    [(5, 5, 5), (6, 6, 6), (7, 7, 7), (8, 8, 8)],
    [(9, 9, 9), (10, 10, 10), (11, 11, 11), (12, 12, 12)],
    [(13, 13, 13), (14, 14, 14), (15, 15, 15), (16, 16, 16)],
])

for l in result:
    print l
