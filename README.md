# bb_file_rename
Python program that organizes student assignments downloaded from Blackboard, an online education tool used by many institutions. This program is especially useful for larger classes with relatively standardized assignments, as it saves time compared to clicking and downloading each individual submission file.

In other words, if you're a TA or instructor who spends far too much time fussing with Blackboard, this should make your life a little bit easier. It has cut my own grading time by about a third. If it helps you, I'd love to hear about it!

## Preparation
Use the Blackboard Grade Center to download the assignments you intend to work with. If you are unfamilar with how to do this, you can find that information at [Blackboard Help](https://help.blackboard.com/). This will enable you to download all the assignments in one big .zip file.

Once you've downloaded the .zip file, unzip it to your directory of choice. Place `bb_file_rename.py` in the same directory as the unzipped files.

After the files are unzipped, you should see that they share a common beginning, which is probably the assignment name. For example, if you are downloading submissions for an assignment called `Assignment 1` on Blackboard, the filenames will look something like:

`Assignment 1_abc0123_attempt_2015-02-12-21-30-34_Assignment_1.pdf`

Your institution's Blackboard settings may vary, but this program is set up with the assumption that Blackboard creates filenames with the following structure:

`{assignment name}_{student ID number}_{timestamp}_{original filename}`

The program splits the filename into tokens with the underscore as a separator. It stops at 4 splits (creating 5 tokens) so that the entire original filename, which may contain underscores, is preserved. If the assignment name contains underscores, then the program will need to be modified to produce the correct number of tokens.

## Running the program

When running the program, the assignment name should be passed as a command-line argument at run-time. If the assignment name contains spaces, be sure to surround it with quotation marks. Again, using the example of an assignment called `Assignment 1`, you would type the following at the command prompt (**including** the quotes):

`python bb_file_rename.py "Assignment 1"`

As is, the program deletes any files with a `.txt` or `.out` extension. If your needs are different, change line 22 to suit your needs.

This should sort the files into folders based on the student ID number. Using our running example, there should be a folder named `abc0123` that contains a file called `Assignment_1.pdf`.

## Troubleshooting

If the program does not run as expected, make sure of the following:

1. All your files, including the program, are in the same directory
2. The assignment name is typed correctly
