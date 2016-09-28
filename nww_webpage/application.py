from flask import Flask, render_template

application = Flask(__name__)


# home page
@application.route('/')
def index():
    return render_template('index.html')

# # about page
# @application.route('/about')
# def about():
#     return render_template('about.html')

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=8080, debug=True)
