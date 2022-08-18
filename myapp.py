import requests, json, pprint
from datetime import date
myheader = {"Authorization":"Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMzhSNkIiLCJzdWIiOiJCNEYzNVEiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJyc29jIHJzZXQgcm94eSBybnV0IHJwcm8gcnNsZSByYWN0IHJsb2MgcnJlcyByd2VpIHJociBydGVtIiwiZXhwIjoxNjkyMjk1NDQ0LCJpYXQiOjE2NjA3NTk0NDR9.bILcGIrPRXPWRrWBZDKRLsZdtTKKqPUpZ4NZZ-U3k5g"}

today = date.today()
today = str(today)

def get_name() :
    myurl = "https://api.fitbit.com/1/user/-/profile.json"
    resp = requests.get(myurl, headers=myheader).json()
    print(resp["user"]["fullName"])

def get_heartrate() :
    myurl = "https://api.fitbit.com/1/user/-/activities/heart/date/" + today + "/1d/1min/time/08:00/08:30.json"
    resp = requests.get(myurl, headers=myheader).json()
    data = resp["activities-heart-intraday"]["dataset"][0]
    hTime = data["time"]
    hour = int(hTime[0:2])
    m = "AM"
    if (hour > 12):
        m = "PM"
        hour = hour - 12
    hour = str(hour)
    print("Your most recently recorded heartrate was " + str(data["value"]) + " BPM at " + hour + " " + m +".")

def get_steps() :
    myurl = "https://api.fitbit.com/1/user/-/activities/date/" + today + ".json"
    resp = requests.get(myurl, headers=myheader).json()
    summ = resp["summary"]
    print("Your total step count today is {}.".format(summ["steps"]))

def get_sleep() :
    myurl = "https://api.fitbit.com/1.2/user/-/sleep/date/" + today + ".json"
    resp = requests.get(myurl, headers=myheader).json()
    minutes = (resp["summary"]["totalMinutesAsleep"])
    print("You slept for " + str(int(minutes/60)) + " hours and " + str(int(minutes%60)) + " minutes last night.")

def get_activeness() :
    myurl = "https://api.fitbit.com/1/user/-/activities/date/" + today + ".json"
    resp = requests.get(myurl, headers=myheader).json()
    summ = resp["summary"]
    sedMin = summ["sedentaryMinutes"]
    laMin = summ["lightlyActiveMinutes"]
    faMin = summ["fairlyActiveMinutes"]
    vaMin = summ["veryActiveMinutes"]
    print("Today you were sedentary for " + str(int(sedMin/60)) + " hours and " + str(sedMin%60) + " minutes.")
    print("You were lightly active for " + str(int(laMin/60)) + " hours and " + str(laMin%60) + " minutes.")
    print("You were fairly active for " + str(int(faMin/60)) + " hours and " + str(faMin%60) + " minutes.")
    print("Finally, you were very active for " + str(int(vaMin/60)) + " hours and " + str(vaMin%60) + " minutes.")

get_name()
get_heartrate()
get_steps()
get_sleep()
get_activeness()