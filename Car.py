class Car(object):
    def __init__ (self, company, model, color, speedLimit):
        self.company = company
        self.model = model
        self.color = color
        self.speedLimit = speedLimit
    def start(self):
        print("started")
    def stop(self):
        print("stopped")   
    def accelerating(self):
        print("accelerating")
    def changeGear(self):
        print("changingGear")
BMW = Car("RangeRover", "Evouqe", "Steel Grey", 300)
#print(BMW.model) 
print(BMW.changeGear())