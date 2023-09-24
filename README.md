# UWaterlooCourseHelperEngine

MongoDB DashBoard: [LINK](https://charts.mongodb.com/charts-project-0-cbzai/public/dashboards/091bc68f-76df-48c0-aa69-b21af14c0a8a)

### Example Schedule: 

![Image text](https://raw.githubusercontent.com/zangjiucheng/UWaterlooCourseHelperEngine/Release/schedule.jpg)

## This Version Still on Test! 

#### Install Steps: 
1. Install Python3 (Developed on py3.11) [Python Website](https://www.python.org/downloads/)
2. Clone this Repository
3. Go into ```OnlineVersion``` Folder
4. Install Requirement With Command ```pip install -r requirement.txt ```
5. Edit main.py Code With following Command:

Choose Term To Attend Class: (It Deisides which Term it Will Looking For!)
#### Current Avalible:  Class2023Fall Class2024Winter (Rest Will be Update Later...)

Example:
```
dbClassUW.switchCollection(collectionName="Class2023Fall")  # Class2023Fall Class2024Winter 
```

#### Add Course on to Print List

```
addCourse(SearchAvalibleInTerm(dbClassUW, COURSE_INDEX))
addCourse(SearchAvalibleInTerm(dbClassUW, COURSE_INDEX,CLASS_ID)) 
```
(If without CLASS_ID, it will print all the avalible class)

#### Example: 
```
addCourse(SearchAvalibleInTerm(dbClassUW, "CS 145"))
addCourse(SearchAvalibleInTerm(dbClassUW, "CS 350",6583))
```

6. Save main.py
7. Run ```pdfschedule schedule``` in CLI. 
8. ```schedule.pdf``` will be create in the folder

#### Enjoy~ 

#### Any Idea or Question, welcome send me an email at: j7zang@uwaterloo.ca

Or you can open an issue, or just find me in school :) 

