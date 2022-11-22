from flask import Flask, request, url_for, redirect
import os

app=Flask(__name__)

@app.route('/')
def index():

    menu = f'''
        <h1>strona główna</h1><br>
        link 1 <a href="{url_for('exchange')}">wymiana walut</a><br>
        <a href="{url_for('cantor', currency='USD', amount=50)}">szybka wymiana 50$</a><br>
        <img src="{url_for('static', filename='dolar.jpg')}"><br>
        <img src="{url_for('static', filename='currencies/euro.jpg')}"><br>
        {os.path.join(app.static_folder, 'currencies/euro.jpg')}
    '''
    return menu

@app.route('/cantor/<string:currency>/<int:amount>')
def cantor(currency, amount):    #nazwy muszą się zgadzac
    message = f'<h1>you selected {currency} and amount {amount}</h1>'
    return message

@app.route('/exchange',  methods=['GET', 'POST'])
def exchange():

    if request.method == 'GET':
        body = '''
            <form id="exchange_form" action="/exchange" method="POST">
                <label for="currency">Currency</label>
                <input type="text" id="currency" name="currency" value="EUR"><br>
                <label for="amount">Amount</label>
                <input type="text" id="amount" name="amount" value="100"><br>
                <input type="submit" value="Send">
            </form>
        '''
        return body
    else:
        currency = 'EUR'
        if 'currency' in request.form:
            currency = request.form['currency']
        
        amount = 100
        if 'amount' in request.form:
            amount = request.form['amount']
        
        body = f'you want to exchange {amount} {currency}'

        return redirect(url_for('cantor', currency=currency, amount=amount))


@app.route('/exchange_process', methods=['POST'])
def exchange_process():

    currency = 'EUR'
    if 'currency' in request.form:
        currency = request.form['currency']
    
    amount = 100
    if 'amount' in request.form:
        amount = request.form['amount']
    
    body = f'you want to exchange {amount} {currency}'

    return body


@app.route('/about')
def about(): 
    a = 10
    b = 10
    return 'about{}'.format(a/b)


if __name__ == '__main__':
    app.run(debug=True)
