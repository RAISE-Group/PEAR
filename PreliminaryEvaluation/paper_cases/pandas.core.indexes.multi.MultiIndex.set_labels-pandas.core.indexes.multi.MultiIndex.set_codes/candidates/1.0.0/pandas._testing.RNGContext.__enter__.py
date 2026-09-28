def __enter__(self):
    self.start_state = np.random.get_state()
    np.random.seed(self.seed)