class fizz_buzz:
    def __init__(self):
        self.empty_ruleset()
        self.default_rules()
    
    def play_SO(self):
        # plays the game by printing to standard output
        for i in range(1, self.max_num+1):
            self.out = ""
            for j in self.conversions.keys():
                if i%j==0:
                    self.out+=self.conversions[j]
            if self.out=="":
                self.out=str(i)
            print(self.out)
    
    def play_GUI(self):
        self.payload = ""
        for i in range(1, self.max_num+1):
            self.out = ""
            for j in self.conversions.keys():
                if i%j==0:
                    self.out+=self.conversions[j]
            if self.out=="":
                self.out=str(i)
            self.payload+=self.out+"\t"
        return(self.payload)
    
    def empty_ruleset(self):
        #erases all rules and sets max_num to 0
        self.conversions = {}
        self.max_num = 0
        
    def default_rules(self):
        #sets the rules to defaults
        self.conversions = {3:'Fizz ',
                       5:'Buzz '}
        self.max_num = 100
        
    def custom_rules(self, conversions, max_num):
        #allows a complete set of rules to be fed into the class
        ## IN:
        # int - max_num
        # dict{int,string} - conversions{}
        ##
        self.conversions = conversions
        self.max_num = max_num
        
    def set_maxnum(self, max_num):
        #changes the value of self.maxnum changing the behaviour of the game
        ## IN: 
        # int - max_num
        ##
        self.max_num=int(max_num)
    
    def add_rule(self, num, phrase):
        #appends a rule to the dict
        ## IN:
        # int - num
        # string - phrase
        ##
        self.conversions[num]=phrase+" "
    
    def remove_rule(self, num):
        # removes a rule from the dict
        ## IN:
        # int - num
        ##
        self.conversions.pop(int(num))
    
    def get_rules(self):
        # returns the list of rules and the max_num value
        ## OUT:
        # tuple(int - max_num, dict - conversions{int,string})
        ##
        return (self.conversions)
    
        
if __name__=="__main__":
    fb = fizz_buzz()
    fb.play_SO()
    c = {2:"Fizz ",
         5:"Buzz ",
         10:"Dec "}
    m= 300
    fb.custom_rules(c, m)
    fb.play_SO()
