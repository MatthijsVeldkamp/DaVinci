from RobotArm import RobotArm

robotArm = RobotArm('exercise 6')
robotArm.speed = 4
# Jouw python instructies zet je vanaf hier:
for i in range(1,8):
    robotArm.moveRight()
robotArm.grab()
for i in range(1,8):
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()
    robotArm.moveLeft()
    robotArm.grab()
robotArm.moveRight()
robotArm.drop()
robotArm.moveLeft()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()