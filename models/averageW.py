class averageW:
    def __init__(self,averageWList) -> None:
        self.year = averageWList[0]
        self.FG = averageWList[1]
        self.Three = averageWList[2]
        self.FT = averageWList[3]
        self.ORB = averageWList[4]
        self.DRB = averageWList[5]
        self.APG = averageWList[6]
        self.SPG = averageWList[7]
        self.BPG = averageWList[8]

    def retAverageWList(self):
        return [self.year,self.FG,self.Three,self.FT,self.ORB,self.DRB,self.APG,self.SPG,self.BPG]