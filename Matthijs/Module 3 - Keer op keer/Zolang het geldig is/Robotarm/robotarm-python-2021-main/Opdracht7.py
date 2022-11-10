from RobotArm import RobotArm
robotArm = RobotArm('exercise 9')
for i in range(1,5):
    for i in range(0,i):
        robotArm.grab()
        for i in range(0,5):
            robotArm.moveRight()
        robotArm.drop()
        for i in range(0,5):
            robotArm.moveLeft()
    robotArm.moveRight()
robotArm.wait()