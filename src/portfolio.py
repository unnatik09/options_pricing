from typing import List
from option import Option
from models import black_scholes
from greeks import delta, gamma, vega, theta, rho

class Portfolio:
    def __init__(self):
        self.positions: List[Option] = []

    def add_option(self, option: Option, quantity=1):
        self.positions.append({'option': option, 'quantity': quantity})

    def remove_option(self, index):
        self.positions.pop(index)

    def total_value(self):
        total = 0
        for pos in self.positions:
            option = pos['option']
            qty = pos['quantity']
            total += black_scholes(option) * qty
        return total

    def portfolio_greeks(self):
        greeks = {'Delta': 0, 'Gamma': 0, 'Vega': 0, 'Theta': 0, 'Rho': 0}
        for pos in self.positions:
            option = pos['option']
            qty = pos['quantity']
            greeks['Delta'] += delta(option) * qty
            greeks['Gamma'] += gamma(option) * qty
            greeks['Vega']  += vega(option)  * qty
            greeks['Theta'] += theta(option) * qty
            greeks['Rho']  += rho(option)   * qty
        return greeks