from .DB.dbClass import dbClass
from .ClassSchedule.runner import SearchCourse, makeSchedule, SearchAvalibleInTerm
from .Utiles.colorMessage import *
from .setting import Setting

from os import system
import argparse
import sys

dbClassUW = dbClass()
setting = Setting()
courseWishList = []

url = "https://github.com/zangjiucheng/CourseExplorer/blob/Release/schema.txt"

def addCourse(course):
    if course != None:
        courseWishList.append(course)


def checkDetail(course):
    SearchCourse(dbClassUW, course)
    exit(0)
    
def parse_arguments():
    """Parse command-line arguments and validate them."""
    parser = argparse.ArgumentParser(
        description="Course Helper: A tool to manage course details and collections.",
        epilog=f"""Hint: Use --course to specify a course 
                  or --file to specify a file with courses using schema: {url}
                  or --export to export the schedule to pdf (.out only).""",
    )
    parser.add_argument(
        "-c", "--course", type=str, help="Specify the course to check details for."
    )
    parser.add_argument(
        "-f", "--file", type=str, help="Specify a file with collection of courses."
    )
    parser.add_argument(
        "-e", "--export", action=str, help="Export the schedule to pdf (.out only)."
    )
    parser.add_argument(
        "-g", "--gray", action="store_true", help="Enable gray color mode for output."
    )

    args = parser.parse_args()

    # Ensure at least one argument is provided
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    return args

def main():
    args = parse_arguments()
    gray = args.gray 
    if args.course:
        checkDetail(args.course)
    elif args.export:
        system("pdfschedule " + args.export)
        print(OKGREEN + "\n\n ---------------- Done!!! ---------------- \n\n" + ENDC)
    elif args.file:
        with open(args.file, "r") as f:
            collection = f.readline().strip().split("#")[0].strip()
            dbClassUW.switchCollection(collection)
            next(f)  # Skip the first line
            for line in f:
                try:
                    if line.startswith("#"):
                        continue
                    info = line.strip().split(",")
                    course = info[0].strip()
                    if len(info) > 1:
                        addCourse(SearchAvalibleInTerm(dbClassUW, course, int(info[1].strip())))
                    else:
                        addCourse(SearchAvalibleInTerm(dbClassUW, course))
                except Exception as e:
                    print(FAIL + f"Error: {e}" + ENDC)
        makeSchedule(dbClassUW, courseWishList=courseWishList, gray=gray)
        system("pdfschedule " + setting.outDir)
        print(OKGREEN + "\n\n ---------------- Done!!! ---------------- \n\n" + ENDC)

if __name__ == "__main__":
    main()