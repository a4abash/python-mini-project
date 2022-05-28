import pyqrcode
from pyqrcode import QRCode

# after running the code please check related folder for qr code

s = 'http://abashshah.com.np' # Your destination link you want to redirect  goes here
url = pyqrcode.create(s)
url.svg("qr.svg",scale = 8)
