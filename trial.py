import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# trial.py
from option import Option
from models import black_scholes, binomial_tree, monte_carlo
from greeks import delta, gamma, vega, theta, rho
from portfolio import Portfolio

portfolio = Portfolio()
num_options = int(input("How many options do you want to add to the portfolio? "))

for i in range(num_options):
    print(f"\n--- Option {i+1} ---")
    S = float(input("Stock price (S): "))
    K = float(input("Strike price (K): "))
    T = float(input("Time to maturity (T, in years): "))
    r = float(input("Risk-free rate (r, e.g., 0.05): "))
    sigma = float(input("Volatility (sigma, e.g., 0.2): "))
    option_type = input("Option type ('call' or 'put'): ").lower()
    quantity = int(input("Quantity: "))
    exercise_type = input("Exercise type ('european' or 'american'): ").lower()

    # Create option
    opt = Option(S=S, K=K, T=T, r=r, sigma=sigma, option_type=option_type)

    # Price option
    if exercise_type == "european":
        price_bs = black_scholes(opt)
        price_mc = monte_carlo(opt)
        print(f"European Option Black-Scholes Price: {price_bs:.2f}")
        print(f"European Option Monte Carlo Price: {price_mc:.2f}")
        option_price = price_bs
    elif exercise_type == "american":
        price_bt = binomial_tree(opt, steps=50)
        print(f"American Option Binomial Tree Price: {price_bt:.2f}")
        option_price = price_bt

    # Print Greeks
    print("Greeks:")
    print(f"Delta: {delta(opt):.4f}")
    print(f"Gamma: {gamma(opt):.4f}")
    print(f"Vega: {vega(opt):.4f}")
    print(f"Theta: {theta(opt):.4f}")
    print(f"Rho: {rho(opt):.4f}")

    # Add to portfolio
    portfolio.add_option(opt, quantity)

# -------------------------------
# Compute total portfolio value
# -------------------------------
total_value = 0
for pos in portfolio.positions:
    opt = pos['option']
    qty = pos['quantity']
    if pos['option'].option_type == 'call':
        price = black_scholes(opt)
    else:
        price = binomial_tree(opt, steps=50)
    total_value += price * qty

print(f"\nTotal portfolio value: {total_value:.2f}")