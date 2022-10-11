import sys
import numpy
import imageio

# RLE (Run Length Encoding) is a simple compression algorithm that
# compresses a string of characters into a string of pairs of
# character and count.
class RLE:
    message = ''
    
    def str_encode(data=""):
        """
        Encodes a string using RLE method (run length encoding).
        `data` is the string to encode.
        """
        if data == "":
            data = RLE.message
        
        if any(x.isdigit() for x in data):
            raise ValueError("Data cannot contain digits.")
        elif len(data) == 0:
            raise ValueError("Data cannot be empty.")
        
        encoded = ""
        count = 1
        for i in range(len(data)):
            if i == len(data) - 1:
                encoded += str(count) + data[i]
            elif data[i] == data[i + 1]:
                count += 1
            else:
                if count == 1:
                    encoded += data[i]
                else:
                    encoded += str(count) + data[i]
                count = 1
 
        RLE.message = encoded
        return encoded

    def str_decode(data=""):
        """
        Decodes a string using RLE.
        """
        if data == "":
            data = RLE.message
        
        decoded = ""
        count = ""
        for i in range(len(data)):
            if data[i].isdigit():
                count += data[i]
            else:
                if count == "":
                    decoded += data[i]
                else:
                    decoded += int(count) * data[i]
                count = ""
        return decoded
    
    def print(only_size=False):
        if only_size:
            if type(RLE.message) == str:
                for i in range(RLE.message[:20]):
                    print(i, end='')
            elif type(RLE.message) == numpy.ndarray:
                print(RLE.message)
        print(f'...\n[*] Size of data is {sys.getsizeof(RLE.message)} bytes')
        
    def encode(data=[]):
        """
        Encodes a string using RLE method (run length encoding).
        `data` is the ndarray with shape (height, width, 4) of the image to encode.
        """
        if data == []:
            data = RLE.message
        
        print(data.shape)
        length, width = data.shape[:2]
        if length == 0:
            raise ValueError("Data cannot be empty.")
        
        encoded = []
        count = 1
        for value in data:
            for index in range(width):
                print(value[index])
                if index == width - 1:
                    encoded.append(str(count) + value[index])
                elif value[index].all() == value[index + 1].all():
                    count += 1
                else:
                    if count == 1:
                        encoded.append(value[index])
                    else:
                        encoded.append(str(count) + value[index])
                    count = 1

        return encoded


    def decode(data=""):
        """
        Decodes a string using RLE.
        """
        if data == "":
            data = RLE.message
        
        decoded = ""
        count = ""
        for i in range(len(data)):
            if data[i].isdigit():
                count += data[i]
            else:
                if count == "":
                    decoded += data[i]
                else:
                    decoded += int(count) * data[i]
                count = ""
        return decoded
        

if __name__ == "__main__":
    message = "Hellllllo Woooooorlddddddd!"
    RLE.str_encode(message)
    assert RLE.str_decode() == message
    
    # encode an image
    image = imageio.imread('https://upload.wikimedia.org/wikipedia/commons/7/7d/Dog_face.png')
    # check the size of the image
    print(f'[*] Size of image is {sys.getsizeof(image)} bytes')
    # encode the image
    RLE.encode(image)
    # check the size of the encoded image
    RLE.print(only_size=True)
    
    # decode the image
    RLE.decode()
    # check the size of the decoded image
    RLE.print(only_size=True)
    
    # check if the decoded image is the same as the original image
    assert RLE.message.all() == image.all()
    