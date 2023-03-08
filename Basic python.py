import json
import argparse
import re
import datetime
from collections import defaultdict
import csv
import pprint
JSON_FILE_PATH = "C:\\Users\\ariel\PycharmProjects\pythonProject\\venv\Scripts\student.json"



class Assignment():


    def Add_homework_assignment(args):

        list_of_inputs = {'name': args.student, 'homework': args.homework, 'date': args.date, 'path': args.path}

        with open(JSON_FILE_PATH, 'r+') as file:
            data = json.load(file)
            data["emp_details"].append(list_of_inputs)
            file.seek(0)
            json.dump(data, file, indent=4)



    def Remove_homework_assignment(args):


        list_of_inputs = {'name': args.student, 'homework': args.homework}

        with open(JSON_FILE_PATH, 'r+') as file:
            data = json.load(file)
            for assinment in data["emp_details"]:
                if assinment["name"]  == args.student and assinment["homework"] == args.homework:
                    del data["emp_details"][data["emp_details"].index(assinment)]
        json.dump(data, open(JSON_FILE_PATH, "w"), indent = 4)



    def Search(args):


        with open(JSON_FILE_PATH, 'r+') as file:
            data = json.load(file)
            for assinment in data["emp_details"]:
                if args.homework in assinment["homework"]:
                    try:
                        with open(assinment["path"], "r") as f:
                            for word in f.readlines():
                                for Item_To_Search in args.list:
                                    if re.search(Item_To_Search, word):
                                        print("The student name is " + assinment["name"], " The path to the file is " + assinment["path"])

                    except:
                        print("Path to the file is incorrect!")



    def Month_Report(args):

        dict_of_assimnets = defaultdict(lambda: defaultdict(int))

        with open(JSON_FILE_PATH, 'r+') as file:
            data = json.load(file)
            for assinment in data["emp_details"]:
                date = datetime.datetime.fromisoformat(assinment["date"]).month

                if re.search(str(datetime.datetime.strptime(args.date, "%Y").year), assinment["date"]):
                    dict_of_assimnets[assinment["name"]][date] += 1
            pprint.pprint(dict_of_assimnets)


    def Dumps_Assignments(args):

        with open(JSON_FILE_PATH, 'r+') as JsFiile:
            JsFiile = json.load(JsFiile)

        with open(args.csv, 'w', newline='') as CsvFile:
            fieldnames = ['Student_Name', 'Homework', 'Date', 'Path']
            writer = csv.DictWriter(CsvFile, fieldnames=fieldnames)
            writer.writeheader()
            for assignment in JsFiile["emp_details"]:
                writer.writerow(
                    {'Student_Name': assignment['name'], 'Homework': assignment['homework'], 'Date': assignment['date'], 'Path': assignment['path']})


def main():



    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers()

    parser_add = subparser.add_parser('add')
    parser_add.add_argument("--student", help="Student name", type=str, required=True)
    parser_add.add_argument("--homework", help="Homework name", type=str, required=True)
    parser_add.add_argument("--date", help="Expected format, YYYY-MM-DD", type=str, required=True)
    parser_add.add_argument("--path", help="File path", type=str, required=True)
    parser_add.set_defaults(func=Assignment.Add_homework_assignment())

    parser_remove = subparser.add_parser('remove')
    parser_remove.add_argument("--student", help="Student name", type=str, required=True)
    parser_remove.add_argument("--homework", help="Homework name", type=str, required=True)
    parser_remove.set_defaults(func=Assignment.Remove_homework_assignment)

    parser_search = subparser.add_parser('search')
    parser_search.add_argument( "--homework", help="Homework name", type=str, required=True)
    parser_search.add_argument("--list", nargs='+', help="List of patterns", type=str, required=True)
    parser_search.set_defaults(func=Assignment.Search)

    parser_month_report = subparser.add_parser('report')
    parser_month_report.add_argument("--date", help="Expected format, YYYY-MM-DD", type=str, required=True)
    parser_month_report.set_defaults(func=Assignment.Month_Report)

    parser_dumps_report = subparser.add_parser('dumps')
    parser_dumps_report.add_argument("--csv", help="Expected path to the csv file", type=str, required=True)
    parser_dumps_report.set_defaults(func=Assignment.Dumps_Assignments)


    args = parser.parse_args()
    args.func(args)



if __name__ == '__main__':
    main()

