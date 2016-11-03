import os

filename = raw_input("Input filename")

os.system("git add {}".format(filename))

commit = raw_input("Input commit")

os.system("git commit -m {}".format(commit))

os.system("git push -u origin master")

