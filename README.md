# Word Counter 

 This is a program for obtaining a list of word frequencies from files containing lecture material for the QA Automation class.

## Software
- You need to install "_git_" to get the source of the project. You can install git from the official site -> [Download Git](https://git-scm.com/downloads)

- If you want run the program through the file "_count.py_" you need to install python.
You can download python using the follow link -> [Download Python](https://www.python.org/downloads/)

- You will also need "_pipenv_" in order to quickly set up the necessary environment for the program to work. You can install it with the following command: `pip install pipenv`

### How to create .exe file 
You need to open cmd (command prompt)  from the root of the repository where the project is located. Run a command  `pip install pyinstaller`  that will install the package to generate an exe file with it. After installation, run the following command where instead of <_YOURFILE.py_> specify the name of your project file.

`pyinstaller --onefile <YOURFILE.py>`

That's all, go to the dist folder where there will be an _.exe_ file that will be called the same as <_YOURFILE.py_>
### Used packages
#### This program uses the following packages:
* pandas
* tkinter
* os
* Presentation
* docx
* PdfFileReader
* datetime

## How to use?

First you need to get the repo from git. For this you need to open git bash on local empty directoryand type:

`git clone https://github.com/9Mikhail9/python_qa_mykhail.git`

After that the repository is cloned, type  `pipenv install`  in to install all required packages.

Open the application "Word Coater.exe".The program will open.An open application should have: an input field, selected file formats for reading and an information field about the program's work performed.
In the input field, you must enter the path to the directory with the files you want to process.Choose the file format you want to use.After pressing the button in the information field, you will see information about the work performed by the program (what files it processed and where the report is located).
The report is saved in the same directory where the files were located but in the "Report Catalog" folder. The folder "Report Catalog" does not need to be created, it will be created automatically or if it already exists, the report will appear in it. The report is saved in .xlsx format with the name "Report", after the name there may be a number if this name is taken.
On the first page of the report, you will see what files were used, the date and time when the report was created.The second page contains a list of words and the number of occurrences of each word in the selected files.