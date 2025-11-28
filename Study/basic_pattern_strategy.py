class TravelStrategy:
    def calculate_time(self, distance_km:int):
        raise NotImplementedError("This method should be implemented by subclasses.")
    
class walkStrategy(TravelStrategy):
    def calculate_time(self, distance_km:int):
        time = distance_km * 10
        print(f"{distance_km} km walked in {time} minutes")

class carStrategy(TravelStrategy):
    def calculate_time(self, distance_km:int):
        time = distance_km * 1
        print(f"{distance_km} km driven in {time} minutes")

class bikeStrategy(TravelStrategy):
    def calculate_time(self, distance_km:int):
        time = distance_km * 4
        print(f"{distance_km} km biked in {time} minutes")

class TravelPlanner:
    def __init__(self, strategy:TravelStrategy ):
        self._strategy = strategy

    def set_strategy(self, strategy:TravelStrategy):
        self._strategy = strategy

    def calculate_time(self,distancekm:int):
        return self._strategy.calculate_time(distancekm)
    
travel = TravelPlanner(walkStrategy())
travel.calculate_time(4)
travel.set_strategy(carStrategy())
travel.calculate_time(4)
travel.set_strategy(bikeStrategy())
travel.calculate_time(4)


