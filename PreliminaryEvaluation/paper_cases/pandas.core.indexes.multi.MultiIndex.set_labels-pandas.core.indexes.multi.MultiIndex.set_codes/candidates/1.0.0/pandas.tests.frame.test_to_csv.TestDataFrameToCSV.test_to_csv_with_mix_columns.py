def test_to_csv_with_mix_columns(self):
    df = DataFrame({0: ['a', 'b', 'c'], 1: ['aa', 'bb', 'cc']})
    df['test'] = 'txt'
    assert df.to_csv() == df.to_csv(columns=[0, 1, 'test'])