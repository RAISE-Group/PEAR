@pytest.mark.filterwarnings('ignore:\\nthe :pandas.io.pytables.AttributeConflictWarning')
def test_retain_index_attributes(self, setup_path):
    df = DataFrame(dict(A=Series(range(3), index=date_range('2000-1-1', periods=3, freq='H'))))
    with ensure_clean_store(setup_path) as store:
        _maybe_remove(store, 'data')
        store.put('data', df, format='table')
        result = store.get('data')
        tm.assert_frame_equal(df, result)
        for attr in ['freq', 'tz', 'name']:
            for idx in ['index', 'columns']:
                assert getattr(getattr(df, idx), attr, None) == getattr(getattr(result, idx), attr, None)
        with catch_warnings(record=True):
            df2 = DataFrame(dict(A=Series(range(3), index=date_range('2002-1-1', periods=3, freq='D'))))
            store.append('data', df2)
        assert store.get_storer('data').info['index']['freq'] is None
        _maybe_remove(store, 'df2')
        df2 = DataFrame(dict(A=Series(range(3), index=[Timestamp('20010101'), Timestamp('20010102'), Timestamp('20020101')])))
        store.append('df2', df2)
        df3 = DataFrame(dict(A=Series(range(3), index=date_range('2002-1-1', periods=3, freq='D'))))
        store.append('df2', df3)