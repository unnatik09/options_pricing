import numpy as np
import plotly.graph_objects as go


# -------------------------------
# 1. Option Payoff Plot
# -------------------------------
def plot_payoff(S_range, payoff, title="Option Payoff"):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=S_range, y=payoff, mode='lines', line=dict(color='purple', width=3)))
    fig.update_layout(
        title=title,
        xaxis_title="Stock Price",
        yaxis_title="Payoff",
        template="plotly_white"
    )
    fig.show()


# -------------------------------
# 2. Option Profit Plot
# -------------------------------
def plot_profit(S_range, payoff, premium, title="Option Profit"):
    profit = payoff - premium
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=S_range, y=profit, mode='lines', line=dict(color='mediumvioletred', width=3)))
    fig.add_hline(y=0, line=dict(color='black', dash='dash'))
    fig.update_layout(
        title=title,
        xaxis_title="Stock Price",
        yaxis_title="Profit",
        template="plotly_white"
    )
    fig.show()


# -------------------------------
# 3. Greeks Plot
# -------------------------------
def plot_greeks(option, S_range):
    from greeks import delta, gamma, vega, theta, rho
    deltas = [delta(option, S) for S in S_range]
    gammas = [gamma(option, S) for S in S_range]
    vegas = [vega(option, S) for S in S_range]
    thetas = [theta(option, S) for S in S_range]
    rhos = [rho(option, S) for S in S_range]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=S_range, y=deltas, mode='lines', name='Delta', line=dict(color='purple')))
    fig.add_trace(go.Scatter(x=S_range, y=gammas, mode='lines', name='Gamma', line=dict(color='mediumorchid')))
    fig.add_trace(go.Scatter(x=S_range, y=vegas, mode='lines', name='Vega', line=dict(color='violet')))
    fig.add_trace(go.Scatter(x=S_range, y=thetas, mode='lines', name='Theta', line=dict(color='plum')))
    fig.add_trace(go.Scatter(x=S_range, y=rhos, mode='lines', name='Rho', line=dict(color='thistle')))

    fig.update_layout(
        title="Option Greeks vs Stock Price",
        xaxis_title="Stock Price",
        yaxis_title="Greeks Value",
        template="plotly_white"
    )
    fig.show()


# -------------------------------
# 4. Monte Carlo Simulation Paths
# -------------------------------
def plot_monte_carlo_paths(option, simulations=50, T=1, steps=50):
    from models import monte_carlo
    dt = T / steps
    paths = []
    S0 = option.S
    sigma = option.sigma
    r = option.r
    np.random.seed(42)

    for _ in range(simulations):
        S_path = [S0]
        for _ in range(steps):
            Z = np.random.normal()
            S_next = S_path[-1] * np.exp((r - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * Z)
            S_path.append(S_next)
        paths.append(S_path)

    fig = go.Figure()
    for path in paths:
        fig.add_trace(go.Scatter(y=path, mode='lines', line=dict(color='purple', width=1), opacity=0.5))
    fig.update_layout(
        title="Monte Carlo Simulated Stock Paths",
        xaxis_title="Time Steps",
        yaxis_title="Stock Price",
        template="plotly_white"
    )
    fig.show()


# -------------------------------
# 5. Portfolio Payoff Plot
# -------------------------------
def plot_portfolio_payoff(portfolio, S_range, title="Portfolio Payoff"):
    total_payoff = np.zeros_like(S_range)
    for pos in portfolio.positions:
        opt = pos['option']
        qty = pos['quantity']
        payoff = np.maximum(S_range - opt.K, 0) if opt.option_type == 'call' else np.maximum(opt.K - S_range, 0)
        total_payoff += qty * payoff

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=S_range, y=total_payoff, mode='lines', line=dict(color='purple', width=3)))
    fig.update_layout(
        title=title,
        xaxis_title="Stock Price",
        yaxis_title="Portfolio Payoff",
        template="plotly_white"
    )
    fig.show()