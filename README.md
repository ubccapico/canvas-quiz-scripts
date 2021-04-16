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

### Running a Python Script

#### assign_quiz
* You can set up the input csv with the following required columns: **SIS_ID** (student id) and **assignment_id**
* If the canvas user id is available, this can be added under a column titled **ID**.
* A student under **SIS_ID** is assigned to the corresponding assignment under **assignment_id**.
* Alternatively, any file which has the required headers can be used as input for this script. All extra/unrecognized columns are ignored  
![Example input file for assign_quiz](https://github.com/Renu-R/documentation_images/blob/main/assign_quiz_sample.png)  
Fig 1: a sample input file for assign_quiz, the bolded column titles are required to run the script  
* To run the script, you can either use your terminal or drag and drop the input csv in the script file.
* When using the terminal, navigate to the folder which contains the local repository and type in `python3 assign_quiz.py [Enter you input file followed by .csv].` Make sure that the input file exits within your local repository folder.

### moderate_quiz
* You can set up the input csv with the following required columns: **SIS_ID** (student id) and **time**
* If the canvas user id is available, this can be added under a column titled **ID**.
* **SIS_ID** refers to the list of students you want to moderate. The **time** column refers to extra time you would like to add to a student's attempt. It can be in a multiplicative or additive form. For example, for a 90 min quiz, a multiplicative input of 1.5  would have the same effect as an additive input of 45 mins. Therefore, both 1.5 and 45 are valid inputs under the column.  
![Example input file for moderate_quiz](https://github.com/Renu-R/documentation_images/blob/main/moderate_sample.png)  
* To run the script, you can either use your terminal or drag and drop the input csv in the script file.
* When using the terminal, navigate to the folder which contains the local repository and type in `python3 moderate_quiz.py [Enter you input file followed by .csv].` Make sure that the input file exits within your local repository folder.

### edit_override
* You can set up the input csv with the following required columns: **SIS_ID** (student id).
* To run the script, you can either use your terminal or drag and drop the input csv in the script file.
* **SIS_ID** refers to the students you would like to add or delete from an override.
* If the canvas user id is available, this can be added under a column titled **ID**.
![Example input file for edit_override](https://github.com/Renu-R/documentation_images/blob/main/edit_override_sample.png)  
* When using the terminal, navigate to the folder which contains the local repository and type in `python3 edit_quiz.py [Enter you input file followed by .csv].` Make sure that the input file exits within your local repository folder.

### Notes
- The **Gradebook** from Canvas can be used as an input file for all of the scripts. Since it already has the user ids in it, there is no need to change the headers. You would only need to add the columns for **time** for **moderate_quiz** or **assignment_id** for **assign_quiz** depending on which script you wish to run.
