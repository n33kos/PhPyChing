#!/usr/bin/env python
# -*- coding: latin-1 -*-
import sched, time, datetime, random, os, sys


#-----------------------------------------
#--------------CLASSES--------------------
#-----------------------------------------
class hexagramObject(object):
	def __init__(self, title, theImage, theJudgment, theLines, upperTrigram, lowerTrigram, hexagram, lines):
		self.title = title
		self.theImage = theImage
		self.theJudgment = theJudgment
		self.theLines = theLines
		self.upperTrigram = upperTrigram
		self.lowerTrigram = lowerTrigram
		self.hexagram = hexagram
		self.lines = lines


#----------------------------------------------------------------
#-------------------------FUNCTIONS------------------------------
#----------------------------------------------------------------
def interpret_lines(hexvalue,linesvalue):
	if hexvalue == "111111":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means: Hidden dragon. Do not act.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means: Dragon appearing in the field. It furthers one to see the great man.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means: All day long the superior man is creatively active. At nightfall his mind is still beset with cares. Danger. No blame.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means: Wavering flight over the depths. No blame.  "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means: Flying dragon in the heavens. It furthers one to see the great man.  "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means: Arrogant dragon will have cause to repent. When all the lines are nines, it means: There appears a flight of dragons without heads. Good fortune.  "
		return linesReturn
	if hexvalue == "000000":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means: When there is hoarfrost underfoot, Solid ice is not far off.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means: Straight, square, great. Without purpose, Yet nothing remains unfurthered.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means: Hidden lines. One is able to remain persevering. If by chance you are in the service of a king, Seek not works, but bring to completion.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means: A tied-up sack. No blame, no praise.  "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means: A yellow lower garment brings supreme good fortune.  "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means: Dragons fight in the meadow. Their blood is black and yellow. When all the lines are sixes, it means: Lasting perseverance furthers.  "
		return linesReturn
	if hexvalue == "100010":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means: Hesitation and hindrance. It furthers one to remain persevering. It furthers one to appoint helpers.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means: Difficulties pile up. Horse and wagon part. He is not a robber; He wants to woo when the time comes. The maiden is chaste, She does not pledge herself. Ten years--then she pledges herself.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means: Whoever hunts deer without the forester Only loses his way in the forest. The superior man understands the signs of the time And prefers to desist. To go on brings humiliation.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means: Horse and wagon part. Strive for union. To go brings good fortune. Everything acts to further.  "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means: Difficulties in blessing. A little perseverance brings good fortune. Great perseverance brings misfortune.  "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means: Horse and wagon part. Bloody tears flow.  "
		return linesReturn
	if hexvalue == "010001":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means: To make a fool develop It furthers one to apply discipline. The fetters should be removed. To go on in this way bring humiliation.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means: To bear with fools in kindliness brings good fortune. To know how to take women Brings good fortune. The son is capable of taking charge of the household.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means: Take not a maiden who. When she sees a man of bronze, Loses possession of herself. Nothing furthers.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means: Entangled folly bring humiliation.  "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means: Childlike folly brings good fortune.   "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means: In punishing folly It does not further one To commit transgressions. The only thing that furthers  Is to prevent transgressions.  "
		return linesReturn
	if hexvalue == "111010":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means: Waiting in the meadow. IT furthers one to abide in what endures. No blame.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means: Waiting on the sand. There is some gossip. The end brings good fortune.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means: Waiting in the mud Brings about the arrival of the enemy.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means: Waiting in blood. Get out of the pit.  "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means: Waiting at meat and drink. Perseverance brings good fortune.  "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means: One falls into the pit. Three uninvited guests arrive. Honor them, and in the end there will be good fortune.   "
		return linesReturn
	if hexvalue == "010111":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means: If one does not perpetuate the affair, There is a little gossip. In the end, good fortune comes.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means: One cannot engage in conflict; One returns home, gives way. The people of his town, Three hundred households,  Remain free of guilt.   "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means: To nourish oneself on ancient virtue induces perseverance. Danger. In the end, good fortune comes. If by chance you are in the service of a king, Seek not works.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means: One cannot engage in conflict. One turns back and submits to fate, Changes one's attitude,  And finds peace in perseverance. Good fortune.  "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means: To contend before him Brings supreme good fortune.   "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means: Even if by chance a leather belt is bestowed on one,' By the end of a morning It will have been snatched away three times.  "
		return linesReturn
	if hexvalue == "010000":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means: An army must set forth in proper order. If the order is not good, misfortune threatens.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means: In the midst of the army. Good fortune. No blame. The king bestows a triple decoration.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means: Perchance the army carries corpses in the wagon. Misfortune.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means: The army retreats. No blame.  "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means: There is game in the field. It furthers one to catch it. Without blame. Let the eldest lead the army. The younger transports corpses; Then perseverance brings misfortune.  "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means: The great prince issues commands, Founds states, vests families with fiefs. Inferior people should not be employed.  "
		return linesReturn
	if hexvalue == "000010":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means: Hold to him in truth and loyalty; This is without blame. Truth, like a full earthen bowl Thus in the end Good fortune comes from without.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means: Hold to him inwardly. Perseverance brings good fortune.   "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means: You hold together with the wrong people.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means: Hold to him outwardly also. Perseverance brings good fortune.  "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means: Manifestation of holding together. In the hunt the king uses beaters on three sides only And forgoes game that runs off in front. The citizens need no warning. Good fortune.   "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means: He finds no head for holding together. Misfortune.   "
		return linesReturn
	if hexvalue == "111011":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means: Return to the way. How could there be blame in this? Good fortune.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means: He allows himself to be drawn into returning. Good fortune.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means: The spokes burst out of the wagon wheels. Man and wife roll their eyes.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means: If you are sincere, blood vanishes and fear gives way. No blame.   "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means: If you are sincere and loyally attached,  You are rich in your neighbor.   "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means: The rain comes, there is rest. This is due to the lasting effect of character. Perseverance brings the woman into danger. The moon is nearly full. If the superior man persists, Misfortune comes.  "
		return linesReturn
	if hexvalue == "110111":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means: Simple conduct. Progress without blame.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means: Treading a smooth, level course. The perseverance of a dark man Brings good fortune.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means: A one-eyed man is able to see, A lame man is able to tread. He treads on the tail of the tiger. The tiger bites the man. Misfortune. Thus does a warrior act on behalf of his great prince.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means: He treads on the tail of the tiger. Caution and circumspection Lead ultimately to good fortune.  "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means: Resolute conduct. Perseverance with awareness of danger.  "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means: Look to your conduct and weigh the favorable signs. When everything is fulfilled, supreme good fortune comes.  "
		return linesReturn
	if hexvalue == "111000":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means: When ribbon grass is pulled up, the sod comes with it. Each according to his kind. Undertakings bring good fortune.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means: Bearing with the uncultured in gentleness, Fording the river with resolution, Not neglecting what is distant, Not regarding one's companions: Thus one may manage to walk in the middle.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means: No plain not followed by a slope. No going not followed by a return. He who remains persevering in danger Is without blame. Do not complain about this truth; Enjoy the good fortune you still possess.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means: He flutters down, not boasting of his wealth, Together with his neighbor, Guileless and sincere.  "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means: The sovereign I Gives his daughter in marriage. And supreme good fortune.  "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means: The wall falls back into the moat. Use no army now. Make your commands known within your own town. Perseverance brings humiliation.  "
		return linesReturn
	if hexvalue == "000111":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means: When ribbon grass is pulled up, the sod comes with it. Each according to his kind. Perseverance brings good fortune and success.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means: They bear and endure; This means good fortune for inferior people. The standstill serves to help the great man to attain success.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means: They bear shame.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means: He who acts at the command of the highest  Remains without blame. Those of like mind partake of the blessing.  "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means: Standstill is giving way. Good fortune for the great man. 'What if it should fail, what if it should fail?' In this way he ties it to a cluster of mulberry shoots.  "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means: The standstill comes to an end. First standstill, then good fortune.  "
		return linesReturn
	if hexvalue == "101111":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means: Fellowship with men at the gate. No blame.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means: Fellowship with men in the clan. Humiliation.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means: He hides weapons in the thicket; He climbs the high hill in front of it. For three years he does not rise up.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means: He climbs up on his wall; he cannot attack. Good fortune.   "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means: Men bound in fellowship first weep and lament, But afterward they laugh. After great struggles they succeed in meeting.  "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means: Fellowship with men in the meadow. No remorse.  "
		return linesReturn
	if hexvalue == "111101":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means: No relationship with what is harmful; There is no blame in this. If one remains conscious of difficulty, One remains without blame.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means: A big wagon for loading. One may undertake something. No blame.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means: A prince offers it to the Son of Heaven. A petty man cannot do this.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means: He makes a difference Between himself and his neighbor. No blame.  "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means: He whose truth is accessible, yet dignified, Has good fortune.  "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means: He is blessed by heaven. Good fortune. Nothing that does not further.  "
		return linesReturn
	if hexvalue == "001000":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means: A superior man modest about his modesty May cross the great water. Good fortune.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means: Modesty that comes to expression. Perseverance brings good fortune.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means: A superior man of modesty and merit Carries things to conclusion. Good fortune.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means: Nothing that would not further modesty In movement.  "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means: No boasting of wealth before one's neighbor.  It is favorable to attack with force. Nothing that would not further.  "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means: Modesty that comes to expression. It is favorable to set armies marching To chastise one's own city and one's country.  "
		return linesReturn
	if hexvalue == "000100":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means: Enthusiasm that expresses itself Brings misfortune.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means: Firm as a rock. Not a whole day. Perseverance brings good fortune. Firm as a rock, what need of a whole day? Hesitation brings remorse.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means: Enthusiasm that looks upward creates remorse. Hesitation brings remorse.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means: The source of enthusiasm. He achieves great things. Doubt not. You gather friends around you As a hair clasp gathers the hair.  "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means: Persistently ill, and still does not die.  "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means: Deluded enthusiasm. But if after completion one changes,  There is no blame.  "
		return linesReturn
	if hexvalue == "100110":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means: The standard is changing. Perseverance brings good fortune. To go out of the door in company Produces deeds.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means: If one clings to the little boy, One loses the strong man.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means: If one clings to the strong man, One loses the little boy. Through following one finds what one seeks. It furthers one to remain persevering.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means: Following creates success. Perseverance brings misfortune. To go one's way with sincerity brings clarity. How could there be blame in this?  "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means: Sincere in the good. Good fortune.  "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means: He meets with firm allegiance And is still further bound. The king introduces him To the Western Mountain.  "
		return linesReturn
	if hexvalue == "011001":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six in the beginning means: Setting right what has been spoiled by the father. If there is a son,  No blame rests upon the departed father.  Danger. In the end good fortune.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means: Setting right what has been spoiled by the mother. One must not be too persevering.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means: Setting right what has been spoiled by the father. There will be a little remorse. No great blame.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means: Tolerating what has been spoiled by the father. In continuing one sees humiliation.   "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means: Setting right what has been spoiled by the father. One meets with praise.  "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means: He does not serve kings and princes, Sets himself higher goals.   "
		return linesReturn
	if hexvalue == "110000":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means: Joint approach. Perseverance brings good fortune.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means: Joint approach. Good fortune. Everything furthers.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means: Comfortable approach. Nothing that would further. If one is induced to grieve over it, One becomes free of blame.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means: Complete approach. No blame. in to his own circle, regardless of class prejudice. This is very favorable.  "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means: Wise approach. This is right for a great prince. Good fortune.  "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means: Great hearted approach. Good-hearted approach. Good fortune. No blame.  "
		return linesReturn
	if hexvalue == "000011":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means: Boy like contemplation. For an inferior man, no blame. For a superior man, humiliation.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means: Contemplation through the crack of the door. Furthering for the perseverance of a woman.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means: Contemplation of my life  Decides the choice Between advance and retreat.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means: Contemplation of the light of the kingdom. It furthers one to exert influence as the guest of a king.  "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means: Contemplation of my life. The superior man is without blame.  "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means: Contemplation of his life. The superior man is without blame.  "
		return linesReturn
	if hexvalue == "100101":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means: His feet are fastened in the stocks, So that his toes disappear. No blame.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six  in the second place means: Bites through tender meat, So that his nose disappears. No blame.   "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six  in the third place means: Bites on old dried meat  And strikes on something poisonous. Slight humiliation.  No blame.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means: Bites on dried gristly meat. Receives metal arrows. It furthers one to be mindful of difficulties And to be persevering. Good fortune.   "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means: Bites on dried lean meat. Receives yellow gold. Perseveringly aware of danger. No blame.  "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means: His neck is fastened in the wooden cangue, So that his ears disappear. Misfortune.  "
		return linesReturn
	if hexvalue == "101001":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means: He lends grace to his toes, leaves the carriage, and walks.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means: Lends grace to the beard on his chin.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means: Graceful and moist. Constant perseverance brings good fortune.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means: Grace or simplicity? A white horse comes as if on wings. He is not a robber, He will woo at the right time.  "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means: Grace in the hills and gardens. The roll of silk is meager and small. Humiliation, but in the end good fortune.  "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means: Simple grace. No blame.  "
		return linesReturn
	if hexvalue == "000001":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means: The leg of the bed is split. Those who persevere are destroyed. Misfortune.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means: The bed is split at the edge. Those who persevere are destroyed. Misfortune.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means: He splits with them. No blame.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means: The bed is split up to the skin. Misfortune.  "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means: A shoal of fishes. Favor comes through the court ladies. Everything acts to further.  "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means: There is a large fruit still uneaten. The superior man receives a carriage. The house of the inferior man is split apart.  "
		return linesReturn
	if hexvalue == "100000":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means: Return from a short distance. No need for remorse. Great good fortune.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means: Quiet return. Good fortune.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means: Repeated return. Danger. No blame.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means: Walking in the midst of others, One returns alone.favorable, for such a resolve to choose the good brings its own reward.   "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means: Noblehearted return. No remorse.  "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means: Missing the return. Misfortune. Misfortune from within and without. If armies are set marching in this way, One will in the end suffer a great defeat,  Disastrous for the ruler of the country. For ten years It will not be possible to attack again.  "
		return linesReturn
	if hexvalue == "100111":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means: Innocent behavior brings good fortune.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means: If one does not count on the harvest while plowing, Nor on the use of the ground while clearing it, It furthers one to undertake something.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means: Undeserved misfortune. The cow that was tethered by someone Is the wanderer's gain, the citizen's loss.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means: He who can be persevering  Remains without blame.   "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means: Use no medicine in an illness Incurred through no fault of your own. It will pass of itself.  "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means: Innocent action brings misfortune. Nothing furthers.  "
		return linesReturn
	if hexvalue == "111001":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means: Danger is at hand. It furthers one to desist.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means: The axletrees are taken from the wagon.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means. A good horse that follows others. Awareness of danger, With perseverance, furthers. Practice chariot driving and armed defense daily.  It furthers one to have somewhere to go.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means: The headboard of a young bull. Great good fortune.  "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means: The tusk of a gelded boar. Good fortune.  "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means: One attains the way of heaven. Success.  "
		return linesReturn
	if hexvalue == "100001":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means: You let your magic tortoise go, And look at me with the corners of your mouth drooping. Misfortune.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means: Turning to the summit for nourishment, Deviating from the path To seek nourishment from the hill. Continuing to do this brings misfortune.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means: Turning away from nourishment. Perseverance brings misfortune. Do not act thus for ten years. Nothing serves to further.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means: Turning to the summit For provision of nourishment Brings good fortune. Spying about with sharp eyes Like a tiger with insatiable craving. No blame.  "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means: Turning away from the path. To remain persevering brings good fortune. One should not cross the great water.  "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means: The source of nourishment. Awareness of danger brings good fortune. It furthers one to cross the great water.  "
		return linesReturn
	if hexvalue == "011110":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means: To spread white rushes underneath. No blame.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means: A dry poplar sprouts at the root. An older man takes a young wife. Everything furthers.   "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means: The ridgepole sags to the breaking point. Misfortune.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means: The ridgepole is braced. Good fortune. If there are ulterior motives, it is humiliating.  "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means: A withered poplar puts forth flowers. An older woman takes a husband.  No blame. No praise.  "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means: One must go through the water. It goes over one's head. Misfortune. No blame.  "
		return linesReturn
	if hexvalue == "010010":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means: Repetition of the Abysmal. In the abyss one falls into a pit. Misfortune.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means: The abyss is dangerous. One should strive to attain small things only.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means: Forward and backward, abyss on abyss. In danger like this, pause at first and wait, Otherwise you will fall into a pit in the abyss. Do not act this way.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means: A jug of wine, a bowl of rice with it; Earthen vessels Simply handed in through the Window. There is certainly no blame in this.  "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means: The abyss is not filled to overflowing, It is filled only to the rim. No blame.  "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means: Bound with cords and ropes, Shut in between thorn-hedged prison walls: For three years one does not find the way. Misfortune.  "
		return linesReturn
	if hexvalue == "101101":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means: The footprints run crisscross. If one is seriously intent, no blame.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means: Yellow light. Supreme good fortune.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means: In the light of the setting sun, Men either beat the pot and sing Or loudly bewail the approach of old age. Misfortune.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means: Its coming is sudden; It flames up, dies down, is thrown away.  "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means: Tears in floods, sighing and lamenting. Good fortune.  "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means: The king used him to march forth and chastise. Then it is best to kill the leaders And take captive the followers. No blame.  "
		return linesReturn
	if hexvalue == "001110":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the top means: The king used him to march forth and chastise. Then it is best to kill the leaders And take captive the followers. No blame.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six at the beginning means: The influence shows itself in the big toe.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the second place means: The influence shows itself in the calves of the legs. Misfortune. Tarrying brings good fortune.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the third place means: The influence shows itself in the thighs. Holds to that which follows it. To continue is humiliating.   "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means: Perseverance brings good fortune. Remorse disappears. If a man is agitated in mind, And his thoughts go hither and thither, Only those friends  On whom he fixes his conscious thoughts Will follow.  "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means: The influence shows itself in the back of the neck. No remorse.  "
		return linesReturn
	if hexvalue == "011100":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the top means: The influence shows itself in the jaws, cheeks, and tongue.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six at the beginning means: Seeking duration too hastily brings misfortune persistently. Nothing that would further.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the second place means: Remorse disappears.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the third place means: He who does not give duration to his character Meets with disgrace. Persistent humiliation.  "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means: No game in the field.  "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six in the fifth place means: Giving duration to one's character through perseverance. This is good fortune for a woman, misfortune for a man.  "
		return linesReturn
	if hexvalue == "001111":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the top means: Restlessness as an enduring condition brings misfortune.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six at the beginning means: At the tail in retreat. This is dangerous. One must not wish to undertake anything.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the second place means: he holds him fast with yellow oxhide. No one can tear him loose. Brings good fortune.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means: Voluntary retreat brings good fortune to the superior man And downfall to the inferior man.  "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means: Friendly retreat. Perseverance brings good fortune.  "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means: Cheerful retreat. Everything serves to further.  "
		return linesReturn
	if hexvalue == "111100":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means: Power in the toes. Continuing brings misfortune. This is certainly true.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means: Perseverance brings good fortune.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means: The inferior man works through power. The superior man does not act thus. To continue is dangerous. A goat butts against a hedge And gets its horns entangled.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means: Perseverance brings good fortune. Remorse disappears. The hedge opens; there is no entanglement. Power depends upon the axle of a big cart.  "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means: Loses the goat with ease. No remorse.  "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means: A goat butts against a hedge. It cannot go backward, it cannot go forward. Nothing serves to further. If one notes the difficulty, this brings good fortune.  "
		return linesReturn
	if hexvalue == "000101":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means: Progressing, but turned back. Perseverance brings good fortune. If one meets with no confidence, one should remain calm. No mistake.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means: Progressing, but in sorrow. Perseverance brings good fortune. Then one obtains great happiness from one's ancestress.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means: All are in accord. Remorse disappears.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means: Progress like a hamster. Perseverance brings danger.  "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means: Remorse disappears. Take not gain and loss to heart. Undertakings bring good fortune. Everything serves to further.   "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means: Making progress with the horns is permissible Only for the purpose of punishing one's own city. To be conscious of danger brings good fortune. No blame.  Perseverance brings humiliation.  "
		return linesReturn
	if hexvalue == "101000":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means: Darkening of the light during flight. He lowers his wings. The superior man does not eat for three days On his wanderings. But he has somewhere to go. The host has occasion to gossip about him.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means: Darkening of the light injures him in the left thigh. He gives aid with the strength of a horse. Good fortune.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means: Darkening of the light during the hunt in the south. Their great leader is captured. One must not expect perseverance too soon.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means: He penetrates the left side of the belly. One gets at the very heart of the darkening of the light.  "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means: Darkening of the light as with Prince Chi. Perseverance furthers.  "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means: Not light but darkness. First he climbed up to heaven, Then plunged into the depths of the earth.  "
		return linesReturn
	if hexvalue == "101011":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means: Firm seclusion within the family. Remorse disappears.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means: She should not follow her whims. She must attend within to the food. Perseverance brings good fortune.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means: When tempers flare up in the family, Too great severity brings remorse. Good fortune nonetheless. When woman and chile dally and laugh It leads in the end to humiliation.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means: She is the treasure of the house. Great good fortune.  "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means: As a king he approaches his family. Fear not. Good fortune.  "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means: His work commands respect.' In the end good fortune comes.  "
		return linesReturn
	if hexvalue == "110101":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means: Remorse disappears. If you lose your horse, do not run after it; It will come back of its own accord. When you see evil people, Guard yourself against mistakes.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means: One meets his lord in a narrow street. No blame.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means: One sees the wagon dragged back, The oxen halted, A man's hair and nose cut off. Not a good beginning, but a good end.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means: Isolated through opposition, One meets a like-minded man With whom one can associate in good faith. Despite the danger, no blame.  "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means: Remorse disappears. The companion bits his way through the wrappings. If one goes to him, How could it be a mistake?  "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means: Isolated through opposition, One sees one's companion as a pig covered with dirt, As a wagon full of devils. First one draws a bow against him, then one lays the bow aside. He is not a robber; he will woo at the right time. As one goes, rain falls; then good fortune comes.  "
		return linesReturn
	if hexvalue == "001010":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means: Going leads to obstructions, Coming meets with praise.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means: The King's servant is beset by obstruction upon obstruction, But it is not his own fault.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means: Going leads to obstructions; Hence he comes back.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means: Going leads to obstructions, Coming leads to union.  "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means: In the midst of the greatest obstructions, Friends come.  "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means: Going leads to obstructions, Coming leads to great good fortune. It furthers one to see the great man.  "
		return linesReturn
	if hexvalue == "010100":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means: Without blame.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means: One kills three foxes in the field And receives a yellow arrow. Perseverance brings good fortune.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means: If a man carries a burden on his back And nonetheless rides in a carriage, He thereby encourages robbers to draw near. Perseverance leads to humiliation.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means: Deliver yourself from your great toe. Then the companion comes, And him you can trust.  "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means: If only the superior man can deliver himself, It brings good fortune. Thus he proves to inferior men that he is in earnest.  "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means: The prince shoots at a hawk on a high wall. He kills it. Everything serves to further.  "
		return linesReturn
	if hexvalue == "110001":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means: Going quickly when one's tasks are finished Is without blame. But one must reflect on how much one may decrease others.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means: Perseverance furthers. To undertake something brings misfortune. Without decreasing oneself, One is able to bring increase to others.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means: When three people journey together, Their number increases by one. When one man journeys alone, He finds a companion.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means: If a man deceases his faults, It makes the other hasten to come and rejoice. No blame.  "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means: Someone does indeed increase him. Ten pairs of tortoises cannot oppose it. Supreme good fortune.   "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means: If one is increased without depriving other, There is no blame. Perseverance brings good fortune. It furthers one to undertake something. One obtains servants But no longer has a separate home.  "
		return linesReturn
	if hexvalue == "100011":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means: It furthers one to accomplish great deeds. Supreme good fortune. No blame.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means: Someone does indeed increase him;  Ten pairs of tortoises cannot oppose it. Constant perseverance brings good fortune. The king presents him before God. Good fortune.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means: One is enriched through unfortunate events. No blame, if you are sincere And walk in the middle, And report with a seal to the prince.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means: If you walk in the middle  And report the prince, He will follow. It furthers one to be used In the removal of the capital.  "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means: If in truth you have a kind heart, ask not. Supreme good fortune. Truly, kindness will be recognized as your virtue.   "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means: He brings increase to no one. Indeed, someone even strikes him. He does not keep his heart constantly steady. Misfortune.  "
		return linesReturn
	if hexvalue == "111110":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means: Mighty in the forward-striding toes. When one goes and is not equal to the task, One makes a mistake.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means: A cry of alarm. Arms at evening and at night. Fear nothing.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means: To be powerful in the cheekbones  Brings misfortune. The superior man is firmly resolved. He walks alone and is caught in the rain. He is bespattered, And people murmur against him. No blame.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means: There is no skin on his thighs, And walking comes hard. If a man were to let himself be led like a sheep, Remorse would disappear. But if these words are heard They will not be believed.  "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means: In dealing with weeds, Firm resolution is necessary. Walking in the middle Remains free of blame.  "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means: No cry. In the end misfortune comes.  "
		return linesReturn
	if hexvalue == "011111":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means: It must be checked with a brake of bronze. Perseverance brings good fortune. If one lets it take its course, one experiences misfortune. Even a lean pig has it in him to rage around.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means: There is a fish in the tank. No blame. Does not further guests.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means:  There is no skin on his thighs, And walking comes hard. If one is mindful of the danger, No great mistake is made.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means: No fish in the tank. This leads to misfortune.  "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means: A melon covered with willow leaves. Hidden lines. Then it drops down to one from heave.  "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means: He comes to meet with his horns. Humiliation. No blame.  "
		return linesReturn
	if hexvalue == "000110":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means: If you are sincere, but not to the end, There will sometimes be confusion, sometimes gathering together. If you call out,  Then after one grasp of the hand you can laugh again. Regret not. Going is without blame.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means: Letting oneself be drawn Brings good fortune and remains blameless. If one is sincere, It furthers one to bring even a small offering.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means: Gathering together amid sighs. Nothing that would further. Going is without blame. Slight humiliation.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means: Great good fortune. No blame.  "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means: If in gathering together one has position, This brings no blame. If there are some who are not yet sincerely in the work, Sublime and enduring perseverance is needed. Then remorse disappears.  "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means: Lamenting and sighing, floods of tears. No blame.  "
		return linesReturn
	if hexvalue == "011000":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means: Pushing upward that meets with confidence Brings great good fortune.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means: If one is sincere, It furthers one to bring even a small offering. No blame.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means: One pushes upward into an empty city.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means: The king offers him Mount Ch'i. Good fortune. No blame.  "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means: Perseverance brings good fortune. One pushes upward by steps.  "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means: Pushing upward in darkness. It furthers one To be unremittingly persevering.  "
		return linesReturn
	if hexvalue == "010110":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means: One sits oppressed under a bare tree And strays into a gloomy valley. For three years one sees nothing.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means: One is oppressed while at meat and drink. The man with the scarlet knee bands is just coming. It furthers one to offer sacrifice. To set forth brings misfortune. No blame.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means: A man permits himself to be oppressed by stone, And leans on thorns and thistles. He enters the house and does not see his wife. Misfortune.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means: He comes very quietly, oppressed in a golden carriage. Humiliation, but the end is reached.  "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means: His nose and feet are cut off. Oppression at the hands of the man with the purple knee bands. Joy comes softly. It furthers one to make offerings and libations.  "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means: He is oppressed by creeping vines. He moves uncertainly and says, 'Movement brings remorse.' If one feels remorse over this and makes a start, Good fortune comes.  "
		return linesReturn
	if hexvalue == "011010":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means: One does not drink the mud of the well. No animals come to an old well.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means: At the well hole one shoots fishes. The jug is broken and leaks.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means: The well is cleaned, but no one drinks from it. This is my heart's sorrow, For one might draw from it. If the king were clear-minded, Good fortune might be enjoyed in common.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means: The well is being lined. No blame.  "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means: In the well there is a clear, cold spring From which one can drink.  "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means: One draws from the well Without hindrance. It is dependable. Supreme good fortune.  "
		return linesReturn
	if hexvalue == "101110":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means: Wrapped in the hide of a yellow cow.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means: When one's own day comes, one may create revolution. Starting brings good fortune. No blame.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means: Starting brings misfortune. Perseverance brings danger. When talk of revolution has gone the rounds three times, One may commit himself, And men will believe him.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means: Remorse disappears. Men believe him. Changing the form of government brings good fortune.  "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means: The great man changes like a tiger. Even before he questions the oracle He is believed.  "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means: The superior man changes like a panther. The inferior man molts in the face. Starting brings misfortune. To remain persevering brings good fortune.   "
		return linesReturn
	if hexvalue == "011101":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means: A ting with legs upturned. Furthers removal of stagnating stuff. One takes a concubine for the sake of her son. No blame.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means: There is food in the ting. My comrades are envious, But they cannot harm me. Good fortune.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means: The handle of the ting is altered. One is impeded in his way of life. The fat of the pheasant is not eaten. Once rain falls, remorse is spent. Good fortune comes in the end.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means: The legs of the ting are broken. The prince's meal is spilled And his person is soiled. Misfortune.  "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means: The ting has yellow handles, golden carrying rings. Perseverance furthers.  "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means: The ting has rings of jade. Great good fortune. Nothing that would not act to further.  "
		return linesReturn
	if hexvalue == "100100":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means: Shock comes-oh, oh! Then follow laughing words-ha, ha! Good fortune.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means: Shock comes bringing danger. A hundred thousand times You lose your treasures And must climb the nine hills. Do not go in pursuit of them. After seven days you will get them back again.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means: Shock comes and makes one distraught. If shock spurs to action One remains free of misfortune.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means: Shock is mired.  "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means: Shock goes hither and thither. Danger. However, nothing at all is lost. Yet there are things to be done.  "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means: Shock brings ruin and terrified gazing around. Going ahead brings misfortune. If it has not yet touched one's own body But has reached one's neighbor first, There is no blame. One's comrades have something to talk about.  "
		return linesReturn
	if hexvalue == "001001":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means: Keeping his toes still. No blame. Continued perseverance furthers.   "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means: Keeping his calves still. He cannot rescue him whom he follows. His heart is not glad.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means: Keeping his hips still. Making his sacrum stiff. Dangerous. The heart suffocates.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means: Keeping his trunk still. No blame.  "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means: Keeping his jaws still. The words have order. Remorse disappears.  "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means: Noblehearted keeping still. Good fortune.  "
		return linesReturn
	if hexvalue == "001011":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means: The wild goose gradually draws near the shore.  The young son is in danger. There is talk. No blame.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means: The wild goose gradually draws near the cliff. Eating and drinking in peace and concord. Good fortune.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means: The wild goose gradually draws near the plateau. The man goes forth and does not return. The woman carries a child but does not bring it forth. Misfortune.  It furthers one to fight off robbers.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means: The wild goose goes gradually draws near the tree. Perhaps it will find a flat branch. No blame.  "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means: The wild goose gradually draws near the summit. For three years the woman has no child. In the end nothing can hinder her. Good fortune.  "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means: The wild goose gradually draws near the clouds heights. Its feathers can be used for the sacred dance. Good fortune.  "
		return linesReturn
	if hexvalue == "110100":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means: The marrying maiden as a concubine. A lame man who is able to tread. Undertakings bring good fortune.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means: A one-eyed man who is able to see. The perseverance of a solitary man furthers.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means: The marrying maiden as a slave. She marries as a concubine.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means: The marrying maiden draws out the allotted time. A late marriage comes in due course.intended for her.   "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means: The sovereign I gave his daughter in marriage. The embroidered garments of the princess Were not as gorgeous As those of the serving maid. The moon that is nearly full Brings good fortune.  "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means: The woman holds the basket, but there are no fruits in it. The man stabs the sheep, but no blood flows. Nothing that acts to further.   "
		return linesReturn
	if hexvalue == "101100":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means: When a man meets his destined ruler, They can be together ten days, And it is not a mistake. Going meets with recognition.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means: The curtain is of such fullness That the polestars can be seen at noon. Through going one meets with mistrust and hate. If one rouses him through truth, Good fortune comes.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means: The underbrush is of such abundance That the small stars can be seen at noon. He breaks his right arm . No blame.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means: The curtain is of such fullness That the polestars can be seen at noon. He meets his ruler, who is of like kind. Good fortune.  "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means: Lines are coming, Blessing and fame draw near. Good fortune.  "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means: His house is in a state of abundance. He screens off his family. He peers through the gate And no longer perceives anyone. For three years he sees nothing. Misfortune.  "
		return linesReturn
	if hexvalue == "001101":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means: If the wanderer busies himself with trivial things,  He draws down misfortune upon himself.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means: The wanderer comes to an inn. He has his property with him. He wins the steadfastness of a young servant.   "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means: The wanderer's inn burns down. He loses the steadfastness of his young servant. Danger.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means: The wanderer rests in a shelter. He obtains his property and an ax. My heart is not glad.  "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means: He shoots a pheasant. It drops with the first arrow. In the end this brings both praise and office.  "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means: The bird's nest burns up. The wanderer laughs at first, Then must needs lament and weep. Through carelessness he loses his cow. Misfortune.  "
		return linesReturn
	if hexvalue == "011011":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means: In advancing and in retreating, The perseverance of a warrior furthers.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means: Penetration under the bed. Priests and magicians are used in great number. Good fortune. No blame.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means: Repeated penetration. Humiliation.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means: Remorse vanishes. During the hunt Three kinds of game are caught.  "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means: Perseverance brings good fortune. Remorse vanishes. Nothing that does not further. No beginning, but an end. Before the change, three days. After the change, three days. Good fortune.  "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means: Penetration under the bed. He loses his property and his ax. Perseverance brings misfortune.  "
		return linesReturn
	if hexvalue == "110110":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means: Contented joyousness. Good fortune.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means: Sincere joyousness. Good fortune. Remorse disappears.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means: Coming joyousness. Misfortune.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means: Joyousness that is weighed is not at peace. After ridding himself of mistakes a man has joy.  "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means: Sincerity toward disintegrating influences is dangerous.  "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means: Seductive joyousness.  "
		return linesReturn
	if hexvalue == "010011":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means: He brings help with the strength of a horse. Good fortune.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means: At the dissolution He hurries to that which supports him. Remorse disappears.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means: He dissolves his self. No remorse.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means: He dissolves his bond with his group. Supreme good fortune. Dispersion leads in turn to accumulation. This is something that ordinary men do not think of.  "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means: His loud cries are as dissolving as sweat. Dissolution! A king abides without blame.   "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means: He dissolves his blood. Departing, keeping at a distance, going out, Is without blame.  "
		return linesReturn
	if hexvalue == "110010":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means: Not going out of the door and the courtyard Is without blame.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means: Not going out of the gate and the courtyard Brings misfortune.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means: He who knows limitation Will have cause to lament. No blame.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means: Contented limitation. Success.  "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means: Sweet limitation brings good fortune. Going brings esteem.   "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means: Galling limitation. Perseverance brings misfortune. Remorse disappears.  "
		return linesReturn
	if hexvalue == "110011":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means: Being prepared brings good fortune. If there are secret designs, it is disquieting.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means: A crane calling in the shade. Its young answers it. I have a good goblet. I will share it with you.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means: He finds a comrade. Now he beats the drum, now he stops. Now he sobs, now he sings.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means: The moon nearly at the full. The team horse goes astray. No blame.  "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means: He possesses truth, which links together. No blame.  "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means: Cockcrow penetrating to heaven. Perseverance brings misfortune.  "
		return linesReturn
	if hexvalue == "001100":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means: The bird meets with misfortune through flying.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means: She passes by her ancestor And meets her ancestress. He does not reach his prince And meets the official. No blame.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means: If one is not extremely careful, Somebody may come up from behind and strike him. Misfortune.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means: No blame. He meets him without passing by. Going brings danger. One must be on guard. Do not act. Be constantly persevering.  "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means: Dense clouds, No rain from our western territory. The prince shoots and hits him who is in the cave.  "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means: He passes him by, not meeting him. The flying bird leaves him. Misfortune. This means bad luck and injury.  "
		return linesReturn
	if hexvalue == "101010":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means: He breaks his wheels. He gets his tail in the water. No blame.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means: The woman loses the curtain of her carriage. Do not run after it; On the seventh day you will get it.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means: The Illustrious Ancestor Disciplines the Devil's Country. After three years he conquers it. Inferior people must not be employed.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means: The finest clothes turn to rags. Be careful all day long.  "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means: The neighbor in the east who slaughters an ox Does not attain as much real happiness As the neighbor in the west With his small offering.  "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means: He gets his head in the water. Danger.  "
		return linesReturn
	if hexvalue == "010101":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means: He gets his tail in the water. Humiliating.  "
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means: He brakes his wheels. Perseverance brings good fortune.  "
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means: Before completion, attack brings misfortune. It furthers one to cross the great water.  "
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means: Perseverance brings good fortune. Remorse disappears. Shock, thus to discipline the Devil's Country. For three years, great realms are rewarded.  "
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means: Perseverance brings good fortune. No remorse. The light of the superior man is true. Good fortune.  "
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means: There is drinking of wine In genuine confidence. No blame. But if one wets his head, He loses it, in truth.  "
		return linesReturn


def interpret_judgment(hexvalue):
	if hexvalue == "111111":
		return "THE CREATIVE works sublime success, Furthering through perseverance."
	if hexvalue == "000000":
		return "THE RECEPTIVE brings about sublime success, Furthering through the perseverance of a mare. If the superior man undertakes something and tries to lead, He goes astray; But if he follows, he finds guidance. It is favorable to find friends in the west and south, To forego friends in the east and north. Quiet perseverance brings good fortune."
	if hexvalue == "100010":
		return "DIFFICULTY AT THE BEGINNING works supreme success, Furthering through perseverance. Nothing should be undertaken. It furthers one to appoint helpers."
	if hexvalue == "010001":
		return "YOUTHFUL FOLLY has success. It is not I who seek the young fool; The young fool seeks me. At the first oracle I inform him.  If he asks two or three times, it is importunity. If he importunes, I give him no information. Perseverance furthers."
	if hexvalue == "111010":
		return "WAITING. If you are sincere,  You have light and success. Perseverance brings good fortune. It furthers one to cross the great water."
	if hexvalue == "010111":
		return "CONFLICT. You are sincere And are being obstructed. A cautious halt halfway brings good fortune. Going through to the end brings misfortune. It furthers one to see the great man. It does not further one to cross the great water."
	if hexvalue == "010000":
		return "THE ARMY. The army needs perseverance And a strong man. Good fortune without blame."
	if hexvalue == "000010":
		return "HOLDING TOGETHER brings good fortune. Inquire of the oracle once again Whether you possess sublimity, constancy, and perseverance; Then there is no blame. Those who are uncertain gradually join. Whoever come too late Meets with misfortune."
	if hexvalue == "111011":
		return "THE TAMING POWER OF THE SMALL Has success. Dense clouds, no rain from our western region."
	if hexvalue == "110111":
		return "TREADING. Treading upon the tail of the tiger. It does not bite the man. Success."
	if hexvalue == "111000":
		return "nPEACE. The small departs, The great approaches. Good fortune. Success."
	if hexvalue == "000111":
		return "STANDSTILL. Evil people do not further The perseverance of the superior man. The great departs; the small approaches."
	if hexvalue == "101111":
		return "FELLOWSHIP WITH MEN in the open. Success. It furthers one to cross the great water. The perseverance of the superior man furthers."
	if hexvalue == "111101":
		return "POSSESSION IN GREAT MEASURE. Supreme success."
	if hexvalue == "001000":
		return "MODESTY creates success. The superior man carries things through."
	if hexvalue == "000100":
		return "ENTHUSIASM. It furthers one to install helpers And to set armies marching."
	if hexvalue == "100110":
		return "FOLLOWING has supreme success. Perseverance furthers. No blame."
	if hexvalue == "011001":
		return "WORK ON WHAT HAS BEEN SPOILED Has supreme success. It furthers one to cross the great water. Before the starting point, three days. After the starting point, three days."
	if hexvalue == "110000":
		return "APPROACH has supreme success. Perseverance furthers. When the eighth month comes, There will be misfortune."
	if hexvalue == "000011":
		return "CONTEMPLATION. The ablution has been made,  But not yet the offering. Full of trust they look up to him."
	if hexvalue == "100101":
		return "BITING THROUGH has success. It is favorable to let justice be administered."
	if hexvalue == "101001":
		return "GRACE has success. In small matters It is favorable to undertake something."
	if hexvalue == "000001":
		return "SPLITTING APART. IT does not further one  To go anywhere."
	if hexvalue == "100000":
		return "RETURN. Success. Going out and coming in without error. Friends come without blame. To and fro goes the way. On the seventh day comes return. It furthers one to have somewhere to go."
	if hexvalue == "100111":
		return "INNOCENCE. Supreme success. Perseverance furthers. If someone is not as he should be, He has misfortune, And it does not further him To undertake anything."
	if hexvalue == "111001":
		return "THE TAMING POWER OF THE GREAT. Perseverance furthers. Not eating at home brings good fortune. It furthers one to cross the great water."
	if hexvalue == "100001":
		return "THE CORNERS OF THE MOUTH. Perseverance brings good fortune. Pay heed to the providing of nourishment And to what a man seeks To fill his own mouth with."
	if hexvalue == "011110":
		return "PREPONDERANCE OF THE GREAT. The ridgepole sags to the breaking point. It furthers one to have somewhere to go. Success."
	if hexvalue == "010010":
		return "The Abysmal repeated. If you are sincere, you have success in your heart, And whatever you do succeeds."
	if hexvalue == "101101":
		return "THE CLINGING. Perseverance furthers. It brings success. Care of the cow brings good fortune."
	if hexvalue == "001110":
		return "Influence. Success. Perseverance furthers. To take a maiden to wife brings good fortune."
	if hexvalue == "011100":
		return "DURATION. Success. No blame. Perseverance furthers. It furthers one to have somewhere to go."
	if hexvalue == "001111":
		return "RETREAT. Success. In what is small, perseverance furthers."
	if hexvalue == "111100":
		return "THE POWER OF THE GREAT. Perseverance furthers."
	if hexvalue == "000101":
		return "PROGRESS. The powerful prince Is honored with horses in large numbers. In a single day he is granted audience three times."
	if hexvalue == "101000":
		return "DARKENING OF THE LIGHT. In adversity It furthers one to be persevering."
	if hexvalue == "101011":
		return "THE FAMILY. The perseverance of the woman furthers."
	if hexvalue == "110101":
		return "OPPOSITION. In small matters, good fortune."
	if hexvalue == "001010":
		return "OBSTRUCTION. The southwest furthers. The northeast does not further. It furthers one to see the great man. Perseverance brings good fortune."
	if hexvalue == "010100":
		return "DELIVERANCE. The southwest furthers. If there is no longer anything where one has to go, Return brings good fortune. If there is still something where one has to go, Hastening brings good fortune."
	if hexvalue == "110001":
		return "DECREASE combined with sincerity Brings about supreme good fortune Without blame. One may be persevering in this. It furthers one to undertake something. How is this to be carried out? One may use two small bowls for the sacrifice."
	if hexvalue == "100011":
		return "INCREASE. It furthers one To undertake something. It furthers one to cross the great water."
	if hexvalue == "111110":
		return "BREAK-THROUGH. One must resolutely make the matter known At the court of the king. It must be announced truthfully. Danger. It is necessary to notify one's own city. It does not further to resort to arms. It furthers one to undertake something."
	if hexvalue == "011111":
		return "COMING TO MEET. The maiden is powerful. One should not marry such a maiden."
	if hexvalue == "000110":
		return "GATHERING TOGETHER. Success. The king approaches his temple. It furthers one to see the great man. This brings success. Perseverance furthers. To bring great offerings creates good fortune. It furthers one to undertake something."
	if hexvalue == "011000":
		return "PUSHING UPWARD has supreme success. One must see the great man. Fear not. Departure toward the south Brings good fortune."
	if hexvalue == "010110":
		return "OPPRESSION. Success. Perseverance. The great man brings about good fortune. No blame. When one has something to say, It is not believed."
	if hexvalue == "011010":
		return "THE WELL. The town may be changed, But the well cannot be changed. It neither decreases nor increases. They come and go and draw from the well. If one gets down almost to the water And the rope does not go all the way, Or the jug breaks, it brings misfortune."
	if hexvalue == "101110":
		return "REVOLUTION. On your own day You are believed. Supreme success, Furthering through perseverance. Remorse disappears."
	if hexvalue == "011101":
		return "THE CALDRON. Supreme good fortune. Success."
	if hexvalue == "100100":
		return "SHOCK brings success. Shock comes-oh, oh! Laughing words -ha, ha! The shock terrifies for a hundred miles, And he does not let fall the sacrificial spoon and chalice."
	if hexvalue == "001001":
		return "KEEPING STILL. Keeping his back still So that he no longer feels his body. He goes into his courtyard And does not see his people. No blame."
	if hexvalue == "001011":
		return "DEVELOPMENT. The maiden Is given in marriage. Good fortune. Perseverance furthers."
	if hexvalue == "110100":
		return "THE MARRYING MAIDEN. Undertakings bring misfortune. Nothing that would further."
	if hexvalue == "101100":
		return "ABUNDANCE has success. The king attains abundance. Be not sad. Be like the sun at midday."
	if hexvalue == "001101":
		return "The Wanderer. Success through smallness. Perseverance brings good fortune To the Wanderer."
	if hexvalue == "011011":
		return "THE GENTLE. Success through what is small. It furthers one to have somewhere to go. It furthers one to see the great man."
	if hexvalue == "110110":
		return "THE JOYOUS. Success. Perseverance is favorable."
	if hexvalue == "010011":
		return "DISPERSION. Success. The king approaches his temple. It furthers one to cross the great water. Perseverance furthers."
	if hexvalue == "110010":
		return "LIMITATION. Success. Galling limitation must not be persevered in."
	if hexvalue == "110011":
		return "INNER TRUTH. Pigs and fishes. Good fortune. It furthers one to cross the great water. Perseverance furthers."
	if hexvalue == "001100":
		return "PREPONDERANCE OF THE SMALL. Success. Perseverance furthers. Small things may be done; great things should not be done. The flying bird brings the message: It is not well to strive upward, It is well to remain below. Great good fortune."
	if hexvalue == "101010":
		return "AFTER COMPLETION. Success in small matters. Perseverance furthers. At the beginning good fortune. At the end disorder."
	if hexvalue == "010101":
		return "BEFORE COMPLETION. Success. But if the little fox, after nearly completing the crossing, Gets his tail in the water, There is nothing that would further."

def interpret_image(hexvalue):
	if hexvalue == "111111":
		return "The movement of heaven is full of power. Thus the superior man makes himself strong and untiring."
	if hexvalue == "000000":
		return "The earth's condition is receptive devotion. Thus the superior man who has breadth of character Carries the outer world."
	if hexvalue == "100010":
		return "Clouds and thunder: The image of DIFFICULTY AT THE BEGINNING. Thus the superior man Brings order out of confusion."
	if hexvalue == "010001":
		return "A spring wells up at the foot of the mountain:  The image of YOUTH. Thus the superior man fosters his character By thoroughness in all that he does."
	if hexvalue == "111010":
		return "Clouds rise up to heaven: The image of WAITING. Thus the superior man eats and drinks, Is joyous and of good cheer"
	if hexvalue == "010111":
		return "Heaven and water go their opposite ways: The image of CONFLICT. Thus in all his transactions the superior man Carefully considers the beginning."
	if hexvalue == "010000":
		return "In the middle of the earth is water: The image of THE ARMY. Thus the superior man increases his masses By generosity toward the people."
	if hexvalue == "000010":
		return "On the earth is water: The image of HOLDING TOGETHER. Thus the kings of antiquity Bestowed the different states as fiefs And cultivated friendly relations With the feudal lords."
	if hexvalue == "111011":
		return "The wind drives across heaven: The image of THE TAMING POWER OF THE SMALL. Thus the superior man Refines the outward aspect of his nature."
	if hexvalue == "110111":
		return "Heaven above, the lake below: The image of TREADING. Thus the superior man discriminates between high and low, And thereby fortifies the thinking of the people."
	if hexvalue == "111000":
		return "Heaven and earth unite: the image of PEACE. Thus the ruler Divides and completes the course of heaven and earth, And so aids the people."
	if hexvalue == "000111":
		return "Heaven and earth do not unite: The image of STANDSTILL. Thus the superior man falls back upon his inner worth  In order to escape the difficulties. He does not permit himself to be honored with revenue."
	if hexvalue == "101111":
		return "Heaven together with fire: The image of FELLOWSHIP WITH MEN. Thus the superior man organizes the clans And makes distinctions between things."
	if hexvalue == "111101":
		return "Fire in heaven above: the image of POSSESSION IN GREAT MEASURE. Thus the superior man curbs evil and furthers good, And thereby obeys the benevolent will of heaven."
	if hexvalue == "001000":
		return "Within the earth, a mountain: The image of MODESTY. Thus the superior man reduces that which is too much, And augments that which is too little. He weighs things and makes them equal."
	if hexvalue == "000100":
		return "Thunder comes resounding out of the earth: The image of ENTHUSIASM. Thus the ancient kings made music  In order to honor merit, And offered it with splendor To the Supreme Deity, Inviting their ancestors to be present."
	if hexvalue == "100110":
		return "Thunder in the middle of the lake: The image of FOLLOWING. Thus the superior man at nightfall Goes indoors for rest and recuperation."
	if hexvalue == "011001":
		return "The wind blows low on the mountain: The image of DECAY. Thus the superior man stirs up the people And strengthens their spirit."
	if hexvalue == "110000":
		return "The earth above the lake: The image of APPROACH. Thus the superior man is inexhaustible In his will to teach, And without limits In his tolerance and protection of the people."
	if hexvalue == "000011":
		return "The wind blows over the earth: The image of CONTEMPLATION. Thus the kings of old visited the regions of the world, Contemplated the people, And gave them instruction."
	if hexvalue == "100101":
		return "Thunder and lighting: The image of BITING THROUGH. Thus the kings of former times made firm the laws Through clearly defined penalties."
	if hexvalue == "101001":
		return "Fire at the foot of the mountain: The image of GRACE. Thus does the superior man proceed  When clearing up current affairs. But he dare not decide controversial issues in this way."
	if hexvalue == "000001":
		return "The mountain rests on the earth: The image of SPLITTING APART. Thus those above can ensure their position Only by giving generously to those below."
	if hexvalue == "100000":
		return "Thunder within the earth: The image of THE TURNING POINT Thus the kings of antiquity closed the passes  At the time of solstice. Merchants and strangers did not go about, And the ruler Did not travel through the provinces."
	if hexvalue == "100111":
		return "Under heaven thunder rolls: All things attain the natural state of innocence. Thus the kings of old, Rich in virtue, and in harmony with the time, Fostered and nourished all beings."
	if hexvalue == "111001":
		return "Heaven within the mountain: The image of THE TAMING POWER OF THE GREAT. Thus the superior man acquaints himself with many sayings of antiquity And many deeds of the past, In order to strengthen his character thereby."
	if hexvalue == "100001":
		return "At the foot of the mountain, thunder: The image of PROVIDING NOURISHMENT. Thus the superior man is careful of his words And temperate in eating and drinking."
	if hexvalue == "011110":
		return "The lake rises above the trees: The image of PREPONDERANCE OF THE GREAT. Thus the superior man, when he stands alone, Is unconcerned, And if he has to renounce the world, He is undaunted."
	if hexvalue == "010010":
		return "Water flows on uninterruptedly and reaches its goal: The image of the Abysmal repeated. Thus the superior man walks in lasting virtue And carries on the business of teaching."
	if hexvalue == "101101":
		return "That which is bright rises twice: The image of FIRE. Thus the great man, by perpetuating this brightness, Illumines the four quarters of the world."
	if hexvalue == "001110":
		return "A lake on the mountain: The image of influence. Thus the superior man encourages people to approach him By his readiness to receive them."
	if hexvalue == "011100":
		return "Thunder and wind: the image of DURATION. Thus the superior man stands firm  And does not change has direction."
	if hexvalue == "001111":
		return "Mountain under heaven: the image of RETREAT. Thus the superior man keeps the inferior man at a distance, Not angrily but with reserve."
	if hexvalue == "111100":
		return "Thunder in heaven above: The image of THE POWER OF THE GREAT. Thus the superior man does not tread upon paths That do not accord with established order."
	if hexvalue == "000101":
		return "The sun rises over the earth: The image of PROGRESS. Thus the superior man himself Brightens his bright virtue."
	if hexvalue == "101000":
		return "The light has sunk into the earth: The image of DARKENING OF THE LIGHT. Thus does the superior man live with the great mass: He veils his light, yet still shines."
	if hexvalue == "101011":
		return "Wind comes forth from fire The image of THE FAMILY. Thus the superior man has substance in his word And duration in his way of life."
	if hexvalue == "110101":
		return "Above, fire; below. The lake The image of OPPOSITION Thus amid all fellowship The superior man retains his individuality."
	if hexvalue == "001010":
		return "Water on the mountain The image of OBSTRUCTION Thus the superior man turns his attention to himself And molds his character."
	if hexvalue == "010100":
		return "Thunder and rain set in The image of DELIVERANCE Thus the superior man pardons mistakes And forgives misdeeds."
	if hexvalue == "110001":
		return "At the foot of the mountain, the lake The image of DECREASE Thus the superior man controls his ange And restrains his instincts."
	if hexvalue == "100011":
		return "Wind and thunder: the image of INCREASE Thus the superior man If he sees good, he imitates it If he has faults, he rids himself of them."
	if hexvalue == "111110":
		return "The lake has risen up to heaven: The image of BREAK-THROUGH. Thus the superior man Dispenses riches downward And refrains from resting on his virtue."
	if hexvalue == "011111":
		return "Under heaven, wind The image of COMING TO MEET Thus does the prince act when disseminating his command And proclaiming them to the four quarters of heaven."
	if hexvalue == "000110":
		return "Over the earth, the lake The image of GATHERING TOGETHER Thus the superior man renews his weapon In order to meet the unforeseen."
	if hexvalue == "011000":
		return "Within the earth, wood grows The image of PUSHING UPWARD Thus the superior man of devoted characte Heaps up small thing In order to achieve something high and great."
	if hexvalue == "010110":
		return "There is not water in the lake The image of EXHAUSTION Thus the superior man stakes his life On following his will."
	if hexvalue == "011010":
		return "Water over wood: the image of THE WELL Thus the superior man encourages the people at their work And exhorts them to help one another."
	if hexvalue == "101110":
		return "Fire in the lake: the image of REVOLUTION Thus the superior man Sets the calendar in orde And makes the seasons clear."
	if hexvalue == "011101":
		return "Fire over wood The image of THE CALDRON Thus the superior man consolidates his fate By making his position correct."
	if hexvalue == "100100":
		return "Thunder repeated: the image of SHOCK Thus in fear and tremblin The superior man sets his life in orde And examines himself."
	if hexvalue == "001001":
		return "Mountains standing close together The image of KEEPING STILL Thus the superior man Does not permit his thoughts To go beyond his situation."
	if hexvalue == "001011":
		return "On the mountain, a tree The image of DEVELOPMENT Thus the superior man abides in dignity and virtue In order to improve the mores."
	if hexvalue == "110100":
		return "Thunder over the lake The image of THE MARRYING MAIDEN Thus the superior man Understands the transitor In the light of the eternity of the end."
	if hexvalue == "101100":
		return "Both thunder and lightning come The image of ABUNDANCE Thus the superior man decides lawsuit And carries out punishments."
	if hexvalue == "001101":
		return "Fire on the mountain The image of THE WANDERER Thus the superior man Is clear-minded and cautious In imposing penalties And protracts no lawsuits."
	if hexvalue == "011011":
		return "Winds following one upon the other The image of THE GENTLY PENETRATING Thus the superior man Spreads his commands abroad And carries out his undertakings."
	if hexvalue == "110110":
		return "Lakes resting one on the other The image of THE JOYOUS Thus the superior man joins with his friend For discussion and practice."
	if hexvalue == "010011":
		return "The wind drives over the water The image of DISPERSION Thus the kings of old sacrificed to the Lor And built temples."
	if hexvalue == "110010":
		return "Water over lake: the image of LIMITATION Thus the superior man Creates number and measure And examines the nature of virtue and correct conduct."
	if hexvalue == "110011":
		return "Wind over lake: the image of INNER TRUTH Thus the superior man discusses criminal cases In order to delay executions."
	if hexvalue == "001100":
		return "Thunder on the mountain: The image of PREPONDERANCE OF THE SMALL. Thus in his conduct the superior man gives preponderance to reverence. In bereavement he gives preponderance to grief. In his expenditures he gives preponderance to thrift."
	if hexvalue == "101010":
		return "Water over fire: the image of the condition In AFTER COMPLETION Thus the superior man Takes thought of misfortun And arms himself against it in advance."
	if hexvalue == "010101":
		return "Fire over water: The image of the condition before transition. Thus the superior man is careful In the differentiation of things, So that each finds its place."

def interpret_hexagram(hexvalue):
	if hexvalue == "111111":
		return "䷀ (Ch'ien) The Creative - 1"
	if hexvalue == "000000":
		return "䷁ (K'un) The Receptive - 2"
	if hexvalue == "100010":
		return "䷂ (Chun) Difficulty at the Beginning - 3"
	if hexvalue == "010001":
		return "䷃ (Meng) Youthful Folly - 4"
	if hexvalue == "111010":
		return "䷄ (Hsu) Waiting (Nourishment) - 5"
	if hexvalue == "010111":
		return "䷅ (Sung) Conflict - 6"
	if hexvalue == "010000":
		return "䷆ (Shih) The Army - 7"
	if hexvalue == "000010":
		return "䷇ (Pi) Holding Together [union] - 8"
	if hexvalue == "111011":
		return "䷈ (Hsiao Ch'u) The Taming Power of the Small - 9"
	if hexvalue == "110111":
		return "䷉ (Lu) Treading [conduct] - 10"
	if hexvalue == "111000":
		return "䷊ (T'ai) Peace - 11"
	if hexvalue == "000111":
		return "䷋ (P'i) Standstill [Stagnation] - 12"
	if hexvalue == "101111":
		return "䷌ (T'ung Jen) Fellowship with Men - 13"
	if hexvalue == "111101":
		return "䷍ (Ta Yu) Possession in Great Measure - 14"
	if hexvalue == "001000":
		return "䷎ (Ch'ien) Modesty - 15"
	if hexvalue == "000100":
		return "䷏ (Yu) Enthusiasm - 16"
	if hexvalue == "100110":
		return "䷐ (Sui) Following - 17"
	if hexvalue == "011001":
		return "䷑ (Ku) Work on what has been spoiled [ Decay ] - 18"
	if hexvalue == "110000":
		return "䷒ (Lin) Approach - 19"
	if hexvalue == "000011":
		return "䷓ (Kuan) Contemplation (View) - 20"
	if hexvalue == "100101":
		return "䷔ (Shih Ho) Biting Through - 21"
	if hexvalue == "101001":
		return "䷕ (Pi) Grace - 22"
	if hexvalue == "000001":
		return "䷖ (Po) Splitting Apart - 23"
	if hexvalue == "100000":
		return "䷗ (Fu) Return (The Turning Point) - 24"
	if hexvalue == "100111":
		return "䷘ (Wu Wang) Innocence (The Unexpected) - 25"
	if hexvalue == "111001":
		return "䷙ (Ta Ch'u) The Taming Power of the Great - 26"
	if hexvalue == "100001":
		return "䷚ (I) Corners of the Mouth (Providing Nourishment) - 27"
	if hexvalue == "011110":
		return "䷛ (Ta Kuo) Preponderance of the Great - 28"
	if hexvalue == "010010":
		return "䷜ (K'an) The Abysmal (Water) - 29"
	if hexvalue == "101101":
		return "䷝ (Li) The Clinging, Fire - 30"
	if hexvalue == "001110":
		return "䷞ (Hsien) Influence (Wooing) - 31"
	if hexvalue == "011100":
		return "䷟ (Heng) Duration - 32"
	if hexvalue == "001111":
		return "䷠ (TUN) Retreat - 33"
	if hexvalue == "111100":
		return "䷡ (Ta Chuang) The Power of the Great - 34"
	if hexvalue == "000101":
		return "䷢ (Chin) Progress - 35"
	if hexvalue == "101000":
		return "䷣ (Ming I) Darkening of the light - 36"
	if hexvalue == "101011":
		return "䷤ (Chia Jen) The Family [The Clan] - 37"
	if hexvalue == "110101":
		return "䷥ (K'uei) Opposition - 38"
	if hexvalue == "001010":
		return "䷦ (Chien) Obstruction - 39"
	if hexvalue == "010100":
		return "䷧ (Hsieh) Deliverance - 40"
	if hexvalue == "110001":
		return "䷨ (Sun) Decrease - 41"
	if hexvalue == "100011":
		return "䷩ (I) Increase - 42"
	if hexvalue == "111110":
		return "䷪ (Kuai) Break-through (Resoluteness) - 43"
	if hexvalue == "011111":
		return "䷫ (Kou) Coming to Meet - 44"
	if hexvalue == "000110":
		return "䷬ (Ts'ui) Gathering Together [Massing] - 45"
	if hexvalue == "011000":
		return "䷭ (Sheng) Pushing Upward - 46"
	if hexvalue == "010110":
		return "䷮ (K'un) Oppression (Exhaustion) - 47"
	if hexvalue == "011010":
		return "䷯ (Ching) The Well - 48"
	if hexvalue == "101110":
		return "䷰ (Ko) Revolution (Molting) - 49"
	if hexvalue == "011101":
		return "䷱ (Ting) The Caldron - 50"
	if hexvalue == "100100":
		return "䷲ (Chen) The Arousing (Shock, Thunder) - 51"
	if hexvalue == "001001":
		return "䷳ (Ken) Keeping Still, Mountain - 52"
	if hexvalue == "001011":
		return "䷴ (Chien) Development (Gradual Progress) - 53"
	if hexvalue == "110100":
		return "䷵ (Kuei Mei) The Marrying Maiden - 54"
	if hexvalue == "101100":
		return "䷶ (Feng) Abundance [Fullness] - 55"
	if hexvalue == "001101":
		return "䷷ (Lu) The Wanderer - 56"
	if hexvalue == "011011":
		return "䷸ (Sun) The Gentle (The Penetrating, Wind) - 57"
	if hexvalue == "110110":
		return "䷹ (Tui) The Joyous, Lake - 58"
	if hexvalue == "010011":
		return "䷺ (Huan) Dispersion [Dissolution] - 59"
	if hexvalue == "110010":
		return "䷻ (Chieh) Limitation - 60"
	if hexvalue == "110011":
		return "䷼ (Chung Fu) Inner Truth - 61"
	if hexvalue == "001100":
		return "䷽ (Hsiao Kuo) Preponderance of the Small - 62"
	if hexvalue == "101010":
		return "䷾ (Chi Chi) After Completion - 63"
	if hexvalue == "010101":
		return "䷿ (Wei Chi) Before Completion - 64"

def interpretUpperTrigram(hexagram):
	#get upper trigram
	uppertest = hexagram[-3:]
	upperTrigram = ""
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
	return upperTrigram

def interpretLowerTrigram(hexagram):
	#get lower trigram
	lowertest = hexagram[:3]
	lowerTrigram = ""
	if lowertest == "000":
		lowerTrigram = "Earth"
	if lowertest == "001":
		lowerTrigram = "Mountain"
	if lowertest == "010":
		lowerTrigram = "Water"
	if lowertest == "011":
		lowerTrigram = "Wood"
	if lowertest == "100":
		lowerTrigram = "Thunder"
	if lowertest == "101":
		lowerTrigram = "Fire"
	if lowertest == "110":
		lowerTrigram = "Lake"
	if lowertest == "111":
		lowerTrigram = "Heaven"
	return lowerTrigram

def printHexagram(hexagram,lines):
	for x in reversed(xrange(3, 6)):
		if hexagram[x] == "1":
			if lines[x] == "1":
				print "------ *"
			else:
				print "------"
		else:
			if lines[x] == "1":
				print "--  -- *"
			else:
				print "--  --"
	for x in reversed(xrange(0, 3)):
		if hexagram[x] == "1":
			if lines[x] == "1":
				print "------ *"
			else:
				print "------"
		else:
			if lines[x] == "1":
				print "--  -- *"
			else:
				print "--  --"

def outputHexagram(hexagram):
	print hexagram.title

	print hexagram.upperTrigram + '/' + hexagram.lowerTrigram

	print '\n---The Judgement---'
	print hexagram.theJudgment

	print '\n---The Image---'
	print hexagram.theImage

	if hexagram.theLines != '':
		print '\n---The Lines---'
		print hexagram.theLines


def createHexagram(randomSeed):
	#get random seed from first argument
	if randomSeed == None:
		randomSeed = 'yinyang'

	#---Three Coin Toss Method---
	#----------------------------
	hexagram = ""
	lines = ""
	lowerTrigram = ""
	upperTrigram = ""
	hexagramNumber = 0

	#grab time
	ts = time.time()
	#format the time
	st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	#add random seed to timestamp
	momentarySeed = randomSeed + unicode(ts)
	#seed the random number generator
	random.seed(momentarySeed)

	for x in xrange(0, 6):
		val1 = random.random()
		val2 = random.random()
		val3 = random.random()
		if val1 > 0.5:
			if val2 > 0.5:
				if val3 > 0.5:
					lines += "1"
					hexagram += "1"
				elif val3 < 0.5:
					lines += "0"
					hexagram += "1"
			elif val2 < 0.5:
				if val3 > 0.5:
					lines += "0"
					hexagram += "1"
				if val3 < 0.5:
					lines += "0"
					hexagram += "0"
		elif val1 < 0.5:
			if val2 < 0.5:
				if val3 < 0.5:
					lines += "1"
					hexagram += "0"
				elif val3 > 0.5:
					lines += "0"
					hexagram += "0"
			elif val2 > 0.5:
				if val3 < 0.5:
					lines += "0"
					hexagram += "0"
				if val3 > 0.5:
					lines += "0"
					hexagram += "1"

	title = interpret_hexagram(hexagram)
	theImage = interpret_image(hexagram)
	theJudgment = interpret_judgment(hexagram)
	theLines = interpret_lines(hexagram, lines)
	upperTrigram = interpretUpperTrigram(hexagram)
	lowerTrigram = interpretLowerTrigram(hexagram)

	hexagramReturn = hexagramObject(title,theImage,theJudgment,theLines,upperTrigram,lowerTrigram,hexagram,lines)
	return hexagramReturn

def ChingChain(initialHexagram, chainLength):
	#Calculate the movement from starting point {initialHexagram} for {chainLength} number of hexagrams.
	#These always result in repeating patterns of 4 hexagrams
	hexagrams = [initialHexagram]
	tempHex = list(initialHexagram.hexagram)
	tempLines = list(initialHexagram.lines)
	for x in range(0, chainLength):
		newesthex = []
		newestline = []
		for y in xrange(0, 6):
			if tempHex[y] == '0':
				if tempLines[y] == '1':
					newesthex.append('1')
				else:
					newesthex.append('0')
			elif tempHex[y] == '1':
				if tempLines[y] == '1':
					newesthex.append('0')
				else:
					newesthex.append('1')
		for z in xrange(0, 6):
			if tempLines[z] == '0':
				newestline.append('1')
			if tempLines[z] == '1':
				newestline.append('0')

		tempHex = newesthex
		tempLines = newestline

		hexagrams.append(getHexagramFromBytes(''.join(newesthex),''.join(newestline)))
	return hexagrams

def getHexagramFromBytes(hexagramByte="111111",linesByte="000000"):
	#---Get a specific hexagram by its hexagram byte---
	title = interpret_hexagram(hexagramByte)
	theImage = interpret_image(hexagramByte)
	theJudgment = interpret_judgment(hexagramByte)
	theLines = interpret_lines(hexagramByte, linesByte)
	upperTrigram = interpretUpperTrigram(hexagramByte)
	lowerTrigram = interpretLowerTrigram(hexagramByte)

	hexagramReturn = hexagramObject(title,theImage,theJudgment,theLines,upperTrigram,lowerTrigram,hexagramByte,linesByte)
	return hexagramReturn


#-----------------------------------------
#-------------ARGUMENTS-------------------
#-----------------------------------------
randomSeed = 'yinyang'
arg1 = sys.argv[0]
if arg1 != '':
	randomSeed = arg1


#-----------------------------------------
#---------------INITS---------------------
#-----------------------------------------
outputHexagram(createHexagram(randomSeed))
