def test_no_overlap_more_informative_error(self):
    dt = datetime.now()
    df1 = DataFrame({'x': ['a']}, index=[dt])
    df2 = DataFrame({'y': ['b', 'c']}, index=[dt, dt])
    msg = 'No common columns to perform merge on. Merge options: left_on={lon}, right_on={ron}, left_index={lidx}, right_index={ridx}'.format(lon=None, ron=None, lidx=False, ridx=False)
    with pytest.raises(MergeError, match=msg):
        merge(df1, df2)