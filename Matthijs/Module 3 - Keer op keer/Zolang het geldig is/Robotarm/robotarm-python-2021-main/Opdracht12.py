from RobotArm import RobotArm
robotArm = RobotArm('exercise 12')
robotArm.speed = 3
pos = int(0) #Positie begint altijd op plaats 0
print(pos)
while True:
    robotArm.grab()
    color = robotArm.scan()
    if color == ("red"):
        print("Rood!")
        print("Positie is: "+str(pos))
        move = int(10 - pos)
        print("Hoeveelheid die de robotarm moet bewegen naar rechts is: "+str(move))
        if pos == 9:
            robotArm.drop()
            break
        else:
            for i in range(1,move):
                robotArm.moveRight()
            robotArm.drop()
            for i in range(1,move):
                robotArm.moveLeft()
            robotArm.moveRight()
            move -= pos
            pos += 1
            continue
    else:
        robotArm.drop()
        robotArm.moveRight()
        pos += 1
        continue
    break
robotArm.wait()