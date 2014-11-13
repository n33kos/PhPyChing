#!/usr/bin/env python
# -*- coding: latin-1 -*-
import sched, time, datetime, random, os, sys

#----------------------------------------------------------------
#-------------Hexagram Interpretation Functions------------------
#----------------------------------------------------------------
def interpret_lines(hexvalue,linesvalue):
	if hexvalue == "111111":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:\nHidden dragon. Do not act.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:\nDragon appearing in the field.\nIt furthers one to see the great man.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means:\nAll day long the superior man is creatively active.\nAt nightfall his mind is still beset with cares.\nDanger. No blame.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:\nWavering flight over the depths.\nNo blame.\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:\nFlying dragon in the heavens.\nIt furthers one to see the great man.\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:\nArrogant dragon will have cause to repent.\nWhen all the lines are nines, it means:\nThere appears a flight of dragons without heads.\nGood fortune.\n\n"
		return linesReturn
	if hexvalue == "000000":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means:\nWhen there is hoarfrost underfoot,\nSolid ice is not far off.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:\nStraight, square, great.\nWithout purpose,\nYet nothing remains unfurthered.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:\nHidden lines.\nOne is able to remain persevering.\nIf by chance you are in the service of a king,\nSeek not works, but bring to completion.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:\nA tied-up sack. No blame, no praise.\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:\nA yellow lower garment brings supreme good fortune.\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:\nDragons fight in the meadow.\nTheir blood is black and yellow.\nWhen all the lines are sixes, it means:\nLasting perseverance furthers.\n\n"
		return linesReturn
	if hexvalue == "100010":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:\nHesitation and hindrance.\nIt furthers one to remain persevering.\nIt furthers one to appoint helpers.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:\nDifficulties pile up.\nHorse and wagon part.\nHe is not a robber;\nHe wants to woo when the time comes.\nThe maiden is chaste,\nShe does not pledge herself.\nTen years--then she pledges herself.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:\nWhoever hunts deer without the forester\nOnly loses his way in the forest.\nThe superior man understands the signs of the time\nAnd prefers to desist.\nTo go on brings humiliation.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:\nHorse and wagon part.\nStrive for union.\nTo go brings good fortune.\nEverything acts to further.\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:\nDifficulties in blessing.\nA little perseverance brings good fortune.\nGreat perseverance brings misfortune.\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:\nHorse and wagon part.\nBloody tears flow.\n\n"
		return linesReturn
	if hexvalue == "010001":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means:\nTo make a fool develop\nIt furthers one to apply discipline.\nThe fetters should be removed.\nTo go on in this way bring humiliation.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:\nTo bear with fools in kindliness brings good fortune.\nTo know how to take women\nBrings good fortune.\nThe son is capable of taking charge of the household.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:\nTake not a maiden who. When she sees a man of bronze,\nLoses possession of herself.\nNothing furthers.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:\nEntangled folly bring humiliation.\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:\nChildlike folly brings good fortune. \n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:\nIn punishing folly\nIt does not further one\nTo commit transgressions.\nThe only thing that furthers \nIs to prevent transgressions.\n\n"
		return linesReturn
	if hexvalue == "111010":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:\nWaiting in the meadow.\nIT furthers one to abide in what endures.\nNo blame.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:\nWaiting on the sand.\nThere is some gossip.\nThe end brings good fortune.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means:\nWaiting in the mud\nBrings about the arrival of the enemy.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:\nWaiting in blood.\nGet out of the pit.\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:\nWaiting at meat and drink.\nPerseverance brings good fortune.\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:\nOne falls into the pit.\nThree uninvited guests arrive.\nHonor them, and in the end there will be good fortune.\n\n\n"
		return linesReturn
	if hexvalue == "010111":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means:\nIf one does not perpetuate the affair,\nThere is a little gossip.\nIn the end, good fortune comes.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:\nOne cannot engage in conflict;\nOne returns home, gives way.\nThe people of his town,\nThree hundred households, \nRemain free of guilt.\n\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:\nTo nourish oneself on ancient virtue induces perseverance.\nDanger. In the end, good fortune comes.\nIf by chance you are in the service of a king,\nSeek not works.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:\nOne cannot engage in conflict.\nOne turns back and submits to fate,\nChanges one's attitude, \nAnd finds peace in perseverance.\nGood fortune.\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:\nTo contend before him\nBrings supreme good fortune.\n\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:\nEven if by chance a leather belt is bestowed on one,'\nBy the end of a morning\nIt will have been snatched away three times.\n\n"
		return linesReturn
	if hexvalue == "010000":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means:\nAn army must set forth in proper order.\nIf the order is not good, misfortune threatens.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:\nIn the midst of the army.\nGood fortune. No blame.\nThe king bestows a triple decoration.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:\nPerchance the army carries corpses in the wagon.\nMisfortune.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:\nThe army retreats. No blame.\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:\nThere is game in the field.\nIt furthers one to catch it.\nWithout blame.\nLet the eldest lead the army.\nThe younger transports corpses;\nThen perseverance brings misfortune.\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:\nThe great prince issues commands,\nFounds states, vests families with fiefs.\nInferior people should not be employed.\n\n"
		return linesReturn
	if hexvalue == "000010":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means:\nHold to him in truth and loyalty;\nThis is without blame.\nTruth, like a full earthen bowl\nThus in the end\nGood fortune comes from without.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:\nHold to him inwardly.\nPerseverance brings good fortune.\n\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:\nYou hold together with the wrong people.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:\nHold to him outwardly also.\nPerseverance brings good fortune.\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:\nManifestation of holding together.\nIn the hunt the king uses beaters on three sides only\nAnd forgoes game that runs off in front.\nThe citizens need no warning.\nGood fortune.\n\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:\nHe finds no head for holding together.\nMisfortune.\n\n\n"
		return linesReturn
	if hexvalue == "111011":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:\nReturn to the way.\nHow could there be blame in this?\nGood fortune.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:\nHe allows himself to be drawn into returning.\nGood fortune.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means:\nThe spokes burst out of the wagon wheels.\nMan and wife roll their eyes.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:\nIf you are sincere, blood vanishes and fear gives way.\nNo blame.\n\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:\nIf you are sincere and loyally attached, \nYou are rich in your neighbor.\n\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:\nThe rain comes, there is rest.\nThis is due to the lasting effect of character.\nPerseverance brings the woman into danger.\nThe moon is nearly full.\nIf the superior man persists,\nMisfortune comes.\n\n"
		return linesReturn
	if hexvalue == "110111":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:\nSimple conduct. Progress without blame.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:\nTreading a smooth, level course.\nThe perseverance of a dark man\nBrings good fortune.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:\nA one-eyed man is able to see,\nA lame man is able to tread.\nHe treads on the tail of the tiger.\nThe tiger bites the man.\nMisfortune.\nThus does a warrior act on behalf of his great prince.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:\nHe treads on the tail of the tiger.\nCaution and circumspection\nLead ultimately to good fortune.\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:\nResolute conduct.\nPerseverance with awareness of danger.\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:\nLook to your conduct and weigh the favorable signs.\nWhen everything is fulfilled, supreme good fortune comes.\n\n"
		return linesReturn
	if hexvalue == "111000":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:\nWhen ribbon grass is pulled up, the sod comes with it.\nEach according to his kind.\nUndertakings bring good fortune.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:\nBearing with the uncultured in gentleness,\nFording the river with resolution,\nNot neglecting what is distant,\nNot regarding one's companions:\nThus one may manage to walk in the middle.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means:\nNo plain not followed by a slope.\nNo going not followed by a return.\nHe who remains persevering in danger\nIs without blame.\nDo not complain about this truth;\nEnjoy the good fortune you still possess.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:\nHe flutters down, not boasting of his wealth,\nTogether with his neighbor,\nGuileless and sincere.\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:\nThe sovereign I\nGives his daughter in marriage.\nAnd supreme good fortune.\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:\nThe wall falls back into the moat.\nUse no army now.\nMake your commands known within your own town.\nPerseverance brings humiliation.\n\n"
		return linesReturn
	if hexvalue == "000111":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means:\nWhen ribbon grass is pulled up, the sod comes with it.\nEach according to his kind.\nPerseverance brings good fortune and success.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:\nThey bear and endure;\nThis means good fortune for inferior people.\nThe standstill serves to help the great man to attain success.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:\nThey bear shame.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:\nHe who acts at the command of the highest \nRemains without blame.\nThose of like mind partake of the blessing.\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:\nStandstill is giving way.\nGood fortune for the great man.\n'What if it should fail, what if it should fail?'\nIn this way he ties it to a cluster of mulberry shoots.\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:\nThe standstill comes to an end.\nFirst standstill, then good fortune.\n\n"
		return linesReturn
	if hexvalue == "101111":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:\nFellowship with men at the gate.\nNo blame.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:\nFellowship with men in the clan.\nHumiliation.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means:\nHe hides weapons in the thicket;\nHe climbs the high hill in front of it.\nFor three years he does not rise up.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:\nHe climbs up on his wall; he cannot attack.\nGood fortune.\n\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:\nMen bound in fellowship first weep and lament,\nBut afterward they laugh.\nAfter great struggles they succeed in meeting.\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:\nFellowship with men in the meadow.\nNo remorse.\n\n"
		return linesReturn
	if hexvalue == "111101":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:\nNo relationship with what is harmful;\nThere is no blame in this.\nIf one remains conscious of difficulty,\nOne remains without blame.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:\nA big wagon for loading.\nOne may undertake something.\nNo blame.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means:\nA prince offers it to the Son of Heaven.\nA petty man cannot do this.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:\nHe makes a difference\nBetween himself and his neighbor.\nNo blame.\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:\nHe whose truth is accessible, yet dignified,\nHas good fortune.\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:\nHe is blessed by heaven.\nGood fortune.\nNothing that does not further.\n\n"
		return linesReturn
	if hexvalue == "001000":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means:\nA superior man modest about his modesty\nMay cross the great water.\nGood fortune.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:\nModesty that comes to expression. Perseverance brings good fortune.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means:\nA superior man of modesty and merit\nCarries things to conclusion.\nGood fortune.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:\nNothing that would not further modesty\nIn movement.\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:\nNo boasting of wealth before one's neighbor. \nIt is favorable to attack with force.\nNothing that would not further.\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:\nModesty that comes to expression.\nIt is favorable to set armies marching\nTo chastise one's own city and one's country.\n\n"
		return linesReturn
	if hexvalue == "000100":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means:\nEnthusiasm that expresses itself\nBrings misfortune.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:\nFirm as a rock. Not a whole day.\nPerseverance brings good fortune.\nFirm as a rock, what need of a whole day?\nHesitation brings remorse.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:\nEnthusiasm that looks upward creates remorse.\nHesitation brings remorse.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:\nThe source of enthusiasm.\nHe achieves great things.\nDoubt not.\nYou gather friends around you\nAs a hair clasp gathers the hair.\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:\nPersistently ill, and still does not die.\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:\nDeluded enthusiasm.\nBut if after completion one changes, \nThere is no blame.\n\n"
		return linesReturn
	if hexvalue == "100110":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:\nThe standard is changing.\nPerseverance brings good fortune.\nTo go out of the door in company\nProduces deeds.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:\nIf one clings to the little boy,\nOne loses the strong man.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:\nIf one clings to the strong man,\nOne loses the little boy.\nThrough following one finds what one seeks.\nIt furthers one to remain persevering.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:\nFollowing creates success.\nPerseverance brings misfortune.\nTo go one's way with sincerity brings clarity.\nHow could there be blame in this?\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:\nSincere in the good. Good fortune.\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:\nHe meets with firm allegiance\nAnd is still further bound.\nThe king introduces him\nTo the Western Mountain.\n\n"
		return linesReturn
	if hexvalue == "011001":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six in the beginning means:\nSetting right what has been spoiled by the father.\nIf there is a son, \nNo blame rests upon the departed father. \nDanger. In the end good fortune.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:\nSetting right what has been spoiled by the mother.\nOne must not be too persevering.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means:\nSetting right what has been spoiled by the father.\nThere will be a little remorse. No great blame.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:\nTolerating what has been spoiled by the father.\nIn continuing one sees humiliation.\n\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:\nSetting right what has been spoiled by the father.\nOne meets with praise.\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:\nHe does not serve kings and princes,\nSets himself higher goals.\n\n\n"
		return linesReturn
	if hexvalue == "110000":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:\nJoint approach.\nPerseverance brings good fortune.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:\nJoint approach.\nGood fortune.\nEverything furthers.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:\nComfortable approach.\nNothing that would further.\nIf one is induced to grieve over it,\nOne becomes free of blame.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:\nComplete approach.\nNo blame.\nin to his own circle, regardless of class prejudice. This is very favorable.\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:\nWise approach.\nThis is right for a great prince.\nGood fortune.\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:\nGreat hearted approach.\nGood-hearted approach.\nGood fortune. No blame.\n\n"
		return linesReturn
	if hexvalue == "000011":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means:\nBoy like contemplation.\nFor an inferior man, no blame.\nFor a superior man, humiliation.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:\nContemplation through the crack of the door.\nFurthering for the perseverance of a woman.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:\nContemplation of my life \nDecides the choice\nBetween advance and retreat.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:\nContemplation of the light of the kingdom.\nIt furthers one to exert influence as the guest of a king.\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:\nContemplation of my life.\nThe superior man is without blame.\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:\nContemplation of his life.\nThe superior man is without blame.\n\n"
		return linesReturn
	if hexvalue == "100101":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:\nHis feet are fastened in the stocks,\nSo that his toes disappear.\nNo blame.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six  in the second place means:\nBites through tender meat,\nSo that his nose disappears.\nNo blame.\n\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six  in the third place means:\nBites on old dried meat \nAnd strikes on something poisonous.\nSlight humiliation.  No blame.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:\nBites on dried gristly meat.\nReceives metal arrows.\nIt furthers one to be mindful of difficulties\nAnd to be persevering.\nGood fortune. \n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:\nBites on dried lean meat.\nReceives yellow gold.\nPerseveringly aware of danger.\nNo blame.\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:\nHis neck is fastened in the wooden cangue,\nSo that his ears disappear.\nMisfortune.\n\n"
		return linesReturn
	if hexvalue == "101001":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:\nHe lends grace to his toes, leaves the carriage, and walks.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:\nLends grace to the beard on his chin.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means:\nGraceful and moist.\nConstant perseverance brings good fortune.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:\nGrace or simplicity?\nA white horse comes as if on wings.\nHe is not a robber,\nHe will woo at the right time.\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:\nGrace in the hills and gardens.\nThe roll of silk is meager and small.\nHumiliation, but in the end good fortune.\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:\nSimple grace. No blame.\n\n"
		return linesReturn
	if hexvalue == "000001":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means:\nThe leg of the bed is split.\nThose who persevere are destroyed.\nMisfortune.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:\nThe bed is split at the edge.\nThose who persevere are destroyed.\nMisfortune.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:\nHe splits with them. No blame.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:\nThe bed is split up to the skin.\nMisfortune.\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:\nA shoal of fishes. Favor comes through the court ladies.\nEverything acts to further.\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:\nThere is a large fruit still uneaten.\nThe superior man receives a carriage.\nThe house of the inferior man is split apart.\n\n"
		return linesReturn
	if hexvalue == "100000":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:\nReturn from a short distance.\nNo need for remorse.\nGreat good fortune.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:\nQuiet return. Good fortune.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:\nRepeated return. Danger. No blame.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:\nWalking in the midst of others,\nOne returns alone.favorable, for such a resolve to choose the good brings its own reward. \n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:\nNoblehearted return. No remorse.\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:\nMissing the return. Misfortune.\nMisfortune from within and without.\nIf armies are set marching in this way,\nOne will in the end suffer a great defeat, \nDisastrous for the ruler of the country.\nFor ten years\nIt will not be possible to attack again.\n\n"
		return linesReturn
	if hexvalue == "100111":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:\nInnocent behavior brings good fortune.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:\nIf one does not count on the harvest while plowing,\nNor on the use of the ground while clearing it,\nIt furthers one to undertake something.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:\nUndeserved misfortune.\nThe cow that was tethered by someone\nIs the wanderer's gain, the citizen's loss.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:\nHe who can be persevering \nRemains without blame.\n\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:\nUse no medicine in an illness\nIncurred through no fault of your own.\nIt will pass of itself.\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:\nInnocent action brings misfortune.\nNothing furthers.\n\n"
		return linesReturn
	if hexvalue == "111001":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:\nDanger is at hand. It furthers one to desist.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:\nThe axletrees are taken from the wagon.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means.\nA good horse that follows others.\nAwareness of danger,\nWith perseverance, furthers.\nPractice chariot driving and armed defense daily. \nIt furthers one to have somewhere to go.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:\nThe headboard of a young bull.\nGreat good fortune.\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:\nThe tusk of a gelded boar.\nGood fortune.\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:\nOne attains the way of heaven.\nSuccess.\n\n"
		return linesReturn
	if hexvalue == "100001":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:\nYou let your magic tortoise go,\nAnd look at me with the corners of your mouth drooping.\nMisfortune.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:\nTurning to the summit for nourishment,\nDeviating from the path\nTo seek nourishment from the hill.\nContinuing to do this brings misfortune.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:\nTurning away from nourishment.\nPerseverance brings misfortune.\nDo not act thus for ten years.\nNothing serves to further.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:\nTurning to the summit\nFor provision of nourishment\nBrings good fortune.\nSpying about with sharp eyes\nLike a tiger with insatiable craving.\nNo blame.\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:\nTurning away from the path.\nTo remain persevering brings good fortune.\nOne should not cross the great water.\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:\nThe source of nourishment.\nAwareness of danger brings good fortune.\nIt furthers one to cross the great water.\n\n"
		return linesReturn
	if hexvalue == "011110":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means:\nTo spread white rushes underneath.\nNo blame.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:\nA dry poplar sprouts at the root.\nAn older man takes a young wife.\nEverything furthers.\n\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means:\nThe ridgepole sags to the breaking point.\nMisfortune.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:\nThe ridgepole is braced. Good fortune.\nIf there are ulterior motives, it is humiliating.\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:\nA withered poplar puts forth flowers.\nAn older woman takes a husband. \nNo blame. No praise.\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:\nOne must go through the water.\nIt goes over one's head.\nMisfortune. No blame.\n\n"
		return linesReturn
	if hexvalue == "010010":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means:\nRepetition of the Abysmal.\nIn the abyss one falls into a pit.\nMisfortune.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:\nThe abyss is dangerous.\nOne should strive to attain small things only.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:\nForward and backward, abyss on abyss.\nIn danger like this, pause at first and wait,\nOtherwise you will fall into a pit in the abyss.\nDo not act this way.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:\nA jug of wine, a bowl of rice with it;\nEarthen vessels\nSimply handed in through the Window.\nThere is certainly no blame in this.\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:\nThe abyss is not filled to overflowing,\nIt is filled only to the rim.\nNo blame.\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:\nBound with cords and ropes,\nShut in between thorn-hedged prison walls:\nFor three years one does not find the way.\nMisfortune.\n\n"
		return linesReturn
	if hexvalue == "101101":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:\nThe footprints run crisscross.\nIf one is seriously intent, no blame.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:\nYellow light. Supreme good fortune.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means:\nIn the light of the setting sun,\nMen either beat the pot and sing\nOr loudly bewail the approach of old age.\nMisfortune.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:\nIts coming is sudden;\nIt flames up, dies down, is thrown away.\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:\nTears in floods, sighing and lamenting.\nGood fortune. \n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "e third place, but with a real change of heart.\n\n\n"
		return linesReturn
	if hexvalue == "001110":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the top means:\nThe king used him to march forth and chastise.\nThen it is best to kill the leaders\nAnd take captive the followers. No blame.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six at the beginning means:\nThe influence shows itself in the big toe.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the second place means:\nThe influence shows itself in the calves of the legs.\nMisfortune.\nTarrying brings good fortune.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the third place means:\nThe influence shows itself in the thighs.\nHolds to that which follows it.\nTo continue is humiliating.\n\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:\nPerseverance brings good fortune.\nRemorse disappears.\nIf a man is agitated in mind,\nAnd his thoughts go hither and thither,\nOnly those friends \nOn whom he fixes his conscious thoughts\nWill follow.\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:\nThe influence shows itself in the back of the neck.\nNo remorse.\n\n"
		return linesReturn
	if hexvalue == "011100":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the top means:\nThe influence shows itself in the jaws, cheeks, and tongue.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six at the beginning means:\nSeeking duration too hastily brings misfortune persistently.\nNothing that would further.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the second place means:\nRemorse disappears.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the third place means:\nHe who does not give duration to his character\nMeets with disgrace.\nPersistent humiliation.\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:\nNo game in the field.\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:\nGiving duration to one's character through perseverance.\nThis is good fortune for a woman, misfortune for a man.\n\n"
		return linesReturn
	if hexvalue == "001111":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the top means:\nRestlessness as an enduring condition brings misfortune.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six at the beginning means:\nAt the tail in retreat. This is dangerous.\nOne must not wish to undertake anything.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the second place means:\nhe holds him fast with yellow oxhide.\nNo one can tear him loose.\nBrings good fortune.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:\nVoluntary retreat brings good fortune to the superior man\nAnd downfall to the inferior man.\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:\nFriendly retreat. Perseverance brings good fortune.\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:\nCheerful retreat. Everything serves to further.\n\n"
		return linesReturn
	if hexvalue == "111100":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:\nPower in the toes.\nContinuing brings misfortune.\nThis is certainly true.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:\nPerseverance brings good fortune.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means:\nThe inferior man works through power.\nThe superior man does not act thus.\nTo continue is dangerous.\nA goat butts against a hedge\nAnd gets its horns entangled.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:\nPerseverance brings good fortune.\nRemorse disappears.\nThe hedge opens; there is no entanglement.\nPower depends upon the axle of a big cart.\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:\nLoses the goat with ease.\nNo remorse.\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:\nA goat butts against a hedge.\nIt cannot go backward, it cannot go forward.\nNothing serves to further.\nIf one notes the difficulty, this brings good fortune.\n\n"
		return linesReturn
	if hexvalue == "000101":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means:\nProgressing, but turned back.\nPerseverance brings good fortune.\nIf one meets with no confidence, one should remain calm.\nNo mistake.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:\nProgressing, but in sorrow.\nPerseverance brings good fortune.\nThen one obtains great happiness from one's ancestress.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:\nAll are in accord. Remorse disappears.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:\nProgress like a hamster.\nPerseverance brings danger.\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:\nRemorse disappears.\nTake not gain and loss to heart.\nUndertakings bring good fortune.\nEverything serves to further.\n\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:\nMaking progress with the horns is permissible\nOnly for the purpose of punishing one's own city.\nTo be conscious of danger brings good fortune.\nNo blame. \nPerseverance brings humiliation.\n\n"
		return linesReturn
	if hexvalue == "101000":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:\nDarkening of the light during flight.\nHe lowers his wings.\nThe superior man does not eat for three days\nOn his wanderings.\nBut he has somewhere to go.\nThe host has occasion to gossip about him.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:\nDarkening of the light injures him in the left thigh.\nHe gives aid with the strength of a horse.\nGood fortune.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means:\nDarkening of the light during the hunt in the south.\nTheir great leader is captured.\nOne must not expect perseverance too soon.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:\nHe penetrates the left side of the belly.\nOne gets at the very heart of the darkening of the light.\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:\nDarkening of the light as with Prince Chi.\nPerseverance furthers.\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:\nNot light but darkness.\nFirst he climbed up to heaven,\nThen plunged into the depths of the earth.\n\n"
		return linesReturn
	if hexvalue == "101011":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:\nFirm seclusion within the family.\nRemorse disappears.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:\nShe should not follow her whims.\nShe must attend within to the food.\nPerseverance brings good fortune.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means:\nWhen tempers flare up in the family,\nToo great severity brings remorse.\nGood fortune nonetheless.\nWhen woman and chile dally and laugh\nIt leads in the end to humiliation.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:\nShe is the treasure of the house.\nGreat good fortune.\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:\nAs a king he approaches his family.\nFear not.\nGood fortune.\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:\nHis work commands respect.'\nIn the end good fortune comes.\n\n"
		return linesReturn
	if hexvalue == "110101":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:\nRemorse disappears.\nIf you lose your horse, do not run after it;\nIt will come back of its own accord.\nWhen you see evil people,\nGuard yourself against mistakes.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:\nOne meets his lord in a narrow street.\nNo blame.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:\nOne sees the wagon dragged back,\nThe oxen halted,\nA man's hair and nose cut off.\nNot a good beginning, but a good end.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:\nIsolated through opposition,\nOne meets a like-minded man\nWith whom one can associate in good faith.\nDespite the danger, no blame.\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:\nRemorse disappears.\nThe companion bits his way through the wrappings.\nIf one goes to him,\nHow could it be a mistake?\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:\nIsolated through opposition,\nOne sees one's companion as a pig covered with dirt,\nAs a wagon full of devils.\nFirst one draws a bow against him,\nthen one lays the bow aside.\nHe is not a robber; he will woo at the right time.\nAs one goes, rain falls; then good fortune comes.\n\n"
		return linesReturn
	if hexvalue == "001010":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means:\nGoing leads to obstructions,\nComing meets with praise.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:\nThe King's servant is beset by obstruction upon obstruction,\nBut it is not his own fault.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means:\nGoing leads to obstructions;\nHence he comes back.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:\nGoing leads to obstructions,\nComing leads to union.\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:\nIn the midst of the greatest obstructions,\nFriends come.\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:\nGoing leads to obstructions,\nComing leads to great good fortune.\nIt furthers one to see the great man.\n\n"
		return linesReturn
	if hexvalue == "010100":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means:\nWithout blame.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:\nOne kills three foxes in the field\nAnd receives a yellow arrow.\nPerseverance brings good fortune.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:\nIf a man carries a burden on his back\nAnd nonetheless rides in a carriage,\nHe thereby encourages robbers to draw near.\nPerseverance leads to humiliation.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:\nDeliver yourself from your great toe.\nThen the companion comes,\nAnd him you can trust.\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:\nIf only the superior man can deliver himself,\nIt brings good fortune.\nThus he proves to inferior men that he is in earnest.\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:\nThe prince shoots at a hawk on a high wall.\nHe kills it. Everything serves to further.\n\n"
		return linesReturn
	if hexvalue == "110001":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:\nGoing quickly when one's tasks are finished\nIs without blame.\nBut one must reflect on how much one may decrease others.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:\nPerseverance furthers.\nTo undertake something brings misfortune.\nWithout decreasing oneself,\nOne is able to bring increase to others.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:\nWhen three people journey together,\nTheir number increases by one.\nWhen one man journeys alone,\nHe finds a companion.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:\nIf a man deceases his faults,\nIt makes the other hasten to come and rejoice.\nNo blame.\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:\nSomeone does indeed increase him.\nTen pairs of tortoises cannot oppose it.\nSupreme good fortune.\n\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:\nIf one is increased without depriving other,\nThere is no blame.\nPerseverance brings good fortune.\nIt furthers one to undertake something.\nOne obtains servants\nBut no longer has a separate home.\n\n"
		return linesReturn
	if hexvalue == "100011":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:\nIt furthers one to accomplish great deeds.\nSupreme good fortune. No blame.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:\nSomeone does indeed increase him; \nTen pairs of tortoises cannot oppose it.\nConstant perseverance brings good fortune.\nThe king presents him before God.\nGood fortune.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:\nOne is enriched through unfortunate events.\nNo blame, if you are sincere\nAnd walk in the middle,\nAnd report with a seal to the prince.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:\nIf you walk in the middle \nAnd report the prince,\nHe will follow.\nIt furthers one to be used\nIn the removal of the capital.\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:\nIf in truth you have a kind heart, ask not.\nSupreme good fortune.\nTruly, kindness will be recognized as your virtue. \n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:\nHe brings increase to no one.\nIndeed, someone even strikes him.\nHe does not keep his heart constantly steady.\nMisfortune.\n\n"
		return linesReturn
	if hexvalue == "111110":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:\nMighty in the forward-striding toes.\nWhen one goes and is not equal to the task,\nOne makes a mistake.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:\nA cry of alarm. Arms at evening and at night.\nFear nothing.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means:\nTo be powerful in the cheekbones \nBrings misfortune.\nThe superior man is firmly resolved.\nHe walks alone and is caught in the rain.\nHe is bespattered,\nAnd people murmur against him.\nNo blame.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:\nThere is no skin on his thighs,\nAnd walking comes hard.\nIf a man were to let himself be led like a sheep,\nRemorse would disappear.\nBut if these words are heard\nThey will not be believed.\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:\nIn dealing with weeds,\nFirm resolution is necessary.\nWalking in the middle\nRemains free of blame.\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:\nNo cry.\nIn the end misfortune comes.\n\n"
		return linesReturn
	if hexvalue == "011111":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means:\nIt must be checked with a brake of bronze.\nPerseverance brings good fortune.\nIf one lets it take its course, one experiences misfortune.\nEven a lean pig has it in him to rage around.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:\nThere is a fish in the tank. No blame.\nDoes not further guests.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means: \nThere is no skin on his thighs,\nAnd walking comes hard.\nIf one is mindful of the danger,\nNo great mistake is made.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:\nNo fish in the tank.\nThis leads to misfortune.\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:\nA melon covered with willow leaves.\nHidden lines.\nThen it drops down to one from heave.\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:\nHe comes to meet with his horns.\nHumiliation. No blame.\n\n"
		return linesReturn
	if hexvalue == "000110":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means:\nIf you are sincere, but not to the end,\nThere will sometimes be confusion, sometimes gathering together.\nIf you call out, \nThen after one grasp of the hand you can laugh again.\nRegret not. Going is without blame.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:\nLetting oneself be drawn\nBrings good fortune and remains blameless.\nIf one is sincere,\nIt furthers one to bring even a small offering.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:\nGathering together amid sighs.\nNothing that would further.\nGoing is without blame.\nSlight humiliation.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:\nGreat good fortune. No blame.\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:\nIf in gathering together one has position,\nThis brings no blame.\nIf there are some who are not yet sincerely in the work,\nSublime and enduring perseverance is needed.\nThen remorse disappears.\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:\nLamenting and sighing, floods of tears.\nNo blame.\n\n"
		return linesReturn
	if hexvalue == "011000":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means:\nPushing upward that meets with confidence\nBrings great good fortune.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:\nIf one is sincere,\nIt furthers one to bring even a small offering.\nNo blame.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means:\nOne pushes upward into an empty city.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:\nThe king offers him Mount Ch'i.\nGood fortune. No blame.\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:\nPerseverance brings good fortune.\nOne pushes upward by steps.\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:\nPushing upward in darkness.\nIt furthers one\nTo be unremittingly persevering.\n\n"
		return linesReturn
	if hexvalue == "010110":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means:\nOne sits oppressed under a bare tree\nAnd strays into a gloomy valley.\nFor three years one sees nothing.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:\nOne is oppressed while at meat and drink.\nThe man with the scarlet knee bands is just coming.\nIt furthers one to offer sacrifice.\nTo set forth brings misfortune.\nNo blame.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:\nA man permits himself to be oppressed by stone,\nAnd leans on thorns and thistles.\nHe enters the house and does not see his wife.\nMisfortune.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:\nHe comes very quietly, oppressed in a golden carriage.\nHumiliation, but the end is reached.\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:\nHis nose and feet are cut off.\nOppression at the hands of the man with the purple knee bands.\nJoy comes softly.\nIt furthers one to make offerings and libations.\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:\nHe is oppressed by creeping vines.\nHe moves uncertainly and says, 'Movement brings remorse.'\nIf one feels remorse over this and makes a start,\nGood fortune comes.\n\n"
		return linesReturn
	if hexvalue == "011010":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means:\nOne does not drink the mud of the well.\nNo animals come to an old well.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:\nAt the well hole one shoots fishes.\nThe jug is broken and leaks.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means:\nThe well is cleaned, but no one drinks from it.\nThis is my heart's sorrow,\nFor one might draw from it.\nIf the king were clear-minded,\nGood fortune might be enjoyed in common.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:\nThe well is being lined. No blame.\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:\nIn the well there is a clear, cold spring\nFrom which one can drink.\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:\nOne draws from the well\nWithout hindrance.\nIt is dependable.\nSupreme good fortune.\n\n"
		return linesReturn
	if hexvalue == "101110":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:\nWrapped in the hide of a yellow cow.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:\nWhen one's own day comes, one may create revolution.\nStarting brings good fortune. No blame.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means:\nStarting brings misfortune.\nPerseverance brings danger.\nWhen talk of revolution has gone the rounds three times,\nOne may commit himself,\nAnd men will believe him.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:\nRemorse disappears. Men believe him.\nChanging the form of government brings good fortune.\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:\nThe great man changes like a tiger.\nEven before he questions the oracle\nHe is believed.\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:\nThe superior man changes like a panther.\nThe inferior man molts in the face.\nStarting brings misfortune.\nTo remain persevering brings good fortune.\n\n\n"
		return linesReturn
	if hexvalue == "011101":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means:\nA ting with legs upturned.\nFurthers removal of stagnating stuff.\nOne takes a concubine for the sake of her son.\nNo blame.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:\nThere is food in the ting.\nMy comrades are envious,\nBut they cannot harm me.\nGood fortune.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means:\nThe handle of the ting is altered.\nOne is impeded in his way of life.\nThe fat of the pheasant is not eaten.\nOnce rain falls, remorse is spent.\nGood fortune comes in the end.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:\nThe legs of the ting are broken.\nThe prince's meal is spilled\nAnd his person is soiled.\nMisfortune.\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:\nThe ting has yellow handles, golden carrying rings.\nPerseverance furthers.\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:\nThe ting has rings of jade.\nGreat good fortune.\nNothing that would not act to further.\n\n"
		return linesReturn
	if hexvalue == "100100":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:\nShock comes-oh, oh!\nThen follow laughing words-ha, ha!\nGood fortune.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:\nShock comes bringing danger.\nA hundred thousand times\nYou lose your treasures\nAnd must climb the nine hills.\nDo not go in pursuit of them.\nAfter seven days you will get them back again.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:\nShock comes and makes one distraught.\nIf shock spurs to action\nOne remains free of misfortune.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:\nShock is mired.\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:\nShock goes hither and thither.\nDanger.\nHowever, nothing at all is lost.\nYet there are things to be done.\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:\nShock brings ruin and terrified gazing around.\nGoing ahead brings misfortune.\nIf it has not yet touched one's own body\nBut has reached one's neighbor first,\nThere is no blame.\nOne's comrades have something to talk about.\n\n"
		return linesReturn
	if hexvalue == "001001":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means:\nKeeping his toes still.\nNo blame.\nContinued perseverance furthers.\n\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:\nKeeping his calves still.\nHe cannot rescue him whom he follows.\nHis heart is not glad.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means:\nKeeping his hips still.\nMaking his sacrum stiff.\nDangerous. The heart suffocates.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:\nKeeping his trunk still.\nNo blame.\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:\nKeeping his jaws still.\nThe words have order.\nRemorse disappears.\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:\nNoblehearted keeping still.\nGood fortune.\n\n"
		return linesReturn
	if hexvalue == "001011":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means:\nThe wild goose gradually draws near the shore. \nThe young son is in danger.\nThere is talk. No blame.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:\nThe wild goose gradually draws near the cliff.\nEating and drinking in peace and concord.\nGood fortune.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means:\nThe wild goose gradually draws near the plateau.\nThe man goes forth and does not return.\nThe woman carries a child but does not bring it forth.\nMisfortune. \nIt furthers one to fight off robbers.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:\nThe wild goose goes gradually draws near the tree.\nPerhaps it will find a flat branch. No blame.\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:\nThe wild goose gradually draws near the summit.\nFor three years the woman has no child.\nIn the end nothing can hinder her.\nGood fortune.\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:\nThe wild goose gradually draws near the clouds heights.\nIts feathers can be used for the sacred dance.\nGood fortune.\n\n"
		return linesReturn
	if hexvalue == "110100":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:\nThe marrying maiden as a concubine.\nA lame man who is able to tread.\nUndertakings bring good fortune.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:\nA one-eyed man who is able to see.\nThe perseverance of a solitary man furthers.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:\nThe marrying maiden as a slave.\nShe marries as a concubine.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:\nThe marrying maiden draws out the allotted time.\nA late marriage comes in due course.intended for her.\n\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:\nThe sovereign I gave his daughter in marriage.\nThe embroidered garments of the princess\nWere not as gorgeous\nAs those of the serving maid.\nThe moon that is nearly full\nBrings good fortune.\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:\nThe woman holds the basket, but there are no fruits in it.\nThe man stabs the sheep, but no blood flows.\nNothing that acts to further.\n\n\n"
		return linesReturn
	if hexvalue == "101100":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:\nWhen a man meets his destined ruler,\nThey can be together ten days,\nAnd it is not a mistake.\nGoing meets with recognition.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:\nThe curtain is of such fullness\nThat the polestars can be seen at noon.\nThrough going one meets with mistrust and hate.\nIf one rouses him through truth,\nGood fortune comes.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means:\nThe underbrush is of such abundance\nThat the small stars can be seen at noon.\nHe breaks his right arm . No blame.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:\nThe curtain is of such fullness\nThat the polestars can be seen at noon.\nHe meets his ruler, who is of like kind.\nGood fortune.\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:\nLines are coming,\nBlessing and fame draw near.\nGood fortune.\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:\nHis house is in a state of abundance.\nHe screens off his family.\nHe peers through the gate\nAnd no longer perceives anyone.\nFor three years he sees nothing.\nMisfortune.\n\n"
		return linesReturn
	if hexvalue == "001101":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means:\nIf the wanderer busies himself with trivial things, \nHe draws down misfortune upon himself.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:\nThe wanderer comes to an inn.\nHe has his property with him.\nHe wins the steadfastness of a young servant.\n\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means:\nThe wanderer's inn burns down.\nHe loses the steadfastness of his young servant.\nDanger.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:\nThe wanderer rests in a shelter.\nHe obtains his property and an ax.\nMy heart is not glad.\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:\nHe shoots a pheasant.\nIt drops with the first arrow.\nIn the end this brings both praise and office.\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:\nThe bird's nest burns up.\nThe wanderer laughs at first,\nThen must needs lament and weep.\nThrough carelessness he loses his cow.\nMisfortune.\n\n"
		return linesReturn
	if hexvalue == "011011":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means:\nIn advancing and in retreating,\nThe perseverance of a warrior furthers.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:\nPenetration under the bed.\nPriests and magicians are used in great number.\nGood fortune. No blame.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means:\nRepeated penetration. Humiliation.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:\nRemorse vanishes.\nDuring the hunt\nThree kinds of game are caught.\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:\nPerseverance brings good fortune.\nRemorse vanishes.\nNothing that does not further.\nNo beginning, but an end.\nBefore the change, three days.\nAfter the change, three days.\nGood fortune.\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:\nPenetration under the bed.\nHe loses his property and his ax.\nPerseverance brings misfortune.\n\n"
		return linesReturn
	if hexvalue == "110110":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:\nContented joyousness. Good fortune.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:\nSincere joyousness. Good fortune.\nRemorse disappears.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:\nComing joyousness. Misfortune.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:\nJoyousness that is weighed is not at peace.\nAfter ridding himself of mistakes a man has joy.\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:\nSincerity toward disintegrating influences is dangerous.\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:\nSeductive joyousness.\n\n"
		return linesReturn
	if hexvalue == "010011":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means:\nHe brings help with the strength of a horse.\nGood fortune.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:\nAt the dissolution\nHe hurries to that which supports him.\nRemorse disappears.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:\nHe dissolves his self. No remorse.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:\nHe dissolves his bond with his group.\nSupreme good fortune.\nDispersion leads in turn to accumulation.\nThis is something that ordinary men do not think of.\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:\nHis loud cries are as dissolving as sweat.\nDissolution! A king abides without blame.\n\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:\nHe dissolves his blood.\nDeparting, keeping at a distance, going out,\nIs without blame.\n\n"
		return linesReturn
	if hexvalue == "110010":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:\nNot going out of the door and the courtyard\nIs without blame.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:\nNot going out of the gate and the courtyard\nBrings misfortune.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:\nHe who knows limitation\nWill have cause to lament.\nNo blame.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:\nContented limitation. Success.\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:\nSweet limitation brings good fortune.\nGoing brings esteem.\n\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:\nGalling limitation.\nPerseverance brings misfortune.\nRemorse disappears.\n\n"
		return linesReturn
	if hexvalue == "110011":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:\nBeing prepared brings good fortune.\nIf there are secret designs, it is disquieting.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:\nA crane calling in the shade.\nIts young answers it.\nI have a good goblet.\nI will share it with you.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:\nHe finds a comrade.\nNow he beats the drum, now he stops.\nNow he sobs, now he sings.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:\nThe moon nearly at the full.\nThe team horse goes astray.\nNo blame.\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:\nHe possesses truth, which links together.\nNo blame.\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:\nCockcrow penetrating to heaven.\nPerseverance brings misfortune.\n\n"
		return linesReturn
	if hexvalue == "001100":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means:\nThe bird meets with misfortune through flying.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:\nShe passes by her ancestor\nAnd meets her ancestress.\nHe does not reach his prince\nAnd meets the official.\nNo blame.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means:\nIf one is not extremely careful,\nSomebody may come up from behind and strike him.\nMisfortune.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:\nNo blame. He meets him without passing by.\nGoing brings danger. One must be on guard.\nDo not act. Be constantly persevering.\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:\nDense clouds,\nNo rain from our western territory.\nThe prince shoots and hits him who is in the cave.\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:\nHe passes him by, not meeting him.\nThe flying bird leaves him.\nMisfortune.\nThis means bad luck and injury.\n\n"
		return linesReturn
	if hexvalue == "101010":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:\nHe breaks his wheels.\nHe gets his tail in the water.\nNo blame.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:\nThe woman loses the curtain of her carriage.\nDo not run after it;\nOn the seventh day you will get it.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means:\nThe Illustrious Ancestor\nDisciplines the Devil's Country.\nAfter three years he conquers it.\nInferior people must not be employed.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:\nThe finest clothes turn to rags.\nBe careful all day long.\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:\nThe neighbor in the east who slaughters an ox\nDoes not attain as much real happiness\nAs the neighbor in the west\nWith his small offering.\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:\nHe gets his head in the water. Danger.\n\n"
		return linesReturn
	if hexvalue == "010101":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means:\nHe gets his tail in the water.\nHumiliating.\n\n"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:\nHe brakes his wheels.\nPerseverance brings good fortune.\n\n"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:\nBefore completion, attack brings misfortune.\nIt furthers one to cross the great water.\n\n"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:\nPerseverance brings good fortune.\nRemorse disappears.\nShock, thus to discipline the Devil's Country.\nFor three years, great realms are rewarded.\n\n"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:\nPerseverance brings good fortune.\nNo remorse.\nThe light of the superior man is true.\nGood fortune.\n\n"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:\nThere is drinking of wine\nIn genuine confidence. No blame.\nBut if one wets his head,\nHe loses it, in truth.\n\n"
		return linesReturn


def interpret_judgment(hexvalue):
	if hexvalue == "111111":
		return "THE CREATIVE works sublime success,\nFurthering through perseverance."
	if hexvalue == "000000":
		return "THE RECEPTIVE brings about sublime success,\nFurthering through the perseverance of a mare.\nIf the superior man undertakes something and tries to lead,\nHe goes astray;\nBut if he follows, he finds guidance.\nIt is favorable to find friends in the west and south,\nTo forego friends in the east and north.\nQuiet perseverance brings good fortune."
	if hexvalue == "100010":
		return "DIFFICULTY AT THE BEGINNING works supreme success,\nFurthering through perseverance.\nNothing should be undertaken.\nIt furthers one to appoint helpers."
	if hexvalue == "010001":
		return "YOUTHFUL FOLLY has success.\nIt is not I who seek the young fool;\nThe young fool seeks me.\nAt the first oracle I inform him. \nIf he asks two or three times, it is importunity.\nIf he importunes, I give him no information.\nPerseverance furthers."
	if hexvalue == "111010":
		return "WAITING. If you are sincere, \nYou have light and success.\nPerseverance brings good fortune.\nIt furthers one to cross the great water."
	if hexvalue == "010111":
		return "CONFLICT. You are sincere\nAnd are being obstructed.\nA cautious halt halfway brings good fortune.\nGoing through to the end brings misfortune.\nIt furthers one to see the great man.\nIt does not further one to cross the great water."
	if hexvalue == "010000":
		return "THE ARMY. The army needs perseverance\nAnd a strong man.\nGood fortune without blame."
	if hexvalue == "000010":
		return "HOLDING TOGETHER brings good fortune.\nInquire of the oracle once again\nWhether you possess sublimity, constancy, and perseverance;\nThen there is no blame.\nThose who are uncertain gradually join.\nWhoever come too late\nMeets with misfortune."
	if hexvalue == "111011":
		return "THE TAMING POWER OF THE SMALL\nHas success.\nDense clouds, no rain from our western region."
	if hexvalue == "110111":
		return "TREADING. Treading upon the tail of the tiger.\nIt does not bite the man. Success."
	if hexvalue == "111000":
		return "nPEACE. The small departs,\nThe great approaches.\nGood fortune. Success."
	if hexvalue == "000111":
		return "STANDSTILL. Evil people do not further\nThe perseverance of the superior man.\nThe great departs; the small approaches."
	if hexvalue == "101111":
		return "FELLOWSHIP WITH MEN in the open.\nSuccess.\nIt furthers one to cross the great water.\nThe perseverance of the superior man furthers."
	if hexvalue == "111101":
		return "POSSESSION IN GREAT MEASURE.\nSupreme success."
	if hexvalue == "001000":
		return "MODESTY creates success.\nThe superior man carries things through."
	if hexvalue == "000100":
		return "ENTHUSIASM. It furthers one to install helpers\nAnd to set armies marching."
	if hexvalue == "100110":
		return "FOLLOWING has supreme success.\nPerseverance furthers. No blame."
	if hexvalue == "011001":
		return "WORK ON WHAT HAS BEEN SPOILED\nHas supreme success.\nIt furthers one to cross the great water.\nBefore the starting point, three days.\nAfter the starting point, three days."
	if hexvalue == "110000":
		return "APPROACH has supreme success.\nPerseverance furthers.\nWhen the eighth month comes,\nThere will be misfortune."
	if hexvalue == "000011":
		return "CONTEMPLATION. The ablution has been made, \nBut not yet the offering.\nFull of trust they look up to him."
	if hexvalue == "100101":
		return "BITING THROUGH has success.\nIt is favorable to let justice be administered."
	if hexvalue == "101001":
		return "GRACE has success.\nIn small matters\nIt is favorable to undertake something."
	if hexvalue == "000001":
		return "SPLITTING APART. IT does not further one \nTo go anywhere."
	if hexvalue == "100000":
		return "RETURN. Success.\nGoing out and coming in without error.\nFriends come without blame.\nTo and fro goes the way.\nOn the seventh day comes return.\nIt furthers one to have somewhere to go."
	if hexvalue == "100111":
		return "INNOCENCE. Supreme success.\nPerseverance furthers.\nIf someone is not as he should be,\nHe has misfortune,\nAnd it does not further him\nTo undertake anything."
	if hexvalue == "111001":
		return "THE TAMING POWER OF THE GREAT.\nPerseverance furthers.\nNot eating at home brings good fortune.\nIt furthers one to cross the great water."
	if hexvalue == "100001":
		return "THE CORNERS OF THE MOUTH.\nPerseverance brings good fortune.\nPay heed to the providing of nourishment\nAnd to what a man seeks\nTo fill his own mouth with."
	if hexvalue == "011110":
		return "PREPONDERANCE OF THE GREAT.\nThe ridgepole sags to the breaking point.\nIt furthers one to have somewhere to go.\nSuccess."
	if hexvalue == "010010":
		return "The Abysmal repeated.\nIf you are sincere, you have success in your heart,\nAnd whatever you do succeeds."
	if hexvalue == "101101":
		return "THE CLINGING. Perseverance furthers.\nIt brings success.\nCare of the cow brings good fortune."
	if hexvalue == "001110":
		return "Influence. Success.\nPerseverance furthers.\nTo take a maiden to wife brings good fortune."
	if hexvalue == "011100":
		return "DURATION. Success. No blame.\nPerseverance furthers.\nIt furthers one to have somewhere to go."
	if hexvalue == "001111":
		return "RETREAT. Success.\nIn what is small, perseverance furthers."
	if hexvalue == "111100":
		return "THE POWER OF THE GREAT. Perseverance furthers."
	if hexvalue == "000101":
		return "PROGRESS. The powerful prince\nIs honored with horses in large numbers.\nIn a single day he is granted audience three times."
	if hexvalue == "101000":
		return "DARKENING OF THE LIGHT. In adversity\nIt furthers one to be persevering."
	if hexvalue == "101011":
		return "THE FAMILY. The perseverance of the woman furthers."
	if hexvalue == "110101":
		return "OPPOSITION. In small matters, good fortune."
	if hexvalue == "001010":
		return "OBSTRUCTION. The southwest furthers.\nThe northeast does not further.\nIt furthers one to see the great man.\nPerseverance brings good fortune."
	if hexvalue == "010100":
		return "DELIVERANCE. The southwest furthers.\nIf there is no longer anything where one has to go,\nReturn brings good fortune.\nIf there is still something where one has to go,\nHastening brings good fortune."
	if hexvalue == "110001":
		return "DECREASE combined with sincerity\nBrings about supreme good fortune\nWithout blame.\nOne may be persevering in this.\nIt furthers one to undertake something.\nHow is this to be carried out?\nOne may use two small bowls for the sacrifice."
	if hexvalue == "100011":
		return "INCREASE. It furthers one\nTo undertake something.\nIt furthers one to cross the great water."
	if hexvalue == "111110":
		return "BREAK-THROUGH. One must resolutely make the matter known\nAt the court of the king.\nIt must be announced truthfully. Danger.\nIt is necessary to notify one's own city.\nIt does not further to resort to arms.\nIt furthers one to undertake something."
	if hexvalue == "011111":
		return "COMING TO MEET. The maiden is powerful.\nOne should not marry such a maiden."
	if hexvalue == "000110":
		return "GATHERING TOGETHER. Success.\nThe king approaches his temple.\nIt furthers one to see the great man.\nThis brings success. Perseverance furthers.\nTo bring great offerings creates good fortune.\nIt furthers one to undertake something."
	if hexvalue == "011000":
		return "PUSHING UPWARD has supreme success.\nOne must see the great man.\nFear not.\nDeparture toward the south\nBrings good fortune."
	if hexvalue == "010110":
		return "OPPRESSION. Success. Perseverance.\nThe great man brings about good fortune.\nNo blame.\nWhen one has something to say,\nIt is not believed."
	if hexvalue == "011010":
		return "THE WELL. The town may be changed,\nBut the well cannot be changed.\nIt neither decreases nor increases.\nThey come and go and draw from the well.\nIf one gets down almost to the water\nAnd the rope does not go all the way,\nOr the jug breaks, it brings misfortune."
	if hexvalue == "101110":
		return "REVOLUTION. On your own day\nYou are believed.\nSupreme success,\nFurthering through perseverance.\nRemorse disappears."
	if hexvalue == "011101":
		return "THE CALDRON. Supreme good fortune.\nSuccess."
	if hexvalue == "100100":
		return "SHOCK brings success.\nShock comes-oh, oh!\nLaughing words -ha, ha!\nThe shock terrifies for a hundred miles,\nAnd he does not let fall the sacrificial spoon and chalice."
	if hexvalue == "001001":
		return "KEEPING STILL. Keeping his back still\nSo that he no longer feels his body.\nHe goes into his courtyard\nAnd does not see his people.\nNo blame."
	if hexvalue == "001011":
		return "DEVELOPMENT. The maiden\nIs given in marriage.\nGood fortune.\nPerseverance furthers."
	if hexvalue == "110100":
		return "THE MARRYING MAIDEN.\nUndertakings bring misfortune.\nNothing that would further."
	if hexvalue == "101100":
		return "ABUNDANCE has success.\nThe king attains abundance.\nBe not sad.\nBe like the sun at midday."
	if hexvalue == "001101":
		return "The Wanderer. Success through smallness.\nPerseverance brings good fortune\nTo the Wanderer."
	if hexvalue == "011011":
		return "THE GENTLE. Success through what is small.\nIt furthers one to have somewhere to go.\nIt furthers one to see the great man."
	if hexvalue == "110110":
		return "THE JOYOUS. Success.\nPerseverance is favorable."
	if hexvalue == "010011":
		return "DISPERSION. Success.\nThe king approaches his temple.\nIt furthers one to cross the great water.\nPerseverance furthers."
	if hexvalue == "110010":
		return "LIMITATION. Success.\nGalling limitation must not be persevered in."
	if hexvalue == "110011":
		return "INNER TRUTH. Pigs and fishes.\nGood fortune.\nIt furthers one to cross the great water.\nPerseverance furthers."
	if hexvalue == "001100":
		return "PREPONDERANCE OF THE SMALL. Success.\nPerseverance furthers.\nSmall things may be done; great things should not be done.\nThe flying bird brings the message:\nIt is not well to strive upward,\nIt is well to remain below.\nGreat good fortune."
	if hexvalue == "101010":
		return "AFTER COMPLETION. Success in small matters.\nPerseverance furthers.\nAt the beginning good fortune.\nAt the end disorder."
	if hexvalue == "010101":
		return "BEFORE COMPLETION. Success.\nBut if the little fox, after nearly completing the crossing,\nGets his tail in the water,\nThere is nothing that would further."

def interpret_image(hexvalue):
	if hexvalue == "111111":
		return "The movement of heaven is full of power.\nThus the superior man makes himself strong and untiring."
	if hexvalue == "000000":
		return "The earth's condition is receptive devotion.\nThus the superior man who has breadth of character\nCarries the outer world."
	if hexvalue == "100010":
		return "Clouds and thunder:\nThe image of DIFFICULTY AT THE BEGINNING.\nThus the superior man\nBrings order out of confusion."
	if hexvalue == "010001":
		return "A spring wells up at the foot of the mountain: \nThe image of YOUTH.\nThus the superior man fosters his character\nBy thoroughness in all that he does."
	if hexvalue == "111010":
		return "Clouds rise up to heaven:\nThe image of WAITING.\nThus the superior man eats and drinks,\nIs joyous and of good cheer"
	if hexvalue == "010111":
		return "Heaven and water go their opposite ways:\nThe image of CONFLICT.\nThus in all his transactions the superior man\nCarefully considers the beginning."
	if hexvalue == "010000":
		return "In the middle of the earth is water:\nThe image of THE ARMY.\nThus the superior man increases his masses\nBy generosity toward the people."
	if hexvalue == "000010":
		return "On the earth is water:\nThe image of HOLDING TOGETHER.\nThus the kings of antiquity\nBestowed the different states as fiefs\nAnd cultivated friendly relations\nWith the feudal lords."
	if hexvalue == "111011":
		return "The wind drives across heaven:\nThe image of THE TAMING POWER OF THE SMALL.\nThus the superior man\nRefines the outward aspect of his nature."
	if hexvalue == "110111":
		return "Heaven above, the lake below:\nThe image of TREADING.\nThus the superior man discriminates between high and low,\nAnd thereby fortifies the thinking of the people."
	if hexvalue == "111000":
		return "Heaven and earth unite: the image of PEACE.\nThus the ruler\nDivides and completes the course of heaven and earth,\nAnd so aids the people."
	if hexvalue == "000111":
		return "Heaven and earth do not unite:\nThe image of STANDSTILL.\nThus the superior man falls back upon his inner worth \nIn order to escape the difficulties.\nHe does not permit himself to be honored with revenue."
	if hexvalue == "101111":
		return "Heaven together with fire:\nThe image of FELLOWSHIP WITH MEN.\nThus the superior man organizes the clans\nAnd makes distinctions between things."
	if hexvalue == "111101":
		return "Fire in heaven above:\nthe image of POSSESSION IN GREAT MEASURE.\nThus the superior man curbs evil and furthers good,\nAnd thereby obeys the benevolent will of heaven."
	if hexvalue == "001000":
		return "Within the earth, a mountain:\nThe image of MODESTY.\nThus the superior man reduces that which is too much,\nAnd augments that which is too little.\nHe weighs things and makes them equal."
	if hexvalue == "000100":
		return "Thunder comes resounding out of the earth:\nThe image of ENTHUSIASM.\nThus the ancient kings made music \nIn order to honor merit,\nAnd offered it with splendor\nTo the Supreme Deity,\nInviting their ancestors to be present."
	if hexvalue == "100110":
		return "Thunder in the middle of the lake:\nThe image of FOLLOWING.\nThus the superior man at nightfall\nGoes indoors for rest and recuperation."
	if hexvalue == "011001":
		return "The wind blows low on the mountain:\nThe image of DECAY.\nThus the superior man stirs up the people\nAnd strengthens their spirit."
	if hexvalue == "110000":
		return "The earth above the lake:\nThe image of APPROACH.\nThus the superior man is inexhaustible\nIn his will to teach,\nAnd without limits\nIn his tolerance and protection of the people."
	if hexvalue == "000011":
		return "The wind blows over the earth:\nThe image of CONTEMPLATION.\nThus the kings of old visited the regions of the world,\nContemplated the people,\nAnd gave them instruction."
	if hexvalue == "100101":
		return "Thunder and lighting:\nThe image of BITING THROUGH.\nThus the kings of former times made firm the laws\nThrough clearly defined penalties."
	if hexvalue == "101001":
		return "Fire at the foot of the mountain:\nThe image of GRACE.\nThus does the superior man proceed \nWhen clearing up current affairs.\nBut he dare not decide controversial issues in this way."
	if hexvalue == "000001":
		return "The mountain rests on the earth:\nThe image of SPLITTING APART.\nThus those above can ensure their position\nOnly by giving generously to those below."
	if hexvalue == "100000":
		return "Thunder within the earth:\nThe image of THE TURNING POINT\nThus the kings of antiquity closed the passes \nAt the time of solstice.\nMerchants and strangers did not go about,\nAnd the ruler\nDid not travel through the provinces."
	if hexvalue == "100111":
		return "Under heaven thunder rolls:\nAll things attain the natural state of innocence.\nThus the kings of old,\nRich in virtue, and in harmony with the time,\nFostered and nourished all beings."
	if hexvalue == "111001":
		return "Heaven within the mountain:\nThe image of THE TAMING POWER OF THE GREAT.\nThus the superior man acquaints himself with many sayings of antiquity\nAnd many deeds of the past,\nIn order to strengthen his character thereby."
	if hexvalue == "100001":
		return "At the foot of the mountain, thunder:\nThe image of PROVIDING NOURISHMENT.\nThus the superior man is careful of his words\nAnd temperate in eating and drinking."
	if hexvalue == "011110":
		return "The lake rises above the trees:\nThe image of PREPONDERANCE OF THE GREAT.\nThus the superior man, when he stands alone,\nIs unconcerned,\nAnd if he has to renounce the world,\nHe is undaunted."
	if hexvalue == "010010":
		return "Water flows on uninterruptedly and reaches its goal:\nThe image of the Abysmal repeated.\nThus the superior man walks in lasting virtue\nAnd carries on the business of teaching."
	if hexvalue == "101101":
		return "That which is bright rises twice:\nThe image of FIRE.\nThus the great man, by perpetuating this brightness,\nIllumines the four quarters of the world."
	if hexvalue == "001110":
		return "A lake on the mountain:\nThe image of influence.\nThus the superior man encourages people to approach him\nBy his readiness to receive them."
	if hexvalue == "011100":
		return "Thunder and wind: the image of DURATION.\nThus the superior man stands firm \nAnd does not change has direction."
	if hexvalue == "001111":
		return "Mountain under heaven: the image of RETREAT.\nThus the superior man keeps the inferior man at a distance,\nNot angrily but with reserve."
	if hexvalue == "111100":
		return "Thunder in heaven above:\nThe image of THE POWER OF THE GREAT.\nThus the superior man does not tread upon paths\nThat do not accord with established order."
	if hexvalue == "000101":
		return "The sun rises over the earth:\nThe image of PROGRESS.\nThus the superior man himself\nBrightens his bright virtue."
	if hexvalue == "101000":
		return "The light has sunk into the earth:\nThe image of DARKENING OF THE LIGHT.\nThus does the superior man live with the great mass:\nHe veils his light, yet still shines."
	if hexvalue == "101011":
		return "Wind comes forth from fire\nThe image of THE FAMILY.\nThus the superior man has substance in his word\nAnd duration in his way of life."
	if hexvalue == "110101":
		return "Above, fire; below. The lake\nThe image of OPPOSITION\nThus amid all fellowship\nThe superior man retains his individuality."
	if hexvalue == "001010":
		return "Water on the mountain\nThe image of OBSTRUCTION\nThus the superior man turns his attention to himself\nAnd molds his character."
	if hexvalue == "010100":
		return "Thunder and rain set in\nThe image of DELIVERANCE\nThus the superior man pardons mistakes\nAnd forgives misdeeds."
	if hexvalue == "110001":
		return "At the foot of the mountain, the lake\nThe image of DECREASE\nThus the superior man controls his ange\nAnd restrains his instincts."
	if hexvalue == "100011":
		return "Wind and thunder: the image of INCREASE\nThus the superior man\nIf he sees good, he imitates it\nIf he has faults, he rids himself of them."
	if hexvalue == "111110":
		return "The lake has risen up to heaven:\nThe image of BREAK-THROUGH.\nThus the superior man\nDispenses riches downward\nAnd refrains from resting on his virtue."
	if hexvalue == "011111":
		return "Under heaven, wind\nThe image of COMING TO MEET\nThus does the prince act when disseminating his command\nAnd proclaiming them to the four quarters of heaven."
	if hexvalue == "000110":
		return "Over the earth, the lake\nThe image of GATHERING TOGETHER\nThus the superior man renews his weapon\nIn order to meet the unforeseen."
	if hexvalue == "011000":
		return "Within the earth, wood grows\nThe image of PUSHING UPWARD\nThus the superior man of devoted characte\nHeaps up small thing\nIn order to achieve something high and great."
	if hexvalue == "010110":
		return "There is not water in the lake\nThe image of EXHAUSTION\nThus the superior man stakes his life\nOn following his will."
	if hexvalue == "011010":
		return "Water over wood: the image of THE WELL\nThus the superior man encourages the people at their work\nAnd exhorts them to help one another."
	if hexvalue == "101110":
		return "Fire in the lake: the image of REVOLUTION\nThus the superior man\nSets the calendar in orde\nAnd makes the seasons clear."
	if hexvalue == "011101":
		return "Fire over wood\nThe image of THE CALDRON\nThus the superior man consolidates his fate\nBy making his position correct."
	if hexvalue == "100100":
		return "Thunder repeated: the image of SHOCK\nThus in fear and tremblin\nThe superior man sets his life in orde\nAnd examines himself."
	if hexvalue == "001001":
		return "Mountains standing close together\nThe image of KEEPING STILL\nThus the superior man\nDoes not permit his thoughts\nTo go beyond his situation."
	if hexvalue == "001011":
		return "On the mountain, a tree\nThe image of DEVELOPMENT\nThus the superior man abides in dignity and virtue\nIn order to improve the mores."
	if hexvalue == "110100":
		return "Thunder over the lake\nThe image of THE MARRYING MAIDEN\nThus the superior man\nUnderstands the transitor\nIn the light of the eternity of the end."
	if hexvalue == "101100":
		return "Both thunder and lightning come\nThe image of ABUNDANCE\nThus the superior man decides lawsuit\nAnd carries out punishments."
	if hexvalue == "001101":
		return "Fire on the mountain\nThe image of THE WANDERER\nThus the superior man\nIs clear-minded and cautious\nIn imposing penalties\nAnd protracts no lawsuits."
	if hexvalue == "011011":
		return "Winds following one upon the other\nThe image of THE GENTLY PENETRATING\nThus the superior man\nSpreads his commands abroad\nAnd carries out his undertakings."
	if hexvalue == "110110":
		return "Lakes resting one on the other\nThe image of THE JOYOUS\nThus the superior man joins with his friend\nFor discussion and practice."
	if hexvalue == "010011":
		return "The wind drives over the water\nThe image of DISPERSION\nThus the kings of old sacrificed to the Lor\nAnd built temples."
	if hexvalue == "110010":
		return "Water over lake: the image of LIMITATION\nThus the superior man\nCreates number and measure\nAnd examines the nature of virtue and correct conduct."
	if hexvalue == "110011":
		return "Wind over lake: the image of INNER TRUTH\nThus the superior man discusses criminal cases\nIn order to delay executions."
	if hexvalue == "001100":
		return "Thunder on the mountain:\nThe image of PREPONDERANCE OF THE SMALL.\nThus in his conduct the superior man gives preponderance to reverence.\nIn bereavement he gives preponderance to grief.\nIn his expenditures he gives preponderance to thrift."
	if hexvalue == "101010":
		return "Water over fire: the image of the condition\nIn AFTER COMPLETION\nThus the superior man\nTakes thought of misfortun\nAnd arms himself against it in advance."
	if hexvalue == "010101":
		return "Fire over water:\nThe image of the condition before transition.\nThus the superior man is careful\nIn the differentiation of things,\nSo that each finds its place."

def interpret_hexagram(hexvalue):
	if hexvalue == "111111":
		return "(Ch'ien) The Creative - 1"
	if hexvalue == "000000":
		return "(K'un) The Receptive - 2"
	if hexvalue == "100010":
		return "(Chun) Difficulty at the Beginning - 3"
	if hexvalue == "010001":
		return "(Meng) Youthful Folly - 4"
	if hexvalue == "111010":
		return "(Hsu) Waiting (Nourishment) - 5"
	if hexvalue == "010111":
		return "(Sung) Conflict - 6"
	if hexvalue == "010000":
		return "(Shih) The Army - 7"
	if hexvalue == "000010":
		return "(Pi) Holding Together [union - 8"
	if hexvalue == "111011":
		return "(Hsiao Ch'u) The Taming Power of the Small - 9"
	if hexvalue == "110111":
		return "(Lu) Treading [conduct] - 10"
	if hexvalue == "111000":
		return "(T'ai) Peace - 11"
	if hexvalue == "000111":
		return "(P'i) Standstill [Stagnation] - 12"
	if hexvalue == "101111":
		return "(T'ung Jen) Fellowship with Men - 13"
	if hexvalue == "111101":
		return "(Ta Yu) Possession in Great Measure - 14"
	if hexvalue == "001000":
		return "(Ch'ien) Modesty - 15"
	if hexvalue == "000100":
		return "(Yu) Enthusiasm - 16"
	if hexvalue == "100110":
		return "(Sui) Following - 17"
	if hexvalue == "011001":
		return "(Ku) Work on what has been spoiled [ Decay ] - 18"
	if hexvalue == "110000":
		return "(Lin) Approach - 19"
	if hexvalue == "000011":
		return "(Kuan) Contemplation (View) - 20"
	if hexvalue == "100101":
		return "(Shih Ho) Biting Through - 21"
	if hexvalue == "101001":
		return "(Pi) Grace - 22"
	if hexvalue == "000001":
		return "(Po) Splitting Apart - 23"
	if hexvalue == "100000":
		return "(Fu) Return (The Turning Point) - 24"
	if hexvalue == "100111":
		return "(Wu Wang) Innocence (The Unexpected) - 25"
	if hexvalue == "111001":
		return "(Ta Ch'u) The Taming Power of the Great - 26"
	if hexvalue == "100001":
		return "(I) Corners of the Mouth (Providing Nourishment) - 27"
	if hexvalue == "011110":
		return "(Ta Kuo) Preponderance of the Great - 28"
	if hexvalue == "010010":
		return "(K'an) The Abysmal (Water) - 29"
	if hexvalue == "101101":
		return "(Li) The Clinging, Fire - 30"
	if hexvalue == "001110":
		return "(Hsien) Influence (Wooing) - 31"
	if hexvalue == "011100":
		return "(Heng) Duration - 32"
	if hexvalue == "001111":
		return "(TUN) Retreat - 33"
	if hexvalue == "111100":
		return "(Ta Chuang) The Power of the Great - 34"
	if hexvalue == "000101":
		return "(Chin) Progress - 35"
	if hexvalue == "101000":
		return "(Ming I) Darkening of the light - 36"
	if hexvalue == "101011":
		return "(Chia Jen) The Family [The Clan] - 37"
	if hexvalue == "110101":
		return "(K'uei) Opposition - 38"
	if hexvalue == "001010":
		return "(Chien) Obstruction - 39"
	if hexvalue == "010100":
		return "(Hsieh) Deliverance - 40"
	if hexvalue == "110001":
		return "(Sun) Decrease - 41"
	if hexvalue == "100011":
		return "(I) Increase - 42"
	if hexvalue == "111110":
		return "(Kuai) Break-through (Resoluteness) - 43"
	if hexvalue == "011111":
		return "(Kou) Coming to Meet - 44"
	if hexvalue == "000110":
		return "(Ts'ui) Gathering Together [Massing] - 45"
	if hexvalue == "011000":
		return "(Sheng) Pushing Upward - 46"
	if hexvalue == "010110":
		return "(K'un) Oppression (Exhaustion) - 47"
	if hexvalue == "011010":
		return "(Ching) The Well - 48"
	if hexvalue == "101110":
		return "(Ko) Revolution (Molting) - 49"
	if hexvalue == "011101":
		return "(Ting) The Caldron - 50"
	if hexvalue == "100100":
		return "(Chen) The Arousing (Shock, Thunder) - 51"
	if hexvalue == "001001":
		return "(Ken) Keeping Still, Mountain - 52"
	if hexvalue == "001011":
		return "(Chien) Development (Gradual Progress) - 53"
	if hexvalue == "110100":
		return "(Kuei Mei) The Marrying Maiden - 54"
	if hexvalue == "101100":
		return "(Feng) Abundance [Fullness] - 55"
	if hexvalue == "001101":
		return "(Lu) The Wanderer - 56"
	if hexvalue == "011011":
		return "(Sun) The Gentle (The Penetrating, Wind) - 57"
	if hexvalue == "110110":
		return "(Tui) The Joyous, Lake - 58"
	if hexvalue == "010011":
		return "(Huan) Dispersion [Dissolution] - 59"
	if hexvalue == "110010":
		return "(Chieh) Limitation - 60"
	if hexvalue == "110011":
		return "(Chung Fu) Inner Truth - 61"
	if hexvalue == "001100":
		return "(Hsiao Kuo) Preponderance of the Small - 62"
	if hexvalue == "101010":
		return "(Chi Chi) After Completion - 63"
	if hexvalue == "010101":
		return "(Wei Chi) Before Completion - 64"


#-----------------------------------------
#-------------Processing------------------
#-----------------------------------------

#get random seed from first argument
randomSeed = 'yinyang'
arg1 = sys.argv[0]
if arg1 != '':
	randomSeed = arg1

#Three Coin Toss Method
hexagrambyte = ""
linesbyte = ""
lowerTrigram = ""
upperTrigram = ""
hexagramNumber = 0
linesStrings = []
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
momentarySeed = randomSeed + unicode(ts)
random.seed(momentarySeed)
for x in xrange(0, 6):
	val1 = random.random()
	val2 = random.random()
	val3 = random.random()
	if val1 > 0.5:
		if val2 > 0.5:
			if val3 > 0.5:
				linesbyte += "1"
				hexagrambyte += "1"
				linesStrings.append("--------- *")
			elif val3 < 0.5:
				linesbyte += "0"
				hexagrambyte += "1"
				linesStrings.append("---------")
		elif val2 < 0.5:
			if val3 > 0.5:
				linesbyte += "0"
				hexagrambyte += "1"
				linesStrings.append("---------")
			if val3 < 0.5:
				linesbyte += "0"
				hexagrambyte += "0"
				linesStrings.append("---   ---")
	elif val1 < 0.5:
		if val2 < 0.5:
			if val3 < 0.5:
				linesbyte += "1"
				hexagrambyte += "0"
				linesStrings.append("---   --- *")
			elif val3 > 0.5:
				linesbyte += "0"
				hexagrambyte += "0"
				linesStrings.append("---   ---")
		elif val2 > 0.5:
			if val3 < 0.5:
				linesbyte += "0"
				hexagrambyte += "0"
				linesStrings.append("---   ---")
			if val3 > 0.5:
				linesbyte += "0"
				hexagrambyte += "1"
				linesStrings.append("---------")
	if x == 2:
		#get lower trigram
		if hexagrambyte == "000":
			lowerTrigram = "Earth"
		if hexagrambyte == "001":
			lowerTrigram = "Mountain"
		if hexagrambyte == "010":
			lowerTrigram = "Water"
		if hexagrambyte == "011":
			lowerTrigram = "Wood"
		if hexagrambyte == "100":
			lowerTrigram = "Thunder"
		if hexagrambyte == "101":
			lowerTrigram = "Fire"
		if hexagrambyte == "110":
			lowerTrigram = "Lake"
		if hexagrambyte == "111":
			lowerTrigram = "Heaven"
	if x == 5:
		#get upper trigram
		uppertest = hexagrambyte[-3:]
		if uppertest == "000":
			upperTrigram = "Earth"
		if uppertest == "001":
			upperTrigram = "Mountain"
		if uppertest == "010":
			upperTrigram = "Water"
		if uppertest == "011":
			upperTrigram = "Wood"
		if uppertest == "100":
			upperTrigram = "Thunder"
		if uppertest == "101":
			upperTrigram = "Fire"
		if uppertest == "110":
			upperTrigram = "Lake"
		if uppertest == "111":
			upperTrigram = "Heaven"

#Output
hexagram = interpret_hexagram(hexagrambyte)
theImage = interpret_image(hexagrambyte)
theJudgment = interpret_judgment(hexagrambyte)
theLines = interpret_lines(hexagrambyte, linesbyte)

#Clear Screen Windows
os.system('cls')
#Clear Screen Linux / os x
os.system('clear')

print ''
print hexagram

for x in reversed(xrange(3, 6)):
	print linesStrings[x]
for x in reversed(xrange(0, 3)):
	print linesStrings[x]

print ''

print upperTrigram
print '----------'
print lowerTrigram

print '\n---The Judgement---'
print theJudgment

print '\n---The Image---'
print theImage

if theLines != '':
	print '\n---The Lines---'
	print theLines