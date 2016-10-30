"""
    File name:  bb_file_rename.py

       Author:  Danielle Gaither

      Purpose:  This file organizes Blackboard assignment files by
                splitting the file name assigned by Blackboard into
                tokens and using that information to sort the files
                into folders based on the student's ID. Each folder
                should have the files that the students originally
                submitted with the names the students gave them.

Last modified:  October 30, 2016
"""

import sys, os

assignment = sys.argv[1] # assignment name passed as command line arg
for root, dirs, files in os.walk(os.getcwd()): # contents of current dir
  for f in files:
    if assignment in f:
      if ".out" in f: # delete extraneous files
        os.remove(f)
      else:
        currFile = f # save full file name
        tokens = f.split('_', 4) # stops at 4 items to preserve filename
        newDirName = tokens[1] # directory name from student ID
        newFileName = tokens[len(tokens)-1] # original file name
        if not os.path.isdir(newDirName): # if directory doesn't exist
          print "Creating directory: " + newDirName
          os.mkdir(newDirName)
        print "Moving " + currFile + " to " + newDirName + '/' + \
            newFileName + "..."
        os.rename(currFile, newDirName + '/' + newFileName)
