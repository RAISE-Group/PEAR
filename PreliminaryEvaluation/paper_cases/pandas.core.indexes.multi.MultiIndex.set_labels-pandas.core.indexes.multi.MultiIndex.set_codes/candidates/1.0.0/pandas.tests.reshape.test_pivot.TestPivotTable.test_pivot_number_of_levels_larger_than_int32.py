@pytest.mark.slow
def test_pivot_number_of_levels_larger_than_int32(self):
    df = DataFrame({'ind1': np.arange(2 ** 16), 'ind2': np.arange(2 ** 16), 'count': 0})
    msg = 'Unstacked DataFrame is too big, causing int32 overflow'
    with pytest.raises(ValueError, match=msg):
        df.pivot_table(index='ind1', columns='ind2', values='count', aggfunc='count')