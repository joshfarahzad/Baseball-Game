from sys import exit
from random import randint

#Executed when the player strikes out
class Out(object):

    ending_lines = [
        "Looks like Michael Kay won't be saying your name :(",
        "Get out of the stadium.",
        "You have been designated for assignment.",
    ]
    
    def __init__(self):
        pass

    def bye(self):
        print "%s" % Out.ending_lines[randint(0, (len(self.ending_lines)-1))]
        exit(1)


class Pitch(object):

    strike_count = 0
    homerun_count = 0

    global hit_it # catchphrases for when player hits ball
    hit_it = [
        "Boom baby! That's gone.",
        "Yeehaw, you hit that one hard.",
        "Woooooo! That thing is gone!",
        "Damn!!! That's a good ball.",
        "ANDDDD, it's gone!!!"
    ]

    global no_hit
    no_hit = [
        "Ouch! Swing and a miss!",
        "Strikeeee!!!",
        "A big cut, and a big miss"
    ]

    def __init__(self):
        pass
    
    def enter(self):
        print "This pitch has not been described yet."
        exit(1)

    def check_homers(self):
        print "You have %d homerun(s)" % Pitch.homerun_count

    def check_strikes(self):
        if Pitch.strike_count < 3:
            print "You have %d strike(s)" % Pitch.strike_count
        else:
            Seya.bye()
            

class Engine(object):

    def __init__(self):
        pass

    def play(self):
        
        while True:
            print "\n ------------"
            pitching = (randint(0,3)-1)
        
            if pitching == 0:
                ball = CurveBall()
                ball.enter()

            elif pitching == 1:
                ball = FastBall()
                ball.enter()
            else:
                ball = Slider()
                ball.enter()
        

class CurveBall(Pitch):

    def enter(self):
        print "The pitcher throws the ball right at you. The pitch moves up"
        print "after its release has seams that run from 10 O'Clock to 4"
        print "O'Clock. The seems look like lateral railroad tracks."

        what_pitch = raw_input("> ")

        if "curveball" in what_pitch:
            print '%s' % hit_it[randint(0,(len(hit_it)-1))]
            Pitch.homerun_count += 1
            super(CurveBall, self).check_homers()
        else:
            print '%s' % no_hit[randint(0,(len(no_hit)-1))]
            Pitch.strike_count += 1
            super(CurveBall, self).check_strikes()
            
            
class FastBall(Pitch):
    
    def enter(self):
        print "From the box, the pitcher throws the straightest"
        print "pitch. You don't see any seems, only a solid formed of brown and red"
        print "matter."

        what_pitch = raw_input("> ")

        if "fastball" in what_pitch:
            print '%s' % hit_it[randint(0,(len(hit_it)-1))]
            Pitch.homerun_count += 1
            super(FastBall, self).check_homers()
        else:
            print '%s' % no_hit[randint(0,(len(no_hit)-1))]
            Pitch.strike_count += 1
            super(FastBall, self).check_strikes()
            

class Slider(Pitch):

    def enter(self):
        print "At first it looks like a fastball, but as it breaks"
        print "down and away, there's a red dot at about 2 O'Clock."

        what_pitch = raw_input("> ")

        if "slider" in what_pitch:
            print "%s" % hit_it[randint(0, (len(hit_it)-1))]
            Pitch.homerun_count += 1
            super(Slider, self).check_homers()
        else:
            print '%s' % no_hit[randint(0,(len(no_hit)-1))]
            Pitch.strike_count += 1
            super(Slider, self).check_strikes()
            

Seya = Out()
a_game = Engine()
a_game.play()