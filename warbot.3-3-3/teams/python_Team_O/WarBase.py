
def actionWarBase():

	#On reçoit tous les messages alliés
	messages = getMessages();

	setDebugString("What?! My servants haven't destroyed you yet?");

	for message in messages :
		#Si un message demande notre position, on l'envoie à l'agent concerné
		if(message.getMessage() == "whereAreYou") :
			setDebugString("Yes, sir!");
			sendMessage(message.getSenderID(), "here", "");

	#Détection des ennemis
	enemies = getPerceptsEnemies();

	#Si on perçoit un (ou +) ennemi(s), on appel à l'aide
	if(haveTargets(enemies)) :
		setDebugString("Swiftly!");
		broadcastMessageToAll("HELP", "");
		#Si le sac n'est pas vide et que la vie est régénérable, on mange
		if(not isBagEmpty() and getHealth() + getFoodHealthGiven() <= getMaxHealth()) :
			return eat();

	#Détection des ingénieurs alliés
	engineers = getPerceptsAlliesWarEngineer();

	#Si on manque d'ingénieur(s)
	if(len(engineers) < 5) :
		#Si on ne peut pas encore en construire sans danger
		if(getHealth() <= EngineerAction.COST) :
			#Si le sac n'est pas vide et que la vie est régénérable, on mange
			if(not isBagEmpty() and getHealth() + getFoodHealthGiven() <= getMaxHealth()) :
				return eat();
			#Sinon on attend
			return idle();
		#Et qu'il n'y a pas d'ingénieur proche, on en créé un
		if(haveNoTargets(engineers)) :
			setNextAgentToCreate(WarAgentType.WarEngineer);
			return create();
		#Et qu'on manque d'ingénieur(s) proche, on en créé un
		if(len(engineers) < 5) :
			#Mais seulement si chaque ingénieur est déjà trop affaibli
			length = 0;
			for engineer in engineers :
				if(engineer.getHealth() * 10 < engineer.getMaxHealth()) :
					length += 1;
			if(length == len(engineers)) :
				setNextAgentToCreate(WarAgentType.WarEngineer);
				return create();

	#Si on peut construire un char, on le fait
	if(getHealth() > HeavyAction.COST) :
		setNextAgentToCreate(WarAgentType.WarHeavy);
		return create();

	#Si le sac n'est pas vide et qu'on perçoit un (ou +) ingénieur(s) allié(s)
	if(not isBagEmpty() and haveNoTargets(engineers)) :
		lowestEngineer = None;
		for engineer in engineers :
			#On cherche l'ingénieur à portée ayant la vie la plus basse
			if(isPossibleToGiveFood(engineer)) :
				if(lowestEngineer is None or engineer.getHealth() < lowestEngineer.getHealth()) :
					lowestEngineer = engineer;
		#Si on peut soigner l'ingénieur le plus affaibli, on lui donne de la nourriture
		if(lowestEngineer is not None and lowestEngineer.getHealth() + getFoodHealthGiven() <= lowestEngineer.getMaxHealth()) :
			setIdNextAgentToGive(lowestEngineer.getID());
			return give();

	#Si le sac n'est pas vide et que la vie est régénérable, on mange
	if(not isBagEmpty() and getHealth() + getFoodHealthGiven() <= getMaxHealth()) :
		return eat();
	#elif(getNbElementsInBag() * 250 > 499 and getHealth() > 0.75 * getMaxHealth()) :
		#setNextAgentToCreate(WarAgentType.WarHeavy);
		#return create();

	#Ne rien faire
	return idle();