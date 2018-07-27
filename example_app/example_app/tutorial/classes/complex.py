import logging


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

    def print(self):
        logging.info('I am ({}, {}i)'.format(self.r, self.i))
