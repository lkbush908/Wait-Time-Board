import requests
import time
from datetime import datetime
import json

currWait = 0
Color = "Grey"


#Attraction class for future use
class Attraction:
    def __init__(self, AttractionName, currentWait, bulbColor):
        self.Name = AttractionName
        self.WaitTime = currentWait
        self.Color = bulbColor
        

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


try: 
    while True:

        #time print when data is pulled
        print("Pulling Data:")
        current_time = datetime.now().strftime("%H:%M:%S")
        print(current_time)

        #Response pull from themeparks.wiki wait time api
        response = requests.get('https://api.themeparks.wiki/v1/entity/7340550b-c14d-4def-80bb-acdb51d49a66/live')

        #Uncomment below  and comment response to run using template .json file

        #with open('studiosData.json') as json_file:
        #   data = json.load(json_file)

        #Converts JSON version of response data into dictionary
        data = response.json()

        with open("IOA.json", "w") as file:
            json.dump(data, file)

        #Array for live data section of dictionary
        liveArray = data["liveData"]

        print("Success")



        for i in range(len(liveArray)):
           
           #loop throigh enitity type object to get wait time and attraction info
           if(liveArray[i]["entityType"] == 'ATTRACTION'):

                attrType = liveArray[i]["entityType"]

                #pull queue data from curent attraction
                if "queue" in liveArray[i]:
                    queueData = liveArray[i]["queue"]
                    if queueData["STANDBY"]["waitTime"] is not None:
                        currWait = queueData["STANDBY"]["waitTime"]
                    else:
                        currWait = "None"
                    Color = colorAssign(queueData["STANDBY"]["waitTime"])
                else:
                    currWait = "None"
                    Color = "Grey"

                #Assign variables for name and color
                Name = liveArray[i]["name"]
                

                #Print Formatting
                print(f"Name: {Name:<65} Type {attrType:<15} Wait Time: {currWait:<10} Color: {Color}")

        #5 Minute Pull Timer
        time.sleep(300)

    
except KeyboardInterrupt:
    print("End pull")
    pass



# TO ADD
# Create list/filter for wait time only attractions/shows
# User Input for Park(?)
# 
# 
# Color scale based on wait time
# 
# 
# 
# 
#
#
#
#
