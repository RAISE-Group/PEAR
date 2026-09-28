@pytest.mark.parametrize('skipna', [True, False])
def test_reduce_series_numeric(self, data, all_numeric_reductions, skipna):
    op_name = all_numeric_reductions
    s = pd.Series(data)
    with pytest.raises(TypeError):
        getattr(s, op_name)(skipna=skipna)