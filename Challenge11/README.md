# Ops Challenge: Python Requests Library

## Overview

Ever wondered how web browsers like Google Chrome communicate with web servers to create the interactive web sites and apps we use every day? One technical answer is HTTP requests. Today, you will be performing HTTP GET requests using the requests Python library. This library is very useful for a security professional to evaluate how a web server responds to outside requests.

## Resources

[Python Requests Library Guide](https://realpython.com/python-requests/)

## Objectives

Create a Python script that performs the following:

* Prompt the user to type a string input as the variable for your destination URL.

* Prompt the user to select a HTTP Method of the following options:
  * GET
  * POST
  * PUT
  * DELETE
  * HEAD
  * PATCH
  * OPTIONS

* Print to the screen the entire request your script is about to send. Ask the user to confirm before proceeding.

* Using the requests library, perform a request against the destination URL with the HTTP Method selected by the user.

* For the given header, translate the codes into plain terms that print to the screen; for example, a 404 error should print Site not found to the terminal instead of 404.

* For the given URL, print response header information to the screen.

## Stretch Goals (Optional Objectives)

Pursue stretch goals if you are a more advanced user or have remaining lab time.

* Have your script perform authentication into api.github.com using the auth command.

* Add timeouts to your script.

* Add error handling to your script.
