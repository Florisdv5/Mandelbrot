import matplotlib.pyplot as plt
import numpy as np

from PIL import Image, ImageDraw

c = complex(2,2)
Z0 = c
Z = Z0

def amount_iter(compl, max_steps, threshold_inf: int = 10):
    c = compl
    z = c
    i = 1
    while (z*z.conjugate()).real < threshold_inf and i < max_steps:
        z = z**2 + c
        i += 1
    return i

amount_iter(0,0.5)

max_steps = 200  # this is equal to i

# Image size (pixels), this is equal to the amount of samples s
X_WIDTH = 2700 * 20
Y_HEIGHT = 1800 * 20

# Plot window
real_minus = -2
real_max = 1
real_dif = real_max - real_minus
imag_minus = -1
imag_max = 1
imag_dif = imag_max - imag_minus

im = Image.new('HSV', (X_WIDTH, Y_HEIGHT), (0, 0, 0))
draw = ImageDraw.Draw(im)
percentage = 0

for pix_x in range(0, X_WIDTH):
    for pix_y in range(0, Y_HEIGHT):
        # Convert pixel coordinate to complex number
        c = complex(real_minus + (pix_x / X_WIDTH) * real_dif,
                    imag_minus + (pix_y / Y_HEIGHT) * imag_dif)
        # Compute the number of iterations
        m = amount_iter(c, max_steps)
        # The color depends on the number of iterations
        hue = int(255 * m / max_steps)
        saturation = 255
        if m < max_steps:
            value = 255
        else:
            value = 0
        # Plot the point
        draw.point([pix_x, pix_y], (hue, saturation, value))
    if percentage != str(round(pix_x / X_WIDTH, 3)*100):
        percentage = str(round(pix_x / X_WIDTH, 3)*100)
        print("Percentage: " + percentage + "%")

im.convert('RGB').save('outputlarge.png', 'PNG')

imgplot = plt.imshow(im.convert('RGB'))
