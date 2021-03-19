# Intercom Activity Submission

## Problem 🌍 

We have some customer records in a text file (customers.txt) -- one customer per line, JSON lines formatted. We want to invite any customer within 100km of our Dublin office for some food and drinks on us. Write a program that will read the full list of customers and output the names and user ids of matching customers (within 100km), sorted by User ID (ascending).

## Installation instructions 👩‍💻 
The project is written in **python 3**. Please follow the below instructions to install Python on your machine.

Download the project using
```bash
git clone https://github.com/uddish/intercom.git
```

### New to Python?

**Pssst... Do you use a Mac?** 👩‍💻 

*Option 1*
- Use Homebrew to install python -> ```brew install python```
- Don't have homebrew installed? [Go to the Install Homebrew section](https://brew.sh/)

*Option 2*
- You can also use the official python installer. [Check this](https://www.python.org/downloads/mac-osx/).

*Option 3*
- Still not sure how to install Python. [Follow this extensive guide](https://realpython.com/installing-python/#how-to-install-python-on-macos) 

**Are you a windows user?** 🖥

*Option 1*
- Use the official [Python installer](https://www.python.org/downloads/windows/). 

*Option 2*
- Still stuck? Follow this [extensive guide](https://realpython.com/installing-python/#how-to-check-your-python-version-on-windows) 

**Linux and Other Platforms?** 💻
- Install python on **Linux** by following this [guide](https://realpython.com/installing-python/#how-to-install-python-on-linux) 
- Install python on **other platforms**. [Check this link](https://www.python.org/download/other/)

### Already have Python installed, don't forget to check the version.

```bash
python --version
```

## Let's talk about the Project Structure 📄 
- The project contains a **main.py** file that acts as the entry point to the program.
- There is a sample **customers.txt** file that is used to read the customer data.
- The output generated is stored in a separate **output.txt** file. 
- The Project contains a **services** folder.
- All the logic related to reading/writing to the files can be found inside **input_output_service.py**
- All the logic related to calculating the distance between the customer and the Intercom office can be found inside **customer_invitation_service.py**
- There is a separate **tests** folder that contains the code related to running the Unit Tests.
- **test.py** contains all the unit tests logic.
- Unit tests have their own input/output files which can also be found inside the **tests** folder.


## Unit Tests are important. Let's see how we can run them 👩‍🏫 
Make sure that you are in the root **/intercom** folder.

Try running the below command to run the Test Cases
```bash
python -m unittest tests/test.py
```
Here, **tests** is the directory where all the test cases and the corresponding input/output files are present.   
**test.py** is the actual file that is being executed. 


## It's time. Let's run the program 💻 .

The project has a sample **customers.txt** file which will be used to read the customer data.

Make sure that you are in the root **/intercom** folder.   

Run the below command to execute the program.
```bash
python main.py
```
Stay with me, let's look at the output 😃   
Check the **output.txt** file to look for the desired output.

## Stuck somewhere?
Please feel free to reach out to me here:
[Uddish Verma](mailto:uddishverma22@gmail.com)
