# LeWarbot
Nos petits scripts warbot pour aller combattre les méchants qui veulent envahir notre territoire.

## Goal
Le but est de créer les agents les + compétitifs possibles et donc les + "intelligents"
grace aux possibilités offertes par Warbot et Python (on pourrait également utiliser java).
On définit des scripts décrivant le cerveau de nos agents, le point clef étant la communication entre nos agents.
En mode duel (le mode qui nous intéresse ici) une partie est considérée comme gagnée lorsque toutes les bases ennemies ont été détruites.
Il est donc important de considérer la défense de sa/ses base(s) et de viser la/les base(s) ennemie(s).

## Warbot manual
Ce manuel comprend une description des différents types d'unités, l'installation de Warbot3 ainsi que la documentation.
http://www.lirmm.fr/~ferber/ProgAgent/Manuel_Warbot3.pdf

## Quick launch
- Clone this repo
- In the folder warbot.3-3-3 click on warbot-3.3.3.jar or do the following command in the terminal :
```java -jar warbot-3.3.3.jar```
- Choose our team vs another team (you can make a folder in warbot-3-3-3/teams and insert your own scripts to create a team)

### Equilibrages de la version 3.3.3 :
Up :  
- Base : +4000 HP  
- Explorer : +10 DistanceOfView  
- Light : +20 DistanceOfView  
- Rocket Launcher : -25 TickToReload  
- WarShell : +1 Autonomy  
- WarBomb : +1 Autonomy  
Nerf :  
- Turret : +200 Cost  
- Heavy : -10 DistanceOfView  
- Rocket Launcher : -0.2 Speed  
- Kamikaze : -1000 Damages  
