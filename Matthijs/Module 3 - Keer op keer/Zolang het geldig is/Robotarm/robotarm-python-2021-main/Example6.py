from RobotArm import RobotArm
robotArm = RobotArm('exercise 7')
for i in range(0,5):
    for i in range(0,6):
        robotArm.moveRight()
        robotArm.grab()
        robotArm.moveLeft()
        robotArm.drop()
    robotArm.moveRight()
    robotArm.moveRight()
robotArm.wait()