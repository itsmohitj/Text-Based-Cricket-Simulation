import numpy as np

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
   
    def outcome_fn(self):
        self.wicket_outcome=['Caught Out','Bowled','Run Out','LBW','Stumped Out']
        self.wicket_outcome_prob=[0.4,0.3,0.1,0.1,0.1]
        self.wicket=np.random.choice(self.wicket_outcome, 1, p=self.wicket_outcome_prob)
        self.outcome=['1','2','3','4','6','Wide','No Ball', self.wicket[0]]
        self.outcome_prob=[0.30,0.15,0.05,0.20,0.15,0.05,0.05,0.05]
        self.result=np.random.choice(self.outcome, 1, p=self.outcome_prob)
        if self.result[0] == self.wicket[0]:
            self.wicket_fallen += 1
            self.current_balls += 1
        elif self.result[0] == 'Wide' or  self.result[0] == 'No Ball':
            self.score +=1
        else:
            self.score += int(''.join(self.result))
            self.current_balls += 1
        return self.score,self.current_balls,self.wicket_fallen
   
#    def current_score(self):
 #       return self.outcome_fn()[0]

    def print_score(self):
        print("After {}.{} overs, score is {}/{}".format((self.current_balls)//6, (self.current_balls) % 6, self.outcome_fn()[0],self.wicket_fallen))
            

players = 11
total_overs=(int(input("Enter the numbers of overs in the match")))
t1= Match(total_overs)
t2= Match(total_overs)

while(t1.current_balls < t1.total_balls() and t1.wicket_fallen < players-1):
    t1.print_score()


