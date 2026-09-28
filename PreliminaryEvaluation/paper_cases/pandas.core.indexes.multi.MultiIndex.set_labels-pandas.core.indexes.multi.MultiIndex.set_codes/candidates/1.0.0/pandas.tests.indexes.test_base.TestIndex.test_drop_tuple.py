@pytest.mark.parametrize('values', [['a', 'b', ('c', 'd')], ['a', ('c', 'd'), 'b'], [('c', 'd'), 'a', 'b']])
@pytest.mark.parametrize('to_drop', [[('c', 'd'), 'a'], ['a', ('c', 'd')]])
def test_drop_tuple(self, values, to_drop):
    index = pd.Index(values)
    expected = pd.Index(['b'])
    result = index.drop(to_drop)
    tm.assert_index_equal(result, expected)
    removed = index.drop(to_drop[0])
    for drop_me in (to_drop[1], [to_drop[1]]):
        result = removed.drop(drop_me)
        tm.assert_index_equal(result, expected)
    removed = index.drop(to_drop[1])
    msg = f'\\"\\[{re.escape(to_drop[1].__repr__())}\\] not found in axis\\"'
    for drop_me in (to_drop[1], [to_drop[1]]):
        with pytest.raises(KeyError, match=msg):
            removed.drop(drop_me)