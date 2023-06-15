# Ops Challenge: Powershell AD Automation

## Overview

Powershell can be a powerful tool in administering Active Directory (AD) users and computers. Today you’ll write a Powershell script to add a new user to AD.

## Resources

* You will need a Windows Server with AD DS installed and the server promoted to Domain Controller

* [Microsoft Documentation: New-ADUser](https://learn.microsoft.com/en-us/powershell/module/activedirectory/new-aduser?view=windowsserver2019-ps)

## Objectives

In your Windows Server, access Powershell ISE.

* Write a Powershell script that adds the below person to AD.

  * Franz Ferdinand is the TPS Reporting Lead at GlobeX USA in Springfield, OR office. Franz is part of the TPS Department. Franz’s email is ferdi@GlobeXpower.com.

Test your script. Verify in ADAC that the user was created with the correct attributes. If anything is missing, delete the user in ADAC and re-attempt from Powershell ISE.

## Stretch Goals (Optional Objectives)

Pursue stretch goals if you are a more advanced user or have remaining lab time.

* Have your script also create a new group in AD.

* Have your script also create a new OU in AD.
