
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

	#Détection des ingénieurs alliés
	engineers = getPerceptsAlliesWarEngineer();

	#Si on perçoit un (ou +) ennemi(s)
	if(haveTargets(enemies)) :
		for enemy in enemies :
			#Si ce n'est pas une fausse alerte
			if(not isFood(enemy)) :
				#On appel à l'aide
				setDebugString("Swiftly!");
				broadcastMessageToAll("HELP", "");
				#S'il n'est pas inoffensif
				if(not isExplorer(enemy)) :
					#Si on manque d'ingénieur(s)
					if(len(engineers) < 5) :
						#Si on ne peut pas encore en construire sans danger
						if(getHealth() <= EngineerAction.COST + getMaxHealth() / 6) :
							#Si le sac n'est pas vide et que la vie est régénérable, on mange
							if(not isBagEmpty() and getHealth() + getFoodHealthGiven() <= getMaxHealth()) :
								return eat();
							#Sinon on attend
							return idle();
						#Et qu'il n'y a pas d'ingénieur proche, on en créé un
						if(haveNoTargets(engineers)) :
							return createEngineer();
						for engineer in engineers :
							#Si un ingénieur est déjà trop affaibli, on en créé un autre
							if(engineer.getHealth() * 10 < engineer.getMaxHealth()) :
								return createEngineer();
					#Si on peut créer un tank
					elif(getHealth() > HeavyAction.COST + getMaxHealth() / 3) :
						setNextAgentToCreate(WarAgentType.WarHeavy);
						return create();
					#Si le sac n'est pas vide et que la vie est régénérable, on mange
					if(not isBagEmpty() and getHealth() + getFoodHealthGiven() <= getMaxHealth()) :
						return eat();

	#Si on peut construire un char, on le fait
	if(getHealth() > HeavyAction.COST + getMaxHealth() / 3) :
		setNextAgentToCreate(WarAgentType.WarHeavy);
		return create();

	#Si le sac n'est pas vide et qu'on perçoit un (ou +) ingénieur(s) allié(s)
	if(not isBagEmpty() and haveTargets(engineers)) :
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

	#Ne rien faire
	return idle();