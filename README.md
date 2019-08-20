# pygrip
This repository contains a bunch of python files created to assist with simple tasks

Thanks to sources such as stackoverflow, Coursera and other forums that have helped me find answers to coding questions I faced in coming up with these files.

A short note about each script follows:

* fxextract - Fetches FX rates from ECB based on currencies and date provided by user. The rates are written into a text file.

* Networkcheck - Checks internet connectivity by pinging google.com at periodic intervals. Writes result to a text file for reference. Also read about Module1.bas, which is a related file to visualize the output.

* Module1.bas - This is an MSExcel recorded macro that uses the output of Networkcheck.py to present a visual line diagram of network uptime and downtime. Do change the file path to ensure that the correct file is picked up by the macro.

* MusicTheory - Gives information about notes in a scale and common chords part of a triad in the scale

* asbot01.py - Python script that controls a Telegram bot. Performs simple functions like writing input to a database (locally hosted). The functions of the bot will be gradually expanded as experimentation continues.

* asbot02_1.py - Modification of asbot01.py with functionality to use api offered by openweathermap.org to retrieve weather information for a location and pass it on to the chat user on Telegram
