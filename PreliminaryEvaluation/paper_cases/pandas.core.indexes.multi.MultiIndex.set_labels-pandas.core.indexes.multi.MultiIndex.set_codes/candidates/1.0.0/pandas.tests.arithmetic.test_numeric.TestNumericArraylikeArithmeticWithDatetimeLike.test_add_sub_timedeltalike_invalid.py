@pytest.mark.parametrize('other', [pd.Timedelta(hours=31), pd.Timedelta(hours=31).to_pytimedelta(), pd.Timedelta(hours=31).to_timedelta64(), pd.Timedelta(hours=31).to_timedelta64().astype('m8[h]'), np.timedelta64('NaT'), np.timedelta64('NaT', 'D'), pd.offsets.Minute(3), pd.offsets.Second(0)])
def test_add_sub_timedeltalike_invalid(self, numeric_idx, other, box):
    left = tm.box_expected(numeric_idx, box)
    with pytest.raises(TypeError):
        left + other
    with pytest.raises(TypeError):
        other + left
    with pytest.raises(TypeError):
        left - other
    with pytest.raises(TypeError):
        other - left