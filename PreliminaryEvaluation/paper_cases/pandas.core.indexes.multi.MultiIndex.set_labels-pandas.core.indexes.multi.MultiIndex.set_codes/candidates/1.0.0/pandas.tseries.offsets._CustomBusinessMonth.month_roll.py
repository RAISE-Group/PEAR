@cache_readonly
def month_roll(self):
    """
        Define default roll function to be called in apply method.
        """
    if self._prefix.endswith('S'):
        roll_func = self.m_offset.rollback
    else:
        roll_func = self.m_offset.rollforward
    return roll_func