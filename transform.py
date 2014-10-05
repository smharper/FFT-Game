import numpy as np
from numpy.fft import fftn, ifftn, fftshift


def transform(img, res):
    #TODO exception if res > 1

    # Perform FFT
    img = fftn(img, axes=(0, 1))

    # Shift the quadrants around so that the FFT is zero centered.
    img = fftshift(img, axes=(0, 1))

    # Filter out high frequency information.
    lim = int(0.5 * (1.0 - res) * img.shape[0])
    img[:lim, :, :] = 0.0
    img[img.shape[0]-lim:, :, :] = 0.0

    lim = int(0.5 * (1.0 - res) * img.shape[1])
    img[:, :lim, :] = 0.0
    img[:, img.shape[1]-lim:, :] = 0.0

    # Undo the shift and then perform the inverse FFT.
    img = fftshift(img, axes=(0, 1))
    img = ifftn(img, axes=(0, 1))

    # Return the transformed image.
    return np.real(img)
