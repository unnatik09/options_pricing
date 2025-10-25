import numpy as np
from scipy.stats import norm
from option import Option


def black_scholes(option: Option):
    """
    Computes Black-Scholes price for European call or put option.
    """
    S = option.S
    K = option.K
    T = option.T
    r = option.r
    sigma = option.sigma

    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option.option_type == 'call':
        price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option.option_type == 'put':
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("option_type must be 'call' or 'put'")

    return price


def binomial_tree(option: Option, steps=100):
    S, K, T, r, sigma = option.S, option.K, option.T, option.r, option.sigma
    dt = T / steps
    u = np.exp(sigma * np.sqrt(dt))
    d = 1 / u
    p = (np.exp(r * dt) - d) / (u - d)

    # Initialize asset prices at maturity
    ST = np.array([S * (u ** j) * (d ** (steps - j)) for j in range(steps + 1)])

    # Option values at maturity
    if option.option_type == 'call':
        option_values = np.maximum(ST - K, 0)
    else:
        option_values = np.maximum(K - ST, 0)

    # Step back through tree
    for i in range(steps - 1, -1, -1):
        option_values = np.exp(-r * dt) * (p * option_values[1:i + 2] + (1 - p) * option_values[0:i + 1])
        if option.option_type in ['call', 'put']:  # American exercise
            ST = ST[:i + 1] / u
            if option.option_type == 'call':
                option_values = np.maximum(option_values, ST - K)
            else:
                option_values = np.maximum(option_values, K - ST)

    return option_values[0]


def monte_carlo(option: Option, num_simulations=100000, seed=42):
    """
    Monte Carlo pricing for European call/put options
    """
    np.random.seed(seed)

    S, K, T, r, sigma, r = option.S, option.K, option.T, option.r, option.sigma, option.quantity
    # Simulate end-of-period stock prices
    ST = S * np.exp((r - 0.5 * sigma ** 2) * T + sigma * np.sqrt(T) * np.random.randn(num_simulations))

    # Compute payoff
    if option.option_type == 'call':
        payoffs = np.maximum(ST - K, 0)
    else:  # put
        payoffs = np.maximum(K - ST, 0)

    # Discount back to present
    price = np.exp(-r * T) * np.mean(payoffs)
    return price