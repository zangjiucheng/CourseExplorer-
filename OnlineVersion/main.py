from DB.dbClass import dbClass
from ClassSchedule.runner import SearchCourse, makeSchedule, SearchAvalibleInTerm
from Utiles.colorMessage import *
from os import system
from setting import Setting

dbClassUW = dbClass()
setting = Setting()
courseWishList = []


def addCourse(course):
    if course != None:
        courseWishList.append(course)


def checkDetail(course):
    SearchCourse(dbClassUW, course)
    exit(0)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    # checkDetail("EMLS 101R")

    ###List of Course
    
    # dbClassUW.switchCollection(
    #       collectionName="Class2024Fall")  # Class2023Fall Class2024Winter Class2024Spring Class2024Fall

    # dbClassUW.switchCollection(
    #       collectionName="Class2023Fall")  # Class2023Fall Class2024Winter Class2024Spring Class2024Fall
    # addCourse(SearchAvalibleInTerm(dbClassUW, "STAT 230",6872))
    # # addCourse(SearchAvalibleInTerm(dbClassUW, "STAT 231",6879))
    # # addCourse(SearchAvalibleInTerm(dbClassUW, "CS 135"))
    # addCourse(SearchAvalibleInTerm(dbClassUW, "CS 145",6287))
    # addCourse(SearchAvalibleInTerm(dbClassUW, "CS 241",6398))
    # addCourse(SearchAvalibleInTerm(dbClassUW, "MATH 237",6203))
    # addCourse(SearchAvalibleInTerm(dbClassUW, "MATH 147",6507))
    # addCourse(SearchAvalibleInTerm(dbClassUW, "MATH 135",6078))
    # # addCourse(SearchAvalibleInTerm(dbClassUW, "COMMST 100"))
    # addCourse(SearchAvalibleInTerm(dbClassUW, "STAT 230"))
    # addCourse(SearchAvalibleInTerm(dbClassUW, "MTHEL 131"))
    # addCourse(SearchAvalibleInTerm(dbClassUW, "COMMST 100",7991))
    # addCourse(SearchAvalibleInTerm(dbClassUW, "CS 350",6583))
    # addCourse(SearchAvalibleInTerm(dbClassUW, "CO 255",6522))
    # addCourse(SearchAvalibleInTerm(dbClassUW, "PHYS 468"))

    # addCourse(SearchAvalibleInTerm(dbClassUW, "ECON 101"))
    # addCourse(SearchAvalibleInTerm(dbClassUW, "STAT 230"))
    # addCourse(SearchAvalibleInTerm(dbClassUW, "CS 146"))
    # addCourse(SearchAvalibleInTerm(dbClassUW, "CS 136L"))
    # addCourse(SearchAvalibleInTerm(dbClassUW, "ENGL 119"))
    # addCourse(SearchAvalibleInTerm(dbClassUW, "MATH 136"))

    
    # dbClassUW.switchCollection(
    #       collectionName="Class2024Spring")  # Class2023Fall Class2024Winter Class2024Spring Class2024Fall

    # # addCourse(SearchAvalibleInTerm(dbClassUW, "EMLS 101R"))
    # # addCourse(SearchAvalibleInTerm(dbClassUW, "CS 486", 3929)) # Introduction to Artificial Intelligence
    # # addCourse(SearchAvalibleInTerm(dbClassUW, "CS 350", 3926)) # Operating Systems

    # addCourse(SearchAvalibleInTerm(dbClassUW, "CS 246", 3982)) # Object-Oriented Software Development
    # addCourse(SearchAvalibleInTerm(dbClassUW, "CS 246", 3981)) # Algorithms
    # addCourse(SearchAvalibleInTerm(dbClassUW, "CS 245", 3980)) # Logic and Computation
    # addCourse(SearchAvalibleInTerm(dbClassUW, "CS 245", 4923)) # Logic and Computation
    # addCourse(SearchAvalibleInTerm(dbClassUW, "CS 349", 3810)) # User Interface Design
    # addCourse(SearchAvalibleInTerm(dbClassUW, "MATH 247", 3914)) # Calculus 3 (Advanced Level)
    # addCourse(SearchAvalibleInTerm(dbClassUW, "STAT 231", 3960)) # Introduction to Combinatorics
    # addCourse(SearchAvalibleInTerm(dbClassUW, "CO 250", 3721)) # Introduction to Optimization
    # addCourse(SearchAvalibleInTerm(dbClassUW, "CS 341", 3881)) # Introduction to Optimization

    
    # dbClassUW.switchCollection(
    #       collectionName="Class2024Fall")  # Class2023Fall Class2024Winter Class2024Spring Class2024Fall
    
    # addCourse(SearchAvalibleInTerm(dbClassUW, "CO 250",6486))
    # addCourse(SearchAvalibleInTerm(dbClassUW, "CO 250",6785))
    # addCourse(SearchAvalibleInTerm(dbClassUW, "MATH 235",6147))
    # addCourse(SearchAvalibleInTerm(dbClassUW, "MATH 235",6966))
    # addCourse(SearchAvalibleInTerm(dbClassUW, "MATH 237",6877))
    # addCourse(SearchAvalibleInTerm(dbClassUW, "MATH 237",6151))
    # addCourse(SearchAvalibleInTerm(dbClassUW, "PHYS 121",7408))
    # addCourse(SearchAvalibleInTerm(dbClassUW, "PHYS 121",7407)) 
    # addCourse(SearchAvalibleInTerm(dbClassUW, "PHYS 121L",7825))
    # addCourse(SearchAvalibleInTerm(dbClassUW, "CS 246E", 6622))
    
    # addCourse(SearchAvalibleInTerm(dbClassUW, "MATH 239", 6621))
    
    dbClassUW.switchCollection(
          collectionName="Class2025Winter")  # Class2023Fall Class2024Winter Class2024Spring Class2024Fall
    
    addCourse(SearchAvalibleInTerm(dbClassUW, "PHYS 234",7166))
    addCourse(SearchAvalibleInTerm(dbClassUW, "CS 431",8788))
    addCourse(SearchAvalibleInTerm(dbClassUW, "PMATH 351",6382))
    addCourse(SearchAvalibleInTerm(dbClassUW, "CO 353"))
    addCourse(SearchAvalibleInTerm(dbClassUW, "STAT 231",6097))
    addCourse(SearchAvalibleInTerm(dbClassUW, "AMATH 250",5967))
    ### List Course End
    
    makeSchedule(dbClassUW, courseWishList=courseWishList, gray=False)
    system("pdfschedule " + setting.outDir)

    print(OKGREEN + "\n\n ---------------- Done!!! ---------------- \n\n" + ENDC)
