# Options Pricing Engine

A **Python-based Options Pricing Engine** that supports **European and American options**, calculates **option Greeks**, and evaluates **portfolios of multiple options**. The project demonstrates a combination of **financial theory, numerical methods, and Python programming**.

---

## Features

- **European Options Pricing**
  - Black-Scholes analytical formula
  - Monte Carlo simulation

- **American Options Pricing**
  - Binomial Tree method

- **Greeks Calculation**
  - Delta, Gamma, Vega, Theta, Rho

- **Portfolio Analysis**
  - Supports multiple options (calls and puts)
  - Computes portfolio value based on option quantities

- **Interactive User Input**
  - Enter multiple options with different parameters
  - Compute individual option prices, Greeks, and total portfolio value

---

## Folder Structure
options_pricing/<br>
│<br>
├── src/<br>
│   ├── option.py           # Option class<br>
│   ├── models.py           # Pricing methods (Black-Scholes, Monte Carlo, Binomial Tree)<br>
│   ├── greeks.py           # Greeks calculation<br>
│   ├── portfolio.py        # Portfolio management<br>
│   └── utils.py            # Utility functions (optional: plotting, payoff calculations)<br>
│<br>
├── trial.py                # Interactive CLI script to price options and portfolios<br>
└── README.md<br>

## Usage

You will be prompted to enter:
	•	Number of options in your portfolio
	•	Stock price, strike price, time to maturity, risk-free rate, volatility
	•	Option type (call/put), exercise style (European/American), and quantity

The script will output:
	•	Individual option prices
	•	Option Greeks
	•	Total portfolio value


<img width="485" height="426" alt="image" src="https://github.com/user-attachments/assets/797884a4-2d2d-444a-bc83-1c30fd2cbc65" />


## Technologies
	•	Python 3.12+
	•	NumPy and SciPy for numerical calculations
	•	Plotly (optional) for interactive visualizations
	•	Modular, object-oriented design for easy extension
