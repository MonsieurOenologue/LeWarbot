def actionWarRocketLauncher():

	setDebugString("Armed and ready.");

	enemies = getPerceptsEnemies();
	worstEnemy = None;

	for enemy in enemies :
		if(isFood(enemy)) :
			sendMessageToExplorers("foodLocated", "");
			continue;
		if(isBase(enemy)) :
			setDebugString("Looks like I'll have to do it MYSELF!");
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

	attempt = 0;

	while(isBlocked()) :
		if(attempt > 9) :
			return idle();
		RandomHeading();
		attempt += 1;

	return move();
