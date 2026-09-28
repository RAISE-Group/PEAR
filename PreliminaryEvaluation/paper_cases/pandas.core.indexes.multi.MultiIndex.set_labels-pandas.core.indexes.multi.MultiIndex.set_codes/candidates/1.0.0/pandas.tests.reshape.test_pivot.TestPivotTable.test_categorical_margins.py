@pytest.mark.xfail(reason='GH#17035 (np.mean of ints is casted back to ints)')
def test_categorical_margins(self, observed):
    df = pd.DataFrame({'x': np.arange(8), 'y': np.arange(8) // 4, 'z': np.arange(8) % 2})
    expected = pd.DataFrame([[1.0, 2.0, 1.5], [5, 6, 5.5], [3, 4, 3.5]])
    expected.index = Index([0, 1, 'All'], name='y')
    expected.columns = Index([0, 1, 'All'], name='z')
    table = df.pivot_table('x', 'y', 'z', dropna=observed, margins=True)
    tm.assert_frame_equal(table, expected)