def _shape(self, df: pd.DataFrame) -> Tuple[int, int]:
    """
        Calculate table chape considering index levels.
        """
    row, col = df.shape
    return (row + df.columns.nlevels, col + df.index.nlevels)