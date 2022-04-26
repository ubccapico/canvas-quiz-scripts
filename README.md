# canvas-quiz-scripts
Bulk assign and moderate canvas quizzes

This repository contains 3 main scripts:  
* **assign_quiz:** assigns a list of students to their respective canvas assignments and quizzes.
* **moderate_quiz:** adds extra time for a list of students in a canvas quiz.
* **edit_override:**  used to add or remove students from an assignment override or delete the entire override.

## Getting Started

### Requirements:
* Clone the repo into your preferred IDE, for example, Visual Studio Code 
* Python 3.9 or later - [found here](http://www.python.org/getit/)
* All libraries listed in requirements.txt. To get these, simply run a pip install in the terminal:
```
pip install -r requirements.txt
```
* **Note**: If the above line results in a “Failed building wheel for pandas” error, change the line "pandas == 1.2.1" to “pandas == 1.4.2” in requirements.txt.
* You will also need a [Canvas API token](https://learninganalytics.ubc.ca/for-students/canvas-api/). Create a blank file with no type named "token", meaning the file does not end with .txt or .py. Paste your generated Canvas API token to the "token" file without any additional characters.


### Creating a .env file
Create a .env file in the root directory with the following fields:
```
CANVAS_API_TOKEN={YOUR API KEY}
INSTANCE={YOUR API DOMAIN}
```
> An example canvas domain is: https://{school}.instructure.com
* **Note**: Do not include the curly brackets when inputting these values. The CANVAS_API_TOKEN is your generated token. The INSTANCE for UBC Canvas is: https://canvas.ubc.ca

### Setting up your environment
> You can set up your environment any way you'd like. Below are instructions for creating it with virtualenv

* `pip install virtualenv` (if you don't already have virtualenv installed)
* `virtualenv venv` to create your new environment (called 'venv' here)
* `source venv/bin/activate` (to enter the virtual environment)
* `pip install -r requirements.txt` (to install the requirements in the current environment)

* **Notes for Windows Users**: `source venv/bin/activate` is a Linux command. The command `venv\Scripts\activate` is for Windows.
* However, another problem may follow for Windows showing scripts are disabled. In this case, go to Windows Powershell by searching for it from Start. Enter the command `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` then try `venv\Scripts\activate` again.

### Running a Python Script

#### assign_quiz
* You can set up the input csv with the following required columns: **id** (student's Canvas ID) and **assignment_id**
* columns with `*` are optional

    |*name           |id      |assignment_id|
    |----------------|--------|-------------|
    |Student 1       |123456  |987654       |
    |Student 2       |54321   |108642       |


* A student under **id** is assigned to the corresponding assignment under **assignment_id**. (assignment id is different from quiz id)
* To run the script, you can either use your terminal or drag and drop the input csv in the script file.
* When using the terminal, navigate to the folder which contains the local repository and type in `python3 assign_quiz.py [Enter you input file followed by .csv].` Make sure that the input file exits within your local repository folder.
* **Note**: Try running `python assign_quiz.py [Enter you input file followed by .csv]` if the above command does not work.

### moderate_quiz
* You can set up the input csv with the following required columns: **id** (student's Canvas ID) and **time**
* **id** refers to the list of students you want to moderate. The **time** column refers to extra time you would like to add to a student's attempt. It can be in a multiplicative or additive form. For example, for a 90 min quiz, a multiplicative input of 1.5  would have the same effect as an additive input of 45 mins. Therefore, both 1.5 and 45 are valid inputs under the column. You will specify if it should be treated as multiplication or addition when running the script. 
* columns with `*` are optional
    |*name           |id      |time         |
    |----------------|--------|-------------|
    |Student 1       |123456  |15           |
    |Student 2       |54321   |45           |
* To run the script, you can either use your terminal or drag and drop the input csv in the script file.
* When using the terminal, navigate to the folder which contains the local repository and type in `python3 moderate_quiz.py [Enter you input file followed by .csv].` Make sure that the input file exits within your local repository folder.

### edit_override
* You can set up the input csv with the following required columns: **id** (student's Canvas ID).
* To run the script, you can either use your terminal or drag and drop the input csv in the script file.
* **id** refers to the students you would like to add or delete from an override.   
* columns with `*` are optional
    |*name           |id      |
    |----------------|--------|
    |Student 1       |123456  |
    |Student 2       |54321   |
* When using the terminal, navigate to the folder which contains the local repository and type in `python3 edit_quiz.py [Enter you input file followed by .csv].` Make sure that the input file exits within your local repository folder.

### Notes
- The **Gradebook** from Canvas can be used as an input file for all of the scripts. Since it already has the Canvas User IDs in it, you can simply rename the column to **id** instread of **ID**. You would also need to add the columns for **time** for **moderate_quiz** or **assignment_id** for **assign_quiz** depending on which script you wish to run.
