from flask import Flask, render_template, redirect, request

from secret_santa import return_santa_list

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():

	if request.method == 'GET':

		return render_template(
			'index.html', people_list=None
		)

	else:

		return render_template(
			'index.html', 
			people_list=return_santa_list(request.form['people_list'].split('\n'))
		)


@app.errorhandler(404)
def page_not_found(error):
	return redirect('/')


if __name__ == '__main__':
	app.run()