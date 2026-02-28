# implement lofi
# bug where maxwell and aloutette overlap in the end
define n = Character("Nyra", colour = "#4e7ac2")
define m = Character ("Maxwell") 
define s = Character ("Siegfried")
define a = Character ("Alouette")
define msl = Character ("Mrs. Loville")
define ls = Character ("Lisbeth")
define v1 = Character ("Voice One")
define v2 = Character ("Voice Two")

# maxwell
image m = "maxwell mild.png"
image mxevil = "maxwell sinister.png"
image mxyippee = "maxwell yippee.png"
# alouette updated
image alkind = "alkind2.png"
image almur = "almurder2.png"
image alom = "alouette ominous2.png"
# siegfried
image sconf = "siege conf.png"
image snorm = "sieg norm.png"
image som = "siege ominous.png"
image ssad = "siege sad.png"
# nyra updated
image nd = "nyra determined.png"
image ns = "nyra scared.png"
image nsh = "nyra shocked.png"
image nsm = "nyra smile.png"


label start:

    scene black with Fade(1.0, 1.0, 1.0)
    scene town 
    show nsm at left

    n "(Thank god they’re leaving in a few hours.)"
    n "(Nothing’s happened to our town so far, but I have a feeling something’s going to go wrong soon...)"

    hide nsm
    show ns at left

    n "(Speaking of things going wrong, where’s Lisbeth? We promised to walk home together.)"
    n "Lisbeth, where are you?" with vpunch
    "    "
    n "Lisbeth?" with vpunch
    "    "
    n "(Is that her in the distance? Who's she walking with? It looks like... I guess she's walking home with her sister.)"
    n "(Did Anya always wear her hair in pigtails?)"
    n "And here I thought we’d go home together. I guess I’ll go check on her tomorrow."

    show ns at offscreenright

    scene black with Fade(1.0, 1.0, 1.0)

label house: 
    
    scene house
    show nn at left

    n "Mrs. Loville? Is Lisbeth home?"
    msl "Nyra, is that you? I was just about to find you. Lisbeth didn’t return last night!"

    hide nsm
    show nsh at left

    n "What? But I saw her walking with Anya."

    show ns at left

    n "(If that wasn’t Anya… then who was that? And why was Lisbeth with her?)"
    n "(No one’s dared to wear pigtails since…)"
    n "(Surely not. I mean, why would Lisbeth go near the circus?)"
    msl "Are you alright?"

    show nsm at left

    n "Oh, yes. I just… I think I know where Lisbeth is. I’ll bring her home safely."
    msl "Oh, thank you, Nyra."

    hide nsm with dissolve
    scene black with Fade(1.0, 1.0, 1.0)

label outsidecircus:
    play music "circus.mp3"

    scene circus
    show nd with moveinleft

    n "Hey, hey, hey, wait! Hold on! Stop the circus! Stop driving!"

    hide nd 
    show ns at center

    n "(They’re either ignoring me or they can’t hear me over the sound of the engine.)"
    n "(I can’t let them leave, not when Lisbeth might be on board!)"
    n "(I have to do something. Surely I don’t have to climb onto the circus, do I..?)"
    n "(I mean, this is Maxwell’s Travelling Circus we’re talking about!)"
    n "(I wouldn’t last a minute in there! They’d find a way to make me disappear for sure.)"

    hide ns
    show nd at center

    n "(But Lisbeth’s my friend, and I promised Mrs. Loville..!)"
    n "You can do this, Nyra."

    play music "circus.mp3" fadeout 2.0

    n "(Three…)"
    n "(Two…)"

    stop music

    n "One!"

    hide nd with dissolve
    scene black with Fade(1.0, 1.0, 1.0)
    

label storeroom:

    scene black

    ls "Hello?"
    ls "Nyra? Anya?"
    ls "Is anyone there?"

    pause 2.0
    show ns with fade 
    
    n "(..Ouch.)"
    n "(It's so dark. My back hurts like crazy. But I think I'm in the circus!)"

    hide ns
    show nsh at center

    v1 "The girl... Yes..."

    hide nsh
    show nd at center

    n "(Someone is coming. I should hide.)"

    hide nd with fade
    scene black at vpunch

    v2 "She's going to be useless and you know it!"
    v1 "If Wrath, of all people, can take an interest in her, it means-"
    v2 "-Wrath’s insane. Just because the girl’s immune to most of Gluttony’s drugs and poisons doesn’t mean-"
    v1 "Or it means we finally have a lab rat that won’t die after a few days."
    v2 "Ugh, why are we always doing the heavy lifting? I thought Pride was recruiting more performers."
    n "(The voices are getting further away...)"

    scene storeroom with fade
    show nd 

    n "(So there was a light here after all.)"
    n "(The girl they were talking about… I’m sure it’s Lisbeth. They’re planning to use her as a lab rat.)"
    n "(I knew there was something off about this circus! The rumours... How can I get Lisbeth out of here?)"
    "    "
    n "(Hold on… Pride was recruiting performers…)"
    n "You got this. Do it for Lisbeth!"

    scene black with Fade(1.0, 1.0, 1.0)

label innercircus:
    
    play music "circus lil creepy.mp3" loop
    scene inner circus
    show nd at left

    n "(It’s surprisingly normal here. I was expecting some ominous darkness but…)"
    n "(People are joking and chatting without a care in the world.)"

    show snorm 
    
    n "Excuse me? Where can I find Pride?"

    hide snorm
    show sconf at right

    s "What do you need the Ringmaster for?"

    hide nd
    show nsm at left

    n "I’m here for the… the recruitments for performers!"

    hide sconf
    show snorm at right

    s "Oh, well you’re quite late, aren’t you? The others have already gone to the Ringmaster’s office. I’ll take you there now. If we’re quick, you can make it."
    n "Thank you."

    hide snorm with dissolve
   
    n "(How kind of him. I thought they’d all be snappish and mean off the bat.)"
    n "(I did hear a rumour that night was when things actually happened. I need to find Lisbeth and get out of here before that.)"

    hide nsm
    scene black with Fade(1.0, 1.0, 1.0)
    play music "circus lil creepy.mp3" fadeout 2.0 

    scene inner circus
    show nsm at right 
    show mxyippee with moveinleft
    play music "circus creepy" loop
    
    m "Welcome to Maxwell’s Travelling Circus. I’m the Ringmaster, Maxwell."

    hide mxyippee
    show m at center

    m "Luckily for you, you’re in the right place! Of course, I may not be the most talented individual, but I believe that all of our performers are equally talented."

    hide m
    show mxevil at center

    m "There are rules you must follow to keep order within the circus, and consequences if you cannot abide by them."

    hide mxevil
    show mxyippee

    m "Of course, if you don’t trust in my ability to punish thoroughly, Alouette is strict enough for all of us!"

    hide nsm
    show ns at right

    n "(Alouette… I know that name. She’s that serial killer that completely disappeared off the radar a few months ago!)"

    hide mxyippee
    show m at center

    m "You may go now. Siegfried will help you get settled down."
    
    hide m with dissolve
    hide ns with dissolve
    
    scene black
    pause 2.0
    play music "circus creepy.mp3" fadeout 1.0
    scene inner circus 
    show nd at left
    play music "circus lil creepy.mp3" fadein 1.0 

    n "(There’s no one here. Where’d everyone go? This is a perfect time to look for Lisbeth.)"

    show alom at right

    a "Hey. What are you doing?"

    hide nd
    show nsh at left

    n "AAAHHHHHHHH!" with vpunch 
    
    hide alom
    show alkind at right

    a "I didn’t mean to scare you. Everyone else is in the dining hall, I was just curious why you’re here. Are you lost?"

    pause 2.0
    hide nsh
    show nsm at left

    n "Y-yeah, I’m lost! It’s a really big circus, and I can’t find my way around.."
    a "I’ll lead you to the dining hall. There’s gonna be a surprise tonight, you know?"

    hide alkind with dissolve
    hide nsm with dissolve
    scene black with Fade(1.0, 1.0, 1.0)
    scene inner circus 
    show ns at left

    n "(Thank god Alouette didn’t sit with me.)"
    n "(I thought my heart was going to burst out of my chest every time she moved!)"

    hide ns
    show nd at left

    n "(Well it’s night-time now, and all the other performers are outside. Alouette told me it was an auction.)"
    n "(I don’t think anyone will realise I’m gone. I just need to find Lisbeth quickly.)"

    show alom at right
    hide nd
    show nsh at left
    play music "circus lil creepy.mp3" fadeout 1.0
    play music "circus creepy.mp3" fadein 1.0

    a "Who’s there?"

    hide alom
    show almur at center 

    a "Come out, little mouse! You know you’re not meant to be here~"

    pause 1.0
    hide nsh
    show ns at left
    pause 0.5
    hide ns with fade

    pause 1.0
    hide snorm
    show snorm at right
    
    hide almur
    show alkind at center
    s "Alouette, what are you doing? The auctions’ starting and they’ve already sold off a bunch of the good stuff. I heard Sloth already scored a whole set of new organs."

    hide snorm
    show som at right

    s "Whatever it is, I’m sure it can wait. No one’s getting out alive tonight."
    n "(...Right. I’m in the underworld now. Nothing functions the same. They’re all criminals with no conscience.)"

    hide alkind
    show alom at center

    a "Ugh, him and his organs! Of course he wouldn’t leave anything good for me!"
    s "Let’s hurry before he and Greed take everything else."

    hide alom with dissolve
    hide som with dissolve
    show ns at left

    n "Phew…"

    show m at right

    m "Busy day?"

    hide ns 
    show nsh at left 

    n "What the-"

    hide m
    show mxevil at right

    m "I’d be quiet if I were you."

    hide nsh
    show ns at left

    m "So, why are you actually here?"
    m "I’m sure someone like you can’t have felt compelled to join my troupe all of a sudden."

    hide mxevil
    show m at right
    
    "(Ringmaster Maxwell’s smile is perfectly polite and kind, but there’s an unmistakable edge of murderous anger.)"
    "(He may not be as well known as Alouette in the criminal world, but his intimidating aura suggests he wasn’t just some petty thief.)"
    "(Where’s the polite, humble man from before?)"
    "(This is the real Maxwell. The proud individual that controlled the entire circus.)"

    n "Ringmaster Maxwell…"
    m "I trust you heard what they said. I’m afraid neither you nor your friend will be leaving any time soon."
    n "(The way he can act like this is just a pleasant teatime chat, while also smiling like he wants to carve out my skull is so frightening.)"
    n "(I can’t run. There’s nowhere to go, and I haven’t found Lisbeth.)"

    show alom at center 

    a "So there’s a mouse hiding here after all~"

    hide ns
    show nsh at left
    hide alom
    show almur at center

    n "(Alouette!? I thought she and Siegfried left already!)" with vpunch

    hide nsh
    show ns at left

    a "Lisbeth’s friend..? Then I’m sure you’ll be overjoyed to join her."
    n "Join her!? What do you-" with vpunch

    hide m
    show mxevil at right

    m "Good night, Nyra."

    play music "circus creepy.mp3" fadeout 9.5 
    scene black with Fade(10.0, 0.0, 0.0)