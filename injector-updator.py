import urllib.request  # the lib that handles the url stuff
target = open("##PATH OF DESTINATION FILE .HTML", 'wb') # creating the file that we will use to populate the data
target_url = "http PUBLISHED ISTUDIEZ WEBCAL HERE"
data = urllib.request.urlopen(target_url) # it's a file like object and works just like a file
i = 0
# The following is the date injector, obviously, it will change based on your time zone...
string = "BEGIN:VTIMEZONE\nTZID:America/Toronto\nTZURL:http://tzurl.org/zoneinfo-outlook/America/Toronto\nX-LIC-LOCATION:America/Toronto\nBEGIN:STANDARD\nTZOFFSETFROM:-0400\nTZOFFSETTO:-0400\nTZNAME:AST\nDTSTART:19700101T000000\nEND:STANDARD\nEND:VTIMEZONE\n"
byte = str.encode(string)
for line in data: # files are iterable
    if i == 5:
        target.write(byte) #this is where we inject that string
    target.write(line)
    i+=1
target.close() #close the file that we just wrote to, DONT FORGET THIS STEP
