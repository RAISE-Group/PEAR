@pytest.mark.parametrize('new_closed', ['left', 'right', 'both', 'neither'])
def test_set_closed(self, name, closed, new_closed):
    index = interval_range(0, 5, closed=closed, name=name)
    result = index.set_closed(new_closed)
    expected = interval_range(0, 5, closed=new_closed, name=name)
    tm.assert_index_equal(result, expected)