import numpy as np
import cv2 as cv
import random

# general parameters
width = 900
height = 600
n_trees = 10
ground_level = height-100

# colours
green, light_green, brown = (40, 185, 40), (25, 220, 0), (30, 65, 155)

# blank image
bg = np.zeros((height, width, 3), dtype=np.uint8)

# draw background
cv.rectangle(bg, (width, 0), (0, ground_level), (255, 225, 95), -1)
cv.rectangle(bg, (width, ground_level), (0, height), green, -1)

# ***************


class Tree:
    def __init__(self, image):
        self.scale = int(np.random.choice(range(1, 4)))
        self.img = image
        self.loc = int(np.random.choice(range(1, 900)))
        self.height = 100 * self.scale
        self.radius = 50

    def draw(self):
        small_radius = (self.radius-20) * self.scale



        # params (image, start_line_position, end_line_position, color, thickness)
        cv.line(self.img, (self.loc, ground_level), (self.loc, ground_level-self.height), (0, 0, 0), 13*self.scale)  # Black contour for the main line
        cv.line(self.img, (self.loc, ground_level-25*self.scale), (self.loc-30*self.scale, ground_level-self.height+50), (0, 0, 0), 8*self.scale)  # Black contour for the left branch
        cv.line(self.img, (self.loc, ground_level-25*self.scale), (self.loc+30*self.scale, ground_level-self.height+50), (0, 0, 0), 8*self.scale)  # Black contour for the right branch

        cv.line(self.img, (self.loc, ground_level), (self.loc, ground_level-self.height), brown, 10*self.scale)
        cv.line(self.img, (self.loc, ground_level-25*self.scale), (self.loc-30*self.scale, ground_level-self.height+50), brown, 5*self.scale)
        cv.line(self.img, (self.loc, ground_level-25*self.scale), (self.loc+30*self.scale, ground_level-self.height+50), brown, 5*self.scale)

        cv.circle(self.img, (self.loc-30*self.scale, ground_level-self.height+50), small_radius, (0, 0, 0), 3)
        cv.circle(self.img, (self.loc+30*self.scale, ground_level-self.height+50), small_radius, (0, 0, 0), 3)

        cv.circle(self.img, (self.loc-30*self.scale, ground_level-self.height+50), small_radius, green, -1)
        cv.circle(self.img, (self.loc+30*self.scale, ground_level-self.height+50), small_radius, green, -1)

        cv.circle(self.img, (self.loc, ground_level-self.height), small_radius+40, (0, 0, 0), 3)
        cv.circle(self.img, (self.loc, ground_level-self.height), small_radius+40, green, -1)

        return self.img


# ***************

# display image
for i in range(n_trees):
    img = Tree(bg).draw()
cv.imshow('forest of objects', img)

cv.waitKey(0)
cv.destroyAllWindows()