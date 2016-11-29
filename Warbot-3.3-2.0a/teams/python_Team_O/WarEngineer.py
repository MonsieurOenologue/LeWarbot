
def actionWarEngineer():

	percepts = getPerceptsAlliesByType(WarAgentType.WarBase);

	if((percepts is None) or (len(percepts) == 0)) :
		messages = getMessages();

		for message in messages :
			if(message.getSenderType() == WarAgentType.WarBase) :
				setHeading(message.getAngle());

		broadcastMessageToAgentType(WarAgentType.WarBase, "whereAreYou", "");
	else :
		base = percepts[0];
		if(base.getDistance() > 2) :
			setHeading(base.getAngle());
			return move();
		elif(base.getHealth() < base.getMaxHealth()) :
			setIdNextBuildingToRepair(base.getID());
			return EngineerAction.ACTION_REPAIR;
		elif(not isBagEmpty()) :
			return eat();

	#if(isBlocked()) :
		#RandomHeading();
	#return move();

	return idle();