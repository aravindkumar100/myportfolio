from flask import Flask,render_template,url_for,request,redirect
import csv
app = Flask(__name__)


@app.route('/')
def home():
	return render_template('index.html')

@app.route('/<username>/<int:post_id>')

def hello_world(username=None,post_id=None):
	return render_template('home.html', name=username,id=post_id)


@app.route('/<string:page_name>')
def myweb(page_name):
	return render_template(page_name)

def writetodatabasefile(data):
	email = data['email']
	subject = data['subject']
	message = data['message']
	with open('database.txt','a') as file:
		new = file.write(f'\n{email}\n,{subject}\n,{message}\n')


def writetodatabasecsv(data):
	email = data['email']
	subject = data['subject']
	message = data['message']
	with open('database.csv',newline='',mode='a') as csvfile:
		writer = csv.writer(csvfile,delimiter=',',quotechar='"',quoting=csv.QUOTE_MINIMAL)
		writer.writerow([email,subject,message])



@app.route('/submit_form',methods=['POST','GET'])
def contactform():
	if request.method == 'POST':
		data= request.form.to_dict()
		writetodatabasecsv(data)
		return redirect('/thankyounote.html')
	else:
		return 'Something went wrong, Try again'
	
