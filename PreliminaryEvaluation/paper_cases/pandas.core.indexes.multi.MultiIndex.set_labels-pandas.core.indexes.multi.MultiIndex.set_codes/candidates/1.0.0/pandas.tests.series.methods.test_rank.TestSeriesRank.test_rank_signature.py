def test_rank_signature(self):
    s = Series([0, 1])
    s.rank(method='average')
    msg = "No axis named average for object type <class 'pandas.core.series.Series'>"
    with pytest.raises(ValueError, match=msg):
        s.rank('average')