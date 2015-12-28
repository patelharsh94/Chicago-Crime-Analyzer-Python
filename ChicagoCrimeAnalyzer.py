__author__ = 'Harsh'
import csv
import operator
from collections import Counter

# +-------------------------------------------------------------------------------+
# | Name: Chicago Crime Analyzer : In Python                                      |
# | author: Harsh Patel                                                           |
# | Desc: This program reads in data about the crimes in Chicago                  |
# |       and provides the user with interesting information about Chicago's crime|
# +-------------------------------------------------------------------------------+

# This class will be used when reading the crimes file and will hold some basic
# information about a crime.
class crimeReport :

    # default constructor.
    def __init__(self):
        return

    # A basic initializer constructor that sets the class member IUCR to IUCR,
    # the class member comNumber to comNumber, and the class member year to year.
    def __init__(self,IUCR,comNumber,year):
        self.IUCR       = IUCR
        self.comNumber  = comNumber
        self.year       = year

    # A basic destructor
    def __del__(self):
        return


# This class is made so that the printing of the first part (info about top 10 crimes) is a little easier
# And to store information about a IUCR code.
class codeDesc :

    # default constructor
    def __init__(self):
        return

    # A initializer constructor that sets the class member IUCR to IUCR, pDesc to pDesc, sDesc to sDesc and num to num
    # This constructor will be used when printing the first part.
    def __init__(self, IUCR, pDesc, sDesc):
        self.IUCR   = IUCR
        self.pDesc  = pDesc
        self.sDesc  = sDesc

    # A default destructor
    def __del__(self):
        return

# A function the reads in the Crimes.csv file and returns
def readInCrimes():
    fileName = "Crimes.csv"                       # fileName
    CrimesFile  = open(fileName,"r")              # Open the csv file
    crimeList   = [0]                             # A list of crimes, the zero'th value is the total number of crimes.
    csvReader   = csv.reader(CrimesFile)          # Read the crimes file as a csv
    totalCrimes = 0                               # A counter for the total number of crimes in Chicago.

    print(">> Reading crime data '{0}' ...".format(fileName))
    CrimesFile.readline()                         # skip the headers
    for row in csvReader:                         # for each row save the IUCR, community number and the year.
        IUCR = str(row[1])
        comNumber = row[7]
        year = row[8]
        totalCrimes+=1
        crimeList.append(crimeReport(IUCR,comNumber,year))  # append to the list of crimes.
    crimeList[0] = totalCrimes              # Saving the total number of crimes.
    print("   Total Crimes :  [{0}]".format(totalCrimes))
    return crimeList

# This function reads in the IUCR file and returns a list of the IUCR's
def readInIUC():
    fileName = "IUCR-codes.csv"                    # The file name
    IUCRFile = open(fileName,"r")                  # opening the file
    IUCRList = []                                  # A list of IUCR's
    totalIUCR = 0                                  # Total number of IUCR's

    print(">> Reading IUCR data '{0}' ... ".format(fileName))

    csvReader = csv.reader(IUCRFile)               # Read the file as a csv
    IUCRFile.readline()                            # skipping the headers
    for row in csvReader:                          # for each row, save the IUCR, primary description , secondary
        IUCR = str(row[0])                         # description and append it to the list.
        pDes = row[1]
        sDes = row[2]
        totalIUCR += 1
        IUCRList.append(codeDesc(IUCR,pDes,sDes))

    print("   Total IUCR : [{0}]".format(totalIUCR))
    return IUCRList

# This function reads in the communities file
def readInCommunities():
    fileName = "Communities.csv"                 # The file name
    COMMUNITIESFile = open(fileName,"r")         # opening the community file
    communitiesList = []                         # The list of communities
    totalCommunities = 0

    print(">> Reading communities '{0}' ...".format(fileName))

    csvReader = csv.reader(COMMUNITIESFile)      # read the file
    COMMUNITIESFile.readline()

    for row in csvReader:                        # save the communities
        communitiesList.append(row [1])
        totalCommunities+=1

    print("   [{0}]".format(totalCommunities))
    return communitiesList

# This function prints the top N crimes
def printTopN(crimeList, IUCRList,n):
    IUCRCount = Counter(IUCR.IUCR for IUCR in crimeList)                    # Counts the total counts of each IUCR in
                                                                            # the crime list.
    sortedIUCRCount = sorted(IUCRCount.items(),key=operator.itemgetter(1))  # sorts and reverse the IUCR bease on the
    sortedIUCRCount.reverse()                                               # count
    i = 0

    print(">> Top {0} Crimes <<".format(n))
    print("Rank\tIUCR\t\tNumber\t\tDescription")                            # printing the header
    while i < n :                                                           # printing the top N
        IUCR =     sortedIUCRCount[i][0]                                    # getting IUCR and count
        count =    sortedIUCRCount[i][1]
        pDes = ""
        sDes = ""
        for a in IUCRList:                                                  # getting the description
            if a.IUCR == IUCR:
                pDes = a.pDesc
                sDes = a.sDesc

        print("{0}.\t\t{1}\t\t{2}\t\t{3} ({4})"                             # printing information
              .format(i+1,IUCR,count,pDes,sDes)
             )

        i+=1
    return

# This function analyzes crimes by community
def printByCommunity(crimeList,IUCRList,comNames):

    homicide    = 0                     # Number of homicide
    comCrime    = 0                     # Number of crimes in the community

    comNumber = input("Please enter a community number [1 .. 77] and 0 to stop: ")  # getting input
    comNumber = int(comNumber)
    totalCrimes = crimeList.__len__()                                               # Getting total crime
    crimes = []
    while comNumber :                   # while some input has been recieved.
        if comNumber == 0:              # if 0 return, if greater then 77 ask again else analyze
            return
        elif comNumber > 0 and comNumber < 78:
            comName = comNames[comNumber-1]                                         # getting community name
            comList = filter(lambda x: x.comNumber == str(comNumber), crimeList)    # getting crimes for only this community

            for e in comList:                                                       # counting crimes and homicides
                comCrime+=1
                if e.IUCR == "0110" or e.IUCR == "0130" or e.IUCR == "0141" or e.IUCR == "0142" :
                    homicide += 1
                crimes.append(e)                                                    # saving the crime in a list.

            percentage = comCrime/totalCrimes * 100                                 # calculating the percentage
            print(">> {0} <<".format(comName))
            print(">> Total: ",totalCrimes)
            print(">> Percentage: {0:.4f}%".format(percentage))
            print(">> Homicide: ",homicide)
            printTopN(crimes,IUCRList,5)                                            # printing the top 5
        print("\n")
        comNumber = int(input("Please enter a community number [1 .. 77] and 0 to stop: "))
    return

# This function prints the crimes by year
def printCrimeByYear(crimeList,IUCRList):

    IUCR = input("Please enter a IUCR crime code [e.g. 0110 or 031A], 0000 to stop: ")   # Ask for user input
    desc = ""                                                         # The description of the crime
    totalCrime = crimeList.__len__()                                  # Total crime in Chicago
    totalIUCRCrime = 0                                                # The number of time the current IUCR has been committed
    yearCount = []                                                    # The amount of crimes by year
    years  = []                                                       # The years themself
    currCount = 0                                                     # The crime for current year
    isIUCR = False                                                    # To check if the IUCR was found
    while IUCR != "0000":                                             # While "0000" is not typed in..
        for e in IUCRList:                                            # Find the IUCR in the list of IUCR's
            if e.IUCR == IUCR:
                isIUCR = True
                desc = e.pDesc + " (" + e.sDesc +")"                  # if found, get the description
                break
            else:
                isIUCR = False
        if isIUCR:                                                    # if found, group by IUCR and by year
            print(">>",desc)
            IUCRGroup = filter(lambda x: x.IUCR == IUCR,crimeList)
            yearGroup = filter(lambda x: x.year,IUCRGroup)
            i = 0
            for e in yearGroup:                                       # for each year in the group, count the number of
                if i == 0:                                            # crimes in that year, and save the values.
                    prevYear = e.year
                    i = 1
                if(e.year == prevYear):
                    currCount+=1
                else:                                                 # save the year and the count and reset the count.
                    years.append(prevYear)
                    yearCount.append(currCount)
                    currCount = 0
                prevYear = e.year
                totalIUCRCrime+=1
            isIUCR = False
            years.append(prevYear)                                    # saving values for the last year
            yearCount.append(currCount+1)
            print(">> Total:\t",totalIUCRCrime)                       # printing the totals and percentages
            print(">> Percentage: {0:.4f}%".format(totalIUCRCrime/totalCrime * 100))
            print(">> By Year: ")
            i = 0
            for e in years:                                           # printing the crime count by year.
                print("   {0}: {1}".format(e,yearCount[i]))
                i+=1
            years.clear()
            yearCount.clear()
            i = 0
        print("\n")
        IUCR = input("Please enter a IUCR crime code [e.g. 0110 or 031A], 0000 to stop: ")
    print(">> Later Gator! ")
    return

crimeList = readInCrimes()
IUCRList  = readInIUC()
comNames  = readInCommunities()
crimeList.pop(0)
print("\n")
printTopN(crimeList,IUCRList,10)                                      # printing the top 10 values
print("\n")
printByCommunity(crimeList,IUCRList,comNames)                         # printing the crimes by communities
print("\n")
printCrimeByYear(crimeList,IUCRList)                                  # printing the crimes by year
