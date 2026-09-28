@pytest.mark.parametrize('skipna', [True, False])
def test_reduce_series_boolean(self, data, all_boolean_reductions, skipna):
    op_name = all_boolean_reductions
    s = pd.Series(data)
    with pytest.raises(TypeError):
        getattr(s, op_name)(skipna=skipna)