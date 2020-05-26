from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def my_home():
	return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
	return render_template(page_name)

def write_to_file(data):
    try:
        with open('database.txt', mode='a') as database:
            email = data["email"]
            subject = data["subject"]
            message = data["message"]
            file = database.write(f'\n{email},{subject},{message}')
            #want new line \n
    except IOError as err:
        print('IO error')
        raise err

def write_to_csv(data):
    #import csv module
    #we want to write headers for the columns
    #commas signify the end of a column (email,subject,message)
    with open('database.csv', mode='a', newline='') as database2:
            email = data["email"]
            subject = data["subject"]
            message = data["message"]
            csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            #csv_writer object = csv.writer(parameters)
            #(whereToWrite, optionParameter)
            #newline option - always add new line when we append
            #there is also a writeheader method but we already have the headers
            csv_writer.writerow([email,subject,message])
            #pass variables in as a list
            
@app.route('/submit_form', methods=['POST', 'GET'])
#we need to create the submit_form
#methods POST and GET are default
#GET means browser wants us to send info
#POST means browser wants us to save info
def submit_form():
    # return 'form submitted hooorayyy!'
    if request.method == 'POST':
    #need to import request
    	# data = request.form['message']
    	# #this is a way to grab different values
    	#an easy way to grab the info is the to_dict()
    	#method which turns the form data into a dictionary
        #add a try except block to catch errors
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            # print(data)
        	#on my backend (in terminal), I get this:
        	#{'email': 'blah@yahoo.com', 'subject': 'howdy', 'message': 'wow you are so cool'}
            return redirect('thankyou.html')
            #need to import redirect module
        except:
            return 'did not save to database'
    else:
    	return 'Something went wrong. Try again!'


#this is our submit form endpoint
#it isn't doing anything right now
#never calling this on the frontend on the browser
#how can we get it to work - on contact.html, what happens when we click the button

# # @app.route('/<username>/<int:post_id>')
# # #this <> is dynamic
# # #flask looks at this as something to pass
# # #on into the function
# # def hello_world(username=None, post_id=None):
# # 	return render_template('index.html', name=username, post_id=post_id)  
# # 	#can pass on the data with second parameter
# # 	#able to read the url and pass in data this way
# # 	#using {{}} in the html
# # 	#this makes our url very specific 
# # 	#http://127.0.0.1:5000/sally/6

# @app.route('/')
# def my_home():
# 	return render_template('index.html')

# @app.route('/<string:page_name>')
# def html_page(page_name):
# 	return render_template(page_name)
# 	#we want to render in the template the data
# 	#that was entered into the url

# #now to remove bugs:
# #components link shows up sometimes b/c
# #each page has the link, so remove from all pages

# #we want to make this more dynamic to avoid
# #copying and pasting code for each html page
# #we have our home route but want to do
# #something for the rest of the pages that is dynamic

# #<> this syntax allows us to dynamically accept
# #different url parameters

# # #my attempt to make the below code dynamic and not repetitious:
# # @app.route('/<page>')
# # def webpage(page=None):
# # 	return render_template(f'{page}', pagename=page)


# # @app.route('/index.html')
# # def home():
# # 	return render_template('index.html')

# # @app.route('/works.html')
# # def my_works():
# # 	return render_template('works.html')

# # @app.route('/work.html')
# # def my_work():
# # 	return render_template('work.html')

# # @app.route('/about.html')
# # def about():
# # 	return render_template('about.html')

# # @app.route('/contact.html')
# # def contact():
# # 	return render_template('contact.html')