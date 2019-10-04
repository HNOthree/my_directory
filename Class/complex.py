class Complex:
    def __init__(self, real, com):
        self.real = real
        self.com = com
    def __str__(self):
        if (self.com>0):
            return  str(self.real)+ "+" + str(self.com)+"i"
        else:
            return  str(self.real)+ str(self.com)+"i"