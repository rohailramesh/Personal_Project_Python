import pyqrcode
from pyqrcode import QRCode

string = 'https://www.rohailramesh.co.uk/'
URL = pyqrcode.create(string)
URL.png('Website_QR_Code.png', scale=8)