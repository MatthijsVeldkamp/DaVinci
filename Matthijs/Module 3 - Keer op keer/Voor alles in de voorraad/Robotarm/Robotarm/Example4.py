from RobotArm import RobotArm

robotArm = RobotArm('exercise 4')

# Jouw python instructies zet je vanaf hier:
robotArm.grab()
for i in range(1,5):
    robotArm.moveRight()
robotArm.drop()
for i in range(1,5):
    robotArm.moveLeft()
robotArm.grab()
for i in range(1,4):
    robotArm.moveRight()
robotArm.drop()
for i in range(1,4):
    robotArm.moveLeft()
robotArm.grab()
robotArm.moveRight()
robotArm.drop()
for i in range(1,3):
    robotArm.moveRight()
robotArm.grab()
for i in range(1,3):
    robotArm.moveLeft()
robotArm.drop()
for i in range(1,4):
    robotArm.moveRight()
robotArm.grab()
for i in range(1,4):
    robotArm.moveLeft()
robotArm.drop()



# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()
