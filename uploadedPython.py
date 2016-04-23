from boto.mturk.connection import MTurkConnection
from boto.mturk.question import ExternalQuestion
import os

fileName = "hit.html"

######  CONFIGURATION PARAMETRS  ######

SANDBOX = True  # Select whether to post to the sandbox (using fake money), or live MTurk site (using REAL money)
HIT_URL = "https://arpita43.github.io/CrowdProgrammingPrj/hit.html"  # Provide the URL that you want workers to sent sent to complete you task

NUMBER_OF_HITS = 1  # Number of different HITs posted for this task
NUMBER_OF_ASSIGNMENTS = 10  # Number of tasks that DIFFERENT workers will be able to take for each HIT
LIFETIME = 60 * 60 * 24 * 2  # How long that the task will stay visible if not taken by a worker (in seconds)
REWARD = 0.05  # Base payment value for completing the task (in dollars)
DURATION = 60*10  # How long the worker will be able to work on a single task (in seconds)
APPROVAL_DELAY = 60*60*10  # How long after the task is completed will the worker be automatically paid if not manually approved (in seconds)


# HIT title (as it will appear on the public listing)
TITLE = 'Enter the event details from the poster'
# Description of the HIT that workers will see when deciding to accept it or not
DESCRIPTION = 'Enter the event details from the poster'
# Search terms for the HIT posting
KEYWORDS = ['Event', 'Poster', 'Mechanical Turk','Venue','Date', 'Time', 'Detail']


# Your Amazon Web Services Access Key (private)
AWS_ACCESS_KEY = 'xx' # <-- TODO: Enter your access key here
# Your Amazon Web Services Secret Key (private)
AWS_SECRET_KEY = 'yy' # <-- TODO: Enter your private key here

#######################################


def create_hits():
	if SANDBOX:
		mturk_url = 'mechanicalturk.sandbox.amazonaws.com'
		preview_url = 'https://workersandbox.mturk.com/mturk/preview?groupId='
	else:
		mturk_url = 'mechanicalturk.amazonaws.com'
		preview_url = 'https://mturk.com/mturk/preview?groupId='

	q = ExternalQuestion(external_url=HIT_URL, frame_height=800)
	conn = MTurkConnection(aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY, host=mturk_url)
	for i in range(0, NUMBER_OF_HITS):
		create_hit_rs = conn.create_hit(question=q, lifetime=LIFETIME, max_assignments=NUMBER_OF_ASSIGNMENTS, title=TITLE, keywords=KEYWORDS, reward=REWARD, duration=DURATION, approval_delay=APPROVAL_DELAY, annotation=DESCRIPTION)
		print(preview_url + create_hit_rs[0].HITTypeId)
		print("HIT ID: " + create_hit_rs[0].HITId)

def addBreak():
	return "</br>"

def addNewLine():
	return "\n"

def makeHTMLPage():
	f = open(fileName,"w") 
	f.write("<!DOCTYPE html>")
	f.write(addNewLine())
	f.write("<html>")
	f.write(addNewLine())
	f.write("<script src='//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js'></script>")
	f.write(addNewLine())
	f.write("<script src='/mturk.js'></script>")
	f.write(addNewLine())
	f.write("<body>")
	f.write(addNewLine())
	f.write("<h2>Add the venue, date and time of the event !!!</h2>")
	f.write(addBreak())
	f.write("<img src='http://i.imgur.com/PrIuXhg.jpg?1.jpg' alt='Poster Image' style='width:700px;height:650px;'>")
	f.write(addBreak())
	f.write(addBreak())
	f.write(addBreak())
	f.write("Enter the following details !!")
	f.write(addBreak())
	f.write(addBreak())
	f.write("Suggested Event Title: <input type = 'text' name = 'title' >")
	f.write(addBreak())
	f.write(addBreak())
	f.write("<form id = 'mturk_form' name = 'mturk' action = 'https://requestersandbox.mturk.com/mturk/externalSubmit' method = 'POST'>")
	f.write("Date: <input type='date' name='date' style = 'left: 1000px;'>")
	f.write(addBreak())
	f.write(addBreak())
	f.write("Time: <input type='time' name='time'>")
	f.write(addBreak())
	f.write(addBreak())
	f.write("Venue: <input type='text'  name = 'venue'>")
	f.write(addBreak())
	f.write(addBreak())
	f.write("Additional Details (Links, Contact Details): </br> <input type = 'text' name = 'details' style = 'width: 300px;'> ")
	f.write(addBreak())
	f.write(addBreak())
	f.write("<input type='submit' value='Submit'>")
	f.write("</form>")
	f.write("</body>")
	f.write("</html>")
	f.close()

def useGithub():
	#script to use github by python
	#os.chdir("github_repo")
	os.system("git init")
	os.system("git add hit.html")
	os.system("git commit -m 'adding hit.html'")
	os.system("git push --set-upstream origin gh-pages")


if __name__ == "__main__":
	makeHTMLPage()
	useGithub()
	create_hits()
