import matplotlib.pyplot as plt


def display_image(img):
    plt.ion()
    artist = plt.imshow(img)
    plt.show()
    return artist


def update_image(disp, array):
    disp.set_array(array)
    plt.draw()


def clean_image():
    plt.clf()
