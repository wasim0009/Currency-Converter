import qrcode
from PIL import Image 

qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.ERROR_CORRECT_H,
                 box_size=10,border=4) 

qr.add_data("https://instagram.com/wasim_khan_0009?igshid=MzNlNGNkZWQ4Mg==")
qr.make(fit=True)
Image=qr.make_image(fill_color='red')
Image.save("image.png")