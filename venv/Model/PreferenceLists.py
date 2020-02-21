import Labels as L


class PreferenceList:
    def __init__(self):
        self.listOfPre = dict.fromkeys(("one", "two", "three", "four", "five"))


    def showname(self):
        print(self.listOfPre['one'].getAllLabel())

    def setPreferenceList(self, position, primary=None, second=None, type=None):
        label = L.Label()
        label.setLabel(primary, second, type)

        self.listOfPre[position] = label

    def getPreference(self,position):
        return self.listOfPre[position]
    def testFun(self):

        self.setPreferenceList("one","primary","second","type")
        self.showname()


