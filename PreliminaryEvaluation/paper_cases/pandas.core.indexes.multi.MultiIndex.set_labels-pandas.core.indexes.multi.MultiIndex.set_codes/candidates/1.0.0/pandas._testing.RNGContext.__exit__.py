def __exit__(self, exc_type, exc_value, traceback):
    np.random.set_state(self.start_state)