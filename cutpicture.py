from PIL import Image
import os
from pathlib import Path

def get_image_files(path=None):
    if path is None:
        path = Path('./pictures/scanf/')
    result = [ f for f in path.glob('*.jpg') ]
    return result


def cut_one_image(img):
    WIDTH,HEIGHT = img.size
    x1=0
    y1=0
    x2=WIDTH
    y2=int(HEIGHT/2)+2
    im2=img.crop((x1,y1,x2,y2))
    return im2

def cut_all_images(files):
    result = []
    for f in files:
        img=Image.open(f)
        img2=cut_one_image(img)
        img2=img2.transpose(Image.Transpose.ROTATE_270)

        result.append( img2)
    return result

def save_images(images):
    for index,img in enumerate(images):
        fn=Path('.','pictures','cut',str(index)+'.jpg')
        print(fn)
        img.save(fn)


if __name__ == "__main__":
    files=get_image_files()
    result = cut_all_images(files)
    save_images(result)


