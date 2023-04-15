from doctest import OutputChecker
from msilib.schema import File
from PIL import Image
import numpy as np

import encrypt_decrypt_func as EDF
import keygen as KG


publickey, privatekey = KG.generate_keys()
print(publickey.__repr__())

im = Image.open("C:\Users\Admin\Downloads\mp\rep.jpg") 
im.show()

encrypt_image = EDF.image_encryption(publickey,im)
EDF.show_encrypted_image(encrypt_image)
inc_bright = EDF.increase_brightness(publickey,encrypt_image,30)
im = EDF.image_decryption(publickey,privatekey,inc_bright)
im.show()