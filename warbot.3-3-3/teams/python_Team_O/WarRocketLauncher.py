def actionWarRocketLauncher():

	percepts = getPercepts();

	for percept in percepts:
		if (percept.getType().equals(WarAgentType.WarRocketLauncher) or percept.getType().equals(WarAgentType.WarLight) or percept.getType().equals(WarAgentType.WarHeavy)):
			if (isEnemy(percept)):
				setDebugString("That's gotta sting.")
				setHeading(percept.getAngle())

				if (isReloaded()):
					setTargetDistance(percept.getDistance())
					return fire()
				else :
					return reloadWeapon()
			else:
				setDebugString("Armed and ready.")

		elif (percept.getType().equals(WarAgentType.WarBase)):
				if (isEnemy(percept)):
					setDebugString("That's gotta sting.")
					setHeading(percept.getAngle())

					if (isReloaded()):
						setTargetDistance(percept.getDistance())
						return fire()
					else :
						return reloadWeapon()
				else:
					setDebugString("Armed and ready.")
		else:
			setDebugString("Armed and ready.")

	if (len(percepts) == 0):
		setDebugString("Armed and ready.")

	if(isBlocked()):
		RandomHeading()


	return move();
