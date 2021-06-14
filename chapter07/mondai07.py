class Car:
    def __init__(self, seats, maxspeed):
        self.__seats = seats
        self.__maxspeed = maxspeed

    def spec(self):
        print('Seat: ' + str(self.seats) + ',' + 'Max speed: ' + str(self.maxspeed))

    @property
    def seats(self):
        return self.__seats

    @property
    def maxspeed(self):
        return self.__maxspeed

    def __eq__(self, other):
        if not isinstance (other, Car):
            return False
        return self.seats == other.seats and self.maxspeed == other.maxspeed


'''
    @seats.setter
    def seats(self, seats):
        self.__seats = seats

    @maxspeed.setter
    def maxspeed(self, maxspeed)
        self.__maxspeed = maxspeed
'''

class Truck(Car):
    def __init__(self, seats, maxspeed, capacity):
        super().__init__(seats, maxspeed)
        self.__capacity = capacity
    def spec(self):
        print('Seat: ' + str(self.seats) + ',' + 'Max speed: ' + str(self.maxspeed) + ', Capacity: '+ str(self.capacity))
    @property
    def capacity(self):
        return self.__capacity
