@pytest.mark.parametrize('file', ['dta2_115', 'dta3_115', 'dta4_115', 'dta14_115', 'dta15_115', 'dta16_115', 'dta17_115', 'dta18_115', 'dta19_115', 'dta20_115'])
@pytest.mark.parametrize('chunksize', [1, 2])
@pytest.mark.parametrize('convert_categoricals', [False, True])
@pytest.mark.parametrize('convert_dates', [False, True])
def test_read_chunks_115(self, file, chunksize, convert_categoricals, convert_dates):
    fname = getattr(self, file)
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter('always')
        parsed = read_stata(fname, convert_categoricals=convert_categoricals, convert_dates=convert_dates)
    itr = read_stata(fname, iterator=True, convert_dates=convert_dates, convert_categoricals=convert_categoricals)
    pos = 0
    for j in range(5):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter('always')
            try:
                chunk = itr.read(chunksize)
            except StopIteration:
                break
        from_frame = parsed.iloc[pos:pos + chunksize, :]
        tm.assert_frame_equal(from_frame, chunk, check_dtype=False, check_datetimelike_compat=True, check_categorical=False)
        pos += chunksize
    itr.close()