class Option:
    def __init__(self, S, K, T, r, sigma, option_type, quantity=1):
        self.S = S
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma
        self.option_type = option_type
        self.quantity = quantity

    def payoff(self, ST):
        """Compute payoff at maturity for given stock price ST"""
        if self.option_type == 'call':
            return max(ST - self.K, 0)
        elif self.option_type == 'put':
            return max(self.K - ST, 0)
        else:
            raise ValueError("option_type must be 'call' or 'put'")