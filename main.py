import requests

class Currency:
    """Class to change currency to PLN with fetch data from NBP API http://api.nbp.pl/"""
    def __init__(self, currency:str):
        self.currency = currency

    def show_rate(self):
        """Function to show actual exchange rate"""
        url = 'http://api.nbp.pl/api/exchangerates/rates/a/' + self.currency
        response = requests.get(url)
        data = response.json()
        rate = data['rates'][0]['mid']
        return  rate
    
    #create function to show actual exchange rate
    def to_pln(self, amount):
        """Function to change currency to PLN"""
        return amount * self.show_rate()


def main():
    #create object with currency code
    currency = Currency('usd')

    #show actual exchange rate
    print(currency.show_rate())

    #change currency to PLN
    print(currency.to_pln(99))

if __name__ == '__main__':
    main()