def test_string_slice(self):
    df = DataFrame([1], Index([pd.Timestamp('2011-01-01')], dtype=object))
    assert df.index.is_all_dates
    with pytest.raises(KeyError, match="'2011'"):
        df['2011']
    with pytest.raises(KeyError, match="'2011'"):
        df.loc['2011', 0]
    df = DataFrame()
    assert not df.index.is_all_dates
    with pytest.raises(KeyError, match="'2011'"):
        df['2011']
    with pytest.raises(KeyError, match="'2011'"):
        df.loc['2011', 0]