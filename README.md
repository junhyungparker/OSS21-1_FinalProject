Today's Menu from HISNet
=========================
###### OSS21-1 Final Project

### What does this project do?
##### + This python code extracts today's menu from the Handong Global University's website - HISNet, prints it out on the screen, and also saves it as a text file in the same directory.
### Why is this project useful?
##### + This project is useful for people who wants to know what the menu is for today, and for people who needs the menu as a text file.
##### + People could also use it as an open source, to extract any text from a website they want the data from. 
### How do I get started?
##### + To get started, you need to install some packages with the following commands:
    1. Python
        - sudo apt-get install python3
    2. Selenium
        - sudo pip3 install selenium
    3. Chrome Driver
        - sudo apt-get install chromium-chromedriver
        - To check the path for the chrome driver:
            - dpkg -L chromium-chromedriver
    
### Information: 
##### + BeautifulSoup does not work because the HISNet website is coded with HTML along with JavaScript, so a heavier program is needed - Selenium. Moreover, the menu text is within another HTML other than the main HTML, so the code:
    search = driver.find_element_by_xpath("/html/frameset/frame[1]")"
is needed to switch from the larger frame of HTML to the HTML frame where the menu text resides in. 

### For further help, contact: 
    <21700303@handong.edu>
### Link to the Instruction Video:
    <https://youtu.be/cFOYpexyJe4>
