from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select

from playsound import playsound

import time, re, os, getpass, sys, argparse


def main():
    classnum = -1
    institution = ""
    term = ""
    year = -1
    subject = ""

    parser = argparse.ArgumentParser()
    parser.add_argument("--classnum", help="class number", type=int)
    parser.add_argument("--institution",
                        help="college name in full eg. Queens College",
                        type=str)
    parser.add_argument("--term",
                        help="Spring, Summer, Fall, Winter",
                        type=str)
    parser.add_argument("--year", help="YYYY", type=int)
    parser.add_argument("--subject",
                        help="Subject name in full eg. Computer Science",
                        type=str)
    parser.add_argument("--visible",
                        help="Makes the browser visible",
                        action="store_true")
    args = parser.parse_args()
    if args.classnum:
        print("Class " + str(args.classnum) + " selected")
        classnum = args.classnum
    if args.institution:
        print("Institution " + args.institution + " selected")
        institution = args.institution
    if args.term:
        print("Term " + args.term + " selected")
        term = args.term
    if args.year:
        print("Year " + str(args.year) + " selected")
        year = args.year
    if args.subject:
        print("Subject " + args.subject + " selected")
        subject = args.subject

    if not args.institution:
        institution = institutionmenu()
        print("Institution " + institution + " selected")

    if not args.year:
        year = yearmenu()
        print("Year " + str(year) + " selected")

    if not args.term:
        term = termmenu()
        print("Term " + term + " selected")

    if not args.subject:
        subject = subjectmenu()
        print("Subject " + subject + " selected")

    if not args.classnum:
        classnum = classmenu()
        print("Class " + str(classnum) + " selected")

    # print all vars and ask the user is this correct? if not we ask again, if yes then we run
    flag = False

    options = Options()
    #options.binary_location = "C:/Program Files (x86)/Google/Chrome Beta/Application/chrome.exe"
    if not args.visible:
        options.add_argument('headless')
    driver = webdriver.Firefox(
        options = options,
        executable_path=r""
    )
    SignUp(driver,term,classnum)
    # driver.get("https://globalsearch.cuny.edu/")
    # time.sleep(3)
    # collegeIDpartial = driver.find_elements_by_xpath("//*[contains(text(),'" + institution + "')]")
    # print("//*[text()[contains(., '" + institution + "')]]")
    # print('List size = ' + str(len(collegeIDpartial)))
    # if(len(collegeIDpartial) == 0): sys.exit()
    # collegeID = collegeIDpartial[0].get_attribute("for")
    # #collegeID = "QNS01"
    # driver.find_element_by_id(collegeID).click()
    # selecttermyear = Select(driver.find_element_by_id('t_pd'))
    # selecttermyear.select_by_visible_text(str(year) + " " + term + " Term")
    # driver.find_element_by_name('next_btn').click()

    # selectsubject = Select(driver.find_element_by_id('subject_ld'))
    # selectsubject.select_by_visible_text(str(subject))
    # selectcareer = Select(driver.find_element_by_id('courseCareerId'))
    # selectcareer.select_by_visible_text('Undergraduate')
    # driver.find_element_by_id(
    #     'open_classId').click()  #uncheck open classes only
    # driver.find_element_by_id('btnGetAjax').click()
    # classhtml = collegeID = driver.find_elements_by_xpath(
    #     "//*[contains(text(), '" + str(classnum) + "')]")[0].get_attribute("href")

    # while not flag:
    #     driver.get(str(classhtml))
    #     classstatus = driver.find_element_by_id(
    #         'SSR_CLS_DTL_WRK_SSR_DESCRSHORT').get_attribute('innerHTML')
    #     if classstatus == "Open":
    #         flag = True
    #         SignUp(driver,term,classnum)
    #     print(classstatus)
    #     time.sleep(30)


def yearmenu():
    return input("Enter a year: ")  # i dont want to handle non int so i wont


def classmenu():
    return input(
        "Enter a 5 digit class number: ")  # i dont want to handle non int so i wont


def termmenu():
    choice = '0'
    while choice == '0':
        print("Choose a term")
        print("Choose 1 for Spring")
        print("Choose 2 for Summer")
        print("Choose 3 for Fall")
        print("Choose 4 for Winter")

        choice = input("Please make a choice: ")

        if choice == "4":
            return "Winter"
        elif choice == "3":
            return "Fall"
        elif choice == "2":
            return "Summer"
        elif choice == "1":
            return "Spring"
        else:
            print("I don't understand your choice.")


def subjectmenu():
    choice = '0'
    while choice == '0':
        print("Choose a subject")
        print("Choose 1 for Computer Science")
        print("Choose 2 for Mathematics")
        print("Choose 3 for Other")

        choice = input("Please make a choice: ")

        if choice == "1":
            return "Computer Science"
        elif choice == "2":
            return "Mathematics"
        elif choice == "3":
            return input("Enter FULL subject name: ")
        else:
            print("I don't understand your choice.")


def institutionmenu():
    choice = '0'
    while choice == '0':
        print("Choose a college")
        print("Choose 1 for Queens College")
        print("Choose 2 for Other")

        choice = input("Please make a choice: ")

        if choice == "1":
            return "Queens College"
        elif choice == "2":
            return input("Enter FULL institution name: ")
        else:
            print("I don't understand your choice.")

def CUNYEmail():
    return input("Enter your Cuny Email: ")

def Password():
    return input("Enter your Cunyfirst Password: ")

def SignUp(driver,term,classnumber):
    email = CUNYEmail()
    password = Password()
    driver.get("https://cunyfirst.cuny.edu")
    Usernameinput = driver.find_element_by_id("CUNYfirstUsernameH")
    Usernameinput.clear()
    Usernameinput.send_keys(email)
    PasswordInput = driver.find_element_by_id("CUNYfirstPassword")
    PasswordInput.send_keys(password)
    driver.find_element_by_id("submit").click()
    time.sleep(3)
    ElementList = driver.find_elements_by_tag_name("tr")
    SCElement = driver.find_element_by_id("crefli_HC_SSS_STUDENT_CENTER")
    SCElement.find_element_by_tag_name("a").click()
    time.sleep(3)
    frame = driver.find_element_by_tag_name("iframe")
    driver.switch_to.frame(frame)
    EnrElement = driver.find_element_by_xpath("//*[contains(text(),'Enroll')]").click()
    #get the element id which contains Semester
    time.sleep(3)
    ID = driver.find_element_by_xpath("//*[contains(text(),'" + term + "')]").get_attribute("id")[-1]
    #combine the id with the expected Radio Button id
    RadioID = "SSR_DUMMY_RECV1$sels$" + ID + "$$0"
    #search for element with RadioID
    driver.find_element_by_id(RadioID).click()
    driver.find_element_by_id("DERIVED_SSS_SCT_SSR_PB_GO").click()
    time.sleep(3)
    classbox = driver.find_element_by_id("DERIVED_REGFRM1_CLASS_NBR")
    classbox.send_keys(classnumber)
    driver.find_element_by_id("DERIVED_REGFRM1_SSR_PB_ADDTOLIST2$9$").click()
    try:
        time.sleep(1)
        driver.find_element_by_id("DERIVED_CLS_DTL_NEXT_PB$280$").click()
    except:
        print("The class is already in the cart")
    time.sleep(3)
    #find the element id that holds the class
    ID = driver.find_element_by_xpath("//a[text()[contains(.,'" + str(classnumber) + "')]]").get_attribute("id")[-1]
    #click on the box with the ID related to the class
    driver.find_element_by_id("P_SELECT$"+ID).click()
    #click on enroll
    driver.find_element_by_id("DERIVED_REGFRM1_LINK_ADD_ENRL").click()
    #remember to uncomment below
    time.sleep(1)
    driver.find_element_by_id("DERIVED_REGFRM1_SSR_PB_SUBMIT").click()
    


main()
