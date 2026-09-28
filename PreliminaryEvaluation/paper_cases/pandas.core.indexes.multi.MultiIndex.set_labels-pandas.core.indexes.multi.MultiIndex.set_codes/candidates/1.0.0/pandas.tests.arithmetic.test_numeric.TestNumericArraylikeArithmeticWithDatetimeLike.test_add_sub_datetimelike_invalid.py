@pytest.mark.parametrize('other', [pd.Timestamp.now().to_pydatetime(), pd.Timestamp.now(tz='UTC').to_pydatetime(), pd.Timestamp.now().to_datetime64(), pd.NaT])
@pytest.mark.filterwarnings('ignore:elementwise comp:DeprecationWarning')
def test_add_sub_datetimelike_invalid(self, numeric_idx, other, box):
    left = tm.box_expected(numeric_idx, box)
    with pytest.raises(TypeError):
        left + other
    with pytest.raises(TypeError):
        other + left
    with pytest.raises(TypeError):
        left - other
    with pytest.raises(TypeError):
        other - left