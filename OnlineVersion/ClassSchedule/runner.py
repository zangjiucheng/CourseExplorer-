from ClassSchedule.SearchInfo import Course
from os import remove
from Utiles.randomColor import randomColor
from setting import Setting
from Utiles.colorMessage import *

setting = Setting()


def SearchCourse(dbClassUW, courseIndex):
    CourseDescribe = dbClassUW.CourseDescribe
    faculty = courseIndex.split(" ")[0]
    courseNum = courseIndex.split(" ")[1]
    FacultyList = CourseDescribe.find({"faculty": faculty})
    for course in FacultyList:
        if course["courseIndex"] == courseNum:
            print("\n" + "$" * 50 + "\n\n")
            print("Description: ", end="")
            print(course["courseDescription"])
            print("\ncourseCredit: ", end="")
            print(course["courseCredit"])
            print("\n\n" + "$" * 50)
            break
    print("\n\n")


def SearchAvalibleInTerm(dbClassUW, courseIndex, classNum=None):
    ClassSchedule = dbClassUW.ClassSchedule
    courseSelect = ClassSchedule.find({"ClassIndex": courseIndex})
    if courseSelect == None:
        print(FAIL + "@_@ Course %s Not Found in %s @_@" % (courseIndex, dbClassUW.ClassCollectionName) + ENDC)
        return None
    else:
        print(OKGREEN + "!! Found Course %s in %s !!" % (courseIndex, dbClassUW.ClassCollectionName) + ENDC)
        if classNum != None:
            return [courseIndex, classNum]
        return [courseIndex]


def makeSchedule(dbClassUW, courseWishList):
    classSchedule = dbClassUW.ClassSchedule
    try:
        remove(setting.outDir)
    except:
        pass
    file = open(setting.outDir, 'w+')
    file.close()
    courseInfo = Course(outDir=setting.outDir)

    ### List Course Here
    for course in courseWishList:
        if len(course) == 2:
            classNum = course[1]
            course = course[0]
        else:
            classNum = None
            course = course[0]
        courseInfo.SearchCourse(CollectionData=classSchedule, courseIndex=course, color=randomColor(),
                                classNum=classNum)
    ###
