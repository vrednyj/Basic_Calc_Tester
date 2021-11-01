# -------------------------------------------------------------------------------
# Name:        Selenium_tester.py
# Project:     Selenium
#
# Author:      Vitaliy Baseckas
#
# Created:     23.10.2021
# Copyright:   (c) Vitaliy Baseckas 2021
# Licence:     <your licence>
# This is a simple tester for online Basic calculator
# 'https://testsheepnz.github.io/BasicCalculator.html#main-body'
# This is a part of CA Lab 2 DevOps Software Engineering
# -------------------------------------------------------------------------------
import  time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

total_errors=0
error=0

list_of_maths=['Add','Subtract','Multiply','Divide','Concatenate']

def math_analisys (math_action='Add',answer=0, num_1=0, num_2=0 ):
    '''
    This function to check if the online calculator results matches with python calculation.

    :param math_action: 'Add','Subtract','Multiply','Divide' or 'Concatenate'
    :param answer: The value returned by online calculator string
    :param num_1: int by default number 1
    :param num_2: int by default number 2
    :return: Pass or Fail
    '''
    #print("Math action: {0} Answere:{1} Num_1: {2} Num_2: {3}".format(math_acation,answer,num_1,num_2)) # for debug

    error=0
    math_calculation=0
    math_results="Fail"
    if math_action == 'Add':
        math_calculation=num_1 + num_2
        if str(math_calculation) == str(answer):
            error+=0
        else:
            error += 1
    if math_action == 'Subtract':
        math_calculation = num_1 - num_2
        if str(math_calculation) == str(answer):
            error += 0
        else:
            error += 1

    if math_action == 'Multiply':
        math_calculation = num_1 * num_2
        if str(math_calculation) == str(answer):
            error+=0
        else:
            error += 1

    if math_action == 'Divide':
        math_calculation = num_1 / num_2
        if str(math_calculation) == str(answer):
            error+=0
        else:
            error += 1
    if math_action == 'Concatenate':
        math_calculation = str(num_1) + str(num_2)
        if math_calculation == answer:
            error+=0
        else:
            error += 1
    if error==0:
        math_results = "Pass"
    #print("Answer {0} Result {1}".format(answer,math_calculation)) #for debug
    return math_results


driver = webdriver.Chrome('C:\Chrome_Driver_Path\chromedriver.exe') #will use the Chrome driver. Make sure chromedriver.exe is downloaded to your lockal machine from here:https://chromedriver.chromium.org/downloads
url = 'https://testsheepnz.github.io/BasicCalculator.html#main-body' # url for the online calc.
driver.get(url)

first_number=10.4 #number to be intered in Num 1 fieald of the caclulator.
second_number=3.2 #number to be intered in Num 1 fieald of the caclulator.

for a in range (10):#we have 10 build on the web
    #For info: The search for each element is on the web is done through try: to make sure the test continue operating on exceptional errors.
    total_errors = 0
    #error = 0
    print("Testing the Build {}".format(a))

    try:
        num1 = driver.find_element("id", 'number1Field')  # serching the element on the web for the first number
        num1.clear()
        num1.send_keys(first_number)  # inserting the element in the field

    except Exception as e:
        total_errors += 1
        print(e)

    try:
        num2 = driver.find_element("id", 'number2Field')  # serching the element on the web for the second number
        num2.clear()
        num2.send_keys(second_number)

    except Exception as e:
        total_errors += 1
        print(e)

    try:
        build_selection = driver.find_element("id",'selectBuild')
        build_selection.send_keys(a)
    except Exception as e:
        total_errors +=1
        print(e)
    try:
        answer = driver.find_element("id", 'numberAnswerField')
        time.sleep(0.5)
    except Exception as e:
        total_errors += 1
        print(e)

#    try: #This is disabled. It is nice to check if int check box presents on the web. It disappaers when 'Concatinate' is selected.
#        int_check_box = driver.find_element("id", 'integerSelect')
#        print(int_check_box.)
#    except:
#        total_errors += 1
#        print(e)

    for i in list_of_maths:
        try:
            dropdown1 = Select(driver.find_element("id",'selectOperationDropdown'))
            dropdown1.select_by_visible_text(i)
            time.sleep(0.5)
        except Exception as e:
            total_errors +=1
            print(e)
        try:
            calc=driver.find_element("id",'calculateButton') #Find Calculate button on the web
            calc.click()                                     # And press it.
            time.sleep(0.5)
        except Exception as e:
            total_errors +=1
            print(e)

        result=math_analisys(i,answer.get_attribute('value'),first_number,second_number)# check if the web calc did right calculations.
        if result == 'Fail':
            total_errors +=1
        else:
            total_errors +=0

    time.sleep(1)

    try:
        clear_button=driver.find_element("id",'clearButton')
        clear_button.click()

    except Exception as e:
        total_errors +=1
        print(e)

    if total_errors>0:
        print("The Build {} has some issues. Total Errors {}".format(a,total_errors))
    else:
        print("The Build {} is ready for deployment. Total Errors {}".format(a,total_errors))

driver.close() #close the web page.


