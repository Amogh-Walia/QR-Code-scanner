#import libraries
import cv2
from pyzbar import pyzbar
# Import QRCode from pyqrcode 
import pyqrcode 
#import png 
from pyqrcode import QRCode 
  
  


def read_barcodes_from_Camera(frame):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y , w, h = barcode.rect
        #1
        barcode_info = barcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)
        
        #2
        font = cv2.FONT_HERSHEY_COMPLEX
        cv2.putText(frame, barcode_info, (x + 6, y - 6), font, 2.0, (0, 255,0), 1)
        #3
        #with open("barcode_result.txt", mode ='w') as file:
            #file.write("Recognized Barcode:" + barcode_info)
    return frame





def main():

    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    #2
    
    while ret:
        ret, frame = camera.read()
        frame = read_barcodes_from_Camera(frame)
        cv2.imshow('Barcode/QR code reader', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    
    #3
    camera.release()
    cv2.destroyAllWindows()

    

main()
    
