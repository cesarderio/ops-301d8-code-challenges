# Ops Challenge: File Permissions

## Overview

Linux sets file permissions by User, Group, and Other. Linux also sorts permission by Read, Write, and Execute. Today, you will be create a bash script that alters file permissions of everything in a directory.

## Objectives

Take care to only perform this operation in user-created directories. Changing permissions in system files/directories is not advised, as this can cause malfunctions in the OS.

### Create a new bash script that performs the following

* Prompts user for input directory path.

* Prompts user for input permissions number (e.g. **777** to perform a **chmod 777**)

* Navigates to the directory input by the user and changes all files inside it to the input setting.

* Prints to the screen the directory contents and the new permissions settings of everything in the directory.

## Stretch Goals (Optional Objectives)

* Pursue stretch goals if you are a more advanced user or have remaining lab time.

* Design your script to output a log file of all actions that were taken by the script.

* Design your script to output to the screen each file changed one by one, with a slight delay between each file changed.
