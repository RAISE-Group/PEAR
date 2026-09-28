@pytest.mark.parametrize('df', [pytest.param(pd.DataFrame({'a': ['a', 'b']}), marks=[pytest.mark.filterwarnings('ignore')]), pd.DataFrame({'a': np.array([-1, 2], dtype=object)}), pd.DataFrame({'a': [Decimal('-1.0'), Decimal('2.0')]})])
def test_pos_object(self, df):
    tm.assert_frame_equal(+df, df)
    tm.assert_series_equal(+df['a'], df['a'])