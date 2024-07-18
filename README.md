# OrangeHRM Leave Assignment Bot

This repository contains a Selenium-based bot that automates the process of assigning leave for multiple employees in the OrangeHRM application.

## Overview

The bot logs into the OrangeHRM system, navigates to the leave assignment section, fills in the required details for each employee, and assigns leave. It also generates a report indicating the success or failure of each leave assignment.

## Demo Video

A demo video showcasing how the bot works can be found 


https://github.com/user-attachments/assets/748c9a40-0389-4afa-954d-56174c9b81bd



## Features

- Logs into OrangeHRM with provided admin credentials
- Iterates over a list of employees to assign leave
- Checks for sufficient leave balance before assignment
- Handles cases where no employee records are found
- Generates a detailed report of leave assignment outcomes
- Includes error handling for various scenarios

## Prerequisites

- Python 3.x
- Chrome WebDriver compatible with your version of Google Chrome
- Selenium package for Python


## Usage

1. **Edit the employee list**:
    - Open the `main.py` file and update the `employees` list with the names of employees for whom you want to assign leave.

2. **Run the bot**:
    ```bash
    python main.py
    ```

## Script Breakdown

### `login()`
This function logs into the OrangeHRM application using the provided admin credentials.

### `fill_the_fields()`
This function fills in the leave type and dates for the leave assignment form.

### `logout()`
This function logs out from the OrangeHRM application.

### `assign_leave()`
This function iterates over the list of employees, fills in the leave assignment form for each employee, and generates a report based on the outcome.

## Report

The bot generates a list of reports indicating the success or failure of each leave assignment. The report is printed to the console at the end of the script.



