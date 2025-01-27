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
* A [Canvas API token](https://learninganalytics.ubc.ca/for-students/canvas-api/). Create a blank file with no type named "token" in the cloned repo folder, meaning the file does not end with .txt or .py. Paste your generated Canvas API token to the "token" file without any additional characters.
* All libraries listed in requirements.txt. To get these, simply run a pip install in the terminal:
```
pip install -r requirements.txt
```
**Troubleshooting for Window Users:**
* Running commands with "pip" or "pip3" heading shows error that the command cannot be found & need to check your path:
    1. In the Window's search bar, find "Edit the system environment variables", a pop up should appear upon clicking it.
    2. Click on "Advanced" from the top bars.
    3. Click "Environment Variables near the bottom right.
    4. Under "System Variables", (NOT "User Variables"), double click on "Path" to open it.
    5. In the new pop up called "Edit environment variable", click "New" on the right.
    6. Enter two new paths depending on where you installed Python, for example: (folder names for Python can change depending on version)
        * C:\Users\[username]\AppData\Local\Programs\Python\Python310\Scripts
        * C:\Users\[username]\AppData\Local\Programs\Python\Python310
    7. Click "Ok" until all pop ups disappear
    
* Failed building wheel for pandas” error:
    1. Change the line "pandas == 1.2.1" to “pandas == 1.4.2” in requirements.txt.


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

**Troubleshooting for Window Users:**
* `source venv/bin/activate` is a Linux command. The command `venv\Scripts\activate` is for Windows, read below if the command still does not work.
* Problem may follow for Windows showing scripts are disabled. In this case, go to Windows Powershell by searching for it from Start. Enter the command `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`, type in "Y" and press enter. Then, try `venv\Scripts\activate` again.

### Running a Python Script

#### assign_quiz
* You can set up the input csv with the following required columns: **id** (student's Canvas ID) and **assignment_id**
* columns with `*` are optional

    |*name           |id      |assignment_id|
    |----------------|--------|-------------|
    |Student 1       |123456  |987654       |
    |Student 2       |54321   |108642       |


* A student under **id** is assigned to the corresponding assignment under **assignment_id**. (assignment id is different from quiz id)
    * **id**: Obtain either from the Canva's Gradebook or the Canvas URL. (canvas.ubc.ca/courses/[course code]/users/[**id**])
    * **assignment_id**: Click into "Assignments" tab inside of the Canvas course, right click the assignment and click "Copy link address". Then, paste it somewhere so you can see the assignment id. (canvas.ubc.ca/courses/[course code]/assignments/[**assignment_id**])
* To run the script, you can either use your terminal or drag and drop the input csv in the script file.
* When using the terminal, navigate to the folder which contains the local repository and type in `python3 assign_quiz.py [Enter you input file followed by .csv].` Make sure that the input file exists within your local repository folder.
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
