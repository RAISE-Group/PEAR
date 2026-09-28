@pytest.mark.parametrize('key', [pd.Timedelta(0), pd.Timedelta(1), timedelta(0)])
def test_timedelta_invalid_key(self, key):
    dti = pd.date_range('1970-01-01', periods=10)
    with pytest.raises(TypeError):
        dti.get_loc(key)