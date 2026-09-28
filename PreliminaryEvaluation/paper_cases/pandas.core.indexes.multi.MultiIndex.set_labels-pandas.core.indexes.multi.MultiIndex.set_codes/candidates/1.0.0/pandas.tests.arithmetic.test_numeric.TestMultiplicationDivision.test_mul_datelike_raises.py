def test_mul_datelike_raises(self, numeric_idx):
    idx = numeric_idx
    with pytest.raises(TypeError):
        idx * pd.date_range('20130101', periods=5)