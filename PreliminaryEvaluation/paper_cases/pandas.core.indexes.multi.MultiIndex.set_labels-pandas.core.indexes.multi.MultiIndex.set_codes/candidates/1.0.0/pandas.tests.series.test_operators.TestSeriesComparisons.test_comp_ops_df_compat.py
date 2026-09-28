def test_comp_ops_df_compat(self):
    s1 = pd.Series([1, 2, 3], index=list('ABC'), name='x')
    s2 = pd.Series([2, 2, 2], index=list('ABD'), name='x')
    s3 = pd.Series([1, 2, 3], index=list('ABC'), name='x')
    s4 = pd.Series([2, 2, 2, 2], index=list('ABCD'), name='x')
    for left, right in [(s1, s2), (s2, s1), (s3, s4), (s4, s3)]:
        msg = 'Can only compare identically-labeled Series objects'
        with pytest.raises(ValueError, match=msg):
            left == right
        with pytest.raises(ValueError, match=msg):
            left != right
        with pytest.raises(ValueError, match=msg):
            left < right
        msg = 'Can only compare identically-labeled DataFrame objects'
        with pytest.raises(ValueError, match=msg):
            left.to_frame() == right.to_frame()
        with pytest.raises(ValueError, match=msg):
            left.to_frame() != right.to_frame()
        with pytest.raises(ValueError, match=msg):
            left.to_frame() < right.to_frame()