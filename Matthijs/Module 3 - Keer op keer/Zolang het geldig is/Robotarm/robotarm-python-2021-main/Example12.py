from RobotArm import RobotArm
# Let op: hier start het anders voor een random level:
robotArm = RobotArm()
robotArm.randomLevel(1,7)
# Jouw python instructies zet je vanaf hier:
position = 1
for i in range(0,9):
    robotArm.grab()
    color = robotArm.scan()
    print("color of block: "+color)
    if color != (""):
        for i in range(0,position):
            robotArm.moveRight()
        robotArm.drop()
        position += 1
        for i in range(0,position-1):
            robotArm.moveLeft()
    else:
        robotArm.wait()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()