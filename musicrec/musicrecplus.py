'''
Authors: Daniel, Aya, James
Pledge: We pledge our honor that we have abided by the Stevens Honor System.
'''

PREF_FILE = 'musicrecplus.txt'

def loadUsers(fileName):
    '''
    Reads in a file of stored users' preferences
    stored in the file 'fileName'.
    Returns a dictionary containing a mapping
    of user names to a list preferred artists
    Modified by Daniel & James
    '''
    try:
        file = open(fileName, 'x')
        file.close()
        file = open(fileName, 'r')
    except:
        file = open(fileName, 'r')
    userDict = {}
    for line in file:
        # Read and parse a single line
        [userName, bands] = line.strip().split(":")
        if bands:
            bandList = bands.split(",")
            bandList.sort()
            for i in range(len(bandList)):
                bandList[i] = bandList[i].strip().title()
        else:
            bandList = []
        #bandList = standardizeAll(bandList)
        userDict[userName] = bandList
    file.close()
    return userDict

def getPreferences(userName, userMap):
    '''
    Returns a list of the uesr's preferred artists.
    If the system already knows about the user,
    it gets the preferences out of the userMap
    dictionary. If the user is new,
    it simply asks the user for their preferences.  
    Modified by Daniel and Aya
    '''
    newPref = ""
    if userName in userMap:
        prefs = userMap[userName]
        print("I see that you have used the system before.")
        print("Your music preferences include:")
        for artist in prefs:
            print(artist)
        print("Please enter another artist or band that you")
        print("like, or just press enter")
        newPref = input("to return to the menu: \n")
        
    else:
        prefs = []
        print("I see that you are a new user.")
        print("Please enter the name of an artist or band")
        newPref = input("that you like: \n")
    while newPref != "":
        prefs.append(newPref.strip().title())
        print("Please enter another artist or band that you")
        print("like, or just press enter")
        newPref = input("to return to the menu: \n")
    # Always keep the lists in sorted order for ease of
    # comparison
    prefs.sort()
    return prefs

def getPreferencesInitial(userName, userMap):
    '''
    Returns a list of the uesr's preferred artists.
    If the system already knows about the user,
    it gets the preferences out of the userMap
    dictionary and then asks the user if she has
    additional preferences. If the user is new,
    it simply asks the user for her preferences.  
    Modified by Daniel
    '''
    newPref = ""
    if userName in userMap:
        prefs = userMap[userName]
        print("I see that you have used the system before.")
        print("Your music preferences include:")
        for artist in prefs:
            print(artist)
    else:
        prefs = []
        print("I see that you are a new user.")
        print("Please enter the name of an artist or band")
        newPref = input("that you like: \n" )
    while newPref != "":
        prefs.append(newPref.strip().title())
        print("Please enter another artist or band that you")
        print("like, or just press enter")
        newPref = input("to return to the menu: \n")
    # Always keep the lists in sorted order for ease of
    # comparison
    prefs.sort()
    return prefs

def getRecommendations(currUser, prefs, userMap):
    '''
    Gets recommendations for a user (currUser) based
    on the users in userMap (a dictionary)
    and the user's preferences in pref (a list).
    Prints a list of recommended artists.
    Returns nothing
    Modified by Aya
    '''
    bestUser = findBestUser(currUser, prefs, userMap)
    if bestUser == None:
        print("I'm sorry but I have no recommendations for you right now.")
    else:
        recommendations = drop(prefs, userMap[bestUser])
        if len(recommendations) == 0:
            print("I'm sorry but I have no recommendations for you right now.")
        else:
            print(currUser, "based on the users I currently know about, I believe you might like:")
            for artist in recommendations:
                print(artist)
            print("I hope you enjoy them! I will save your preferred artists and have new recommendations for you in the future")
        
def findBestUser(currUser, prefs, userMap):
    '''
    Find the user whose tastes are closest to the current
    user(excluding those in private mode). Return the best user's name (a string)
    Modified by Aya
    '''
    users = userMap.keys()
    bestUser = None
    bestScore = -1
    for user in users:
        if user[-1] != '$':
            score = numMatches(prefs, userMap[user])
            if score > bestScore and currUser != user:
                bestScore = score
                bestUser = user
    return bestUser

def drop(list1, list2):
    '''
    Return a new list that contains only the elements in
    list2 that were NOT in list1.
    Written by textbook
    '''
    list3 = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            list3.append(list2[j])
            j += 1
    return list3

def numMatches( list1, list2 ):
    '''
    return the number of elements that match between
    two sorted lists
    Written by textbook
    '''
    matches = 0
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            matches += 1
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    return matches
  
def mostPopular(fileName):
    '''
    prints the top 3 artists
    Returns nothing
    Written by Aya
    '''
    count = {}
    artists = loadUsers(fileName)
    for key in list(artists.keys()):
        if key[-1] != '$':
            for i in range(len(artists[key])):
                if artists[key][i] in count:
                    count[artists[key][i]] += 1
                else:
                    count[artists[key][i]] = 1
    if count == {}:
        print('Sorry, no artists found')
    else:
        sortedCount = list(sorted(count.items(), key = lambda count: count[1]))
        if len(sortedCount) == 1:
            print(sortedCount[0][0])
        elif len(sortedCount) == 2:
            print(sortedCount[-1][0] + '\n' + sortedCount[-2][0])
        else:
            print(sortedCount[-1][0] + '\n' + sortedCount[-2][0] + '\n' + sortedCount[-3][0])
        
                  

def howPopular(fileName):
    '''
    prints the number of likes the most popular artist has
    Returns nothing
    written by Aya
    '''
    count = {}
    artists = loadUsers(fileName)
    for key in list(artists.keys()):
        if key[-1] != '$':
            for i in range(len(artists[key])):
                if artists[key][i] in count:
                    count[artists[key][i]] += 1
                else:
                    count[artists[key][i]] = 1
    if count == {}:
        return 'Sorry, no artists found'
    else:
        sortedCount = list(sorted(count.items(), key = lambda count: count[1]))
        return sortedCount[-1][1]

def saveUserPreferences(userName, prefs, userMap, fileName):
    '''
    Writes all of the user preferences to the file.
    Returns nothing. 
    Modified by Daniel and Aya and James
    '''
    if userName in userMap:
        prefs = userMap[userName]
    else:
        userMap[userName] = prefs
    file = open(fileName, "w")
    for user in userMap:
        toSave = str(user) + ":" + ",".join(userMap[user]) + "\n" # 199 differnce
        file.write(toSave)
    file.close()

def currentPreferences(userName, prefs, userMap):
    '''
    Writes all of the user preferences to the file.
    Prints updated list of preferences. 
    Written by Daniel
    '''
    
    if userName.strip() in userMap:
        prefs = userMap[userName]
        for artist in prefs:
            print(artist)

def deletion(userName, prefs, userMap):
    '''
    removes an artist from the user's current preferences
    Returns nothing.
    Written by Aya
    '''
    currentPreferences(userName, prefs, userMap)
    remove = input("Enter an artist from the above list you would like to remove from your current preferences.\n")
    count = 0
    for i in userMap[userName]:
        if remove == i:
            userMap[userName].remove(i)
            saveUserPreferences(userName, prefs, userMap, PREF_FILE)
            count +=1
    if count == 0:
        print("Artist was not found in your preferences.")
    else:
        print("Artist has been successfully removed from your preferences.")

def TheMostLikes(userMap):
    '''
    finds the user who has liked the most artists, returns the user
    Written by James
    '''
    maxCount = 0
    users = userMap.keys()
    king = 'Sorry, no users found.'
    for user in users:
        # check artist count of user against previous max
        # if greater, usurp old king, change maxCount
        if len(userMap[user]) > maxCount:
            # update new maxCount
            maxCount = len(userMap[user])
            #usurp
            king = user
            if '$' in king:
                maxCount = 0
    return king


def main():
    #Enter a letter to choose an option :
    #e - Enter preferences
    #r - Get recommendations
    #p - Show most popular artists
    #h - How popular is the most popular
    #m - Which user has the most likes
    #q - Save and quit
    '''
    The main recommendation function 
    Modified by Daniel
    '''
    userMap = loadUsers(PREF_FILE)
    print("Welcome to the music recommender system!")
    userName = input("Please enter your name (put a '$' after your name if you wish for your preferenes to remain annonymous: ")
    print ("Welcome,", userName)
    action = True
    #recs = []
    prefs = getPreferencesInitial(userName, userMap)
    saveUserPreferences(userName, prefs, userMap, PREF_FILE)
    result = []
    for i in userMap[userName]: 
        if i not in result: 
            result.append(i)
    userMap[userName] = result
    while action:
        action = input('Enter a letter to choose an option :\ne - Enter preferences\nr - Get recommendations\np - Show most popular artists\nh - How popular is the most popular\nm - Which user has the most likes\nd - Delete Preference\ns - See current preferences\nq - Save and quit\n')
        if action == 'e':
            prefs = getPreferences(userName, userMap)
            
            saveUserPreferences(userName, prefs, userMap, PREF_FILE)
        if action == 'r':
            if prefs == []:
                prefs = userMap[userName]
            getRecommendations(userName, prefs, userMap)
        if action == 'p':
            mostPopular(PREF_FILE)
        if action == 'h':
            saveUserPreferences(userName, prefs, userMap, PREF_FILE)
            print(howPopular(PREF_FILE))
        if action == 'm':
            print(TheMostLikes(userMap))
        if action == 's':
            currentPreferences(userName, prefs, userMap)
        if action == 'q':
            saveUserPreferences(userName, prefs, userMap, PREF_FILE)
            action = ''
        if action == 'd':
            deletion(userName, prefs, userMap)
            

if __name__ == "__main__": main()
