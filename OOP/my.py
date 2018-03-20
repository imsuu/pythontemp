class Robot:
    population=0
    def __init__(self,name):
        self.name=name
        print("Init {}".format(self.name))
        Robot.population+=1
    def die(self):
        print("{} is die".format(self.name))
        Robot.population-=1
        if Robot.population==0:
            print("{} is the last one".format(self.name))
        else:
            print("There are still {:d} Robots".format(Robot.population))
    def say_hi(self):
        print("hello my name is {}".format(self.name))

    @classmethod
    def how_many(cls):
        print("we hava {:d} Robots".format(cls.population))

robot1=Robot("111")
robot1.say_hi()
Robot.how_many()

robot2=Robot("222")
robot2.say_hi()
Robot.how_many()

robot1.die()
