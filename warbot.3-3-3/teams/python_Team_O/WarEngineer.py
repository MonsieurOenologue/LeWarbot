
def actionWarEngineer():

	bases = getPerceptsAlliesWarBase();

	if(getHealth() > 20) :
		if(haveNoTargets(bases)) :
			messages = getMessages();

			for message in messages :
				if(isMessageOfWarBase(message)) :
					setHeading(message.getAngle());
			
			sendMessageToBases("whereAreYou", "");
		else :
			base = bases[0];
			if(base.getHealth() < base.getMaxHealth()) :
				face(base);
				if(base.getDistance() > 4) :
					if(not isBlocked()) :
						return move();
				else :
					setIdNextBuildingToRepair(base.getID());
					return EngineerAction.ACTION_REPAIR;

	#if(getHealth() > TurretAction.COST) :
		#return createTurret();

	attempt = 0;

	while(isBlocked()) :
		if(attempt > 9) :
			return idle();
		RandomHeading();
		attempt += 1;

	return move();
