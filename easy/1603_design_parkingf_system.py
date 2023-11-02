class ParkingSystem(object):
    
    place = dict()

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        # self.big = big 
        # self.medium = medium
        # self.small = small
        self.place[1] = big
        self.place[2] = medium
        self.place[3] = small

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        # if carType == 1 and self.big>0:
        #     self.big -= 1
        #     return True
        # elif carType == 2 and self.medium>0:
        #     self.medium -= 1
        #     return True
        # elif carType == 3 and self.small>0:
        #     self.small -= 1
        #     return True
        # else:
        #     return False
        
        if self.place[carType] > 0:
            self.place[carType] -= 1
            return True
        else:
            return False