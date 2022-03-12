class MyPoint:
    """
    A point has coordinates and a colour
    """
    def __init__(self, x=0, y=0, c=""):
        """
        Initial values of a point
        """
        self.__coord_x = x
        self.__coord_y = y
        self.__colour = c

    def getCoord_x(self):
        return self.__coord_x

    def getCoord_y(self):
        return self.__coord_y

    def getColour(self):
        return self.__colour

    def setCoord_x(self, x):
        self.__coord_x = x

    def setCoord_y(self, y):
        self.__coord_y = y

    def setColour(self, c):
        if c == "red" or c == "yellow" or c == "blue" or c == "green" or c == "magenta":
            self.__colour = c

    def __str__(self):
        return "Point (" + str(self.__coord_x) + "," + str(self.__coord_y) + ") of colour " + self.__colour
