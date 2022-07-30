# Data Generation
# A simple GUI that can be used to quickly sort images into
# eight 45 degree segments around a unit circle.
# Additional functions provided for ROI finding, shuffling
# all images in a directory, and bordering images to allow
# for cases when the ROI is toward the edges of an image.

import cv2 as cv
import numpy as np
import os
import random

from future.moves import tkinter
from PIL import Image, ImageTk

class GUI:
    def __init__(self):
        self.dirName = ''
        self.prevDirName = ''
        self.fullFileName = ''
        self.prevFileName = ''
        self.fileName = ''
        self.crosshairs = True

        # root window for displaying objects
        self.root = tkinter.Tk()
        self.content = tkinter.Frame(self.root)

    def setDirName(self, dirName):
        self.dirName = dirName

    def moveFile0to45(self):
        #print('0 to 45')
        self.prevFileName = self.fileName
        os.rename(self.fullFileName, 'C:/Users/green/Pictures/DATA/split_dataset/0to45/' + self.fileName)
        self.prevDirName = 'C:/Users/green/Pictures/DATA/split_dataset/0to45/'
        self.refreshImage()

    def moveFile45to90(self):
        #print('45 to 90')
        self.prevFileName = self.fileName
        os.rename(self.fullFileName, 'C:/Users/green/Pictures/DATA/split_dataset/45to90/' + self.fileName)
        self.prevDirName = 'C:/Users/green/Pictures/DATA/split_dataset/45to90/'
        self.refreshImage()

    def moveFile90to135(self):
        #print('90 to 135')
        self.prevFileName = self.fileName
        os.rename(self.fullFileName, 'C:/Users/green/Pictures/DATA/split_dataset/90to135/' + self.fileName)
        self.prevDirName = 'C:/Users/green/Pictures/DATA/split_dataset/90to135/'
        self.refreshImage()

    def moveFile135to180(self):
        #print('135 to 180')
        self.prevFileName = self.fileName
        os.rename(self.fullFileName, 'C:/Users/green/Pictures/DATA/split_dataset/135to180/' + self.fileName)
        self.prevDirName = 'C:/Users/green/Pictures/DATA/split_dataset/135to180/'
        self.refreshImage()

    def moveFile180to225(self):
        #print('180 to 225')
        self.prevFileName = self.fileName
        os.rename(self.fullFileName, 'C:/Users/green/Pictures/DATA/split_dataset/180to225/' + self.fileName)
        self.prevDirName = 'C:/Users/green/Pictures/DATA/split_dataset/180to225/'
        self.refreshImage()

    def moveFile225to270(self):
        #print('225 to 270')
        self.prevFileName = self.fileName
        os.rename(self.fullFileName, 'C:/Users/green/Pictures/DATA/split_dataset/225to270/' + self.fileName)
        self.prevDirName = 'C:/Users/green/Pictures/DATA/split_dataset/225to270/'
        self.refreshImage()

    def moveFile270to315(self):
        #print('270 to 315')
        self.prevFileName = self.fileName
        os.rename(self.fullFileName, 'C:/Users/green/Pictures/DATA/split_dataset/270to315/' + self.fileName)
        self.prevDirName = 'C:/Users/green/Pictures/DATA/split_dataset/270to315/'
        self.refreshImage()

    def moveFile315to360(self):
        #print('315 to 360')
        self.prevFileName = self.fileName
        os.rename(self.fullFileName, 'C:/Users/green/Pictures/DATA/split_dataset/315to360/' + self.fileName)
        self.prevDirName = 'C:/Users/green/Pictures/DATA/split_dataset/315to360/'
        self.refreshImage()

    def moveFileBadImage(self):
        #print('bad image')
        self.prevFileName = self.fileName
        os.rename(self.fullFileName, 'C:/Users/green/Pictures/DATA/bad_images/' + self.fileName)
        self.prevDirName = 'C:/Users/green/Pictures/DATA/bad_images/'
        self.refreshImage()

    def showCrosshairs(self):
        #print('show crosshairs')
        if self.crosshairs:
            self.crosshairs = False
        else:
            self.crosshairs = True

        self.refreshImage()

    def undo(self):
        os.rename(self.prevDirName + self.prevFileName, 'C:/Users/green/Pictures/DATA/roi_dataset/' + self.prevFileName)
        self.refreshImage()

    def refreshImage(self):
        self.fileName = os.listdir(self.dirName)[0]
        self.fullFileName = self.dirName + os.listdir(self.dirName)[0]
        self.img = cv.imread(self.fullFileName)  # store original image
        self.imgDraw = self.img.copy()  # cloned image for drawing purposes

        if self.crosshairs:
            buttonCross = tkinter.Button(self.content, text='Hide Crosshairs', command=self.showCrosshairs)

            height = self.imgDraw.shape[0]
            width = self.imgDraw.shape[1]

            cv.line(self.imgDraw, (0, 100), (width, 100), (255, 100, 0), 2)
            cv.line(self.imgDraw, (100, 0), (100, height), (255, 100, 0), 2)
            cv.line(self.imgDraw, (0, 0), (width, height), (255, 100, 0), 2)
            cv.line(self.imgDraw, (width, 0), (0, height), (255, 100, 0), 2)

            # BGR
            cv.circle(self.imgDraw, (150, 10), 7, (0, 0, 255), -1)
            cv.circle(self.imgDraw, (190, 60), 7, (0, 130, 255), -1)
            cv.circle(self.imgDraw, (190, 150), 7, (0, 255, 255), -1)
            cv.circle(self.imgDraw, (150, 190), 7, (50, 200, 50), -1)
            cv.circle(self.imgDraw, (50, 190), 7, (255, 0, 0), -1)
            cv.circle(self.imgDraw, (10, 150), 7, (150, 50, 150), -1)
            cv.circle(self.imgDraw, (10, 60), 7, (0, 75, 160), -1)
            cv.circle(self.imgDraw, (50, 10), 7, (150, 150, 255), -1)
        else:
            self.imgDraw = self.img
            buttonCross = tkinter.Button(self.content, text='Show Crosshairs', command=self.showCrosshairs)

        # rearrange the color channel
        b, g, r = cv.split(self.imgDraw)
        self.imgDraw = cv.merge((r, g, b))

        # scale the display image
        resized = cv.resize(self.imgDraw, (400, 400), interpolation = cv.INTER_AREA)

        # convert the Image object into a TkPhoto object
        im = Image.fromarray(resized)
        self.imgtk = ImageTk.PhotoImage(image=im)

        image = tkinter.Label(self.content, image=self.imgtk)

        image.grid(column=0, row=0, columnspan=2, rowspan=2, padx=20, pady=20)
        buttonCross.grid(column=2, row=0, padx=20)

        imageLabel = tkinter.Label(self.content, text=self.fullFileName)
        imageLabel.grid(column=0, row=10)

    def startGUI(self):
        self.content.grid(column=0, row=0)

        # define widgets
        button1 = tkinter.Button(self.content, text='0 to 45', command=self.moveFile0to45, bg='red')
        button2 = tkinter.Button(self.content, text='45 to 90', command=self.moveFile45to90, bg='orange')
        button3 = tkinter.Button(self.content, text='90 to 135', command=self.moveFile90to135, bg='yellow')
        button4 = tkinter.Button(self.content, text='135 to 180', command=self.moveFile135to180, bg='green')
        button5 = tkinter.Button(self.content, text='180 to 225', command=self.moveFile180to225, bg='blue')
        button6 = tkinter.Button(self.content, text='225 to 270', command=self.moveFile225to270, bg='purple')
        button7 = tkinter.Button(self.content, text='270 to 315', command=self.moveFile270to315, bg='brown')
        button8 = tkinter.Button(self.content, text='315 to 360', command=self.moveFile315to360, bg='pink')
        button9 = tkinter.Button(self.content, text='Bad Image', command=self.moveFileBadImage)
        buttonUndo = tkinter.Button(self.content, text='Undo', command=self.undo)

        # put all widgets in the display window
        buttonUndo.grid(column=2, row=1)
        button1.grid(column=0, row=3, pady=20)
        button2.grid(column=0, row=4, pady=20)
        button3.grid(column=0, row=5, pady=20)
        button4.grid(column=0, row=6, pady=20)
        button5.grid(column=1, row=3)
        button6.grid(column=1, row=4)
        button7.grid(column=1, row=5)
        button8.grid(column=1, row=6)
        button9.grid(column=2, row=3)

        self.refreshImage()

        self.root.title("Data Organizer")
        self.root.mainloop()  # Start the GUI

    def findROI(self, dirNameIn, dirNameOut, write):
        directory = os.fsencode(dirNameIn)
        targets = []
        tgt_count = 1
        for file in os.listdir(directory):
            fileName = str(dirNameIn) + str(os.fsdecode(file))
            img = cv.imread(fileName) # store original image
            imgDraw = img.copy() # cloned image for drawing purposes

            dilation_size = 5
            erosion_size = 3

            erosion_element = cv.getStructuringElement(cv.MORPH_RECT, (erosion_size, erosion_size))
            dilation_element = cv.getStructuringElement(cv.MORPH_RECT, (dilation_size, dilation_size))

            eroded = cv.erode(imgDraw, erosion_element, iterations = 1)

            # cv.imshow("Eroded", eroded)
            # cv.waitKey(1)

            dilated = cv.dilate(eroded, dilation_element, iterations = 1)

            # cv.imshow("Dilated", dilated)
            # cv.waitKey(1)

            b, g, r = cv.split(dilated)

            # amplify red color
            r = cv.multiply(r, 0.8)

            # reduce blue and green colors
            redProcess = cv.subtract(r, b)
            redProcess = cv.subtract(redProcess, g)

            # threshold using red color
            ret, thresh = cv.threshold(redProcess, 20, 255,
                                       cv.THRESH_BINARY)

            # find red contours
            contours, hierarchies = cv.findContours(
                thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

            # draw valid contours
            # for contour in contours:
            #     moment = cv.moments(contour)
            #     if moment['m00'] != 0:
            #         Array_Size = len(contour)
            #         # center of the contour
            #         cx = int(moment['m10'] / moment['m00'])
            #         cy = int(moment['m01'] / moment['m00'])
            #         if cv.contourArea(contour) > 100:
            #             cv.drawContours(imgDraw, [contour], -1, (0, 255, 0), 2)
            #             #cv.circle(img, (cx, cy), 7, (255, 0, 0), -1)
            #             # draw a rectangle centering on each contour
            #             #cv.rectangle(imgDraw, (cx-100, cy-100), (cx+100, cy+100), (255, 0, 0), 2)
            #             if (cy-100 >= 0) and (cy+100 <= 1280) and (cx-100 >= 0) and (cx+100 <= 720) and write:
            #                 target = img[cy-100:cy+100, cx-100:cx+100]
            #                 targets.append(target)
            #                 #cv.imwrite('C:/Users/green/Pictures/DATA/roi_dataset/' + str(tgt_count) + '.jpg', target)
            #                 #tgt_count += 1

            # find largest contour
            areas = [cv.contourArea(c) for c in contours]
            max_index = np.argmax(areas)
            contour = contours[max_index]

            if write:
                moment = cv.moments(contour)
                if moment['m00'] != 0:
                    # center of the contour
                    cx = int(moment['m10'] / moment['m00'])
                    cy = int(moment['m01'] / moment['m00'])
                    target = img[cy - 200:cy + 200, cx - 200:cx + 200]
                    cv.imwrite(dirNameOut + str(os.fsdecode(file)), target)

        # random.shuffle(targets) # randomize dataset order
        # for target in targets:
        #     # rotate every other image by 180deg
        #     if (tgt_count % 2) == 0:
        #         target = cv.rotate(target, cv.ROTATE_180)
        #
        #     # flip every tenth image
        #     if (tgt_count % 10) == 0:
        #         target = cv.flip(target, 1)
        #
        #     cv.imwrite(dirNameOut + str(tgt_count) + '.jpg', target)
        #     tgt_count += 1

    def shuffleImages(self, dirNameIn, dirNameOut):
        directory = os.fsencode(dirNameIn)
        targets = []
        tgt_count = 1
        for file in os.listdir(directory):
            fileName = str(dirNameIn) + str(os.fsdecode(file))
            img = cv.imread(fileName)
            targets.append(img)

        random.shuffle(targets)  # randomize dataset order

        for target in targets:
            cv.imwrite(dirNameOut + str(tgt_count) + '.jpg', target)
            tgt_count += 1

    def borderImages(self, dirName):
        directory = os.fsencode(dirName)

        for file in os.listdir(directory):
            fileName = str(dirName) + str(os.fsdecode(file))
            img = cv.imread(fileName)  # store original image

            img = cv.copyMakeBorder(img, 200, 200, 200, 200, cv.BORDER_CONSTANT, value=[0, 0, 0])
            cv.imwrite(fileName, img)

if __name__ == '__main__':
    gui = GUI()
    #gui.shuffleImages('C:/Users/green/Pictures/DATA/simplified_roi_dataset/test_set_old/', 'C:/Users/green/Pictures/DATA/simplified_roi_dataset/test_set/')
    #gui.borderImages('C:/Users/green/Pictures/DATA/a_test/')
    #gui.findROI('C:/Users/green/Pictures/DATA/a_test/', 'C:/Users/green/Pictures/DATA/simplified_roi_dataset/', True)
    gui.setDirName('C:/Users/green/Pictures/DATA/roi_dataset/')
    gui.startGUI()

