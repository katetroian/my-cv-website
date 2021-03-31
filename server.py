from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

# @app.route('/<username>/<int:post_id>')
# def hello_world(username=None, post_id=None):
#     return render_template('index.html', name=username, post_id=post_id)
# set(for wind)(export) FLASK_ENV=development - debag mode

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

# def write_to_file(data):
# 	with open('db.txt', mode='a') as db:
# 		email = data['email']
# 		subj = data['subject']
# 		mess = data['message']
# 		file = db.write(f'\n{email}, {subj}, {mess}')

def write_to_csv(data):
	with open('database.csv', mode='a', newline='\r\n') as db:
		email = data['email']
		subj = data['subject']
		mess = data['message']
		csv_writer = csv.writer(db, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email, subj, mess])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			write_to_csv(data)
			return redirect('/thankyou.html')
		except:
			return 'Did not save t DB'
	else:
		return 'Smth went wrong'

    #return render_template('submit_form.html', error=error)