**HPDF WEEK ONE TASK**
------------------


----------


### Requirements




 Python 3,
 pip, flask


----------


### Installation Instructions
Download python from https://www.python.org/downloads/release/python-363/ and install.
Add path in environment variables in windows System Settings as `C:\Python363\` and `C:\Python363\scripts`.
Download pip from https://bootstrap.pypa.io/get-pip.py and run the script.

Goto command prompt and run these commands

    pip install virtualenv
    pip install virtualenvwrapper-win

Create a virtualenv :

 

    mkvirtualenv project_name

 Now virtual environment is active  and anything we install now will be specific to this project and install Flask and other frameworks by running these commands in command prompt

 

    pip install flask
    pip install flask-wtf
    pip install requests
     

Create a folder and change Directory
 

    mkdir folder_name
    cd folder_name
    setprojectdir .

Now clone this Repository in this directory and run the application with this command in cmd

    python weekone.py


----------


### Tasks:


For execution of tasks access the urls in your browser.

1. A simple hello-world at http://localhost:8080/ that displays a simple string like "Hello World"

		http://localhost:5000

2. Add a route, for e.g. http://localhost:8080/authors, which:

	a. Fetches a list of authors from a request to https://jsonplaceholder.typicode.com/users

		http://localhost:5000/users

	b. Fetches a list of posts from a request to https://jsonplaceholder.typicode.com/posts

		http://localhost:5000/posts

	c. Respond with only a list of authors and the count of their posts (a newline for each author).

		http://localhost:5000/authors

3. Set a simple cookie (if it has not already been set) at http://localhost:8080/setcookie with the following values: name=<your-first-name> and age=<your-age>.

	    http://localhost:5000/setcookie

4. Fetch the set cookie with http://localhost:8080/getcookies and display the stored key-values in it.

		http://localhost:5000/getcookies

5. Deny requests to your http://localhost:8080/robots.txt page. (or you can use the response at http://httpbin.org/deny if needed)

		http://localhost:5000/robots.txt

6. Render an HTML page at http://localhost:8080/html or an image at http://localhost:8080/image

		http://localhost:5000/html

7. A text box at http://localhost:8080/input which sends the data as POST to any endpoint of your choice. This endpoint should log the received the received to stdout.

		http://localhost:5000/input
