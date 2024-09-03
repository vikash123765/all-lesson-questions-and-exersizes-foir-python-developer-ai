class Car:


    def __init__(self,model,year,color,speed):
        self.model=model
        self.year=year
        self.color=color
        self.speed=speed



    def drive(self):
        print(f"you are driving the{self.model} and it is {self.color}")


    def stop(self):
        print(f"you are stopping th car while driving at {self.speed} km/h")





        