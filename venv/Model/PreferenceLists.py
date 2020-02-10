import Labels as L


class PreferenceList:
    def __init__(self):
        self.listOfPre = dict.fromkeys(("one", "two", "three", "four", "five"))


    def showname(self):
        print(self.listOfPre)

    def setPreferenceList(self, position, primary, second, type):
        label = L.Label()
        label.setLabel("primary", "second", "type")

        self.listOfPre[position] = label

    def testFun(self):

        self.setPreferenceList("one","primary","second","type")
        self.showname()


