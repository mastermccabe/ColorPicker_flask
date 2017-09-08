from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html",phrase="hello",times = 5)


@app.route('/', methods=['POST'])
def change_color():
    # name = request.form['name_val']
    red_color = request.form['red_color']

    green_color = request.form['green_color']

    blue_color = request.form['blue_color']

    
    # Here's the line that changed. We're rendering a template from a post route now.
    return render_template('index.html', red_color =red_color, green_color = green_color, blue_color= blue_color)

#
# def hello_world():
#     return render_template('index.html')
#
# @app.route('/projects')
# def success():
#     return render_template('projects.html')
#
# @app.route('/about')
# def hello():
#     return render_template('about.html')


app.run(debug=True)
