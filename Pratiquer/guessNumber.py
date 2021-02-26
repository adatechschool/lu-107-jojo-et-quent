class Guesser:
    def __init__(self, number, lives):
        self.number = number
        self.lives = lives

    def guess(self,n):
        if (self.lives>0):
            if (n!=self.number):
                res = False
                self.lives-=1
            else : 
                res = True
        else: 
            raise TypeError("Omae wa mo shindeiru")
        return res