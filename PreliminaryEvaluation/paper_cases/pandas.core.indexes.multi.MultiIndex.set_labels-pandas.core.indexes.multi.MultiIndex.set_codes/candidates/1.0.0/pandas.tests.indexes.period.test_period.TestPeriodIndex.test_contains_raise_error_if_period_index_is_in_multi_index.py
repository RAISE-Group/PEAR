@pytest.mark.parametrize('msg, key', [("Period\\('2019', 'A-DEC'\\), 'foo', 'bar'", (Period(2019), 'foo', 'bar')), ("Period\\('2019', 'A-DEC'\\), 'y1', 'bar'", (Period(2019), 'y1', 'bar')), ("Period\\('2019', 'A-DEC'\\), 'foo', 'z1'", (Period(2019), 'foo', 'z1')), ("Period\\('2018', 'A-DEC'\\), Period\\('2016', 'A-DEC'\\), 'bar'", (Period(2018), Period(2016), 'bar')), ("Period\\('2018', 'A-DEC'\\), 'foo', 'y1'", (Period(2018), 'foo', 'y1')), ("Period\\('2017', 'A-DEC'\\), 'foo', Period\\('2015', 'A-DEC'\\)", (Period(2017), 'foo', Period(2015))), ("Period\\('2017', 'A-DEC'\\), 'z1', 'bar'", (Period(2017), 'z1', 'bar'))])
def test_contains_raise_error_if_period_index_is_in_multi_index(self, msg, key):
    """
        parse_time_string return parameter if type not matched.
        PeriodIndex.get_loc takes returned value from parse_time_string as a tuple.
        If first argument is Period and a tuple has 3 items,
        process go on not raise exception
        """
    df = DataFrame({'A': [Period(2019), 'x1', 'x2'], 'B': [Period(2018), Period(2016), 'y1'], 'C': [Period(2017), 'z1', Period(2015)], 'V1': [1, 2, 3], 'V2': [10, 20, 30]}).set_index(['A', 'B', 'C'])
    with pytest.raises(KeyError, match=msg):
        df.loc[key]