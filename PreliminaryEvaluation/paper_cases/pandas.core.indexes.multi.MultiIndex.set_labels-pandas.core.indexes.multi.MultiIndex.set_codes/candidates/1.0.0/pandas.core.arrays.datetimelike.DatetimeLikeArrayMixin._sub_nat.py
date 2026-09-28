def _sub_nat(self):
    """
        Subtract pd.NaT from self
        """
    result = np.zeros(self.shape, dtype=np.int64)
    result.fill(iNaT)
    return result.view('timedelta64[ns]')