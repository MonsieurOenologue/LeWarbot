from math import *

def actionWarHeavy():

	setDebugString("Armed and ready.");

	enemies = getPerceptsEnemies();
	worstEnemy = None;

	for enemy in enemies :
		if(isFood(enemy)) :
			sendMessageToExplorers("foodLocated", [repr(enemy.getDistance()), repr(enemy.getAngle())]);
			continue;
		if(isBase(enemy)) :
			setDebugString("Looks like I'll have to do it MYSELF!");
			broadcastMessageToAll("baseAcquired", [repr(enemy.getDistance()), repr(enemy.getAngle())]);
			face(enemy);
			return shootTarget();
		if(worstEnemy is None) :
			worstEnemy = enemy;
		elif(isEngineer(enemy) and not isEngineer(worstEnemy)) :
			worstEnemy = enemy;
		elif(enemy.getType().equals(WarAgentType.WarHeavy) and not worstEnemy.getType().equals(WarAgentType.WarHeavy)) :
			worstEnemy = enemy;
		elif(isKamikaze(enemy) and not isKamikaze(worstEnemy)) :
			worstEnemy = enemy;
		elif(isRocketLauncher(enemy) and not isRocketLauncher(worstEnemy)) :
			worstEnemy = enemy;
		elif(isTurret(enemy) and not isTurret(worstEnemy)) :
			worstEnemy = enemy;
		elif(enemy.getType().equals(WarAgentType.WarLight) and not worstEnemy.getType().equals(WarAgentType.WarLight)) :
			worstEnemy = enemy;
		else :
			worstEnemy = enemy;

	if(worstEnemy is not None) :
		setDebugString("That's gotta sting.");
		face(worstEnemy);
		return shootTarget();
	elif(not isReloaded()) :
		return reloadWeapon();

	messages = getMessages();
	relevantMessage = None;

	for message in messages :
		if(message.getMessage() == "HELP" and isMessageOfWarBase(message) and (relevantMessage is None or relevantMessage.getMessage() == "beSafe" or message.getDistance() < relevantMessage.getDistance())) :
			relevantMessage = message;
		elif(message.getMessage() == "baseAcquired" and (relevantMessage is None or relevantMessage.getMessage() == "beSafe" or message.getDistance() < relevantMessage.getDistance())) :
			relevantMessage = message;
		#elif(message.getMessage() == "HELP" and (relevantMessage is None or message.getDistance() * 2 < relevantMessage.getDistance() + 50)) :
			#relevantMessage = message;
		elif(message.getMessage() == "beSafe" and relevantMessage is None) :
			relevantMessage = message;

	if(relevantMessage is not None and relevantMessage.getMessage() != "beSafe") :
		setDebugString("Captain Team_O on duty.");
		data = relevantMessage.getContent();
		if(len(data) > 1) :
			Ax = relevantMessage.getDistance() * cos(relevantMessage.getAngle());
			Ay = relevantMessage.getDistance() * sin(relevantMessage.getAngle());
			Bx = float(data[0]) * cos(float(data[1]));
			By = float(data[0]) * sin(float(data[1]));
			Cx = Ax + Bx;
			Cy = Ay + By;
			Cr = sqrt(Cx * Cx + Cy * Cy);
			C0 = degrees(atan2(Cy, Cx));
			setHeading(C0);
	elif(relevantMessage is not None and isMessageOfWarBase(relevantMessage) and relevantMessage.getDistance() > BaseAction.DISTANCE_OF_VIEW - 10) :
		face(message);

	attempt = 0;

	while(isBlocked()) :
		if(attempt > 9) :
			return idle();
		RandomHeading();
		attempt += 1;

	return move();
