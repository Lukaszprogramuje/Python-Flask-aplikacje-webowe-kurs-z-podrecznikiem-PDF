from flask import Flask, render_template, url_for, request, flash

app = Flask(__name__)

app.config['SECRET_KEY'] = 'SomethingSecret'

class Currency:
    def __init__(self, code, name, flag):
        self.code = code
        self.name = name
        self.flag = flag
    
    def __repr__(self):
        return '<Currency: {}>'.format(self.code)

class CantorOffer:
    def __init__(self):
        self.currencies = []
        self.denied_codes = []

    def load_offer(self):
        self.currencies.append(Currency('USD', 'Dolar', 'dolar.jpg'))
        self.currencies.append(Currency('EUR', 'Euro', 'euro.jpg'))
        self.currencies.append(Currency('GBP', 'Funt', 'funt.jpg'))
        self.denied_codes.append('USD')
    
    def get_by_code(self, code):
        for currency in self.currencies:
            if currency.code == code:
                return currency
        return Currency('unknown', 'unknown', 'cantor.jpg')

@app.route('/')
def index():

    return 'index'

@app.route('/exchange', methods=['GET', 'POST'])
def exchange():

    offer = CantorOffer()
    offer.load_offer()
    if request.method == 'GET':
        return render_template('exchange.html', offer=offer) 
    else:
        flash('Debug in POST mode')
        currency = 'EUR'
        if 'currency' in request.form:
            currency = request.form['currency']
        
        if currency in offer.denied_codes:
            flash('The currency {} is not accepted.'.format(currency))
        elif offer.get_by_code(currency) == 'unknown':
            flash('The currency is unknown')
        else:
            flash('Request to exchange {} is accepted.'.format(currency))
        
        amount = 100
        if 'amount' in request.form:
            amount = request.form['amount']

        return render_template('exchange_results.html', currency=currency, amount=amount, 
                                    currency_info=offer.get_by_code(currency))
        

