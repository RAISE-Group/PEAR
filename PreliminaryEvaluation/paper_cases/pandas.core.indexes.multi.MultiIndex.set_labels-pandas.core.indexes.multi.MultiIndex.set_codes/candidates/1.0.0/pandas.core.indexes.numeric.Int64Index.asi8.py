@property
def asi8(self) -> np.ndarray:
    return self.values.view('i8')