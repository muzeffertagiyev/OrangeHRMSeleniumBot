from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time

# Because of seeing error possibilities i tried to use multiple employee names,then in the code you will see that i have used for loop for iterating all employees
employees = ["Jasmine Morgan" ,"Peter Mac Anderson", "Russel  Hamilton" , "Charles  Carter", "Timothy Lewis Amiano"]

# for making the browser to be open all the time
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")


def login():
    """This section makes sign in into account"""

    username_field = driver.find_element(By.XPATH, value='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input')
    password_field = driver.find_element(By.XPATH, value='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')

    username_field.send_keys("Admin")
    password_field.send_keys("admin123")
    password_field.send_keys(Keys.ENTER)

    
def fill_the_fields():
    """This function fills the required fields such as leave type and dates"""

    # choosing the leave type
    leave_type_field = driver.find_element(By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div' ).click()
    choose_leave_type = driver.find_element(By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/div/div[2]/div[11]/span').click()
    

    from_date_field = driver.find_element(By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[1]/div/div[2]/div/div/input')
    to_date_field = driver.find_element(By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[2]/div/div[2]/div/div/input')

    # because of the next employee we are clearing the date fields 
    from_date_field.send_keys(Keys.BACK_SPACE * len(from_date_field.get_attribute("value")))
    from_date_field.send_keys('2020-10-19')

    # after filling from date field it is require to click to the to date field. that is the reason click function has been used here 
    to_date_field.click()
    to_date_field.send_keys(Keys.BACK_SPACE * len(to_date_field.get_attribute("value")))
    to_date_field.send_keys('2020-10-23')

def logout():
    """This section logout the user, we will use this function after all process completed """
    # it is for clicking to the dropdown menu next to the profile picture
    dropdown = driver.find_element(By.XPATH, value='//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/i' ).click()

    # after dropdown menu is opened then we make our robot to click the logout 
    logout = driver.find_element(By.XPATH, value='//*[@id="app"]/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a').click()

def assign_leave():
    """This section goes to assign leave section and fill the forms and assigns"""
    # a list created to add errors or other actions into it and to print in the end for the HR person
    reports = []

    # after login robot will find the assign button and will click it
    assign_page = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[3]/div/div[2]/div/div[1]/button')))
    assign_page.click()

    # for the employee name field
    employee_name_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/div/div/input')))

    # now we are iterating all employees from the list which we created above
    for employee_name in employees:
        # we make sure that employee name field is clean , because after one employee details we will need to add another one till the list ends.
        employee_name_field.send_keys(Keys.BACK_SPACE * len(employee_name_field.get_attribute("value")))
        employee_name_field.send_keys(employee_name)

        time.sleep(5)
        choose_name = driver.find_element(By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/div/div[2]/div')

        # when the user name is not found then we will just add the not found message to the report and start from the another employee
        if choose_name.text == "No Records Found":
            reports.append(f"{employee_name} has not been found")
        else:
            # after employee found then in clicks to the employee name in the below opened section 
            choose_name.click()
            # then it starts to fill the data 
            fill_the_fields()
            # after filing all data then robot looks at the balance of the leaving day of the employee
            balance = driver.find_element(By.XPATH, value='//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/p')

            # then all data was filled ,robot clicks to the assign button
            assign_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[6]/button')))
            assign_button.click()

            time.sleep(2)

            # then we are checking if the balance text was insufficient or not, it it was not insufficient then first we just add the message to the report list, then we try click to the ok button which will be appeared after clicking to the assign button, then the assignment will be finished for the more proper message to be added to the report
            if balance.text == 'Balance not sufficient':
                reports.append(f"{employee_name} did not have sufficient leave balance ")
                try:
                    confirm_leave_assignment = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[3]/div/div/div')))
                    if confirm_leave_assignment:
                        ok_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]')))
                        ok_button.click()
                        reports.append(f"Leave assignment confirmed for {employee_name} after insufficient balance")
                except Exception as e:
                    pass

            # after assignment we will see a disappearing  pop-up message which will appear on the left bottom of the page so we will get the report from that too , if the message failed then we can consider the assignment that it is already done for the employee ,otherwise it is success 
            try:
                pop_up_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oxd-toaster_1"]/div/div[1]/div[2]/p[2]')))
                if pop_up_message.text == 'Failed to Submit':
                    reports.append(f"Error: Most probably before ,leave has been assigned for {employee_name}")
                else:
                    reports.append(f"Success: Leave has been successfully saved for the {employee_name}")
            except Exception as e:
                pass
    # printing the report
    print(reports)                

# in this section we are running the functions and putting time among them, and also quit the app after completion of the process
if __name__ == "__main__":
    
    time.sleep(10)
    login()
    assign_leave()
    time.sleep(5)
    logout()
    driver.quit()