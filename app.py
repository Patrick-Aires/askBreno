from flask import Flask, render_template
from flask_ask import Ask, statement, question, convert_errors

app = Flask(__name__)
ask = Ask(app, '/')

@ask.launch
def start_skill():
    welcome_message = 'Fala meu chegado, seja bem-vindo!'
    return statement(welcome_message)

@ask.intent('HelloIntent')
def hello(firstname):
    text = render_template('hello', firstname=firstname)
    return statement(text).simple_card('Hello', text)

@ask.intent('AgredirLeoIntent')
def leo():
    text = 'Toma soco Leo'
    return statement(text)

@ask.intent('AgredirIntent', convert={'person': str})
def hit(person):
    if person in convert_errors:
        return question('Poderia repetir o nome de quem deseja agredir?')
    
    if person is None:
        return question('Quem você deseja agredir?')

    return statement('Vou te encher de porrada {}, tome!'.format(person))


if __name__ == '__main__':
    app.run(debug=True)