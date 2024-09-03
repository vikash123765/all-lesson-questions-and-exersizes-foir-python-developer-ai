class Account:
    
     
    def __init__(self,balance):   ## without __bool__ and the return condition the balance would be true evem if 0 
        self.balance= balance


    def __bool__(self): ## this chnages the behaviour as of now if you pass a 0 value bool value will be false 
        return self.balance > 0







acount1 = Account(500)
print(bool(acount1))

acount2 = Account(0)
print(bool(acount2))

