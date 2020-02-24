class LabelCounter:
    def __init__(self):
        self.dicOfLabels = dict()

    def creatPrimary(self, primary: str):
        self.dicOfLabels[primary] = dict()

    def creatSecond(self, primary, second):
        self.dicOfLabels[primary][second] = {"p":0, "t":0}


    def addLabel(self, Label):
        primary = Label["primary"]
        second = Label["second"]
        thetype = Label["type"]#tyep is origanil variable thus use thetpye to avoid confuse
        if primary in self.dicOfLabels:
            if second in self.dicOfLabels[primary]:
                self.dicOfLabels[primary][second][thetype] += 1
            else:
                self.creatSecond(primary, second)
                self.dicOfLabels[primary][second][thetype] += 1
        else:
            self.creatPrimary(primary)
            self.creatSecond(primary, second)
            self.dicOfLabels[primary][second][thetype] += 1

    def countLabel(self, label):
        "通过这个方法返回 某个特定标签的数量。 当second有值的时候 primary不能为空"
        primary = label["primary"]
        second = label["second"]
        thetype = label["type"]
        #all of p,s,t has value
        if (primary is not None) & (second is not None) & (thetype is not None):
            self.count = self.dicOfLabels[primary][second][thetype]
            return self.count


        #both p and s has value, t == None
        elif (primary is not None) & (second is not None):
            self.count = 0
            for value in self.dicOfLabels[primary][second].values():
                self.count = self.count + value
            return self.count

        #both p and t has value, s == None
        elif (primary is not None) & (thetype is not None):
            self.count = 0
            for thelabel in self.dicOfLabels[primary].values():
                self.count = self.count + thelabel[thetype]
            return self.count

        #only p has value, s == None and t == None
        elif (primary is not None):
            self.count = 0
            primaryDict = self.dicOfLabels[primary]
            for thesecondlabel in primaryDict:
                for value in primaryDict[thesecondlabel].values():
                    self.count = self.count + value
            return  self.count

        #only t has value, p == None and s == None
        elif (thetype is not None):
            self.count = 0
            for thelabel in self.dicOfLabels.values():
                for secLabel in thelabel.values():
                    self.count = self.count + secLabel[thetype]
            return self.count
        else:
            print("counter function has an input error")