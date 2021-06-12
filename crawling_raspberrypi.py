from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True

chr_path = '/usr/lib/chromium-browser/chromedriver'
driver = webdriver.Chrome(chr_path, options=options)

driver.get("https://hisnet.handong.edu")

search = driver.find_element_by_xpath("/html/frameset/frame[1]")
driver.switch_to.frame(search)

text = driver.find_elements_by_class_name("cls_td_food_text")

#Cafeteria
KorTb_Br = driver.find_element_by_xpath('//*[@id="tr_box11_001"]/td/div/table/tbody/tr[3]/td[1]').get_attribute("title")
KorTb_Ln = driver.find_element_by_xpath('//*[@id="tr_box11_001"]/td/div/table/tbody/tr[3]/td[2]').get_attribute("title")
KorTb_Dn = driver.find_element_by_xpath('//*[@id="tr_box11_001"]/td/div/table/tbody/tr[3]/td[3]').get_attribute("title")
FryFry = driver.find_element_by_xpath('//*[@id="tr_box11_002"]/td/div/table/tbody/tr').get_attribute("title")
Noodle = driver.find_element_by_xpath('//*[@id="tr_box11_003"]/td/div/table/tbody/tr').get_attribute("title")
Hao = driver.find_element_by_xpath('//*[@id="tr_box11_004"]/td/div/table/tbody/tr').get_attribute("title")
GraceGd = driver.find_element_by_xpath('//*[@id="tr_box11_005"]/td/div/table/tbody/tr').get_attribute("title")
MixRice = driver.find_element_by_xpath('//*[@id="tr_box11_006"]/td/div/table/tbody/tr').get_attribute("title")

#Mom's
Moms_Br = driver.find_element_by_xpath('//*[@id="tr_box11_2"]/td/table[2]/tbody/tr/td/div/table/tbody/tr[3]/td[1]').get_attribute("title")
Moms_Ln = driver.find_element_by_xpath('//*[@id="tr_box11_2"]/td/table[2]/tbody/tr/td/div/table/tbody/tr[3]/td[2]').get_attribute("title")
Moms_Dn = driver.find_element_by_xpath('//*[@id="tr_box11_2"]/td/table[2]/tbody/tr/td/div/table/tbody/tr[3]/td[3]').get_attribute("title")

#Handong Lounge
Lounge_Br = driver.find_element_by_xpath('//*[@id="tr_box11_3"]/td/table[2]/tbody/tr/td/div/table/tbody/tr[3]/td[1]').get_attribute("title")
Lounge_Ln = driver.find_element_by_xpath('//*[@id="tr_box11_3"]/td/table[2]/tbody/tr/td/div/table/tbody/tr[3]/td[2]').get_attribute("title")
Lounge_Dn = driver.find_element_by_xpath('//*[@id="tr_box11_3"]/td/table[2]/tbody/tr/td/div/table/tbody/tr[3]/td[3]').get_attribute("title")

#Grace Table
GraceTb = driver.find_element_by_xpath('//*[@id="tr_box11_4"]/td/table[2]/tbody/tr/td/div/table/tbody/tr[3]/td[2]').get_attribute("title")

driver.quit()

print('-----------MENU-----------\n')
print('A. Cafeteria\n')
print('B. Mom\'s\n')
print('C. Handong Lounge\n')
print('D. Grace Table\n')
print('Which menu do you want to see?\n')
menu = input()

if(menu == 'A'):
    print(KorTb_Br,'\n',KorTb_Ln,'\n',KorTb_Dn,'\n',FryFry,'\n',Noodle,'\n',Hao,'\n',GraceGd,'\n',MixRice,'\n')
elif(menu == 'B'):
    print(Moms_Br,'\n',Moms_Ln,'\n',Moms_Dn,'\n',)
elif(menu == 'C'):
    print(Lounge_Br,'\n',Lounge_Ln,'\n',Lounge_Dn,'\n',)
elif(menu == 'D'):
    print(GraceTb,'\n')
else:
    print('Not in Menu, exiting program\n')

f = open("menu_cafeteria.txt", 'w')
f.writelines([KorTb_Br,'\n',KorTb_Ln,'\n',KorTb_Dn,'\n',FryFry,'\n',Noodle,'\n',Hao,'\n',GraceGd,'\n',MixRice,'\n'])
f.close()

f = open("menu_moms.txt",'w')
f.writelines([Moms_Br,'\n',Moms_Ln,'\n',Moms_Dn,'\n'])
f.close()

f = open("menu_lounge.txt", 'w')
f.writelines([Lounge_Br,'\n',Lounge_Ln,'\n',Lounge_Dn,'\n'])
f.close()

f = open("menu_grace.txt", 'w')
f.writelines([GraceTb,'\n'])
f.close()
