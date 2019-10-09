
#Author: Paulo Moreira. 08-10-2019
class Container:

    #Constructor
    def __init__(self, code, weight):
        self.code = code
        self.weight = weight

    #Getter for code. Immutable var
    def get_code(self):
        return self.code

    #getter for weight
    def get_weight(self):
        return self.weight

    #setter for weight
    def set_weight(self, weight):
        self.weight = weight