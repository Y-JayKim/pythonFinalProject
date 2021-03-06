import os
import sys
sys.path.append('C:/Python/Python36-32/Lib/site-packages/cv2')
import cv2
import numpy
import zbar
import time
import threading
import Tkinter
from multiprocessing import Process, Queue
from Queue import Empty
from PIL import Image, ImageTk

class BarCodeScanner(threading.Thread, Tkinter.Toplevel):
    def __init__(self):
        threading.Thread.__init__(self)
        #self.WINDOW_NAME = 'Camera'
        self.CV_SYSTEM_CACHE_CNT = 5 # Cv has 5-frame cache
        self.LOOP_INTERVAL_TIME = 0.2
        #cv.NamedWindow(self.WINDOW_NAME, cv.CV_WINDOW_NORMAL)
        self.cam = cv2.VideoCapture(-1)
        # check if webcam device is free
        self.proceede = self.cam.isOpened()
        if not self.proceede:
            return
        self.confirm = 0

    def scan(self, aframe):
        imgray = cv2.cvtColor(aframe, cv2.COLOR_BGR2GRAY)
        raw = str(imgray.data)
        scanner = zbar.ImageScanner()
        scanner.parse_config('enable')
        width = int(self.cam.get(cv.CV_CAP_PROP_FRAME_WIDTH))
        height = int(self.cam.get(cv.CV_CAP_PROP_FRAME_HEIGHT))
        imageZbar = zbar.Image(width, height,'Y800', raw)
        scanner.scan(imageZbar)
        for symbol in imageZbar:
            print('decoded', symbol.type, 'symbol', '"%s"' % symbol.data)
            return symbol.data

    def run(self):
        if not self.proceede:
            return
        def show_frame():
            _, img = self.cam.read()
            img = cv2.flip(img,1)
            cv2image = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)
            img = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(image=img)
            img_label.imgtk = imgtk
            img_label.configure(image=imgtk)
            video_window.after(250, show_frame)

        def destroy_video_window():
            self.cam.release()
            video_window.destroy()

        # Toplevel GUI
        video_window = Tkinter.Toplevel()
        video_window.title('QR Scan !!')
        img_label = Tkinter.Label(video_window)
        img_label.pack(side=Tkinter.TOP)
        close_button = Tkinter.Button(video_window, text='close', command = destroy_video_window)
        close_button.pack(side=Tkinter.RIGHT)
        show_frame()

        self.datalst = []
        print('BarCodeScanner run', time.time())
        while True:
            for i in range(0,self.CV_SYSTEM_CACHE_CNT):
                self.cam.read()
            img = self.cam.read()
            self.data = self.scan(img[1])
            time.sleep(self.LOOP_INTERVAL_TIME)
            if self.data:
                self.datalst.append(self.data)
            if len(self.datalst) == 2 and len(set(self.datalst)) <= 1:
                video_window.destroy()
                break
        self.cam.release()

def main():
    root = Tkinter.Tk()
    button_scanQr = Tkinter.Button(root, text='QR Scan', command=scaner)
    button_scanQr.pack()
    root.mainloop()

def scaner():
    scanner = BarCodeScanner()
    scanner.start()


if __name__ == '__main__':
    main()