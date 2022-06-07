# Solving the Dollar Game using Constraint Programming

This is the project for my bachelor thesis. 

It starts a Selenium Browser instance and plays the levels on the website <a href="thedollargame.io">thedollargame.io</a>. 

This project uses the libraries Selenium Webdriver, Python OpenCV, MiniZinc and Tesseract OCR.

To start the program, you will need create and start virtual environment. After that, you can install the dependencies using <br><br>
``` pip install -r requirements.txt ``` 

Start the program using 

``` python main.py -mode=standard ```


The argument "-mode" accepts 3 values: "standard", "start_at_level" and "calculate_level". 
For the last two, you will need to add a ``` --world``` and a ``` --level``` argument. 

<h2>Start at a specific Level </h2>
This mode allows you start at a different level besides the first one. <br>
<b>Please note:</b> You can only play Levels you already solved or the next one. thedollargame.io saves user progress on the server and identifies the user with a userId written to the local storage. 
If you use the one, that is currently in the repository in the first line of the file "local_storage.txt", you can play until level 3 world 35. 

<h2> Calculate Level </h2>
This mode analyzes the level screenshot and calculates the solution, but does not start a browser instance and actually play the level. 
This mode is for debugging purposes only and you can only start if there is screenshot for the level in the corresponding directory in "/activegame".
