@pytest.mark.parametrize('mi,expected', [(MultiIndex.from_tuples([(1, 2), (4, 5)]), np.array([True, True])), (MultiIndex.from_tuples([(1, 2), (4, 6)]), np.array([True, False]))])
def test_equals_op_multiindex(self, mi, expected):
    df = pd.read_csv(StringIO('a,b,c\n1,2,3\n4,5,6'), index_col=[0, 1])
    result = df.index == mi
    tm.assert_numpy_array_equal(result, expected)