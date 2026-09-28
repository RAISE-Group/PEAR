@pytest.mark.parametrize('other', ['a', 1, 1.5, np.array(2)])
def test_td64arr_addsub_numeric_scalar_invalid(self, box_with_array, other):
    tdser = pd.Series(['59 Days', '59 Days', 'NaT'], dtype='m8[ns]')
    tdarr = tm.box_expected(tdser, box_with_array)
    assert_invalid_addsub_type(tdarr, other)