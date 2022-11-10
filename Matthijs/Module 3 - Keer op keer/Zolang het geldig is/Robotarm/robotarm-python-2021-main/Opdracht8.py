from RobotArm import RobotArm
robotArm = RobotArm('exercise 10')
for i in range(8,0,-1):
        if i % 2 == 0:
            robotArm.grab()
            for y in range(i):
                robotArm.moveRight()
        else:
            robotArm.drop()
            for p in range(i):
                robotArm.moveLeft()
robotArm.wait()