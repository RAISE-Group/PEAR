@pytest.mark.parametrize('names', [['a', ('b', 'c')], [('a', 'b'), 'c']])
def test_crosstab_tuple_name(self, names):
    s1 = pd.Series(range(3), name=names[0])
    s2 = pd.Series(range(1, 4), name=names[1])
    mi = pd.MultiIndex.from_arrays([range(3), range(1, 4)], names=names)
    expected = pd.Series(1, index=mi).unstack(1, fill_value=0)
    result = pd.crosstab(s1, s2)
    tm.assert_frame_equal(result, expected)