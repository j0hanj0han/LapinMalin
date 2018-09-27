# read a text file as a list of lines
# find the last line, change to a file you have
import ast
import json

fileHandle = open('jenkins_status.log', "r")
lineList = fileHandle.readlines()
fileHandle.close()
print(lineList)
print("The last line is:")


json_data = json.dumps(lineList[-1])
#json_dict = json.loads(lineList[-1])

new_line = ast.literal_eval(lineList[-1])

print(new_line)
print(type(new_line))

for job in new_line:
    print(job['color'])




