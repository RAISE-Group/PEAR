def _construct_result(self, result) -> 'DataFrame':
    """
        Wrap the result of an arithmetic, comparison, or logical operation.

        Parameters
        ----------
        result : DataFrame

        Returns
        -------
        DataFrame
        """
    out = self._constructor(result, index=self.index, copy=False)
    out.columns = self.columns
    return out