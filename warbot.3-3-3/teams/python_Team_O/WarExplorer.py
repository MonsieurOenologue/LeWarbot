
def actionWarExplorer():

    setDebugString("I'll scout ahead!");

    enemies = getPerceptsEnemies();

    for enemy in enemies :
        if(isBase(enemy)) :
            setDebugString("Never underestimate the power of the Scout's code.");
            broadcastMessageToAll("baseAcquired", [repr(enemy.getDistance()), repr(enemy.getAngle())]);
            face(enemy);
            if(enemy.getDistance() < 2 or isBlocked()) :
                return idle();
            else :
                return move();
        elif(not isFood(enemy)) :
            setDebugString("You want Team_O? Come and get him!");
            broadcastMessageToAll("HELP", [repr(enemy.getDistance()), repr(enemy.getAngle())]);
        else :
            setDebugString("I forget what started the fighting...");
            sendMessageToExplorers("foodLocated", [repr(enemy.getDistance()), repr(enemy.getAngle())]);

        if(pickableFood(enemy) and isNotBagFull()) :
            face(enemy);
            return take();
        elif(isFood(enemy) and isNotBagFull() and not isBlocked()) :
            face(enemy);
            return move();

    if(isBagFull()) :
        setDebugString("Reporting in.");

        bases = getPerceptsAlliesWarBase();

        if(haveNoTargets(bases)) :

            messages = getMessages();

            for message in messages :
                if(isMessageOfWarBase(message)) :
                    face(message);

            sendMessageToBases("whereAreYou", "");

        else :
            base = bases[0];

            if(isPossibleToGiveFood(base)) :
                setIdNextAgentToGive(base.getID());
                return give();
            elif(not isBlocked()) :
                face(base);
                return move();

    if(isBlocked()) :
        angle1 = 0;
        angle2 = 0;
        currentHeading = getHeading();
        while(isBlocked()) :
            if(angle1 == 360) :
                return idle();
            angle1 += 15;
            setHeading(currentHeading + angle1);
        setHeading(currentHeading);
        while(isBlocked()) :
            if(angle2 == -360) :
                return idle();
            angle2 -= 15;
            setHeading(currentHeading + angle2);
        setHeading(currentHeading + (angle1 if (angle1 < -angle2) else angle2));

    return move();
