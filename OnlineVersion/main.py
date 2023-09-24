from DB.dbClass import dbClass
from ClassSchedule.runner import SearchCourse, makeSchedule, SearchAvalibleInTerm
from Utiles.colorMessage import *

dbClassUW = dbClass()
courseWishList = []


def addCourse(course):
    if course != None:
        courseWishList.append(course)


def checkDetail(course):
    SearchCourse(dbClassUW, course)
    exit(0)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    # checkDetail("CO 255")

    ###List of Course
    dbClassUW.switchCollection(
          collectionName="Class2023Fall")  # Class2023Fall Class2024Winter Class2024Spring Class2024Fall
    addCourse(SearchAvalibleInTerm(dbClassUW, "STAT 230",6872))
    # addCourse(SearchAvalibleInTerm(dbClassUW, "STAT 231",6879))
    # addCourse(SearchAvalibleInTerm(dbClassUW, "CS 135"))
    addCourse(SearchAvalibleInTerm(dbClassUW, "CS 145",6287))
    addCourse(SearchAvalibleInTerm(dbClassUW, "CS 241",6398))
    addCourse(SearchAvalibleInTerm(dbClassUW, "MATH 237",6203))
    addCourse(SearchAvalibleInTerm(dbClassUW, "MATH 147",6507))
    addCourse(SearchAvalibleInTerm(dbClassUW, "MATH 135",6078))
    # addCourse(SearchAvalibleInTerm(dbClassUW, "COMMST 100"))
    # addCourse(SearchAvalibleInTerm(dbClassUW, "STAT 230"))
    addCourse(SearchAvalibleInTerm(dbClassUW, "MTHEL 131"))
    addCourse(SearchAvalibleInTerm(dbClassUW, "COMMST 100",7991))
    addCourse(SearchAvalibleInTerm(dbClassUW, "CS 350",6583))
    addCourse(SearchAvalibleInTerm(dbClassUW, "CO 255",6522))
    addCourse(SearchAvalibleInTerm(dbClassUW, "PHYS 468"))

    # dbClassUW.switchCollection(
    #       collectionName="Class2024Winter")  # Class2023Fall Class2024Winter Class2024Spring Class2024Fall
    # addCourse(SearchAvalibleInTerm(dbClassUW, "ECON 101"))
    # addCourse(SearchAvalibleInTerm(dbClassUW, "STAT 230"))
    # addCourse(SearchAvalibleInTerm(dbClassUW, "CS 146"))
    # addCourse(SearchAvalibleInTerm(dbClassUW, "CS 136L"))
    # addCourse(SearchAvalibleInTerm(dbClassUW, "ENGL 119"))
    # addCourse(SearchAvalibleInTerm(dbClassUW, "MATH 136"))

    ### List Course End
    makeSchedule(dbClassUW, courseWishList=courseWishList)

    print(OKGREEN + "\n\n ---------------- Done!!! ---------------- \n\n" + ENDC)
