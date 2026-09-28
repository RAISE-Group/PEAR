@cache_readonly
def m_offset(self):
    if self._prefix.endswith('S'):
        moff = MonthBegin(n=1, normalize=False)
    else:
        moff = MonthEnd(n=1, normalize=False)
    return moff