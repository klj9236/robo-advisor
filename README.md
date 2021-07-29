# robo-advisor
Setup

Repo Setup

Use the GitHub.com online interface to create a new remote project repository called something like "robo-advisor". When prompted by the GitHub.com online interface, let's get in the habit of adding a "README.md" file and a Python-flavored ".gitignore" file (and also optionally a "LICENSE") during the repo creation process. After this process is complete, you should be able to view the repo on GitHub.com at an address like https://github.com/YOUR_USERNAME/robo-advisor.

After creating the remote repo, use GitHub Desktop software or the command-line to download or "clone" it onto your computer. Choose a familiar download location like the Desktop.

After cloning the repo, navigate there from the command-line:

``cd ~/Desktop/robo-advisor

Use your text editor or the command-line to create a new sub-directory called "app" with a file called "robo_advisor.py", and then place inside some example print statements like the following:

# this is the "app/robo_advisor.py" file

print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print("LATEST DAY: 2018-02-20")
print("LATEST CLOSE: $100,000.00")
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")
Make sure to save Python files like this whenever you're done editing them. After setting up a virtual environment, we will be ready to run this file.

Use your text editor or the command-line to create a new file called "requirements.txt" in the root directory of your repository, and then place inside the following contents:

# this is the "requirements.txt" file
# it might be helpful to use pandas. if you do, uncomment the last line below ...

requests
python-dotenv
# pandas 
After setting up a virtual environment, we will be ready to install these packages.

Environment Setup

Create and activate a new Anaconda virtual environment:

conda create -n stocks-env python=3.8 # (first time only)
conda activate stocks-env
From within the virtual environment, install the required packages specified in the "requirements.txt" file you created:

pip install -r requirements.txt
From within the virtual environment, demonstrate your ability to run the Python script from the command-line:

``python app/robo_advisor.py
