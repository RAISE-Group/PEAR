@ignore_natural_naming_warning
def test_to_hdf_with_object_column_names(self, setup_path):
    types_should_fail = [tm.makeIntIndex, tm.makeFloatIndex, tm.makeDateIndex, tm.makeTimedeltaIndex, tm.makePeriodIndex]
    types_should_run = [tm.makeStringIndex, tm.makeCategoricalIndex, tm.makeUnicodeIndex]
    for index in types_should_fail:
        df = DataFrame(np.random.randn(10, 2), columns=index(2))
        with ensure_clean_path(setup_path) as path:
            with catch_warnings(record=True):
                msg = 'cannot have non-object label DataIndexableCol'
                with pytest.raises(ValueError, match=msg):
                    df.to_hdf(path, 'df', format='table', data_columns=True)
    for index in types_should_run:
        df = DataFrame(np.random.randn(10, 2), columns=index(2))
        with ensure_clean_path(setup_path) as path:
            with catch_warnings(record=True):
                df.to_hdf(path, 'df', format='table', data_columns=True)
                result = pd.read_hdf(path, 'df', where='index = [{0}]'.format(df.index[0]))
                assert len(result)