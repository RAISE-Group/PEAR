@pytest.mark.parametrize('closed', ['left', 'right'])
def test_bdays_and_open_boundaries(self, closed):
    start = '2018-07-21'
    end = '2018-07-29'
    result = pd.date_range(start, end, freq='B', closed=closed)
    bday_start = '2018-07-23'
    bday_end = '2018-07-27'
    expected = pd.date_range(bday_start, bday_end, freq='D')
    tm.assert_index_equal(result, expected)