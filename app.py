from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Types of Sound Frequencies</title>
    </head>
    <body>
        <h1>Types of Sound Frequencies</h1>

        <h2>1. Infrasound</h2>
        <p>Infrasound refers to sound frequencies below the lower limit of human audibility (20 Hz).</p>

        <h2>2. Audible Sound</h2>
        <p>Audible sound frequencies range from 20 Hz to 20,000 Hz and are within the range of human hearing.</p>

        <h2>3. Ultrasound</h2>
        <p>Ultrasound refers to sound frequencies above the upper limit of human audibility (20,000 Hz).</p>
    </body>
    </html>
    '''


if __name__ == '__main__':
    app.run(debug=True)