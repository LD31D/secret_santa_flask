from flask import Flask, render_template, redirect, request

from secret_santa import return_santa_list

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
	return render_template(
		'index.html', people_list=None
	)



@app.route('/get-list/', methods=['POST'])
def get_list():
	return render_template(
			'list.html', 
			people_list=return_santa_list(request.form['people_list'].split('\n'))
		)


@app.errorhandler(404)
def page_not_found(error):
	return redirect('/')


@app.errorhandler(405)
def page_not_found(error):
	return redirect('/')


if __name__ == '__main__':
	app.run()
