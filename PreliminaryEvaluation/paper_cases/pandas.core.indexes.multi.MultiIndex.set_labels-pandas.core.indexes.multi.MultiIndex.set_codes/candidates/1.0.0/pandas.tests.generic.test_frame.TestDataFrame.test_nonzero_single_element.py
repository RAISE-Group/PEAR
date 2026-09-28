def test_nonzero_single_element(self):
    df = DataFrame([[True]])
    assert df.bool()
    df = DataFrame([[False]])
    assert not df.bool()
    df = DataFrame([[False, False]])
    with pytest.raises(ValueError):
        df.bool()
    with pytest.raises(ValueError):
        bool(df)