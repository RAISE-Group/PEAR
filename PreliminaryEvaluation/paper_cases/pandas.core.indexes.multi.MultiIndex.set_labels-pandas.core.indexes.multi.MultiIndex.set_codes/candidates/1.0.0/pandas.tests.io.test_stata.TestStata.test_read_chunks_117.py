@pytest.mark.parametrize('file', ['dta1_117', 'dta2_117', 'dta3_117', 'dta4_117', 'dta14_117', 'dta15_117', 'dta16_117', 'dta17_117', 'dta18_117', 'dta19_117', 'dta20_117'])
@pytest.mark.parametrize('chunksize', [1, 2])
@pytest.mark.parametrize('convert_categoricals', [False, True])
@pytest.mark.parametrize('convert_dates', [False, True])
def test_read_chunks_117(self, file, chunksize, convert_categoricals, convert_dates):
    fname = getattr(self, file)
    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter('always')
        parsed = read_stata(fname, convert_categoricals=convert_categoricals, convert_dates=convert_dates)
    itr = read_stata(fname, iterator=True, convert_categoricals=convert_categoricals, convert_dates=convert_dates)
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