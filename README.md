# canvas-quiz-scripts
Bulk assign and moderate canvas quizzes

This respository contains 3 main scripts:  
* **assign_quiz:** assigns a list of students to their respective canvas assignments and quizzes.
* **moderate_quiz:** adds extra time for a list of students in a canvas quiz.
* **edit_override:**  used to add or remove students from an assignment override or delete the entire override.

## Getting Started

### Requirements:
* Python 3.9 or later - [found here](http://www.python.org/getit/)
* All libraries listed in requirements.txt. To get these, simply run a pip install:
```
pip install -r requirements.txt
```
* You will also need a [Canvas API token](https://community.canvaslms.com/docs/DOC-10806-4214724194) which you can simply paste to the file named "token" without any additional characters.


### Creating a .env file
Create a .env file in the root directory with the following fields:
```
CANVAS_API_TOKEN={YOUR API KEY}
INSTANCE={YOUR API DOMAIN}
```
> An example canvas domain is: https://{school}.instructure.com


### Setting up your environment
> You can set up your environment any way you'd like. Below are instructions for creating it with virtualenv

* `pip install virtualenv` (if you don't already have virtualenv installed)
* `virtualenv venv` to create your new environment (called 'venv' here)
* `source venv/bin/activate` (to enter the virtual environment)
* `pip install -r requirements.txt` (to install the requirements in the current environment)

### Running a Python Script

#### assign_quiz
* You can set up the input csv with the following required columns: **sis_id** (student id) and **assignment_id**
* columns with `*` are optional

    |*name           |sis_id  |assignment_id|
    |----------------|--------|-------------|
    |Student 1       |12345678|987654       |
    |Student 2       |24681012|108642       |


* A student under **sis_id** is assigned to the corresponding assignment under **assignment_id**.
* To run the script, you can either use your terminal or drag and drop the input csv in the script file.
* When using the terminal, navigate to the folder which contains the local repository and type in `python3 assign_quiz.py [Enter you input file followed by .csv].` Make sure that the input file exits within your local repository folder.

### moderate_quiz
* You can set up the input csv with the following required columns: **sis_id** (student id) and **time**
* **SIS_ID** refers to the list of students you want to moderate. The **time** column refers to extra time you would like to add to a student's attempt. It can be in a multiplicative or additive form. For example, for a 90 min quiz, a multiplicative input of 1.5  would have the same effect as an additive input of 45 mins. Therefore, both 1.5 and 45 are valid inputs under the column.  
* columns with `*` are optional
    |*name           |sis_id  |time         |
    |----------------|--------|-------------|
    |Student 1       |12345678|15           |
    |Student 2       |24681012|45           |
* To run the script, you can either use your terminal or drag and drop the input csv in the script file.
* When using the terminal, navigate to the folder which contains the local repository and type in `python3 moderate_quiz.py [Enter you input file followed by .csv].` Make sure that the input file exits within your local repository folder.

### edit_override
* You can set up the input csv with the following required columns: **sis_id** (student id).
* To run the script, you can either use your terminal or drag and drop the input csv in the script file.
* **sis_id** refers to the students you would like to add or delete from an override.   
* columns with `*` are optional
    |*name           |sis_id  |
    |----------------|--------|
    |Student 1       |12345678|
    |Student 2       |24681012|
* When using the terminal, navigate to the folder which contains the local repository and type in `python3 edit_quiz.py [Enter you input file followed by .csv].` Make sure that the input file exits within your local repository folder.

### Notes
- The **Gradebook** from Canvas can be used as an input file for all of the scripts. Since it already has the SIS User Ids in it, you can simply rename the column to **sis_id**. You would also need to add the columns for **time** for **moderate_quiz** or **assignment_id** for **assign_quiz** depending on which script you wish to run.
