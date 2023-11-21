from bitstring import BitArray
from PIL import Image

LSB_PAYLOAD_LENGTH_BITS = 32

def obfuscate(data, input_file, output_file):
    data = BitArray(uint=len(data) * 8, length=LSB_PAYLOAD_LENGTH_BITS).bin + BitArray(bytes=data).bin
    i = 0

    try:
        with Image.open(input_file) as img:
            width, height = img.size
            if len(data) > width * height * 3:
                print("Data too large! Data contains {} bytes, maximum is {}".format(
                    int(len(data) / 8), int(width * height * 3 / 8)))
                exit(1)

            for x in range(0, width):
                for y in range(0, height):
                    pixel = list(img.getpixel((x, y)))
                    for n in range(0, 3):
                        if i < len(data):
                            pixel[n] = pixel[n] & ~1 | int(data[i])
                            i += 1
                    img.putpixel((x, y), tuple(pixel))
                    if i >= len(data):
                        break
                if i >= len(data):
                    break

            img.save(output_file, "png")

    except IOError:
        print("Could not open {}".format(input_file))
        exit(1)
    print("Data hidden in {}".format(output_file))


argument1 = "testest"
argument2 = "Spectacular-landscape.png"
argument3 = "new_image.png"
data = argument1.encode()
input_file = argument2.encode()
output_file = argument3.encode()


obfuscate(data, input_file, output_file)