def _values_for_factorize(self) -> Tuple[np.ndarray, Any]:
    return (self.to_numpy(na_value=np.nan), np.nan)