def test_dropna_empty(self):
    s = Series([], dtype=object)
    assert len(s.dropna()) == 0
    s.dropna(inplace=True)
    assert len(s) == 0
    msg = "No axis named 1 for object type <class 'pandas.core.series.Series'>"
    with pytest.raises(ValueError, match=msg):
        s.dropna(axis=1)