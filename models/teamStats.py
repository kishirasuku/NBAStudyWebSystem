class teamStats:
    def __init__(self,teamStatsList) -> None:
        self.teamName = teamStatsList[0]
        self.FG = teamStatsList[1]
        self.Three = teamStatsList[2]
        self.FT = teamStatsList[3]
        self.ORB = teamStatsList[4]
        self.DRB = teamStatsList[5]
        self.APG = teamStatsList[6]
        self.SPG = teamStatsList[7]
        self.BPG = teamStatsList[8]

    def retTeamStatsList(self):
        return [self.teamName,self.FG,self.Three,self.FT,self.ORB,self.DRB,self.APG,self.SPG,self.BPG]