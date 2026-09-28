@pytest.mark.parametrize('df', [_integer, _integer2, _integer * np.random.randint(0, 2, size=np.shape(_integer)), _frame, _frame2, _mixed, _mixed2])
def test_arithmetic(self, df):
    kinds = {x.kind for x in df.dtypes.values}
    should = len(kinds) == 1
    self.run_frame(df, df, run_binary=should)