@cache_readonly
def reconstructed_codes(self) -> List[np.ndarray]:
    return [np.r_[0, np.flatnonzero(self.bins[1:] != self.bins[:-1]) + 1]]