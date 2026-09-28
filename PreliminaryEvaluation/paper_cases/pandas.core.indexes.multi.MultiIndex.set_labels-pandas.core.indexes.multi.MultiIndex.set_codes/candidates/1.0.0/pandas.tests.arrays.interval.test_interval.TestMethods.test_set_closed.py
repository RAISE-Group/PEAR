@pytest.mark.parametrize('new_closed', ['left', 'right', 'both', 'neither'])
def test_set_closed(self, closed, new_closed):
    array = IntervalArray.from_breaks(range(10), closed=closed)
    result = array.set_closed(new_closed)
    expected = IntervalArray.from_breaks(range(10), closed=new_closed)
    tm.assert_extension_array_equal(result, expected)