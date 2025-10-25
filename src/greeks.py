import numpy as np
from scipy.stats import norm
from option import Option

def delta(option: Option):
    S, K, T, r, sigma = option.S, option.K, option.T, option.r, option.sigma
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    return norm.cdf(d1) if option.option_type == 'call' else norm.cdf(d1) - 1

def gamma(option: Option):
    S, K, T, r, sigma = option.S, option.K, option.T, option.r, option.sigma
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    return norm.pdf(d1) / (S * sigma * np.sqrt(T))

def vega(option: Option):
    S, K, T, r, sigma = option.S, option.K, option.T, option.r, option.sigma
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    return S * norm.pdf(d1) * np.sqrt(T)

def theta(option: Option):
    S, K, T, r, sigma = option.S, option.K, option.T, option.r, option.sigma
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    if option.option_type == 'call':
        return (-S * norm.pdf(d1) * sigma / (2 * np.sqrt(T))
                - r * K * np.exp(-r * T) * norm.cdf(d2))
    else:
        return (-S * norm.pdf(d1) * sigma / (2 * np.sqrt(T))
                + r * K * np.exp(-r * T) * norm.cdf(-d2))

def rho(option: Option):
    S, K, T, r, sigma = option.S, option.K, option.T, option.r, option.sigma
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return K * T * np.exp(-r * T) * norm.cdf(d2) if option.option_type == 'call' else -K * T * np.exp(-r * T) * norm.cdf(-d2)