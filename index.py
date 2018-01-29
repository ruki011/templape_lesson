from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    context = {
        'author': 'Тенембаун',
        'books': [
            {
                'title': 'Архитектура компьютера',
                'pages': 820
            },
            {
                'title': 'Архитектура компьютера',
                'pages': 820
            }
        ]
    }
    return render_template('home.html', **context)



@app.route('/books/')
def books():
    book_name ='Архитектура компьютера'
    return  render_template('books.html', book_name=book_name)




@app.route('/contact/')
@app.route('/contact/<phone>')
def contact(phone=None):
    if phone is None:
        phone = '9494949'
    return 'Мой телефон ' + phone



if __name__ == '__main__':
    app.run(debug =True)