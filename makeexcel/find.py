#!/user/bin/env python3
## script to search for a pattern match
import os, fnmatch
import pyexcel


def listypy(pattern, path):
    result = []
    for root, dirs, files in os.walk(path, topdown=True):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(name)
    return result

def write_excel(prog_list):
    data = []
    for name in prog_list:
        inp = input(f"What description do you want to add to {name}")
        prog = {"Filename": name, "Description" : inp}
        data.append(prog)
    print(data)
    filename = "Program-list.xls"
    pyexcel.save_as(records=data, dest_file_name=filename)

write_excel(listypy("*.py", "/home/student/mycode/makeexcel"))

