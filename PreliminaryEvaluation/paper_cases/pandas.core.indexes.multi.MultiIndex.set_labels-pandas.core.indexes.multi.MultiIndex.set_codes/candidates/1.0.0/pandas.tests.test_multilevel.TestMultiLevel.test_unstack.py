def test_unstack(self):
    unstacked = self.ymd.unstack()
    unstacked.unstack()
    self.ymd.astype(int).unstack()
    self.ymd.astype(np.int32).unstack()