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

### Runnng a Python Script

#### assign_quiz
* You can paste your input values into our data.csv file under the corresponding headers. 
* The **ID** column refers to the **user ids** and **assignment_id** refers to the **assignment id**. Note that student ids are different from user ids and assignment ids are different from quiz ids.
* Alternatively, any file which has the same headers as the data.csv file can be used as input for this script. All extra/unrecognized columns are ignored
* To run the script, you can either use your terminal or drag and drop the input csv in the script file.
* When using the terminal, navigate to the folder which contains the local repository and type in `python3 assign_quiz.py data.csv` (or whatever the name of your input file may be). Make sure that the input file exits within your local repository folder.

