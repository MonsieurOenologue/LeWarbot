
def actionWarExplorer():

    percepts = getPercepts();

    for percept in percepts :
        if(isEnemy(percept)) :
            broadcastMessageToAll("HELP", "");
        elif(isFood(percept)) :
            broadcastMessageToAgentType(WarAgentType.WarExplorer, "food!", "");

        if(pickableFood(percept) and isNotBagFull()) :
            face(percept);
            return take();
        elif(isFood(percept) and isNotBagFull()) :
            face(percept);

    if(isBagFull()) :
        setDebugString("Reporting in.");

        percepts = getPerceptsAlliesWarBase();

        if((percepts is None) or (len(percepts) == 0)) :

            messages = getMessages();

            for message in messages :
                if(message.getSenderType() == WarAgentType.WarBase):
                    setHeading(message.getAngle());

            broadcastMessageToAgentType(WarAgentType.WarBase, "whereAreYou", "");

        else :
            base = percepts[0];

            if(base.getDistance() > maxDistanceGive()):
                setHeading(base.getAngle());
                return move();
            else:
                setIdNextAgentToGive(base.getID());
                return give();
    else :
        setDebugString("I'll scout ahead!");

    angle1 = 0;
    angle2 = 0;
    currentHeading = getHeading();

    if(isBlocked()) :
        while(isBlocked()) :
            if(angle1 == 360) :
                return idle();
            angle1 += 1;
            setHeading(currentHeading + angle1);
        setHeading(currentHeading);
        while(isBlocked()) :
            if(angle2 == -360) :
                return idle();
            angle2 -= 1;
            setHeading(currentHeading + angle2);
        setHeading(currentHeading + (angle1 if (angle1 < -angle2) else angle2));

    return move();
