import requests
import time
from datetime import datetime
import json
from resortLists import ResortOptions
import os

currWait = 0
Color = "Grey"
requestString = None
usrURL = None


#Attraction class for future use
class Attraction:
    def __init__(self, AttractionName, currentWait, bulbColor):
        self.Name = AttractionName
        self.WaitTime = currentWait
        self.Color = bulbColor


def resortSearch(usrResort):
    for resort in range(len(ResortOptions)):
        if usrResort == ResortOptions[resort].numID:
            return ResortOptions[resort].parks
        
    print("Invalid Resort ID.")
    return
    
#Function assigning "node" colors based on wait time
def colorAssign(waitTime):

    if waitTime is not None:
        if(waitTime >= 0 and waitTime < 30):
            return "Green"
        if waitTime < 60:
            return "Yellow"
        if(waitTime >= 60):
            return "Red"
    else:
            #None value catch
            return "Grey"
    
def pullDataFromRequest(liveURL):

    response = requests.get(liveURL)

    data = response.json()

    #Array for live data section of dictionary
    return data["liveData"]

try: 
    while True:
        print("Resort Options:")
        for resort in range(len(ResortOptions)):
            print("Name: ", ResortOptions[resort], "\tResort ID: ", ResortOptions[resort].numID)

        while True:
                currResort = resortSearch(int(input("Enter a Resort ID number: ")))
        
                if  currResort != None:
                    break    

        print("Park Options:")


        for park in range(len(currResort)):
            print(f"Name: {currResort[park].name:<25} \t Park ID: {currResort[park].numID:<4} \t")

        #WHile loop of some kind. Ending early because for loop
        while True:
            usrPark = int(input("Enter a Park ID Number: "))
            findParkID = next((obj for obj in currResort if obj.numID == usrPark), None)
                
            if findParkID is not None:
                usrURL = findParkID.liveURL
                break
            else:
                print("Not a valid Park ID.")

        try: 
            while True:

                #time print when data is pulled
                print("Pulling Data:")
                current_time = datetime.now().strftime("%H:%M:%S")
                print(current_time)

                print(usrURL)
                #Response pull from themeparks.wiki wait time api
                if usrURL != None:
                    liveArray = pullDataFromRequest(usrURL)
                else:
                    break
                
                #Converts JSON version of response data into dictionary
                


                #Uncomment below  and comment response to run using template .json file

                #with open('pulledData.json') as json_file:
                #  data = json.load(json_file)

                #with open("DowntimeAttraction.json", "w") as file:
                #    json.dump(data, file)        

                print("Data Pull Successful")

                for i in range(len(liveArray)):
                
                #loop throigh enitity type object to get wait time and attraction info
                    if(liveArray[i]["entityType"] == 'ATTRACTION'):

                        attrType = liveArray[i]["entityType"]

                        #pull queue data from curent attraction
                        if "queue" in liveArray[i] and liveArray[i]["status"] == 'OPERATING':
                            queueData = liveArray[i]["queue"]
                            if "STANDBY" not in queueData:
                                currWait = "UNKNOWN"
                                Color = "Grey"
                                

                            elif queueData["STANDBY"]["waitTime"] is not None:
                                currWait = queueData["STANDBY"]["waitTime"]
                                Color = colorAssign(queueData["STANDBY"]["waitTime"])
                            else:
                                currWait = "None"
                                Color = colorAssign(queueData["STANDBY"]["waitTime"])
                        elif liveArray[i]["status"] != 'OPERATING':
                            currWait = liveArray[i]["status"]
                            Color = "Grey"
                        else:
                            currWait = "None"
                            Color = "Grey"

                        #Assign variables for name and color
                        Name = liveArray[i]["name"]
                        

                        #Print Formatting
                        print(f"Name: {Name:<65} Type {attrType:<15} Wait Time: {currWait:<10} Color: {Color}")

                print("\nPress ctrl + c to return to resort selection menu.")
                #5 Minute Pull Timer

                time.sleep(300)

            
        except KeyboardInterrupt:
            os.system('cls' if os.name == 'nt' else 'clear')
            pass

except KeyboardInterrupt:
    print("\nEnd pull")
    pass

    # TO ADD
    # Create list/filter for wait time only attractions/shows
    # User Input for Park(?)
    # 
    # 



    #SCRAPPED CODE FOR REFERENCE
    #response = requests.get(resortLists.CaliAdventure.liveURL)
            #data = response.json()
            #liveArray = data["liveData"]