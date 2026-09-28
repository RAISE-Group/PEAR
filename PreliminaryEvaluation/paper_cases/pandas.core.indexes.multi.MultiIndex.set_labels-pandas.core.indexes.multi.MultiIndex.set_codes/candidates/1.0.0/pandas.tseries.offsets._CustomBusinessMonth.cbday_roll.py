@cache_readonly
def cbday_roll(self):
    """
        Define default roll function to be called in apply method.
        """
    cbday = CustomBusinessDay(n=self.n, normalize=False, **self.kwds)
    if self._prefix.endswith('S'):
        roll_func = cbday.rollforward
    else:
        roll_func = cbday.rollback
    return roll_func