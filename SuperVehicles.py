class Vechicles:
    def __init__(self, Name, MPG):
        # all that was needed was Name of vechicle and the MPG
        self.Name = Name
        self.MPG = MPG

# calculations kept here so it does not have to be repeated for all
    def fuel_needed(self, distance):
        return distance / self.MPG
    
    def description(self):
        return f"{self.Name} gets {self.MPG} miles per gallon."

# shows vechicles being the super class of car and others below
class Car(Vechicles):
    def __init__(self):
        # all that is needed is to declair it being a super class and the name and MPG for all vechicles
        super().__init__("Car", 30)

class Truck(Vechicles):
    def __init__(self):
        super().__init__("Truck", 15)

class Motorcycle(Vechicles):
    def __init__(self):
        super().__init__("Motorcycle", 50)

class Bus(Vechicles):
    def __init__(self):
        super().__init__("Bus", 8)


#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  IF THERE IS ANY CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓         PLEASE DO NOT MODIFY IF       ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 