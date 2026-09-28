@td.skip_if_no('xlwt')
@td.skip_if_no('openpyxl')
@pytest.mark.parametrize('header,expected', [(None, DataFrame([0] + [np.nan] * 4)), (0, DataFrame([np.nan] * 4))])
def test_read_one_empty_col_with_header(self, ext, header, expected):
    filename = 'with_header'
    df = pd.DataFrame([['', 1, 100], ['', 2, 200], ['', 3, 300], ['', 4, 400]])
    with tm.ensure_clean(ext) as path:
        df.to_excel(path, 'with_header', index=False, header=True)
        result = pd.read_excel(path, filename, usecols=[0], header=header)
    tm.assert_frame_equal(result, expected)