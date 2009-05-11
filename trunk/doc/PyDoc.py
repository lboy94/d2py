'''
WHAT I WANT TO DO:

	I want to write a scriptable D2 botting system. My goal is to split it
into two parts. A small, thin Core that provides an interface between the bot and 
D2 and has no restrictions on how it's implemented; and a large, fancy Python bot
that builds up a complex system from the Core's elementary building blocks.
	Putting most of the work into the Python engine will allow the Core to
survive patches, and provide many possible ways to implement it. The same bot could
use a RedVex-based core, or an injection-based core, or even a fully clientless one!


WHY AM I DOING THIS:

	I want to learn.
        Writing a stable D2 bot that's easy to expand and politely handles connection
drops and deaths is a fairly generic challenge that should teach me many lessons and 
transfer over to any project (even some non-software ones) that I work on in the future.
	Yes, I realize that D2BS and Awesome-O are open source and can always use 
contributions. However, learning to design large projects is an obsession of mine:
it transcends mere grunt-work programming and works on a totally different (and
fascinating) level.
	I realize that devoting my time to existing projects would produce more
results, but starting from scratch will let me apply everything I've learned and
heard about and see how it really works.
	Besides: united we fall, divided we stand. The more options there are,
the better.


WILL I BE A DICK AND CHARGE $25 BUCKS PER COPY IF IT GETS DONE:

No. :(


DESIGN PRINCIPLES:

	Perfection is reached not when there's no more features to add, but
when there's no unnecessary bulk left to remove.
	Don't optimize unnecessarily. Avoid making choices that improve
performance at the cost of abstraction at all costs.
	Abstract the details. Use bot-specific strings instead of D2-specific
flags and ids. Use item/monster/player objects instead of protocol-specific
identifiers.
	Document and plan before implementing. Comment thoroughly. 


SYSTEM OVERVIEW:

It will come in two main parts, CORE and ENGINE:

	The CORE is an API that gives the bot access to the game. It must be:
Flexible: it has to provide enough interfaces to write a bot with.
General: allowing varied implementations (redvex, injection, clientless, w/e)
Abstraction: the details of the implementation are hidden whenever possible, 
	so the script writer doesn't care how it's interfaced to the game.
Modular: to allow different implementations, the Core is segmented into different
	portions. There are critical parts that any implementation must implement,
	and optional parts that may or may not be implemented.

	The ENGINE is a pile of Python that builds on the basic blocks of the core
to provide botting functionality. It should call all the shots, and be expandable
via custom modules.

	The MODULES follow a common structure, each one providing some key
piece of functionality. I have some ideas (oh god I'm so excited) on how this can
be done.


The goal is to make sure most of the work is put into the Engine and Modules. The 
core should be a thin layer, providing an abstraction of the D2 game. This makes
it easy to replace with something totally different (and possibly more secure) so
we don't have something like D2JSP, where a large collection of helpful and creative
scripts were rendered useless.


	Let's get something straight: I like botting, and I like Diablo 2, and I
don't think one harms the other when done by individuals for their own enjoyment.
TPPK, item shops, and lag dupes hurt D2. Bots provide people with an introduction
to software automation and programming, provoke an interest in computer science,
and make the best damn screensavers I've ever seen. The end goal of this project
is to enrich people's D2 experience.




Bot goals, easy to hard:
	gem cuber module
	shopbot/gambler module
	pvp bear-bot
	travincial runner
	baal tppk bot
	baal runner
	uberbot
	leecher
	cower-bot
	team bot
	full rush bot
	full 1-90 bot


	Sample loop:
start d2
log in
make game
town
	repair
	sell loot, buy pots/scrolls
	revive merc
path2baal
	waypoint
	teleportl3, kill en route?
	teleportl4, kill en route?
clear throne
tp & party
clear throne until baal runs
follow baal and kill him
exit
repeat from "make game"


All the following modules are in d2py.baal unless specified otherwise:

baalbot		// failure response:
-1234 		//	d2 crash: throw out 1-level, baalbot reseeds
 startup	// 	key/login fail: throw out 0-level, bot fails
 login		// 	network timeout fail: replace 1-level with delay module
 runbaal	// 
baalbot 	// 
-1234
 startup* 	// * means executed and no longer on stack
 login*
  channel
  newgame
  baalrun
  exit
 runbaal
baalbot
-1234
  channel*
  newgame*
   town		// baalrun, unlike baalbot/runbaal, is replaced rather than preceded
   path2baal
   clearthrone	// failure response:
   party	// 	c/i: throw out 3-level
   tp		// 	hard chicken: throw out 3-level
   baalwaves	//	death: throw out 3-level, runbaal must handle death!
   waitbaal	//	hostile: shitlist player+quit?
   path2throneroom // no money: if no scrolls, quit lol
   killbaal	// no scrolls: gg no rm
  exit
 runbaal
baalbot
-1234
    identify*
    malah*
    repair*
    merc*
   
    buff*
    wp*
    tele*
    door*
    tele*
    door*
    tele*
     attacktarget*
    killtarget*
   clearthrone
   party
   tp
     buff
    waitminions
      attacktarget
     killtarget
    cleararea
    baalwaves2345
   baalwaves
   waitbaal

Hey wait... These are the same as functions. I want to rebiuld a function stack from
scratch. Hum.

This problem is similar to a process scheduler in an operating system. There are tasks
of varying priorities: critical "I'm dying!" high "phat lewt!" normal "kill target"
and low "repair gear soon-ish", "buff myself".

Have to do multiple stacks somehow. Scheduling algorithms come into play. Priority
pre-emptive, priority non-pre-emptive, shortest job first?
I mean, some tasks (pickingup+dropping merc weapon to reset aura) may NOT be interrupted
so there needs to be a way to ensure that.


Actions fall into categories:
	instant: doesn't need to be scheduled
potions, exit, chat 
	hold: cannot be interrupted
cast spell, attack, take waypoint?
	fragile: broken if interrupted
walking
	strong: can be interrupted
waiting
	



Problem: what if you move an item, but lag delays the move?


startd2
login
selchar
baalloop
-- execution runs fine down to baalloop, which explodes
chatannounce
newgame
baalrun
exit
baalloop
-- execution runs down to baalrun, which explodes
town
path2baal
clearthrone
party
tp
baalwaves	# waitminions-clearminions repeated 5 times
waitbaal
followbaal
killbaal
exit
baalloop
--




Idea: configuration is a dictionary key:value list passed to everything,
missing config throws exception resulting in restart. Check config completeness
prior to running, print __doc__ messages for missing config if check fails.


GENERAL ACTION DESCRIPTION:

	Actions can be grouped into hierarchy, with large actions broken up into
many smaller ones. A way to implement them is to have a stack: start stack with
"baalbot", which explodes into "startD2;login;baalloop", each one of those exploding
into more components.
	This has the potential of injecting N-level components without interrupting
the overall logic flow: example is soft-chicken, merc revives.
	Actions are implemented as modules.
	Modules/actions (I need to settle on a name) conform to a hierarchy that
determines which state they are valid in? States are: started/loggedin/inchat/ingame.
Possibly even more states: town/combat/dead?

	Challenges that must be solved:
-politely handling exceptions like connection drop/realm down/death
-handling instant actions (switch skill) possibly long actions (teleport to XY)
and response 'callback' actions (hp change, network lag, player joins, monster spawns?)
-handling module failures - what if pathing failed due to desynch, or a seal is bugged
and can't be popped, or teleporting/killing a monster fails due to lag/position?

Idea: position stack. Push a position (state?+act+area+XY) to save it, then a pop()
function paths back to that position.

repair
	pushPosition
	pathTo(repairNPC)
	repair
	popPosition


cube
	clear out cube?
	find lowest-level gem/rune combo
	put components into cube
	cube
	take components out
	repeat

Idea: polymorphic modules. Example: player joined module, have unconditional party
or unconditional hostile or whitelist-based or "this player hostiled me" shitlist based
invite system.

Idea: swap gear with that in stash to BO/BC buff (use swap item trick)

EXCEPTIONS:
	
	Error: game connection dropped
	Response: pop all in-game modules present, restart from 'make game'

	Error: realm down
	Response: pop almost all modules, add a wait module to re-try later

	Error: death
	Response: pop all in-game modules, start new game, get corpse

	Error: out of gold
	Response: gg no rm

	Error: gamecrash
	Response: pop all, redo from complete start?



Idea: use python filter (is that the right name?) functions to filter lists?
'''

#CORE:


Events:
	hpChange
	playerJoined/Left
	networkStillForNSeconds
	itemDropped
        chatReceived?


# this could be done by filtering owned items of type scroll and interacting
# if a result is found: I guess it should thus be a module, not a Core feature
bool townPortal()	
''' Fast-opens a town portal by activating a tome or scroll of town
portal in the inventory. Does not muck about with skill switching.
    If no tome/scroll visible in inventory or belt, returns false, else
returns true.
'''

Idea: priority queues, allowing several tasks (teleport to baal + kill all superuniques
+ loot all awesome items) to be run at once?







