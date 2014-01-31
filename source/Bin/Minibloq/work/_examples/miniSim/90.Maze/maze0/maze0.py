import math
import pygame
from miniSim import MiniSim
from miniSim import MobileRobot
miniSim = MiniSim()
robot = miniSim.robot0

def go():
	miniSim.resetRobot(robot)
	import maze
	maze.drawMaze(robot)
miniSim.go = go
miniSim.run()
