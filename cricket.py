import numpy as np
import time

class Team():
    def __init__(self,number_of_players):
        self.number_of_players = number_of_players


class Match():
    def __init__(self,overs):
        self.overs = overs
        self.score = 0
        self.wicket_fallen = 0
        self.current_balls = 0
        
    def total_balls(self):
        return self.overs * 6
   
    def one_run(self):
        self.single_possible_outcome=["Just a single",
                "A quick single",
                "changed the strike with one run",
                "Just one run"]
        self.single_outcome = np.random.choice(self.single_possible_outcome, 1)
        return self.single_outcome[0]

    def two_run(self):
        self.double_possible_outcome=["They have taken two",
                "Good running between the wickets, they have taken two",
                "Easy two"]
        self.double_outcome = np.random.choice(self.double_possible_outcome, 1)
        return self.double_outcome[0]

    def three_run(self):
        self.triple_possible_outcome=["They have taken three runs!!",
                "Misfield in the deep and they have taken three",
                "They are quite energetic, completed three runs"]
        self.triple_outcome = np.random.choice(self.triple_possible_outcome, 1)
        return self.triple_outcome[0]
   
    def four_run(self):
        self.four_possible_outcome=["Excellent Shot",
                "Great cover drive",
                "Straight down the ground for four",
                "very well executed shot"]
        self.four_outcome = np.random.choice(self.four_possible_outcome, 1)
        return self.four_outcome[0]

    def six_run(self):
        self.six_possible_outcome=["Excellent Shot",
                "This one is gonna touch the sky",
                "Sky shot",
                "Phenomenal"]
        self.six_outcome = np.random.choice(self.six_possible_outcome, 1)
        return self.six_outcome[0]

    def wkt_caught(self):
        self.caught_possible_outcome=["He has taken this one",
                "Great Catch!!",
                "A dolly",
                "High up in the air and taken"]
        self.caught_outcome = np.random.choice(self.caught_possible_outcome, 1)
        return self.caught_outcome[0]

    def wkt_bowled(self):
        self.bowled_possible_outcome=["Bowled Him!!",
                "Middle Stump Gone!!",
                "Nice Bowl, hitting the stump"]
        self.bowled_outcome = np.random.choice(self.bowled_possible_outcome, 1)
        return self.bowled_outcome[0]

    def wkt_run_out(self):    
        self.runout_possible_outcome=["Great fielding, throw hitting the stump and he's gone....Run OUT!!!",
                "Misunderstanding between the batsmen and out!",
                "Slow Running"]
        self.runout_outcome = np.random.choice(self.runout_possible_outcome, 1)
        return self.runout_outcome[0]

    def wkt_lbw(self):
        self.lbw_possible_outcome=["LBW"]
        self.lbw_outcome = np.random.choice(self.lbw_possible_outcome, 1)
        return self.lbw_outcome[0]
    
    def wkt_stump(self):
        self.stump_possible_outcome=["Batsman was outside the crease and keeper have stumped him",
                "Nice stumping",
                "Awesome reflexes shown by keeper and he's out stumped!!!"]
        self.stump_outcome = np.random.choice(self.stump_possible_outcome, 1)
        return self.stump_outcome[0]

    def outcome_fn(self):
        self.wicket_outcome=['Caught Out','Bowled','Run Out','LBW','Stumped Out']
        self.wicket_outcome_prob=[0.4,0.3,0.1,0.1,0.1]
        self.wicket=np.random.choice(self.wicket_outcome, 1, p=self.wicket_outcome_prob)
        self.outcome=['1','2','3','4','6','Wide','No Ball', self.wicket[0]]
        self.outcome_prob=[0.30,0.15,0.05,0.20,0.15,0.05,0.05,0.05]
        self.result=np.random.choice(self.outcome, 1, p=self.outcome_prob)
        if self.result[0] == self.wicket[0]:
            if(self.result[0]=='Caught Out'):
                print(self.wkt_caught())
            elif(self.result[0]=='Bowled'):
                print(self.wkt_bowled())
            elif(self.result[0]=='Run Out'):
                print(self.wkt_run_out())
            elif(self.result[0]=='LBW'):
                print(self.wkt_lbw())
            elif(self.result[0]=='Stumped Out'):
                print(self.wkt_stump)
            else:
                print("Out")
            self.wicket_fallen += 1
            self.current_balls += 1
        elif self.result[0] == 'Wide' or  self.result[0] == 'No Ball':
            self.score +=1
        else:
            current_run_score =  int(''.join(self.result))
            if(current_run_score==1):
                print(self.one_run())
            elif(current_run_score==2):
                print(self.two_run())
            elif(current_run_score==3):
                print(self.three_run())
            elif(current_run_score==4):
                print(self.four_run())
            elif(current_run_score==6):
                print(self.six_run())
            else:
                print("Invalid")
            self.score += current_run_score 
            self.current_balls += 1
            
        return self.score,self.current_balls,self.wicket_fallen
   
#    def current_score(self):
 #       return self.outcome_fn()[0]

    def print_score(self):
        print("After {}.{} overs, score is {}/{}\n".format((self.current_balls)//6, (self.current_balls) % 6, self.outcome_fn()[0],self.wicket_fallen))
        time.sleep(0.1)
            

players = 11
total_overs=(int(input("Enter the numbers of overs in the match")))
t1= Match(total_overs)
t2= Match(total_overs)

while(t1.current_balls <= t1.total_balls() and t1.wicket_fallen < players-1):
    t1.print_score()

t1_score = t1.outcome_fn()[0]

print("Second Innings Starts now\n")

while(t2.current_balls <= t2.total_balls() and t2.wicket_fallen < players - 1):
    t2.print_score()
t2_score = t2.outcome_fn()[0]

if(t1_score < t2_score):
    print("Team 1 Wins")
elif(t1_score < t2_score):
    print("Team 2 Wins")
else:
    print("Its a Draw")
