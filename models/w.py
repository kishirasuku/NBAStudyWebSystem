class w:
    
    def __init__(self,statsList) -> None:
        self.FG = statsList[0]
        self.Three = statsList[1]
        self.FT = statsList[2]
        self.ORB = statsList[3]
        self.DRB = statsList[4]
        self.APG = statsList[5]
        self.SPG = statsList[6]
        self.BPG = statsList[7]

    def retStatsList(self):
        return [self.FG,self.Three,self.FT,self.ORB,self.DRB,self.APG,self.SPG,self.BPG]

