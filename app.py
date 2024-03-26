from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World from Jacob Korba! This is my first code change'

@app.route('/about')
def about():  # put application's code here
    return render_template('about.html')

@app.route('/about-css')
def aboutcss():  # put application's code here
    return render_template('about-css.html')

@app.route('/hello')
def hello():  # put application's code here
    return render_template('hello.html')

@app.route('/favorite-course')
def favcourse():  # put application's code here
    return render_template('favorite-course.html')

@app.route('/contact', methods=['GET','POST'])
def contact():  # put application's code here
    if request.method == 'POST':
        return render_template('contact.html', form_submitted=True)
    else:
        return render_template('contact.html')

@app.route('/base')
def base():  # put application's code here
    return render_template('base.html')

if __name__ == '__main__':
    app.run()
