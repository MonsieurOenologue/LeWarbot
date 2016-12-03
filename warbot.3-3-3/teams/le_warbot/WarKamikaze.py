
def actionWarKamikaze():
	percepts = getPercepts();

	for percept in percepts:
		if (percept.getType().equals(WarAgentType.WarRocketLauncher) or percept.getType().equals(WarAgentType.WarLight) or percept.getType().equals(WarAgentType.WarHeavy)):
			if (isEnemy(percept)):
				setDebugString("Mode hunter")
				setHeading(percept.getAngle())
				setDebugString("KABOOOOOOM")
				return("fire");

		elif (percept.getType().equals(WarAgentType.WarBase)):
			if (isEnemy(percept)):
				setDebugString("Mode hunter")
				setHeading(percept.getAngle())
				setDebugString("KABOOOOOOM")
				return("fire");

	if (len(percepts) == 0):
		setDebugString("No cible")

	if(isBlocked()):
		RandomHeading()


	return move();
