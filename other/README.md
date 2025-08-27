#Python Projects

##Project 1 -  Extract Contact Information from Large Documents

Roadmap:
* Get the text from the clipboard.
* Find all phone numbers and email addresses in the text.
* Paste them onto the clipboard.
    - The code will need to do the following:
        * Use the pyperclip module to copy and paste strings.
        * Create two regexes, one for matching phone numbers and one for matching email  addresses.
        * Find all matches (not just the first match) of both regexes.
        * Neatly format the matched strings into a single string to paste.
        * Display some kind of message if no matches were found in the text.

#######################################################################################

##Project 2- Remove headers from CSV Files

At a high level, the program must do the following:
*Find all the CSV files in the current working directory.
*Read the full contents of each file.
*Write the contents, skipping the first line, to a new CSV file.

At the code level, this means the program will need to do the following:
*Loop over a list of files from os.listdir(), skipping the non-CSV files.
*Create a CSV reader object and read the contents of the file, using the line_num attribute to *figure out which line to skip.
*Create a CSV writer object and write the read-in data to the new file.
