import pyscreenshot as ImageGrab
from PIL import Image as img

RESET = '\033[0m'
def get_color_escape(r, g, b, background=False):
    return '\033[{};2;{};{};{}m'.format(48 if background else 38, r, g, b)

im = ImageGrab.grab(bbox=(20, 740, 22, 742))  # X1,Y1,X2,Y2

im.save('pixels.png')

imagen = img.open('pixels.png')
pix = imagen.load()
value1=hex(pix[1,1][0]).replace('0x','')
value2=hex(pix[1,1][1]).replace('0x','')
value3=hex(pix[1,1][2]).replace('0x','')

v1 = pix[1,1][0]
v2 = pix[1,1][1]
v3 = pix[1,1][2]

rgb = '#'+value1+value2+value3
print(rgb)

print(get_color_escape(v1+30, v2+30, v3+30) 
      + get_color_escape(v1, v2, v3, True)
      + 'Fancy colors!' 
      + RESET)
