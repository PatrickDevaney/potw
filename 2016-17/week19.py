import http.client
import json

# Get the data from the API
def getLanguageData():
    connection = http.client.HTTPConnection("potw.quinnftw.com")
    connection.request("GET", "/api/solution_languages")
    return json.loads(connection.getresponse().read().decode("utf-8"))['data']

class Week:
    def __init__(self):
        self.count = 0
        self.languageCounts = {}
        self.languageRatios = {}
    def addSubmission(self, language):
        self.count += 1
        if language in self.languageCounts:
            self.languageCounts[language] += 1
        else:
            self.languageCounts[language] = 1
    def getCount(self):
        return self.count
    def getLanguageCounts(self):
        return self.languageCounts
    def getLanguageRatios(self):
        for language in self.languageCounts:
            self.languageRatios[language] = self.languageCounts[language] / self.count
        return self.languageRatios

# All submissions up to this point
class Year:
    def __init__(self):
        self.count = 0
        self.languageCounts = {}
        self.languageRatios = {}
        self.weeks = {}
    def addWeek(self, weekNumber):
        self.weeks[weekNumber] = Week()
    def addSubmission(self, week, language):
        if week not in self.weeks:
            self.addWeek(week)
        self.weeks[week].addSubmission(language)
        self.count += 1
        if language in self.languageCounts:
            self.languageCounts[language] += 1
        else:
            self.languageCounts[language] = 1
    def getLanguageCounts(self):
        return self.languageCounts
    def getLanguageRatios(self):
        for language in self.languageCounts:
            self.languageRatios[language] = self.languageCounts[language] / self.count
        return self.languageRatios
    def getTrending(self, week):
        weekRatios = self.weeks[week].getLanguageRatios()
        globalRatios = self.getLanguageRatios()
        maxRatio = 0
        for language in weekRatios:
            if (weekRatios[language] / globalRatios[language]) > maxRatio:
                maxRatio = (weekRatios[language] / globalRatios[language])
                trending = [language]
            elif (weekRatios[language] / globalRatios[language]) == maxRatio:
                trending.append(language)
        trending.sort()
        outputString = str(trending[0])
        for lang in trending[1:]:
            outputString = outputString + "/" + lang
        return outputString
    def getCount(self):
        return self.count

submissions = getLanguageData()
year = Year()
for submission in submissions:
    year.addSubmission(submission['week'], submission['language'])

for i in range(18):
    print("Week " + str(i+1) + ": " + str(year.getTrending(i+1)))
