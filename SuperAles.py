class Drinks:
    def __init__(self, Name, Abv):
        #depictable by all Drinks having Name and ABV
        self.Name = Name
        self.Abv = Abv
    #keeping the calculation together so they can be accessed in 1 class so it didn't have be repeated
    def alcohol_content(self, volume_in_oz):
        return self.Abv * volume_in_oz
    
    def description(self):
        return f"{self.Name}: {self.Abv*100:.1f}% ABV"
    


#shows the Drinks being the super class of IPA and the rest of the drinks below
class IPA(Drinks):
    def __init__(self):
        #all that was needed was the name and the ABV
        super().__init__("IPA", 0.065)

class Stout(Drinks):
    def __init__(self):
        super().__init__("Stout", 0.07)

class Porter(Drinks):
    def __init__(self):
        super().__init__("Porter", 0.6)

class PaleAle(Drinks):
    def __init__(self):
        super().__init__("PaleAle", 0.055)






#--------------------------------------------------------------------------------#
# ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎  WRITE YOUR CODE ABOVE THIS  LINE ⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎⬆︎

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓  IF THERE IS ANY CODE BELOW THIS LINE ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓         PLEASE DO NOT MODIFY IF       ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
#--------------------------------------------------------------------------------#
# 