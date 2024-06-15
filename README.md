# Monkeytype Hacker

This quick script is designed to trick *monkeytype.com* by typing the words automatically, not by hand. The highest words-per-minute score that I was able to get was **433**, which is way above the world record. I would assume it is possible to get a much higher score if you are using a CPU that is more powerful than *Intel Celeron N4020*. However, monkeytype is smart enough to recognize such cheats, so after the script's execution, there is a comment that says that the WPM score is invalid.

## Packages installation
The script requires 2 external packages: *selenium* and *BeautifulSoup*.  
To install them, simply execute following commands in the command line:  
`pip install selenium`  
`pip install bs4`

## Execution
After running the script, a new window with *monkeytype.com* will pop up. There is a 5 second delay between the moment that the page is loaded and the beginning of auto-typing. During this delay, you can change the typing time from the default, which is 30 seconds, to 15 seconds to make sure that the script doesn't run out of words. Then, it should start typing right away.

## Chrome
The script only works with chrome, so you have to have it installed.