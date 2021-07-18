
[Automatic Web form filling Documentations:]

[Prerequisites:]
1.Clone the code in to the local system 
2.To Run Selenium python scripts ,Install pycharm in your system
3.Google Chrome need to be installed in the server or local machine.
4.Chrome driver need to be downloaded based on your chrome browser version and placed in the Webform_Automation/Driver folder
5.Open the terminal in pycharm console and execute the following command
    sudo pip3 install -r Requirement.txt
  
[Steps to install the google chrome]
-Open the terminal (Ctrl+Alt+t) in the ubuntu 
-wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
-sudo apt install ./google-chrome-stable_current_amd64.deb
-Check chrome brower version using command -> google-chrome -version
  	
[Steps to Download the chrome driver] 
Note: Based on chrome browser version need to download chrome driver 
   https://sites.google.com/a/chromium.org/chromedriver/downloads

6.In pycharm configure the interpreter as python 3.8
7.Place the csv file or excel in Excel_Directory
8.Go to locators folder -> selenium_locators.py -> Provide the Excel_file name in filename variable
9.Go to resuse_funcs.py file and add the url of web page in driver.get()
10. To Run the Test suite -> Test_Scripts/test_suite.py [Right click on mouse and click on run option]
else other wise run the command in terminal : [python3 -m unittest Test_Scripts/test_suite.py]

