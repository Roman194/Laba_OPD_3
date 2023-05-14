
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def start():
    return render_template("home.html")


@app.route('/add_file')
def about():
    return render_template("add_file.html")


@app.route('/add_file', methods=['post', 'get'])
def form():
    if request.method == 'POST':
        file = request.files['file_1']
        extension=file.filename
        if extension.endswith('.txt'):
            words = file.read().decode('utf-8').split()
        else:
            return render_template('add_file.html',result='Файл неподдерживаемого формата. Требуется:.txt Получено: '+extension)
        word_amounts={}
        for word in words:
            word=word.replace('.','').replace(',','').replace('!','').replace('?','').replace(';','').replace(':','').replace('-','').replace('(','').replace(')','')
            word_lwr=word.lower()
            print(word_lwr)
            if word_lwr in word_amounts:
                word_amounts[word_lwr] += 1
            else:
                word_amounts[word_lwr] = 1
        for amounts in word_amounts.items():

            if amounts[1]==max(word_amounts.values()):
                popular_world_key =amounts[0]
                popular_world = amounts[1]

    return render_template('add_file.html',result='В файле '+extension+' самое популярное слово "'+popular_world_key+'" встречается '+str(popular_world)+' раз')


if __name__ == '__main__':
    app.run(debug=True)


