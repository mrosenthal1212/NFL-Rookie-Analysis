import pandas as pd

#Imports dataframe
df = pd.read_excel('2019 Rookie Data.xlsx')

#Gets rid of \xxx in the player column
def fixPlayerColumn():
    playerColumn = []
    for i in range(len(df['Player'])):
        playerNameWithSlash = df['Player'][i]
        updatedName = playerNameWithSlash.split("\\")
        playerColumn.append(updatedName[0])
    df['Player'] = playerColumn

#Splits the Drafted (tm/rdn/yr) column into 3 seperate columns
def splitDraftedColumn():
    teamDrafted = []
    draftRoundColumn = []
    overallPickColumn = []
    for i in range(len(df['Drafted (tm/rnd/yr)'])):
        try:
             textToSplit = df['Drafted (tm/rnd/yr)'][i]
             splitText = textToSplit.split(" / ")
             teamDrafted.append(splitText[0])
             draftRoundColumn.append(splitText[1])
             overallPickColumn.append(splitText[2])
        except AttributeError:
            teamDrafted.append('null')
            draftRoundColumn.append('null')
            overallPickColumn.append('null')

    df['Draft Rd.'] = draftRoundColumn
    df['Ovr. Pick'] = overallPickColumn
    df['Drafted by'] = teamDrafted



#Want to remove suffix of 1st, 2nd, etc. e.g. 1st => 1 ...Future make this one for loop
def removeDraftSuffix():
    newDraftRd = []
    for i in range(len(df['Draft Rd.'])):
        try:
            newDraftRd.append(int(df['Draft Rd.'][i][0]))
        except (TypeError, ValueError):
            newDraftRd.append(8) #8 Shows undrafted in NFL
    df['Draft Rd.'] = newDraftRd

def addNullValues():
    new40time = []
    for i in range(len(df['40yd'])):
        if df['40yd'][i] > 0:
            new40time.append(df['40yd'][i])
        else:
            new40time.append('null')

    newVertical = []
    for i in range(len(df['Vertical'])):
        if df['Vertical'][i] > 0:
            newVertical.append(df['Vertical'][i])
        else:
            newVertical.append('null')

    newBench = []
    for i in range(len(df['Bench'])):
        if df['Bench'][i] > 0:
            newBench.append(df['Bench'][i])
        else:
            newBench.append('null')

    newBroad = []
    for i in range(len(df['Broad Jump'])):
        if df['Broad Jump'][i] > 0:
            newBroad.append(df['Broad Jump'][i])
        else:
            newBroad.append('null')

    new3Cone = []
    for i in range(len(df['3Cone'])):
        if df['3Cone'][i] > 0:
            new3Cone.append(df['3Cone'][i])
        else:
            new3Cone.append('null')

    newShuttle = []
    for i in range(len(df['Shuttle'])):
        if df['Shuttle'][i] > 0:
            newShuttle.append(df['Shuttle'][i])
        else:
            newShuttle.append('null')

    newPFF = []
    for i in range(len(df['PFF Grades'])):
        if df['PFF Grades'][i] > 0:
            newPFF.append(df['PFF Grades'][i])
        else:
            newPFF.append('null')

    df['40yd'] = new40time
    df['Vertical'] = newVertical
    df['Bench'] = newBench
    df['Broad Jump'] = newBroad
    df['3Cone'] = new3Cone
    df['Shuttle'] = newShuttle
    df['PFF Grades'] = newPFF

fixPlayerColumn()
splitDraftedColumn()
removeDraftSuffix()
addNullValues()
df.drop('Drafted (tm/rnd/yr)', axis=1, inplace=True)
df.to_excel('testOfPyProgram.xlsx')
