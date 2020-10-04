import os
import cv2

from range_color import Range
from logger import Logger
from config import DISPLAY_IMAGE


class ReadImage:
    def __init__(self, display_image=DISPLAY_IMAGE):
        self.__width = 0
        self.__height = 0
        self.__renderedImage = None
        self.__features = []
        self.__displayImage = display_image

        self.__bobHair = 0
        self.__bobPants = 0
        self.__bobShirt = 0
        self.__krustyHair = 0
        self.__krustyPants = 0
        self.__krustyShirt = 0

    def read(self, img):
        Logger.log(f'Image received {img}')
        image = cv2.imread(img)

        self.__height, self.__width, channels = image.shape

        if self.__displayImage:
            Logger.log('Cloned image')
            self.__renderedImage = image.copy()

        Logger.log('Handle width and height')
        for height in range(self.__height):
            for width in range(self.__width):
                pixel = image[height, width]
                self.handle_range_colors(pixel, width, height)

        if self.__displayImage:
            cv2.imshow('image', self.__renderedImage)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        return self.normalizeFeatures(img)

    """
      Receive a pixel (R, G, B) and call range_color.py
      https://stackoverflow.com/questions/28981417/how-do-i-access-the-pixels-of-an-image-using-opencv-python/50588950
    """

    def handle_range_colors(self, pixel, index_width, index_height):
        range = Range()
        b, g, r = pixel

        # check for Bob characteristics
        if range.bob_is_hair(r, g, b):
            self.__bobHair += 1
            if self.__displayImage:
                self.set_color(self.__bobHair, index_width, index_height)

        if range.bob_is_pants(r, g, b):
            self.__bobPants += 1
            if self.__displayImage:
                self.set_color(self.__bobPants, index_width, index_height)

        if range.bob_is_shirt(r, g, b):
            self.__bobShirt += 1
            if self.__displayImage:
                self.set_color(self.__bobShirt, index_width, index_height)

        # check for Krusty
        if range.krusty_is_hair(r, g, b):
            self.__krustyHair += 1
            if self.__displayImage:
                self.set_color(self.__krustyHair, index_width, index_height)

        if range.krusty_is_pants(r, g, b):
            self.__krustyPants += 1
            if self.__displayImage:
                self.set_color(self.__krustyPants, index_width, index_height)

        if range.krusty_is_shirt(r, g, b):
            self.__krustyShirt += 1
            if self.__displayImage:
                self.set_color(self.__krustyShirt, index_width, index_height)

    """
      TODO: estudar como associar uma variável recebida com o self
      Ex.: receber `variable` e associar self.variable += 1
    """

    def set_color(self, variable, index_width, index_height):
        self.__renderedImage[index_height][index_width] = [0, 255, 128]

    def calc_normalize(self, value):
        if value != 0.0:
            return (value / (self.__width * self.__height)) * 100

        return 0.0

    """
      Normalizes the features by the number of total pixels of the image to % 
    """

    def normalizeFeatures(self, img):
        Logger.log('Normalize Features')

        self.__bobHair = self.calc_normalize(self.__bobHair)
        self.__bobPants = self.calc_normalize(self.__bobPants)
        self.__bobShirt = self.calc_normalize(self.__bobShirt)
        self.__krustyHair = self.calc_normalize(self.__krustyHair)
        self.__krustyPants = self.calc_normalize(self.__krustyPants)
        self.__krustyShirt = self.calc_normalize(self.__krustyShirt)

        bob_or_krusty = 0.0  # Bob
        filename = os.path.basename(img)[0]

        if filename == 'k':
            bob_or_krusty = 1.0  # Krusty

        features = [
            self.__bobHair,
            self.__bobPants,
            self.__bobShirt,
            self.__krustyHair,
            self.__krustyPants,
            self.__krustyShirt,
            bob_or_krusty
        ]

        Logger.log(features)
        return features
