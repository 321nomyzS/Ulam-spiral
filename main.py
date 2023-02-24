from PIL import Image
import sieve
import time


def set_pixel(cor, value, primes, image_obj):
    if len(primes) == 0:
        return primes

    if value == primes[0]:
        (x, y) = cor
        image_obj.putpixel((x - 1, y - 1), (0, 0, 0))
        return primes[1:]
    else:
        return primes


def spiral(n, primes, image_obj):
    """
        Function that create Ulam Spiral
        :param n: width or height of result image
        :param primes: list of prime numbers
        :param image_obj: image that we draw on pixels
        :return:
        """
    primes.reverse()
    current_number = n*n
    x, y = 0, -1
    layer = n
    while layer > 0:
        # Calculate movement
        move = [layer, max(layer - 1, 0), max(layer - 1, 0), max(layer - 2, 0)]
        layer -= 2

        # Go down
        for i in range(move[0]):
            y += 1
            primes = set_pixel((x, y), current_number, primes, image_obj)
            current_number -= 1

        # Go right
        for i in range(move[1]):
            x += 1
            primes = set_pixel((x, y), current_number, primes, image_obj)
            current_number -= 1

        # Go up
        for i in range(move[2]):
            y -= 1
            primes = set_pixel((x, y), current_number, primes, image_obj)
            current_number -= 1

        # Go left
        for i in range(move[3]):
            x -= 1
            primes = set_pixel((x, y), current_number, primes, image_obj)
            current_number -= 1


def main():
    N = int(input("Size of ulam spiral: "))
    img = Image.new('RGB', (N, N), color=(255, 255, 255))
    start_time = time.time()
    primes = sieve.sieve_of_eratosthenes(N * N)
    spiral(N, primes, img)
    end_time = time.time()
    print(f"Ulam spiral has been generated in {end_time - start_time} seconds")
    img.save("ulam.png")


if __name__ == "__main__":
    main()
