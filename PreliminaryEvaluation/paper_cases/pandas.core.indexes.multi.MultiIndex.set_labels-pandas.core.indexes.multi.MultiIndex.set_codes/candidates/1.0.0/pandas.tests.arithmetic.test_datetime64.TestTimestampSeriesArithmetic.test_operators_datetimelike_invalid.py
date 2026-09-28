def test_operators_datetimelike_invalid(self, all_arithmetic_operators):
    op_str = all_arithmetic_operators

    def check(get_ser, test_ser):
        op = getattr(get_ser, op_str, None)
        with pytest.raises(TypeError, match='operate|[cC]annot|unsupported operand'):
            op(test_ser)
    td1 = Series([timedelta(minutes=5, seconds=3)] * 3)
    td1.iloc[2] = np.nan
    dt1 = Series([Timestamp('20111230'), Timestamp('20120101'), Timestamp('20120103')])
    dt1.iloc[2] = np.nan
    dt2 = Series([Timestamp('20111231'), Timestamp('20120102'), Timestamp('20120104')])
    if op_str not in ['__sub__', '__rsub__']:
        check(dt1, dt2)
    if op_str not in ['__add__', '__radd__', '__sub__']:
        check(dt1, td1)
    tz = 'US/Eastern'
    dt1 = Series(date_range('2000-01-01 09:00:00', periods=5, tz=tz), name='foo')
    dt2 = dt1.copy()
    dt2.iloc[2] = np.nan
    td1 = Series(pd.timedelta_range('1 days 1 min', periods=5, freq='H'))
    td2 = td1.copy()
    td2.iloc[1] = np.nan
    if op_str not in ['__add__', '__radd__', '__sub__', '__rsub__']:
        check(dt2, td2)