#import libraries
import cv2
from pyzbar import pyzbar
# Import QRCode from pyqrcode 
import pyqrcode 
import png 
from pyqrcode import QRCode 
  
  
def generateQR(data,filename):
    

  
    # Generate QR code  
    url = pyqrcode.create(data) 
  
    # Create and save the png file naming "myqr.png" 
    url.png(filename+'.png', scale = 6) 


def read_barcodes_from_Camera(frame):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y , w, h = barcode.rect
        #1
        barcode_info = barcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y),(x+w, y+h), (0, 255, 0), 2)
        
        #2
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, barcode_info, (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)
        #3
        #with open("barcode_result.txt", mode ='w') as file:
            #file.write("Recognized Barcode:" + barcode_info)
    return frame

def read_barcode_from_memory(frame):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        x, y , w, h = barcode.rect
        #1
        barcode_info = barcode.data.decode('utf-8')
        #3
        with open("barcode_result.txt", mode ='w') as file:
            file.write("Recognized Barcode:" + barcode_info)
    return frame



def main():
    print(1)
    t = input("Enter the data")
    generateQR(t,"myqr")
    print(1)
    #1
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

    

    '''
    img = cv2.imread("myqr.png")
    print(1)
    read_barcode_from_memory(img)
    print(1)
    '''
#4
if __name__ == '__main__':
    print('lol')
    main()
    
