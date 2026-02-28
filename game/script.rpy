
define n = Character("Nyra")
define m = Character ("Maxwell") 
define a = Character ("Siegfried")
define at = Character ("Alouette")
define msl = Character ("Mrs. Loville")

image maxwell="maxwell yippee.png"

label start:

    scene town square night
    show nyra neutral

    n "(Thank god they’re leaving in a few hours.)"
    n "(Nothing’s happened to our town so far, but I have a feeling something’s going to go wrong soon...)"
    n "(Speaking of things going wrong, where’s Lisbeth? We promised to walk home together.)"
    n "Lisbeth, where are you?"
    "    "
    n "Lisbeth?"
    "    "
    n "(Is that her in the distance? Who's she walking with? It looks like... I guess she's walking home with her sister.)"
    n "(Did Anya always wear her hair in pigtails?)"
    n "And here I thought we’d go home together. I guess I’ll go check on her tomorrow."

    scene black

label house: 
    
    scene house morning
    show maxwell at truecenter 

    n "Mrs. Loville? Is Lisbeth home?"
    msl "Nyra, is that you? I was just about to find you. Lisbeth didn’t return last night!"
    n "What? But I saw her walking with Anya."

    hide maxwell 

    n "(If that wasn’t Anya… then who was that? And why was Lisbeth with her?)"
    n "(No one’s dared to wear pigtails since…)"
    n "(Surely not. I mean, why would Lisbeth go near the circus?)"
    msl "Are you alright?"
    n "Oh, yes. I just… I think I know where Lisbeth is. I’ll bring her home safely."
    msl "Oh, thank you, Nyra."

label circus
    
    scene circus

    n "Hey, hey, hey, wait! Hold on! Stop the circus! Stop driving!"
    n "(They’re either ignoring me or they can’t hear me over the sound of the engine.)"
    n "(I can’t let them leave, not when Lisbeth might be on board!)"
    n "(I have to do something. Surely I don’t have to climb onto the circus, do I..?)"
    n "(I mean, this is Maxwell’s Travelling Circus we’re talking about!)"
    n "(I wouldn’t last a minute in there! They’d find a way to make me disappear for sure.)"
    n "(But Lisbeth’s my friend, and I promised Mrs. Loville..!)"
    n "You can do this, Nyra."
    n "(Three…)"
    n "(Two…)"
    n "One!"

    hide nyra
    scene black

label inner circus
    
    scene inner circus

    n "(It’s surprisingly normal here. I was expecting some ominous darkness but…)"
    n "(People are joking and chatting without a care in the world.)"



    



