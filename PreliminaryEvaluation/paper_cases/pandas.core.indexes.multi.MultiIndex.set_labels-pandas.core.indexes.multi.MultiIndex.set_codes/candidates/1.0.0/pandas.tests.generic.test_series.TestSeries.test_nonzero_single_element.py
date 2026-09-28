def test_nonzero_single_element(self):
    s = Series([True])
    assert s.bool()
    s = Series([False])
    assert not s.bool()
    msg = 'The truth value of a Series is ambiguous'
    for s in [Series([np.nan]), Series([pd.NaT]), Series([True]), Series([False])]:
        with pytest.raises(ValueError, match=msg):
            bool(s)
    msg = 'bool cannot act on a non-boolean single element Series'
    for s in [Series([np.nan]), Series([pd.NaT])]:
        with pytest.raises(ValueError, match=msg):
            s.bool()
    msg = 'The truth value of a Series is ambiguous'
    for s in [Series([True, True]), Series([False, False])]:
        with pytest.raises(ValueError, match=msg):
            bool(s)
        with pytest.raises(ValueError, match=msg):
            s.bool()
    for s in [Series([1]), Series([0]), Series(['a']), Series([0.0])]:
        msg = 'The truth value of a Series is ambiguous'
        with pytest.raises(ValueError, match=msg):
            bool(s)
        msg = 'bool cannot act on a non-boolean single element Series'
        with pytest.raises(ValueError, match=msg):
            s.bool()