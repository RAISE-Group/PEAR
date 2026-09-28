@pytest.mark.parametrize('na_filter', [None, True, False])
def test_excel_passes_na_filter(self, read_ext, na_filter):
    kwargs = {}
    if na_filter is not None:
        kwargs['na_filter'] = na_filter
    with pd.ExcelFile('test5' + read_ext) as excel:
        parsed = pd.read_excel(excel, 'Sheet1', keep_default_na=True, na_values=['apple'], **kwargs)
    if na_filter is False:
        expected = [['1.#QNAN'], [1], ['nan'], ['apple'], ['rabbit']]
    else:
        expected = [[np.nan], [1], [np.nan], [np.nan], ['rabbit']]
    expected = DataFrame(expected, columns=['Test'])
    tm.assert_frame_equal(parsed, expected)