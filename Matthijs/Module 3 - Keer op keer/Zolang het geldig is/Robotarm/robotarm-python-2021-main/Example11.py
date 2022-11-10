from RobotArm import RobotArm
robotArm = RobotArm('exercise 12')
x = True
for i in range(0,9):
    robotArm.moveRight()
position = 1
for i in range(0,9):
    robotArm.moveLeft()
    print(x)
    if x == True:
        position += 1
    x = True
    print(position)
    robotArm.grab()
    color = robotArm.scan()
    if color == ("red"):
        print("Red!")
        for i in range(0,position-1):
            robotArm.moveRight()
        robotArm.drop()
        for i in range(0,position-1):
            robotArm.moveLeft()
    else:
        print("Other color!")
        robotArm.drop()
        position += 1
        x = False  
robotArm.wait()