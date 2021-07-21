# -*- coding: latin-1 -*-
import sched, time, datetime, random, os, sys

#----------------------------------------------------------------
#-------------Hexagram Interpretation Functions------------------
#----------------------------------------------------------------
def interpret_lines(hexvalue,linesvalue):
	if hexvalue == "111111":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:<br>Hidden dragon. Do not act.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:<br>Dragon appearing in the field.<br>It furthers one to see the great man.<br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means:<br>All day long the superior man is creatively active.<br>At nightfall his mind is still beset with cares.<br>Danger. No blame.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:<br>Wavering flight over the depths.<br>No blame.<br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:<br>Flying dragon in the heavens.<br>It furthers one to see the great man.<br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:<br>Arrogant dragon will have cause to repent.<br>When all the lines are nines, it means:<br>There appears a flight of dragons without heads.<br>Good fortune.<br><br>"
		return linesReturn
	if hexvalue == "000000":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means:<br>When there is hoarfrost underfoot,<br>Solid ice is not far off.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:<br>Straight, square, great.<br>Without purpose,<br>Yet nothing remains unfurthered.<br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:<br>Hidden lines.<br>One is able to remain persevering.<br>If by chance you are in the service of a king,<br>Seek not works, but bring to completion.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:<br>A tied-up sack. No blame, no praise.<br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:<br>A yellow lower garment brings supreme good fortune.<br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:<br>Dragons fight in the meadow.<br>Their blood is black and yellow.<br><br>When all the lines are sixes, it means:<br>Lasting perseverance furthers.<br><br>"
		return linesReturn
	if hexvalue == "100010":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:<br>Hesitation and hindrance.<br>It furthers one to remain persevering.<br>It furthers one to appoint helpers.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:<br>Difficulties pile up.<br>Horse and wagon part.<br>He is not a robber;<br>He wants to woo when the time comes.<br>The maiden is chaste,<br>She does not pledge herself.<br>Ten years--then she pledges herself.<br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:<br>Whoever hunts deer without the forester<br>Only loses his way in the forest.<br>The superior man understands the signs of the time<br>And prefers to desist.<br>To go on brings humiliation.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:<br>Horse and wagon part.<br>Strive for union.<br>To go brings good fortune.<br>Everything acts to further.<br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:<br>Difficulties in blessing.<br>A little perseverance brings good fortune.<br>Great perseverance brings misfortune.<br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:<br>Horse and wagon part.<br>Bloody tears flow.<br><br>"
		return linesReturn
	if hexvalue == "010001":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means:<br>To make a fool develop<br>It furthers one to apply discipline.<br>The fetters should be removed.<br>To go on in this way bring humiliation.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:<br>To bear with fools in kindliness brings good fortune.<br>To know how to take women<br>Brings good fortune.<br>The son is capable of taking charge of the household.<br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:<br>Take not a maiden who. When she sees a man of bronze,<br>Loses possession of herself.<br>Nothing furthers.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:<br>Entangled folly bring humiliation.<br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:<br>Childlike folly brings good fortune. <br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:<br>In punishing folly<br>It does not further one<br>To commit transgressions.<br>The only thing that furthers <br>Is to prevent transgressions.<br><br>"
		return linesReturn
	if hexvalue == "111010":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:<br>Waiting in the meadow.<br>IT furthers one to abide in what endures.<br>No blame.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:<br>Waiting on the sand.<br>There is some gossip.<br>The end brings good fortune.<br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means:<br>Waiting in the mud<br>Brings about the arrival of the enemy.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:<br>Waiting in blood.<br>Get out of the pit.<br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:<br>Waiting at meat and drink.<br>Perseverance brings good fortune.<br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:<br>One falls into the pit.<br>Three uninvited guests arrive.<br>Honor them, and in the end there will be good fortune.<br><br><br>"
		return linesReturn
	if hexvalue == "010111":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means:<br>If one does not perpetuate the affair,<br>There is a little gossip.<br>In the end, good fortune comes.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:<br>One cannot engage in conflict;<br>One returns home, gives way.<br>The people of his town,<br>Three hundred households, <br>Remain free of guilt.<br><br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:<br>To nourish oneself on ancient virtue induces perseverance.<br>Danger. In the end, good fortune comes.<br>If by chance you are in the service of a king,<br>Seek not works.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:<br>One cannot engage in conflict.<br>One turns back and submits to fate,<br>Changes one's attitude, <br>And finds peace in perseverance.<br>Good fortune.<br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:<br>To contend before him<br>Brings supreme good fortune.<br><br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:<br>Even if by chance a leather belt is bestowed on one,'<br>By the end of a morning<br>It will have been snatched away three times.<br><br>"
		return linesReturn
	if hexvalue == "010000":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means:<br>An army must set forth in proper order.<br>If the order is not good, misfortune threatens.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:<br>In the midst of the army.<br>Good fortune. No blame.<br>The king bestows a triple decoration.<br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:<br>Perchance the army carries corpses in the wagon.<br>Misfortune.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:<br>The army retreats. No blame.<br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:<br>There is game in the field.<br>It furthers one to catch it.<br>Without blame.<br>Let the eldest lead the army.<br>The younger transports corpses;<br>Then perseverance brings misfortune.<br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:<br>The great prince issues commands,<br>Founds states, vests families with fiefs.<br>Inferior people should not be employed.<br><br>"
		return linesReturn
	if hexvalue == "000010":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means:<br>Hold to him in truth and loyalty;<br>This is without blame.<br>Truth, like a full earthen bowl<br>Thus in the end<br>Good fortune comes from without.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:<br>Hold to him inwardly.<br>Perseverance brings good fortune.<br><br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:<br>You hold together with the wrong people.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:<br>Hold to him outwardly also.<br>Perseverance brings good fortune.<br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:<br>Manifestation of holding together.<br>In the hunt the king uses beaters on three sides only<br>And forgoes game that runs off in front.<br>The citizens need no warning.<br>Good fortune.<br><br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:<br>He finds no head for holding together.<br>Misfortune.<br><br><br>"
		return linesReturn
	if hexvalue == "111011":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:<br>Return to the way.<br>How could there be blame in this?<br>Good fortune.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:<br>He allows himself to be drawn into returning.<br>Good fortune.<br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means:<br>The spokes burst out of the wagon wheels.<br>Man and wife roll their eyes.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:<br>If you are sincere, blood vanishes and fear gives way.<br>No blame.<br><br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:<br>If you are sincere and loyally attached, <br>You are rich in your neighbor.<br><br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:<br>The rain comes, there is rest.<br>This is due to the lasting effect of character.<br>Perseverance brings the woman into danger.<br>The moon is nearly full.<br>If the superior man persists,<br>Misfortune comes.<br><br>"
		return linesReturn
	if hexvalue == "110111":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:<br>Simple conduct. Progress without blame.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:<br>Treading a smooth, level course.<br>The perseverance of a dark man<br>Brings good fortune.<br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:<br>A one-eyed man is able to see,<br>A lame man is able to tread.<br>He treads on the tail of the tiger.<br>The tiger bites the man.<br>Misfortune.<br>Thus does a warrior act on behalf of his great prince.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:<br>He treads on the tail of the tiger.<br>Caution and circumspection<br>Lead ultimately to good fortune.<br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:<br>Resolute conduct.<br>Perseverance with awareness of danger.<br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:<br>Look to your conduct and weigh the favorable signs.<br>When everything is fulfilled, supreme good fortune comes.<br><br>"
		return linesReturn
	if hexvalue == "111000":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:<br>When ribbon grass is pulled up, the sod comes with it.<br>Each according to his kind.<br>Undertakings bring good fortune.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:<br>Bearing with the uncultured in gentleness,<br>Fording the river with resolution,<br>Not neglecting what is distant,<br>Not regarding one's companions:<br>Thus one may manage to walk in the middle.<br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means:<br>No plain not followed by a slope.<br>No going not followed by a return.<br>He who remains persevering in danger<br>Is without blame.<br>Do not complain about this truth;<br>Enjoy the good fortune you still possess.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:<br>He flutters down, not boasting of his wealth,<br>Together with his neighbor,<br>Guileless and sincere.<br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:<br>The sovereign I<br>Gives his daughter in marriage.<br>And supreme good fortune.<br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:<br>The wall falls back into the moat.<br>Use no army now.<br>Make your commands known within your own town.<br>Perseverance brings humiliation.<br><br>"
		return linesReturn
	if hexvalue == "000111":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means:<br>When ribbon grass is pulled up, the sod comes with it.<br>Each according to his kind.<br>Perseverance brings good fortune and success.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:<br>They bear and endure;<br>This means good fortune for inferior people.<br>The standstill serves to help the great man to attain success.<br><br><br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:<br>They bear shame.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:<br>He who acts at the command of the highest <br>Remains without blame.<br>Those of like mind partake of the blessing.<br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:<br>Standstill is giving way.<br>Good fortune for the great man.<br>'What if it should fail, what if it should fail?'<br>In this way he ties it to a cluster of mulberry shoots.<br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:<br>The standstill comes to an end.<br>First standstill, then good fortune.<br><br>"
		return linesReturn
	if hexvalue == "101111":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:<br>Fellowship with men at the gate.<br>No blame.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:<br>Fellowship with men in the clan.<br>Humiliation.<br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means:<br>He hides weapons in the thicket;<br>He climbs the high hill in front of it.<br>For three years he does not rise up.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:<br>He climbs up on his wall; he cannot attack.<br>Good fortune.<br><br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:<br>Men bound in fellowship first weep and lament,<br>But afterward they laugh.<br>After great struggles they succeed in meeting.<br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:<br>Fellowship with men in the meadow.<br>No remorse.<br><br>"
		return linesReturn
	if hexvalue == "111101":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:<br>No relationship with what is harmful;<br>There is no blame in this.<br>If one remains conscious of difficulty,<br>One remains without blame.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:<br>A big wagon for loading.<br>One may undertake something.<br>No blame.<br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means:<br>A prince offers it to the Son of Heaven.<br>A petty man cannot do this.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:<br>He makes a difference<br>Between himself and his neighbor.<br>No blame.<br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:<br>He whose truth is accessible, yet dignified,<br>Has good fortune.<br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:<br>He is blessed by heaven.<br>Good fortune.<br>Nothing that does not further.<br><br>"
		return linesReturn
	if hexvalue == "001000":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means:<br>A superior man modest about his modesty<br>May cross the great water.<br>Good fortune.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:<br>Modesty that comes to expression. Perseverance brings good fortune.<br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means:<br>A superior man of modesty and merit<br>Carries things to conclusion.<br>Good fortune.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:<br>Nothing that would not further modesty<br>In movement.<br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:<br>No boasting of wealth before one's neighbor. <br>It is favorable to attack with force.<br>Nothing that would not further.<br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:<br>Modesty that comes to expression.<br>It is favorable to set armies marching<br>To chastise one's own city and one's country.<br><br>"
		return linesReturn
	if hexvalue == "000100":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means:<br>Enthusiasm that expresses itself<br>Brings misfortune.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:<br>Firm as a rock. Not a whole day.<br>Perseverance brings good fortune.<br>Firm as a rock, what need of a whole day?<br>Hesitation brings remorse.<br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:<br>Enthusiasm that looks upward creates remorse.<br>Hesitation brings remorse.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:<br>The source of enthusiasm.<br>He achieves great things.<br>Doubt not.<br>You gather friends around you<br>As a hair clasp gathers the hair.<br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:<br>Persistently ill, and still does not die.<br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:<br><br>Deluded enthusiasm.<br>But if after completion one changes, <br>There is no blame.<br><br>"
		return linesReturn
	if hexvalue == "100110":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:<br>The standard is changing.<br>Perseverance brings good fortune.<br>To go out of the door in company<br>Produces deeds.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:<br>If one clings to the little boy,<br>One loses the strong man.<br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:<br>If one clings to the strong man,<br>One loses the little boy.<br>Through following one finds what one seeks.<br>It furthers one to remain persevering.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:<br>Following creates success.<br>Perseverance brings misfortune.<br>To go one's way with sincerity brings clarity.<br>How could there be blame in this?<br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:<br>Sincere in the good. Good fortune.<br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:<br>He meets with firm allegiance<br>And is still further bound.<br>The king introduces him<br>To the Western Mountain.<br><br>"
		return linesReturn
	if hexvalue == "011001":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six in the beginning means:<br>Setting right what has been spoiled by the father.<br>If there is a son, <br>No blame rests upon the departed father. <br>Danger. In the end good fortune.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:<br>Setting right what has been spoiled by the mother.<br>One must not be too persevering.<br><br><br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means:<br>Setting right what has been spoiled by the father.<br>There will be a little remorse. No great blame.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:<br>Tolerating what has been spoiled by the father.<br>In continuing one sees humiliation.<br><br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:<br>Setting right what has been spoiled by the father.<br>One meets with praise.<br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:<br>He does not serve kings and princes,<br>Sets himself higher goals.<br><br><br>"
		return linesReturn
	if hexvalue == "110000":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:<br>Joint approach.<br>Perseverance brings good fortune.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:<br>Joint approach.<br>Good fortune.<br>Everything furthers.<br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:<br>Comfortable approach.<br>Nothing that would further.<br>If one is induced to grieve over it,<br>One becomes free of blame.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:<br>Complete approach.<br>No blame.<br>in to his own circle, regardless of class prejudice. This is very favorable.<br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:<br>Wise approach.<br>This is right for a great prince.<br>Good fortune.<br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:<br>Great hearted approach.<br>Good-hearted approach.<br>Good fortune. No blame.<br><br>"
		return linesReturn
	if hexvalue == "000011":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means:<br>Boy like contemplation.<br>For an inferior man, no blame.<br>For a superior man, humiliation.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:<br>Contemplation through the crack of the door.<br>Furthering for the perseverance of a woman.<br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:<br>Contemplation of my life <br>Decides the choice<br>Between advance and retreat.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:<br>Contemplation of the light of the kingdom.<br>It furthers one to exert influence as the guest of a king.<br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:<br>Contemplation of my life.<br>The superior man is without blame.<br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:<br>Contemplation of his life.<br>The superior man is without blame.<br><br>"
		return linesReturn
	if hexvalue == "100101":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:<br>His feet are fastened in the stocks,<br>So that his toes disappear.<br>No blame.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six  in the second place means:<br>Bites through tender meat,<br>So that his nose disappears.<br>No blame.<br><br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six  in the third place means:<br>Bites on old dried meat <br>And strikes on something poisonous.<br>Slight humiliation.  No blame.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:<br>Bites on dried gristly meat.<br>Receives metal arrows.<br>It furthers one to be mindful of difficulties<br>And to be persevering.<br>Good fortune. <br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:<br>Bites on dried lean meat.<br>Receives yellow gold.<br>Perseveringly aware of danger.<br>No blame.<br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:<br>His neck is fastened in the wooden cangue,<br>So that his ears disappear.<br>Misfortune.<br><br>"
		return linesReturn
	if hexvalue == "101001":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:<br>He lends grace to his toes, leaves the carriage, and walks.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:<br>Lends grace to the beard on his chin.<br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means:<br>Graceful and moist.<br>Constant perseverance brings good fortune.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:<br>Grace or simplicity?<br>A white horse comes as if on wings.<br>He is not a robber,<br>He will woo at the right time.<br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:<br>Grace in the hills and gardens.<br>The roll of silk is meager and small.<br>Humiliation, but in the end good fortune.<br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:<br>Simple grace. No blame.<br><br>"
		return linesReturn
	if hexvalue == "000001":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means:<br>The leg of the bed is split.<br>Those who persevere are destroyed.<br>Misfortune.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:<br>The bed is split at the edge.<br>Those who persevere are destroyed.<br>Misfortune.<br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:<br>He splits with them. No blame.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:<br>The bed is split up to the skin.<br>Misfortune.<br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:<br>A shoal of fishes. Favor comes through the court ladies.<br>Everything acts to further.<br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:<br>There is a large fruit still uneaten.<br>The superior man receives a carriage.<br>The house of the inferior man is split apart.<br><br>"
		return linesReturn
	if hexvalue == "100000":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:<br>Return from a short distance.<br>No need for remorse.<br>Great good fortune.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:<br>Quiet return. Good fortune.<br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:<br>Repeated return. Danger. No blame.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:<br>Walking in the midst of others,<br>One returns alone.favorable, for such a resolve to choose the good brings its own reward. <br><br><br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:<br>Noblehearted return. No remorse.<br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:<br>Missing the return. Misfortune.<br>Misfortune from within and without.<br>If armies are set marching in this way,<br>One will in the end suffer a great defeat, <br>Disastrous for the ruler of the country.<br>For ten years<br>It will not be possible to attack again.<br><br>"
		return linesReturn
	if hexvalue == "100111":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:<br>Innocent behavior brings good fortune.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:<br>If one does not count on the harvest while plowing,<br>Nor on the use of the ground while clearing it,<br>It furthers one to undertake something.<br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:<br>Undeserved misfortune.<br>The cow that was tethered by someone<br>Is the wanderer's gain, the citizen's loss.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:<br>He who can be persevering <br>Remains without blame.<br><br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:<br>Use no medicine in an illness<br>Incurred through no fault of your own.<br>It will pass of itself.<br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:<br>Innocent action brings misfortune.<br>Nothing furthers.<br><br>"
		return linesReturn
	if hexvalue == "111001":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:<br>Danger is at hand. It furthers one to desist.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:<br>The axletrees are taken from the wagon.<br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means.<br>A good horse that follows others.<br>Awareness of danger,<br>With perseverance, furthers.<br>Practice chariot driving and armed defense daily. <br>It furthers one to have somewhere to go.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:<br>The headboard of a young bull.<br>Great good fortune.<br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:<br>The tusk of a gelded boar.<br>Good fortune.<br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:<br>One attains the way of heaven.<br>Success.<br><br>"
		return linesReturn
	if hexvalue == "100001":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:<br>You let your magic tortoise go,<br>And look at me with the corners of your mouth drooping.<br>Misfortune.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:<br>Turning to the summit for nourishment,<br>Deviating from the path<br>To seek nourishment from the hill.<br>Continuing to do this brings misfortune.<br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:<br>Turning away from nourishment.<br>Perseverance brings misfortune.<br>Do not act thus for ten years.<br>Nothing serves to further.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:<br>Turning to the summit<br>For provision of nourishment<br>Brings good fortune.<br>Spying about with sharp eyes<br>Like a tiger with insatiable craving.<br>No blame.<br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:<br>Turning away from the path.<br>To remain persevering brings good fortune.<br>One should not cross the great water.<br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:<br>The source of nourishment.<br>Awareness of danger brings good fortune.<br>It furthers one to cross the great water.<br><br>"
		return linesReturn
	if hexvalue == "011110":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means:<br>To spread white rushes underneath.<br>No blame.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:<br>A dry poplar sprouts at the root.<br>An older man takes a young wife.<br>Everything furthers.<br><br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means:<br>The ridgepole sags to the breaking point.<br>Misfortune.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:<br>The ridgepole is braced. Good fortune.<br>If there are ulterior motives, it is humiliating.<br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:<br>A withered poplar puts forth flowers.<br>An older woman takes a husband. <br>No blame. No praise.<br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:<br>One must go through the water.<br>It goes over one's head.<br>Misfortune. No blame.<br><br>"
		return linesReturn
	if hexvalue == "010010":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means:<br>Repetition of the Abysmal.<br>In the abyss one falls into a pit.<br>Misfortune.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:<br>The abyss is dangerous.<br>One should strive to attain small things only.<br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:<br>Forward and backward, abyss on abyss.<br>In danger like this, pause at first and wait,<br>Otherwise you will fall into a pit in the abyss.<br>Do not act this way.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:<br>A jug of wine, a bowl of rice with it;<br>Earthen vessels<br>Simply handed in through the Window.<br>There is certainly no blame in this.<br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:<br>The abyss is not filled to overflowing,<br>It is filled only to the rim.<br>No blame.<br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:<br>Bound with cords and ropes,<br>Shut in between thorn-hedged prison walls:<br>For three years one does not find the way.<br>Misfortune.<br><br>"
		return linesReturn
	if hexvalue == "101101":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:<br>The footprints run crisscross.<br>If one is seriously intent, no blame.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:<br>Yellow light. Supreme good fortune.<br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means:<br>In the light of the setting sun,<br>Men either beat the pot and sing<br>Or loudly bewail the approach of old age.<br>Misfortune.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:<br>Its coming is sudden;<br>It flames up, dies down, is thrown away.<br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:<br>Tears in floods, sighing and lamenting.<br>Good fortune. <br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:<br>The king used him to march forth and chastise.<br>Then it is best to kill the leaders<br>And take captive the followers. No blame.<br><br>"
		return linesReturn
	if hexvalue == "001110":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the top means:<br>The king used him to march forth and chastise.<br>Then it is best to kill the leaders<br>And take captive the followers. No blame.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six at the beginning means:<br>The influence shows itself in the big toe.<br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the second place means:<br>The influence shows itself in the calves of the legs.<br>Misfortune.<br>Tarrying brings good fortune.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the third place means:<br>The influence shows itself in the thighs.<br>Holds to that which follows it.<br>To continue is humiliating.<br><br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:<br>Perseverance brings good fortune.<br>Remorse disappears.<br>If a man is agitated in mind,<br>And his thoughts go hither and thither,<br>Only those friends <br>On whom he fixes his conscious thoughts<br>Will follow.<br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:<br>The influence shows itself in the back of the neck.<br>No remorse.<br><br>"
		return linesReturn
	if hexvalue == "011100":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the top means:<br>The influence shows itself in the jaws, cheeks, and tongue.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six at the beginning means:<br>Seeking duration too hastily brings misfortune persistently.<br>Nothing that would further.<br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the second place means:<br>Remorse disappears.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the third place means:<br>He who does not give duration to his character<br>Meets with disgrace.<br>Persistent humiliation.<br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:<br>No game in the field.<br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:<br>Giving duration to one's character through perseverance.<br>This is good fortune for a woman, misfortune for a man.<br><br>"
		return linesReturn
	if hexvalue == "001111":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the top means:<br>Restlessness as an enduring condition brings misfortune.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six at the beginning means:<br>At the tail in retreat. This is dangerous.<br>One must not wish to undertake anything.<br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the second place means:<br>he holds him fast with yellow oxhide.<br>No one can tear him loose.<br>Brings good fortune.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:<br>Voluntary retreat brings good fortune to the superior man<br>And downfall to the inferior man.<br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:<br>Friendly retreat. Perseverance brings good fortune.<br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:<br>Cheerful retreat. Everything serves to further.<br><br>"
		return linesReturn
	if hexvalue == "111100":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:<br>Power in the toes.<br>Continuing brings misfortune.<br>This is certainly true.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:<br>Perseverance brings good fortune.<br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means:<br>The inferior man works through power.<br>The superior man does not act thus.<br>To continue is dangerous.<br>A goat butts against a hedge<br>And gets its horns entangled.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:<br>Perseverance brings good fortune.<br>Remorse disappears.<br>The hedge opens; there is no entanglement.<br>Power depends upon the axle of a big cart.<br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:<br>Loses the goat with ease.<br>No remorse.<br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:<br>A goat butts against a hedge.<br>It cannot go backward, it cannot go forward.<br>Nothing serves to further.<br>If one notes the difficulty, this brings good fortune.<br><br>"
		return linesReturn
	if hexvalue == "000101":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means:<br>Progressing, but turned back.<br>Perseverance brings good fortune.<br>If one meets with no confidence, one should remain calm.<br>No mistake.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:<br>Progressing, but in sorrow.<br>Perseverance brings good fortune.<br>Then one obtains great happiness from one's ancestress.<br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:<br>All are in accord. Remorse disappears.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:<br>Progress like a hamster.<br>Perseverance brings danger.<br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:<br>Remorse disappears.<br>Take not gain and loss to heart.<br>Undertakings bring good fortune.<br>Everything serves to further.<br><br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:<br>Making progress with the horns is permissible<br>Only for the purpose of punishing one's own city.<br>To be conscious of danger brings good fortune.<br>No blame. <br>Perseverance brings humiliation.<br><br>"
		return linesReturn
	if hexvalue == "101000":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:<br>Darkening of the light during flight.<br>He lowers his wings.<br>The superior man does not eat for three days<br>On his wanderings.<br>But he has somewhere to go.<br>The host has occasion to gossip about him.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:<br>Darkening of the light injures him in the left thigh.<br>He gives aid with the strength of a horse.<br>Good fortune.<br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means:<br>Darkening of the light during the hunt in the south.<br>Their great leader is captured.<br>One must not expect perseverance too soon.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:<br>He penetrates the left side of the belly.<br>One gets at the very heart of the darkening of the light.<br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:<br>Darkening of the light as with Prince Chi.<br>Perseverance furthers.<br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:<br>Not light but darkness.<br>First he climbed up to heaven,<br>Then plunged into the depths of the earth.<br><br>"
		return linesReturn
	if hexvalue == "101011":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:<br>Firm seclusion within the family.<br>Remorse disappears.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:<br>She should not follow her whims.<br>She must attend within to the food.<br>Perseverance brings good fortune.<br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means:<br>When tempers flare up in the family,<br>Too great severity brings remorse.<br>Good fortune nonetheless.<br>When woman and chile dally and laugh<br>It leads in the end to humiliation.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:<br>She is the treasure of the house.<br>Great good fortune.<br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:<br>As a king he approaches his family.<br>Fear not.<br>Good fortune.<br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:<br>His work commands respect.'<br>In the end good fortune comes.<br><br>"
		return linesReturn
	if hexvalue == "110101":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:<br>Remorse disappears.<br>If you lose your horse, do not run after it;<br>It will come back of its own accord.<br>When you see evil people,<br>Guard yourself against mistakes.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:<br>One meets his lord in a narrow street.<br>No blame.<br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:<br>One sees the wagon dragged back,<br>The oxen halted,<br>A man's hair and nose cut off.<br>Not a good beginning, but a good end.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:<br>Isolated through opposition,<br>One meets a like-minded man<br>With whom one can associate in good faith.<br>Despite the danger, no blame.<br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:<br>Remorse disappears.<br>The companion bits his way through the wrappings.<br>If one goes to him,<br>How could it be a mistake?<br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:<br>Isolated through opposition,<br>One sees one's companion as a pig covered with dirt,<br>As a wagon full of devils.<br>First one draws a bow against him,<br>then one lays the bow aside.<br>He is not a robber; he will woo at the right time.<br>As one goes, rain falls; then good fortune comes.<br><br>"
		return linesReturn
	if hexvalue == "001010":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means:<br>Going leads to obstructions,<br>Coming meets with praise.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:<br>The King's servant is beset by obstruction upon obstruction,<br>But it is not his own fault.<br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means:<br>Going leads to obstructions;<br>Hence he comes back.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:<br>Going leads to obstructions,<br>Coming leads to union.<br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:<br>In the midst of the greatest obstructions,<br>Friends come.<br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:<br>Going leads to obstructions,<br>Coming leads to great good fortune.<br>It furthers one to see the great man.<br><br>"
		return linesReturn
	if hexvalue == "010100":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means:<br>Without blame.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:<br>One kills three foxes in the field<br>And receives a yellow arrow.<br>Perseverance brings good fortune.<br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:<br>If a man carries a burden on his back<br>And nonetheless rides in a carriage,<br>He thereby encourages robbers to draw near.<br>Perseverance leads to humiliation.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:<br>Deliver yourself from your great toe.<br>Then the companion comes,<br>And him you can trust.<br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:<br>If only the superior man can deliver himself,<br>It brings good fortune.<br>Thus he proves to inferior men that he is in earnest.<br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:<br>The prince shoots at a hawk on a high wall.<br>He kills it. Everything serves to further.<br><br>"
		return linesReturn
	if hexvalue == "110001":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:<br>Going quickly when one's tasks are finished<br>Is without blame.<br>But one must reflect on how much one may decrease others.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:<br>Perseverance furthers.<br>To undertake something brings misfortune.<br>Without decreasing oneself,<br>One is able to bring increase to others.<br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:<br>When three people journey together,<br>Their number increases by one.<br>When one man journeys alone,<br>He finds a companion.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:<br>If a man deceases his faults,<br>It makes the other hasten to come and rejoice.<br>No blame.<br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:<br>Someone does indeed increase him.<br>Ten pairs of tortoises cannot oppose it.<br>Supreme good fortune.<br><br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:<br>If one is increased without depriving other,<br>There is no blame.<br>Perseverance brings good fortune.<br>It furthers one to undertake something.<br>One obtains servants<br>But no longer has a separate home.<br><br>"
		return linesReturn
	if hexvalue == "100011":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:<br>It furthers one to accomplish great deeds.<br>Supreme good fortune. No blame.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:<br>Someone does indeed increase him; <br>Ten pairs of tortoises cannot oppose it.<br>Constant perseverance brings good fortune.<br>The king presents him before God.<br>Good fortune.<br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:<br>One is enriched through unfortunate events.<br>No blame, if you are sincere<br>And walk in the middle,<br>And report with a seal to the prince.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:<br>If you walk in the middle <br>And report the prince,<br>He will follow.<br>It furthers one to be used<br>In the removal of the capital.<br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:<br>If in truth you have a kind heart, ask not.<br>Supreme good fortune.<br>Truly, kindness will be recognized as your virtue. <br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:<br>He brings increase to no one.<br>Indeed, someone even strikes him.<br>He does not keep his heart constantly steady.<br>Misfortune.<br><br><br><br>"
		return linesReturn
	if hexvalue == "111110":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:<br>Mighty in the forward-striding toes.<br>When one goes and is not equal to the task,<br>One makes a mistake.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:<br>A cry of alarm. Arms at evening and at night.<br>Fear nothing.<br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means:<br>To be powerful in the cheekbones <br>Brings misfortune.<br>The superior man is firmly resolved.<br>He walks alone and is caught in the rain.<br>He is bespattered,<br>And people murmur against him.<br>No blame.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:<br>There is no skin on his thighs,<br>And walking comes hard.<br>If a man were to let himself be led like a sheep,<br>Remorse would disappear.<br>But if these words are heard<br>They will not be believed.<br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:<br>In dealing with weeds,<br>Firm resolution is necessary.<br>Walking in the middle<br>Remains free of blame.<br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:<br>No cry.<br>In the end misfortune comes.<br><br>"
		return linesReturn
	if hexvalue == "011111":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means:<br>It must be checked with a brake of bronze.<br>Perseverance brings good fortune.<br>If one lets it take its course, one experiences misfortune.<br>Even a lean pig has it in him to rage around.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:<br>There is a fish in the tank. No blame.<br>Does not further guests.<br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means: <br>There is no skin on his thighs,<br>And walking comes hard.<br>If one is mindful of the danger,<br>No great mistake is made.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:<br>No fish in the tank.<br>This leads to misfortune.<br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:<br>A melon covered with willow leaves.<br>Hidden lines.<br>Then it drops down to one from heaven.<br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:<br>He comes to meet with his horns.<br>Humiliation. No blame.<br><br>"
		return linesReturn
	if hexvalue == "000110":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means:<br>If you are sincere, but not to the end,<br>There will sometimes be confusion, sometimes gathering together.<br>If you call out, <br>Then after one grasp of the hand you can laugh again.<br>Regret not. Going is without blame.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:<br>Letting oneself be drawn<br>Brings good fortune and remains blameless.<br>If one is sincere,<br>It furthers one to bring even a small offering.<br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:<br>Gathering together amid sighs.<br>Nothing that would further.<br>Going is without blame.<br>Slight humiliation.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:<br>Great good fortune. No blame.<br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:<br>If in gathering together one has position,<br>This brings no blame.<br>If there are some who are not yet sincerely in the work,<br>Sublime and enduring perseverance is needed.<br>Then remorse disappears.<br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:<br>Lamenting and sighing, floods of tears.<br>No blame.<br><br>"
		return linesReturn
	if hexvalue == "011000":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means:<br>Pushing upward that meets with confidence<br>Brings great good fortune.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:<br>If one is sincere,<br>It furthers one to bring even a small offering.<br>No blame.<br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means:<br>One pushes upward into an empty city.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:<br>The king offers him Mount Ch'i.<br>Good fortune. No blame.<br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:<br>Perseverance brings good fortune.<br>One pushes upward by steps.<br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:<br>Pushing upward in darkness.<br>It furthers one<br>To be unremittingly persevering.<br><br>"
		return linesReturn
	if hexvalue == "010110":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means:<br>One sits oppressed under a bare tree<br>And strays into a gloomy valley.<br>For three years one sees nothing.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:<br>One is oppressed while at meat and drink.<br>The man with the scarlet knee bands is just coming.<br>It furthers one to offer sacrifice.<br>To set forth brings misfortune.<br>No blame.<br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:<br>A man permits himself to be oppressed by stone,<br>And leans on thorns and thistles.<br>He enters the house and does not see his wife.<br>Misfortune.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:<br>He comes very quietly, oppressed in a golden carriage.<br>Humiliation, but the end is reached.<br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:<br>His nose and feet are cut off.<br>Oppression at the hands of the man with the purple knee bands.<br>Joy comes softly.<br>It furthers one to make offerings and libations.<br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:<br>He is oppressed by creeping vines.<br>He moves uncertainly and says, 'Movement brings remorse.'<br>If one feels remorse over this and makes a start,<br>Good fortune comes.<br><br>"
		return linesReturn
	if hexvalue == "011010":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means:<br>One does not drink the mud of the well.<br>No animals come to an old well.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:<br>At the well hole one shoots fishes.<br>The jug is broken and leaks.<br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means:<br>The well is cleaned, but no one drinks from it.<br>This is my heart's sorrow,<br>For one might draw from it.<br>If the king were clear-minded,<br>Good fortune might be enjoyed in common.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:<br>The well is being lined. No blame.<br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:<br>In the well there is a clear, cold spring<br>From which one can drink.<br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:<br>One draws from the well<br>Without hindrance.<br>It is dependable.<br>Supreme good fortune.<br><br>"
		return linesReturn
	if hexvalue == "101110":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:<br>Wrapped in the hide of a yellow cow.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:<br>When one's own day comes, one may create revolution.<br>Starting brings good fortune. No blame.<br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means:<br>Starting brings misfortune.<br>Perseverance brings danger.<br>When talk of revolution has gone the rounds three times,<br>One may commit himself,<br>And men will believe him.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:<br>Remorse disappears. Men believe him.<br>Changing the form of government brings good fortune.<br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:<br>The great man changes like a tiger.<br>Even before he questions the oracle<br>He is believed.<br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:<br>The superior man changes like a panther.<br>The inferior man molts in the face.<br>Starting brings misfortune.<br>To remain persevering brings good fortune.<br><br><br>"
		return linesReturn
	if hexvalue == "011101":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means:<br>A ting with legs upturned.<br>Furthers removal of stagnating stuff.<br>One takes a concubine for the sake of her son.<br>No blame.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:<br>There is food in the ting.<br>My comrades are envious,<br>But they cannot harm me.<br>Good fortune.<br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means:<br>The handle of the ting is altered.<br>One is impeded in his way of life.<br>The fat of the pheasant is not eaten.<br>Once rain falls, remorse is spent.<br>Good fortune comes in the end.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:<br>The legs of the ting are broken.<br>The prince's meal is spilled<br>And his person is soiled.<br>Misfortune.<br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:<br>The ting has yellow handles, golden carrying rings.<br>Perseverance furthers.<br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:<br>The ting has rings of jade.<br>Great good fortune.<br>Nothing that would not act to further.<br><br>"
		return linesReturn
	if hexvalue == "100100":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:<br>Shock comes-oh, oh!<br>Then follow laughing words-ha, ha!<br>Good fortune.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:<br>Shock comes bringing danger.<br>A hundred thousand times<br>You lose your treasures<br>And must climb the nine hills.<br>Do not go in pursuit of them.<br>After seven days you will get them back again.<br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:<br>Shock comes and makes one distraught.<br>If shock spurs to action<br>One remains free of misfortune.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:<br>Shock is mired.<br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:<br>Shock goes hither and thither.<br>Danger.<br>However, nothing at all is lost.<br>Yet there are things to be done.<br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:<br>Shock brings ruin and terrified gazing around.<br>Going ahead brings misfortune.<br>If it has not yet touched one's own body<br>But has reached one's neighbor first,<br>There is no blame.<br>One's comrades have something to talk about.<br><br>"
		return linesReturn
	if hexvalue == "001001":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means:<br>Keeping his toes still.<br>No blame.<br>Continued perseverance furthers.<br><br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:<br>Keeping his calves still.<br>He cannot rescue him whom he follows.<br>His heart is not glad.<br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means:<br>Keeping his hips still.<br>Making his sacrum stiff.<br>Dangerous. The heart suffocates.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:<br>Keeping his trunk still.<br>No blame.<br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:<br>Keeping his jaws still.<br>The words have order.<br>Remorse disappears.<br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:<br>Noblehearted keeping still.<br>Good fortune.<br><br>"
		return linesReturn
	if hexvalue == "001011":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means:<br>The wild goose gradually draws near the shore. <br>The young son is in danger.<br>There is talk. No blame.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:<br>The wild goose gradually draws near the cliff.<br>Eating and drinking in peace and concord.<br>Good fortune.<br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means:<br>The wild goose gradually draws near the plateau.<br>The man goes forth and does not return.<br>The woman carries a child but does not bring it forth.<br>Misfortune. <br>It furthers one to fight off robbers.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:<br>The wild goose goes gradually draws near the tree.<br>Perhaps it will find a flat branch. No blame.<br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:<br>The wild goose gradually draws near the summit.<br>For three years the woman has no child.<br>In the end nothing can hinder her.<br>Good fortune.<br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:<br>The wild goose gradually draws near the clouds heights.<br>Its feathers can be used for the sacred dance.<br>Good fortune.<br><br>"
		return linesReturn
	if hexvalue == "110100":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:<br>The marrying maiden as a concubine.<br>A lame man who is able to tread.<br>Undertakings bring good fortune.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:<br>A one-eyed man who is able to see.<br>The perseverance of a solitary man furthers.<br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:<br>The marrying maiden as a slave.<br>She marries as a concubine.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:<br>The marrying maiden draws out the allotted time.<br>A late marriage comes in due course.intended for her.<br><br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:<br>The sovereign I gave his daughter in marriage.<br>The embroidered garments of the princess<br>Were not as gorgeous<br>As those of the serving maid.<br>The moon that is nearly full<br>Brings good fortune.<br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:<br>The woman holds the basket, but there are no fruits in it.<br>The man stabs the sheep, but no blood flows.<br>Nothing that acts to further.<br><br><br>"
		return linesReturn
	if hexvalue == "101100":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:<br>When a man meets his destined ruler,<br>They can be together ten days,<br>And it is not a mistake.<br>Going meets with recognition.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:<br>The curtain is of such fullness<br>That the polestars can be seen at noon.<br>Through going one meets with mistrust and hate.<br>If one rouses him through truth,<br>Good fortune comes.<br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means:<br>The underbrush is of such abundance<br>That the small stars can be seen at noon.<br>He breaks his right arm . No blame.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:<br>The curtain is of such fullness<br>That the polestars can be seen at noon.<br>He meets his ruler, who is of like kind.<br>Good fortune.<br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:<br>Lines are coming,<br>Blessing and fame draw near.<br>Good fortune.<br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:<br>His house is in a state of abundance.<br>He screens off his family.<br>He peers through the gate<br>And no longer perceives anyone.<br>For three years he sees nothing.<br>Misfortune.<br><br>"
		return linesReturn
	if hexvalue == "001101":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means:<br>If the wanderer busies himself with trivial things, <br>He draws down misfortune upon himself.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:<br>The wanderer comes to an inn.<br>He has his property with him.<br>He wins the steadfastness of a young servant.<br><br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means:<br>The wanderer's inn burns down.<br>He loses the steadfastness of his young servant.<br>Danger.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:<br>The wanderer rests in a shelter.<br>He obtains his property and an ax.<br>My heart is not glad.<br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:<br>He shoots a pheasant.<br>It drops with the first arrow.<br>In the end this brings both praise and office.<br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:<br>The bird's nest burns up.<br>The wanderer laughs at first,<br>Then must needs lament and weep.<br>Through carelessness he loses his cow.<br>Misfortune.<br><br>"
		return linesReturn
	if hexvalue == "011011":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means:<br>In advancing and in retreating,<br>The perseverance of a warrior furthers.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:<br>Penetration under the bed.<br>Priests and magicians are used in great number.<br>Good fortune. No blame.<br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means:<br>Repeated penetration. Humiliation.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:<br>Remorse vanishes.<br>During the hunt<br>Three kinds of game are caught.<br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:<br>Perseverance brings good fortune.<br>Remorse vanishes.<br>Nothing that does not further.<br>No beginning, but an end.<br>Before the change, three days.<br>After the change, three days.<br>Good fortune.<br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:<br>Penetration under the bed.<br>He loses his property and his ax.<br>Perseverance brings misfortune.<br><br>"
		return linesReturn
	if hexvalue == "110110":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:<br>Contented joyousness. Good fortune.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:<br>Sincere joyousness. Good fortune.<br>Remorse disappears.<br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:<br>Coming joyousness. Misfortune.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:<br>Joyousness that is weighed is not at peace.<br>After ridding himself of mistakes a man has joy.<br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:<br>Sincerity toward disintegrating influences is dangerous.<br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:<br>Seductive joyousness.<br><br>"
		return linesReturn
	if hexvalue == "010011":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means:<br>He brings help with the strength of a horse.<br>Good fortune.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:<br>At the dissolution<br>He hurries to that which supports him.<br>Remorse disappears.<br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:<br>He dissolves his self. No remorse.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:<br>He dissolves his bond with his group.<br>Supreme good fortune.<br>Dispersion leads in turn to accumulation.<br>This is something that ordinary men do not think of.<br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:<br>His loud cries are as dissolving as sweat.<br>Dissolution! A king abides without blame.<br><br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:<br>He dissolves his blood.<br>Departing, keeping at a distance, going out,<br>Is without blame.<br><br>"
		return linesReturn
	if hexvalue == "110010":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:<br>Not going out of the door and the courtyard<br>Is without blame.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:<br>Not going out of the gate and the courtyard<br>Brings misfortune.<br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:<br>He who knows limitation<br>Will have cause to lament.<br>No blame.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:<br>Contented limitation. Success.<br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:<br>Sweet limitation brings good fortune.<br>Going brings esteem.<br><br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:<br>Galling limitation.<br>Perseverance brings misfortune.<br>Remorse disappears.<br><br>"
		return linesReturn
	if hexvalue == "110011":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:<br>Being prepared brings good fortune.<br>If there are secret designs, it is disquieting.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:<br>A crane calling in the shade.<br>Its young answers it.<br>I have a good goblet.<br>I will share it with you.<br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:<br>He finds a comrade.<br>Now he beats the drum, now he stops.<br>Now he sobs, now he sings.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:<br>The moon nearly at the full.<br>The team horse goes astray.<br>No blame.<br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:<br>He possesses truth, which links together.<br>No blame.<br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:<br>Cockcrow penetrating to heaven.<br>Perseverance brings misfortune.<br><br>"
		return linesReturn
	if hexvalue == "001100":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means:<br>The bird meets with misfortune through flying.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:<br>She passes by her ancestor<br>And meets her ancestress.<br>He does not reach his prince<br>And meets the official.<br>No blame.<br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means:<br>If one is not extremely careful,<br>Somebody may come up from behind and strike him.<br>Misfortune.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:<br>No blame. He meets him without passing by.<br>Going brings danger. One must be on guard.<br>Do not act. Be constantly persevering.<br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:<br>Dense clouds,<br>No rain from our western territory.<br>The prince shoots and hits him who is in the cave.<br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:<br>He passes him by, not meeting him.<br>The flying bird leaves him.<br>Misfortune.<br>This means bad luck and injury.<br><br>"
		return linesReturn
	if hexvalue == "101010":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Nine at the beginning means:<br>He breaks his wheels.<br>He gets his tail in the water.<br>No blame.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Six in the second place means:<br>The woman loses the curtain of her carriage.<br>Do not run after it;<br>On the seventh day you will get it.<br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Nine in the third place means:<br>The Illustrious Ancestor<br>Disciplines the Devil's Country.<br>After three years he conquers it.<br>Inferior people must not be employed.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Six in the fourth place means:<br>The finest clothes turn to rags.<br>Be careful all day long.<br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Nine in the fifth place means:<br>The neighbor in the east who slaughters an ox<br>Does not attain as much real happiness<br>As the neighbor in the west<br>With his small offering.<br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Six at the top means:<br>He gets his head in the water. Danger.<br><br>"
		return linesReturn
	if hexvalue == "010101":
		linesReturn = ""
		if linesvalue[0] == "1":
			linesReturn = linesReturn + "Six at the beginning means:<br>He gets his tail in the water.<br>Humiliating.<br><br>"
		if linesvalue[1] == "1":
			linesReturn = linesReturn + "Nine in the second place means:<br>He brakes his wheels.<br>Perseverance brings good fortune.<br><br>"
		if linesvalue[2] == "1":
			linesReturn = linesReturn + "Six in the third place means:<br>Before completion, attack brings misfortune.<br>It furthers one to cross the great water.<br><br>"
		if linesvalue[3] == "1":
			linesReturn = linesReturn + "Nine in the fourth place means:<br>Perseverance brings good fortune.<br>Remorse disappears.<br>Shock, thus to discipline the Devil's Country.<br>For three years, great realms are rewarded.<br><br>"
		if linesvalue[4] == "1":
			linesReturn = linesReturn + "Six in the fifth place means:<br>Perseverance brings good fortune.<br>No remorse.<br>The light of the superior man is true.<br>Good fortune.<br><br>"
		if linesvalue[5] == "1":
			linesReturn = linesReturn + "Nine at the top means:<br>There is drinking of wine<br>In genuine confidence. No blame.<br>But if one wets his head,<br>He loses it, in truth.<br><br>"
		return linesReturn


def interpret_judgment(hexvalue):
	if hexvalue == "111111":
		return "THE CREATIVE works sublime success,<br>Furthering through perseverance."
	if hexvalue == "000000":
		return "THE RECEPTIVE brings about sublime success,<br>Furthering through the perseverance of a mare.<br>If the superior man undertakes something and tries to lead,<br>He goes astray;<br>But if he follows, he finds guidance.<br>It is favorable to find friends in the west and south,<br>To forego friends in the east and north.<br>Quiet perseverance brings good fortune."
	if hexvalue == "100010":
		return "DIFFICULTY AT THE BEGINNING works supreme success,<br>Furthering through perseverance.<br>Nothing should be undertaken.<br>It furthers one to appoint helpers."
	if hexvalue == "010001":
		return "YOUTHFUL FOLLY has success.<br>It is not I who seek the young fool;<br>The young fool seeks me.<br>At the first oracle I inform him. <br>If he asks two or three times, it is importunity.<br>If he importunes, I give him no information.<br>Perseverance furthers."
	if hexvalue == "111010":
		return "WAITING. If you are sincere, <br>You have light and success.<br>Perseverance brings good fortune.<br>It furthers one to cross the great water."
	if hexvalue == "010111":
		return "CONFLICT. You are sincere<br>And are being obstructed.<br>A cautious halt halfway brings good fortune.<br>Going through to the end brings misfortune.<br>It furthers one to see the great man.<br>It does not further one to cross the great water."
	if hexvalue == "010000":
		return "THE ARMY. The army needs perseverance<br>And a strong man.<br>Good fortune without blame."
	if hexvalue == "000010":
		return "HOLDING TOGETHER brings good fortune.<br>Inquire of the oracle once again<br>Whether you possess sublimity, constancy, and perseverance;<br>Then there is no blame.<br>Those who are uncertain gradually join.<br>Whoever come too late<br>Meets with misfortune."
	if hexvalue == "111011":
		return "THE TAMING POWER OF THE SMALL<br>Has success.<br>Dense clouds, no rain from our western region."
	if hexvalue == "110111":
		return "TREADING. Treading upon the tail of the tiger.<br>It does not bite the man. Success."
	if hexvalue == "111000":
		return "nPEACE. The small departs,<br>The great approaches.<br>Good fortune. Success."
	if hexvalue == "000111":
		return "STANDSTILL. Evil people do not further<br>The perseverance of the superior man.<br>The great departs; the small approaches."
	if hexvalue == "101111":
		return "FELLOWSHIP WITH MEN in the open.<br>Success.<br>It furthers one to cross the great water.<br>The perseverance of the superior man furthers."
	if hexvalue == "111101":
		return "POSSESSION IN GREAT MEASURE.<br>Supreme success."
	if hexvalue == "001000":
		return "MODESTY creates success.<br>The superior man carries things through."
	if hexvalue == "000100":
		return "ENTHUSIASM. It furthers one to install helpers<br>And to set armies marching."
	if hexvalue == "100110":
		return "FOLLOWING has supreme success.<br>Perseverance furthers. No blame."
	if hexvalue == "011001":
		return "WORK ON WHAT HAS BEEN SPOILED<br>Has supreme success.<br>It furthers one to cross the great water.<br>Before the starting point, three days.<br>After the starting point, three days."
	if hexvalue == "110000":
		return "APPROACH has supreme success.<br>Perseverance furthers.<br>When the eighth month comes,<br>There will be misfortune."
	if hexvalue == "000011":
		return "CONTEMPLATION. The ablution has been made, <br>But not yet the offering.<br>Full of trust they look up to him."
	if hexvalue == "100101":
		return "BITING THROUGH has success.<br>It is favorable to let justice be administered."
	if hexvalue == "101001":
		return "GRACE has success.<br>In small matters<br>It is favorable to undertake something."
	if hexvalue == "000001":
		return "SPLITTING APART. IT does not further one <br>To go anywhere."
	if hexvalue == "100000":
		return "RETURN. Success.<br>Going out and coming in without error.<br>Friends come without blame.<br>To and fro goes the way.<br>On the seventh day comes return.<br>It furthers one to have somewhere to go."
	if hexvalue == "100111":
		return "INNOCENCE. Supreme success.<br>Perseverance furthers.<br>If someone is not as he should be,<br>He has misfortune,<br>And it does not further him<br>To undertake anything."
	if hexvalue == "111001":
		return "THE TAMING POWER OF THE GREAT.<br>Perseverance furthers.<br>Not eating at home brings good fortune.<br>It furthers one to cross the great water."
	if hexvalue == "100001":
		return "THE CORNERS OF THE MOUTH.<br>Perseverance brings good fortune.<br>Pay heed to the providing of nourishment<br>And to what a man seeks<br>To fill his own mouth with."
	if hexvalue == "011110":
		return "PREPONDERANCE OF THE GREAT.<br>The ridgepole sags to the breaking point.<br>It furthers one to have somewhere to go.<br>Success."
	if hexvalue == "010010":
		return "The Abysmal repeated.<br>If you are sincere, you have success in your heart,<br>And whatever you do succeeds."
	if hexvalue == "101101":
		return "THE CLINGING. Perseverance furthers.<br>It brings success.<br>Care of the cow brings good fortune."
	if hexvalue == "001110":
		return "Influence. Success.<br>Perseverance furthers.<br>To take a maiden to wife brings good fortune."
	if hexvalue == "011100":
		return "DURATION. Success. No blame.<br>Perseverance furthers.<br>It furthers one to have somewhere to go."
	if hexvalue == "001111":
		return "RETREAT. Success.<br>In what is small, perseverance furthers."
	if hexvalue == "111100":
		return "THE POWER OF THE GREAT. Perseverance furthers."
	if hexvalue == "000101":
		return "PROGRESS. The powerful prince<br>Is honored with horses in large numbers.<br>In a single day he is granted audience three times."
	if hexvalue == "101000":
		return "DARKENING OF THE LIGHT. In adversity<br>It furthers one to be persevering."
	if hexvalue == "101011":
		return "THE FAMILY. The perseverance of the woman furthers."
	if hexvalue == "110101":
		return "OPPOSITION. In small matters, good fortune."
	if hexvalue == "001010":
		return "OBSTRUCTION. The southwest furthers.<br>The northeast does not further.<br>It furthers one to see the great man.<br>Perseverance brings good fortune."
	if hexvalue == "010100":
		return "DELIVERANCE. The southwest furthers.<br>If there is no longer anything where one has to go,<br>Return brings good fortune.<br>If there is still something where one has to go,<br>Hastening brings good fortune."
	if hexvalue == "110001":
		return "DECREASE combined with sincerity<br>Brings about supreme good fortune<br>Without blame.<br>One may be persevering in this.<br>It furthers one to undertake something.<br>How is this to be carried out?<br>One may use two small bowls for the sacrifice."
	if hexvalue == "100011":
		return "INCREASE. It furthers one<br>To undertake something.<br>It furthers one to cross the great water."
	if hexvalue == "111110":
		return "BREAK-THROUGH. One must resolutely make the matter known<br>At the court of the king.<br>It must be announced truthfully. Danger.<br>It is necessary to notify one's own city.<br>It does not further to resort to arms.<br>It furthers one to undertake something."
	if hexvalue == "011111":
		return "COMING TO MEET. The maiden is powerful.<br>One should not marry such a maiden."
	if hexvalue == "000110":
		return "GATHERING TOGETHER. Success.<br>The king approaches his temple.<br>It furthers one to see the great man.<br>This brings success. Perseverance furthers.<br>To bring great offerings creates good fortune.<br>It furthers one to undertake something."
	if hexvalue == "011000":
		return "PUSHING UPWARD has supreme success.<br>One must see the great man.<br>Fear not.<br>Departure toward the south<br>Brings good fortune."
	if hexvalue == "010110":
		return "OPPRESSION. Success. Perseverance.<br>The great man brings about good fortune.<br>No blame.<br>When one has something to say,<br>It is not believed."
	if hexvalue == "011010":
		return "THE WELL. The town may be changed,<br>But the well cannot be changed.<br>It neither decreases nor increases.<br>They come and go and draw from the well.<br>If one gets down almost to the water<br>And the rope does not go all the way,<br>Or the jug breaks, it brings misfortune."
	if hexvalue == "101110":
		return "REVOLUTION. On your own day<br>You are believed.<br>Supreme success,<br>Furthering through perseverance.<br>Remorse disappears."
	if hexvalue == "011101":
		return "THE CALDRON. Supreme good fortune.<br>Success."
	if hexvalue == "100100":
		return "SHOCK brings success.<br>Shock comes-oh, oh!<br>Laughing words -ha, ha!<br>The shock terrifies for a hundred miles,<br>And he does not let fall the sacrificial spoon and chalice."
	if hexvalue == "001001":
		return "KEEPING STILL. Keeping his back still<br>So that he no longer feels his body.<br>He goes into his courtyard<br>And does not see his people.<br>No blame."
	if hexvalue == "001011":
		return "DEVELOPMENT. The maiden<br>Is given in marriage.<br>Good fortune.<br>Perseverance furthers."
	if hexvalue == "110100":
		return "THE MARRYING MAIDEN.<br>Undertakings bring misfortune.<br>Nothing that would further."
	if hexvalue == "101100":
		return "ABUNDANCE has success.<br>The king attains abundance.<br>Be not sad.<br>Be like the sun at midday."
	if hexvalue == "001101":
		return "The Wanderer. Success through smallness.<br>Perseverance brings good fortune<br>To the Wanderer."
	if hexvalue == "011011":
		return "THE GENTLE. Success through what is small.<br>It furthers one to have somewhere to go.<br>It furthers one to see the great man."
	if hexvalue == "110110":
		return "THE JOYOUS. Success.<br>Perseverance is favorable."
	if hexvalue == "010011":
		return "DISPERSION. Success.<br>The king approaches his temple.<br>It furthers one to cross the great water.<br>Perseverance furthers."
	if hexvalue == "110010":
		return "LIMITATION. Success.<br>Galling limitation must not be persevered in."
	if hexvalue == "110011":
		return "INNER TRUTH. Pigs and fishes.<br>Good fortune.<br>It furthers one to cross the great water.<br>Perseverance furthers."
	if hexvalue == "001100":
		return "PREPONDERANCE OF THE SMALL. Success.<br>Perseverance furthers.<br>Small things may be done; great things should not be done.<br>The flying bird brings the message:<br>It is not well to strive upward,<br>It is well to remain below.<br>Great good fortune."
	if hexvalue == "101010":
		return "AFTER COMPLETION. Success in small matters.<br>Perseverance furthers.<br>At the beginning good fortune.<br>At the end disorder."
	if hexvalue == "010101":
		return "BEFORE COMPLETION. Success.<br>But if the little fox, after nearly completing the crossing,<br>Gets his tail in the water,<br>There is nothing that would further."

def interpret_image(hexvalue):
	if hexvalue == "111111":
		return "The movement of heaven is full of power.<br>Thus the superior man makes himself strong and untiring."
	if hexvalue == "000000":
		return "The earth's condition is receptive devotion.<br>Thus the superior man who has breadth of character<br>Carries the outer world."
	if hexvalue == "100010":
		return "Clouds and thunder:<br>The image of DIFFICULTY AT THE BEGINNING.<br>Thus the superior man<br>Brings order out of confusion."
	if hexvalue == "010001":
		return "A spring wells up at the foot of the mountain: <br>The image of YOUTH.<br>Thus the superior man fosters his character<br>By thoroughness in all that he does."
	if hexvalue == "111010":
		return "Clouds rise up to heaven:<br>The image of WAITING.<br>Thus the superior man eats and drinks,<br>Is joyous and of good cheer"
	if hexvalue == "010111":
		return "Heaven and water go their opposite ways:<br>The image of CONFLICT.<br>Thus in all his transactions the superior man<br>Carefully considers the beginning."
	if hexvalue == "010000":
		return "In the middle of the earth is water:<br>The image of THE ARMY.<br>Thus the superior man increases his masses<br>By generosity toward the people."
	if hexvalue == "000010":
		return "On the earth is water:<br>The image of HOLDING TOGETHER.<br>Thus the kings of antiquity<br>Bestowed the different states as fiefs<br>And cultivated friendly relations<br>With the feudal lords."
	if hexvalue == "111011":
		return "The wind drives across heaven:<br>The image of THE TAMING POWER OF THE SMALL.<br>Thus the superior man<br>Refines the outward aspect of his nature."
	if hexvalue == "110111":
		return "Heaven above, the lake below:<br>The image of TREADING.<br>Thus the superior man discriminates between high and low,<br>And thereby fortifies the thinking of the people."
	if hexvalue == "111000":
		return "Heaven and earth unite: the image of PEACE.<br>Thus the ruler<br>Divides and completes the course of heaven and earth,<br>And so aids the people."
	if hexvalue == "000111":
		return "Heaven and earth do not unite:<br>The image of STANDSTILL.<br>Thus the superior man falls back upon his inner worth <br>In order to escape the difficulties.<br>He does not permit himself to be honored with revenue."
	if hexvalue == "101111":
		return "Heaven together with fire:<br>The image of FELLOWSHIP WITH MEN.<br>Thus the superior man organizes the clans<br>And makes distinctions between things."
	if hexvalue == "111101":
		return "Fire in heaven above:<br>the image of POSSESSION IN GREAT MEASURE.<br>Thus the superior man curbs evil and furthers good,<br>And thereby obeys the benevolent will of heaven."
	if hexvalue == "001000":
		return "Within the earth, a mountain:<br>The image of MODESTY.<br>Thus the superior man reduces that which is too much,<br>And augments that which is too little.<br>He weighs things and makes them equal."
	if hexvalue == "000100":
		return "Thunder comes resounding out of the earth:<br>The image of ENTHUSIASM.<br>Thus the ancient kings made music <br>In order to honor merit,<br>And offered it with splendor<br>To the Supreme Deity,<br>Inviting their ancestors to be present."
	if hexvalue == "100110":
		return "Thunder in the middle of the lake:<br>The image of FOLLOWING.<br>Thus the superior man at nightfall<br>Goes indoors for rest and recuperation."
	if hexvalue == "011001":
		return "The wind blows low on the mountain:<br>The image of DECAY.<br>Thus the superior man stirs up the people<br>And strengthens their spirit."
	if hexvalue == "110000":
		return "The earth above the lake:<br>The image of APPROACH.<br>Thus the superior man is inexhaustible<br>In his will to teach,<br>And without limits<br>In his tolerance and protection of the people."
	if hexvalue == "000011":
		return "The wind blows over the earth:<br>The image of CONTEMPLATION.<br>Thus the kings of old visited the regions of the world,<br>Contemplated the people,<br>And gave them instruction."
	if hexvalue == "100101":
		return "Thunder and lighting:<br>The image of BITING THROUGH.<br>Thus the kings of former times made firm the laws<br>Through clearly defined penalties."
	if hexvalue == "101001":
		return "Fire at the foot of the mountain:<br>The image of GRACE.<br>Thus does the superior man proceed <br>When clearing up current affairs.<br>But he dare not decide controversial issues in this way."
	if hexvalue == "000001":
		return "The mountain rests on the earth:<br>The image of SPLITTING APART.<br>Thus those above can ensure their position<br>Only by giving generously to those below."
	if hexvalue == "100000":
		return "Thunder within the earth:<br>The image of THE TURNING POINT<br><br>Thus the kings of antiquity closed the passes <br>At the time of solstice.<br>Merchants and strangers did not go about,<br>And the ruler<br>Did not travel through the provinces."
	if hexvalue == "100111":
		return "Under heaven thunder rolls:<br>All things attain the natural state of innocence.<br>Thus the kings of old,<br>Rich in virtue, and in harmony with the time,<br>Fostered and nourished all beings."
	if hexvalue == "111001":
		return "Heaven within the mountain:<br>The image of THE TAMING POWER OF THE GREAT.<br>Thus the superior man acquaints himself with many sayings of antiquity<br>And many deeds of the past,<br>In order to strengthen his character thereby."
	if hexvalue == "100001":
		return "At the foot of the mountain, thunder:<br>The image of PROVIDING NOURISHMENT.<br>Thus the superior man is careful of his words<br>And temperate in eating and drinking."
	if hexvalue == "011110":
		return "The lake rises above the trees:<br>The image of PREPONDERANCE OF THE GREAT.<br>Thus the superior man, when he stands alone,<br>Is unconcerned,<br>And if he has to renounce the world,<br>He is undaunted."
	if hexvalue == "010010":
		return "Water flows on uninterruptedly and reaches its goal:<br>The image of the Abysmal repeated.<br>Thus the superior man walks in lasting virtue<br>And carries on the business of teaching."
	if hexvalue == "101101":
		return "That which is bright rises twice:<br>The image of FIRE.<br>Thus the great man, by perpetuating this brightness,<br>Illumines the four quarters of the world."
	if hexvalue == "001110":
		return "A lake on the mountain:<br>The image of influence.<br>Thus the superior man encourages people to approach him<br>By his readiness to receive them."
	if hexvalue == "011100":
		return "Thunder and wind: the image of DURATION.<br>Thus the superior man stands firm <br>And does not change has direction."
	if hexvalue == "001111":
		return "Mountain under heaven: the image of RETREAT.<br>Thus the superior man keeps the inferior man at a distance,<br>Not angrily but with reserve."
	if hexvalue == "111100":
		return "Thunder in heaven above:<br>The image of THE POWER OF THE GREAT.<br>Thus the superior man does not tread upon paths<br>That do not accord with established order."
	if hexvalue == "000101":
		return "The sun rises over the earth:<br>The image of PROGRESS.<br>Thus the superior man himself<br>Brightens his bright virtue."
	if hexvalue == "101000":
		return "The light has sunk into the earth:<br>The image of DARKENING OF THE LIGHT.<br>Thus does the superior man live with the great mass:<br>He veils his light, yet still shines."
	if hexvalue == "101011":
		return "Wind comes forth from fire<br>The image of THE FAMILY.<br>Thus the superior man has substance in his word<br>And duration in his way of life."
	if hexvalue == "110101":
		return "Above, fire; below. The lake<br>The image of OPPOSITION<br>Thus amid all fellowship<br>The superior man retains his individuality."
	if hexvalue == "001010":
		return "Water on the mountain<br>The image of OBSTRUCTION<br>Thus the superior man turns his attention to himself<br>And molds his character."
	if hexvalue == "010100":
		return "Thunder and rain set in<br>The image of DELIVERANCE<br>Thus the superior man pardons mistakes<br>And forgives misdeeds."
	if hexvalue == "110001":
		return "At the foot of the mountain, the lake<br>The image of DECREASE<br>Thus the superior man controls his ange<br>And restrains his instincts."
	if hexvalue == "100011":
		return "Wind and thunder: the image of INCREASE<br>Thus the superior man<br>If he sees good, he imitates it<br>If he has faults, he rids himself of them."
	if hexvalue == "111110":
		return "The lake has risen up to heaven:<br>The image of BREAK-THROUGH.<br>Thus the superior man<br>Dispenses riches downward<br>And refrains from resting on his virtue."
	if hexvalue == "011111":
		return "Under heaven, wind<br>The image of COMING TO MEET<br>Thus does the prince act when disseminating his command<br>And proclaiming them to the four quarters of heaven."
	if hexvalue == "000110":
		return "Over the earth, the lake<br>The image of GATHERING TOGETHER<br>Thus the superior man renews his weapon<br>In order to meet the unforeseen."
	if hexvalue == "011000":
		return "Within the earth, wood grows<br>The image of PUSHING UPWARD<br>Thus the superior man of devoted characte<br>Heaps up small thing<br>In order to achieve something high and great."
	if hexvalue == "010110":
		return "There is not water in the lake<br>The image of EXHAUSTION<br>Thus the superior man stakes his life<br>On following his will."
	if hexvalue == "011010":
		return "Water over wood: the image of THE WELL<br>Thus the superior man encourages the people at their work<br>And exhorts them to help one another."
	if hexvalue == "101110":
		return "Fire in the lake: the image of REVOLUTION<br>Thus the superior man<br>Sets the calendar in orde<br>And makes the seasons clear."
	if hexvalue == "011101":
		return "Fire over wood<br>The image of THE CALDRON<br>Thus the superior man consolidates his fate<br>By making his position correct."
	if hexvalue == "100100":
		return "Thunder repeated: the image of SHOCK<br>Thus in fear and tremblin<br>The superior man sets his life in orde<br>And examines himself."
	if hexvalue == "001001":
		return "Mountains standing close together<br>The image of KEEPING STILL<br>Thus the superior man<br>Does not permit his thoughts<br>To go beyond his situation."
	if hexvalue == "001011":
		return "On the mountain, a tree<br>The image of DEVELOPMENT<br>Thus the superior man abides in dignity and virtue<br>In order to improve the mores."
	if hexvalue == "110100":
		return "Thunder over the lake<br>The image of THE MARRYING MAIDEN<br>Thus the superior man<br>Understands the transitor<br>In the light of the eternity of the end."
	if hexvalue == "101100":
		return "Both thunder and lightning come<br>The image of ABUNDANCE<br>Thus the superior man decides lawsuit<br>And carries out punishments."
	if hexvalue == "001101":
		return "Fire on the mountain<br>The image of THE WANDERER<br>Thus the superior man<br>Is clear-minded and cautious<br>In imposing penalties<br>And protracts no lawsuits."
	if hexvalue == "011011":
		return "Winds following one upon the other<br>The image of THE GENTLY PENETRATING<br>Thus the superior man<br>Spreads his commands abroad<br>And carries out his undertakings."
	if hexvalue == "110110":
		return "Lakes resting one on the other<br>The image of THE JOYOUS<br>Thus the superior man joins with his friend<br>For discussion and practice."
	if hexvalue == "010011":
		return "The wind drives over the water<br>The image of DISPERSION<br>Thus the kings of old sacrificed to the Lor<br>And built temples."
	if hexvalue == "110010":
		return "Water over lake: the image of LIMITATION<br>Thus the superior man<br>Creates number and measure<br>And examines the nature of virtue and correct conduct."
	if hexvalue == "110011":
		return "Wind over lake: the image of INNER TRUTH<br>Thus the superior man discusses criminal cases<br>In order to delay executions."
	if hexvalue == "001100":
		return "Thunder on the mountain:<br>The image of PREPONDERANCE OF THE SMALL.<br>Thus in his conduct the superior man gives preponderance to reverence.<br>In bereavement he gives preponderance to grief.<br>In his expenditures he gives preponderance to thrift."
	if hexvalue == "101010":
		return "Water over fire: the image of the condition<br>In AFTER COMPLETION<br>Thus the superior man<br>Takes thought of misfortun<br>And arms himself against it in advance."
	if hexvalue == "010101":
		return "Fire over water:<br>The image of the condition before transition.<br>Thus the superior man is careful<br>In the differentiation of things,<br>So that each finds its place."

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
		return "(Pi) Holding Together [union] - 8"
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
				linesStrings.append('<div class="oldyin">&nbsp;</div>')
			elif val3 < 0.5:
				linesbyte += "0"
				hexagrambyte += "1"
				linesStrings.append('<div class="yin">&nbsp;</div>')
		elif val2 < 0.5:
			if val3 > 0.5:
				linesbyte += "0"
				hexagrambyte += "1"
				linesStrings.append('<div class="yin">&nbsp;</div>')
			if val3 < 0.5:
				linesbyte += "0"
				hexagrambyte += "0"
				linesStrings.append('<div class="yang">&nbsp;</div>')
	elif val1 < 0.5:
		if val2 < 0.5:
			if val3 < 0.5:
				linesbyte += "1"
				hexagrambyte += "0"
				linesStrings.append('<div class="oldyang">&nbsp;</div>')
			elif val3 > 0.5:
				linesbyte += "0"
				hexagrambyte += "0"
				linesStrings.append('<div class="yang">&nbsp;</div>')
		elif val2 > 0.5:
			if val3 < 0.5:
				linesbyte += "0"
				hexagrambyte += "0"
				linesStrings.append('<div class="yang">&nbsp;</div>')
			if val3 > 0.5:
				linesbyte += "0"
				hexagrambyte += "1"
				linesStrings.append('<div class="yin">&nbsp;</div>')
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


print '<h1>'
print hexagram
print '</h1>'

print '<div class="hexagram">'
for x in reversed(xrange(3, 6)):
	print linesStrings[x]
for x in reversed(xrange(0, 3)):
	print linesStrings[x]
print '</div>'

print '<div class="trigrams">'
print '<div class="uppertrigram ' + upperTrigram + '">'
print upperTrigram
print '</div>'
print '<div class="lowertrigram ' + lowerTrigram + '">'
print lowerTrigram
print '</div>'
print '</div>'

print '<h3>The Judgement</h3>'
print theJudgment

print '<h3>The Image</h3>'
print theImage

if theLines != '':
	print '<h3>The Lines</h3>'
	print theLines
