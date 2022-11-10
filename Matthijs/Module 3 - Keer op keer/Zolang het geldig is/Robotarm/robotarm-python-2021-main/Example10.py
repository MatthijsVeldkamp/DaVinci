from RobotArm import RobotArm
robotArm = RobotArm('exercise 11')
border = 0
robotArm.speed = 3
for i in range(0,8):
    robotArm.moveRight()
while True:
    if border < 9:
        robotArm.grab()
        color = robotArm.scan()
        if color == ("white"):
            robotArm.moveRight()
            robotArm.drop()
            robotArm.moveLeft()
            robotArm.moveLeft()
            border += 1
            print(border)
        else:
            robotArm.drop()
            robotArm.moveLeft()
            border += 1
            print(border)
    
    else:
        break



robotArm.wait()