# iStudiez ics Injector for Outlook Web App (OWA)
A Quick little hack, made with <3

## Synopsis

This program was built to provide a workaround for iStudiez "calendar sync" feature not working on Outlook Web App.

For whatever reason, Microsoft requires you define time-zone information in the header of your webcal or ics. Without it, the calendar will not appear and not sync in OWA.

This script takes your schedule feed from iStudiez, injects the appropriate header information, and spits out a new file, that will work in iStudiez.

The script is meant to be run on a web server, updating periodically. It should spit the finished file into a public folder, from which you can add to OWA.

## File Description
 - The main python file is the script
 - the `playground` folder is a Jupyter Notebook that I used for testing and debugging.

## Installation and Usage

The script is written in Python. The only difference is that, in python 2, the URL handler is called `urllib2`. In python 3, the name changed to `urllib.request`. Depending on what version of python you are running, you may have to make this change.

### Instructions:

1. Download the script and place it in a directory on your web server
2. Update the following variables in the script:
    - path of destination file (line 2)
    - your published istudiez calendar (line 3)
    - your appropriate timezone (line 7)
3. Run the script under a cron task to update however often you want.
4. Get the url path of the updated file, and add that as a calendar in OWA.

**USEFUL HINTS**: make sure the "target/destination" file is in a public location on your web server, so that if you went there in your browser, you would be greated with a very large page of text, and not a 403 forbidden.

## BUGS
As of this version, there are no known bugs. Make sure you have all your relative paths correct or you'll get errors. *You have been warned.*

## Contributions

Do as you wish. I'm satisfied but if there's something fun you want to add be my guest.

## License

GNU General Public License. In other words, go nuts. 
