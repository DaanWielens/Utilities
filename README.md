# Utilities
This folder contains several (unrelated) utilities.

**[Python] GPXheatmap**
This *tool* can be used to create heat maps from GPX data: Garmin Activity Data. Simply export the activity data from the Garmin app, store all GPX files in the same folder, and run this file from within that same folder. The script will create simple heat maps.

**[Python] batch-recur**

This *template* is for batch conversion/analysis of files. If a certain (commandline) script must be executed for a lot of files, this script can do that in an automated way. The script must be changed in order to work!

** [Python] WAgroup**
This *tool* can be used to create a bar plot of number of messages per person in a WhatsApp group. In WhatsApp, export the chat. Place the .txt file in the same folder as the script, edit the filename in the script (i.e. `file = 'yourgroupchathere.txt'`) and run the script. The script will save the graph in the same folder.

Credits for WAgroup partially go to https://github.com/BASTAHT for the initial idea, on which this version is based (completely rewritten).
