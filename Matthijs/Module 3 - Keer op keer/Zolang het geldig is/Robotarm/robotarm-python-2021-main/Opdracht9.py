from RobotArm import RobotArm
robotArm = RobotArm('exercise 11')
border = 0
robotArm.speed = 3
while True:
    if border < 8:
        robotArm.grab()
        color = robotArm.scan()
        if color == ("white"):
            robotArm.moveRight()
            robotArm.drop()
            robotArm.moveRight()
            border += 1
            print(border)
        else:
            robotArm.drop()
            robotArm.moveRight()
            border += 1
            print(border)

    else:
        break
robotArm.wait()