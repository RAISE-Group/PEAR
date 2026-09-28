def test_duplicate_mi(self):
    df = DataFrame([['foo', 'bar', 1.0, 1], ['foo', 'bar', 2.0, 2], ['bah', 'bam', 3.0, 3], ['bah', 'bam', 4.0, 4], ['foo', 'bar', 5.0, 5], ['bah', 'bam', 6.0, 6]], columns=list('ABCD'))
    df = df.set_index(['A', 'B'])
    df = df.sort_index(level=0)
    expected = DataFrame([['foo', 'bar', 1.0, 1], ['foo', 'bar', 2.0, 2], ['foo', 'bar', 5.0, 5]], columns=list('ABCD')).set_index(['A', 'B'])
    result = df.loc['foo', 'bar']
    tm.assert_frame_equal(result, expected)