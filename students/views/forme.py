class Zalupa(object):
    def __init__(self,arm,let):
        self.arm = arm
        self.let = let

    def lol(self):
        return 2*self.arm


lol = Zalupa(1 , 2)
asd = lol
print asd.lol()