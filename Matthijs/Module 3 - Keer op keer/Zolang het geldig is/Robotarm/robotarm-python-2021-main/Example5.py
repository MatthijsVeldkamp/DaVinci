from RobotArm import RobotArm
robotArm = RobotArm('exercise 6')
robotArm.speed = 4
# Jouw python instructies zet je vanaf hier:
robotArm.moveRight()
for i in range(1,4):
    robotArm.grab()
    robotArm.moveRight()
    robotArm.drop()
    robotArm.moveLeft()
    robotArm.grab()
    robotArm.moveLeft()
    robotArm.drop()
    robotArm.moveRight()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()