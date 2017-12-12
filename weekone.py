import requests
from flask import Flask, render_template, url_for, request, redirect, flash, make_response, abort
from logging import DEBUG

from flask_wtf import Form
from wtforms.fields import StringField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, email
app = Flask(__name__)
app.config['SECRET_KEY'] = b'\xb7\xd8\xa0\x8b\x82\r\xa4W\xb00\x13s\x00\x1e\xd6hT\xc3F@3\xff<\x1e'

app.logger.setLevel(DEBUG)

inputs=[]

def store_input(name,email):
	inputs.append(dict(
		name = name,
		email = email))


# Task 1: Say Hello world
@app.route('/')
def task1():
	return 'Hello World Karthik'


# Task 2.a: fetches a list of authors
@app.route('/users')
def task2a():
	authors,posts={},{}
	# Task 2.a: fetches a list of authors
	authors_url = 'https://jsonplaceholder.typicode.com/users'
	author_data= requests.get(authors_url).json()
	for i in author_data:
		authors[i['id']]=i['name']
	return render_template('users.html',authors=authors)


# Task 2.b: fetches a list of posts
@app.route('/posts')
def task2b():
	posts_url = 'https://jsonplaceholder.typicode.com/posts'
	posts_data= requests.get(posts_url).json()
	posts =[]
	for i in posts_data:
		posts.append(i['title'])
	return render_template('posts.html',posts=posts)


#Task 3: Return A list of authors and the count of their posts
@app.route('/authors')
def task2c():
	authors,posts={},{}
	author_data= requests.get('https://jsonplaceholder.typicode.com/users').json()
	for i in author_data:
		authors[i['id']]=i['name']

	posts_data= requests.get('https://jsonplaceholder.typicode.com/posts').json()
	for i in posts_data:
		if i['userId'] not in posts:
			posts[i['userId']] = [i['title']]
		else:
			posts[i['userId']].append(i['title'])

	authors_posts_count=[]
	number_of_authors=len(authors)
	for i in range(1,number_of_authors+1):
		authors_posts_count.append([authors[i],len(posts[i])])
	return render_template('authors.html',authors_n_posts = authors_posts_count) 


#Task 3: Setting a Cookie
@app.route('/setcookie')
def task3():
	resp = make_response(render_template('setcookie.html'))
	resp.set_cookie('name', b'Karthik')
	resp.set_cookie('age', b'26')
	return resp


# Task 4: Display the stored cookies
@app.route('/getcookies')
def task4():
	name=request.cookies.get('name')
	age=request.cookies.get('age')
	return render_template('getcookies.html',name = name, age = age)

# Task 5: Deny requests to robots.txt
@app.route('/robots.txt')
def task5():
	abort(401)

# Task 6: Rendering Html page
@app.route('/html')
def task6():
	return render_template('html.html')


class InputForm(Form):
	"""docstring for InputForm"""
	name = StringField('name', validators = [DataRequired()])
	email = EmailField('email', validators = [DataRequired(), email()])	


@app.route('/input',methods=['GET','POST'])
def task7():
	form = InputForm()
	if form.validate_on_submit():
		name = form.name.data
		email = form.email.data
		store_input(name, email)
		#logging the input to stdout
		app.logger.debug('Submitted Successfully :-)\nName: '+name +'\nEmail : '+ email)
		print('Submitted Successfully :-)\nName: '+name +'\nEmail : '+ email)
		flash('Submitted Successfully :-) Name: '+name +' | Email : '+ email)
		return redirect(url_for('task6'))
	return render_template('input.html',form = form)


@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'), 404

@app.errorhandler(401)
def access_denied(e):
	return render_template('401.html'), 401

if __name__ == '__main__':
	app.run(debug = True)
