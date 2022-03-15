from flask import Flask, url_for
import os
from waitress import serve


app = Flask(__name__)

frazes = ['Человечество вырастает из детства.',
          'Человечеству мала одна планета.',
          'Мы сделаем обитаемыми безжизненные пока планеты.',
          'И начнем с Марса!',
          'Присоединяйся!']


@app.route('/')
def mission():
    return "Миссия Колонизация Марса"


@app.route('/index')
def motto():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return '<br>'.join(frazes)


@app.route('/image_mars')
def red_planet():
    return f'<title>Привет, Марс!</title>' \
           f'<h1>Жди нас, Марс!</h1>' \
           f'''<img src="{url_for("static", filename="img/mars.png")}"
           alt="здесь Марс" width="300" height="300">
           <br>Вот она какая, красная планета.'''


@app.route('/promotion_image')
def color_strings():
    url_pic = url_for('static', filename='img/mars.png')
    url_style = url_for('static', filename='css/style.css')
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{}" />
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{}" alt="Здесь Марс" width="300" height="300">
                    <div class="alert-dark" role="alert">
                      <br><h3>{}</h3>
                    </div>
                    <div class="alert-success" role="alert">
                      <br><h3>{}</h3>
                    </div>
                    <div class="alert-secondary" role="alert">
                      <br><h3>{}</h3>
                    </div>
                    <div class="alert-warning" role="alert">
                      <br><h3>{}</h3>
                    </div>
                    <div class="alert-danger" role="alert">
                      <br><h3>{}</h3>
                    </div>
                  </body>
                </html>""".format(url_style, url_pic, *frazes)


if __name__ == '__main__':
   
    port = int(os.environ.get("PORT", 5000))
    serve(app, host='0.0.0.0', port=port)
