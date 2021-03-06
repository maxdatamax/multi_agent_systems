import numpy as np

class BusStop:
    def __init__(self, stop_id, name, x, y):
        self.stop_id = stop_id
        self.name = name
        self.passengers_waiting = []
        self.x = x
        self.y = y
        # self.passengers_that_arrived = [] 
        
    def add_waiting_passenger(self, passenger):
        self.passengers_waiting.append(passenger.passenger_id)
        passenger.current_stop = self
        
    def remove_waiting_passenger(self, passenger):
        assert passenger.passenger_id in self.passengers_waiting 
        self.passengers_waiting.remove(passenger.passenger_id)
        passenger.current_stop = None
        
    def distance(self, other):
        return np.sqrt((self.x-other.x)**2 + (self.y-other.y)**2)
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.stop_id == other.stop_id
        else:
            return False

    def reset(self):
        self.passengers_waiting.clear()

    def __str__(self):
        return "Stop # %s" % self.stop_id

    def __repr__(self):
        return str(self)