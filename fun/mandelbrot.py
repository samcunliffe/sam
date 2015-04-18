
import numpy as np
from pylab import show, imshow, savefig
from timeit import default_timer as timer


def modsq(z):
    return z.real*z.real + z.imag*z.imag


def mandel(real, imag, max_iters):
    """ Mandelbrot set

    Given the real and imaginary parts of a complex number,
    determine if it is a candidate for membership in the Mandelbrot
    set given a maximum number of iterations.
    """
    c, z = complex(real, imag), 0.0j
    for i in range(max_iters):
        z = z*z + c
        if modsq(z) >= 4:
            return i

    return max_iters


def create_fractal(min_x, max_x, min_y, max_y, image, iters):
    height = image.shape[0]
    width = image.shape[1]

    pixel_size_x = (max_x - min_x) / width
    pixel_size_y = (max_y - min_y) / height

    for x in range(width):
        real = min_x + x * pixel_size_x
        for y in range(height):
            imag = min_y + y * pixel_size_y
            color = mandel(real, imag, iters)
            image[y, x] = color

    return


def main():
    """Make the famous Mandelbrot plot"""
    image = np.zeros((1024, 1536), dtype=np.uint8)
    start = timer()
    create_fractal(-2.0, 1.0, -1.0, 1.0, image, iters=20)
    dt = timer() - start

    print "Mandelbrot created in %f s" % dt
    imshow(image)
    f = show()
    f.savefig("hello.pdf")

    return


if __name__ == "__main__":
    main()
