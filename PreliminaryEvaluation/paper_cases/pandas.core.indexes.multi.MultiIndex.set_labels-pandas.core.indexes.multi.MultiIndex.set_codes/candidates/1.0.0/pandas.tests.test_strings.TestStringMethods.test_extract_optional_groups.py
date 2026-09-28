def test_extract_optional_groups(self):
    result = Series(['A11', 'B22', 'C33']).str.extract('([AB])([123])(?:[123])', expand=True)
    exp = DataFrame([['A', '1'], ['B', '2'], [np.nan, np.nan]])
    tm.assert_frame_equal(result, exp)
    result = Series(['A1', 'B2', '3']).str.extract('(?P<letter>[AB])?(?P<number>[123])', expand=True)
    e_list = [['A', '1'], ['B', '2'], [np.nan, '3']]
    exp = DataFrame(e_list, columns=['letter', 'number'])
    tm.assert_frame_equal(result, exp)
    result = Series(['A1', 'B2', 'C']).str.extract('(?P<letter>[ABC])(?P<number>[123])?', expand=True)
    e_list = [['A', '1'], ['B', '2'], ['C', np.nan]]
    exp = DataFrame(e_list, columns=['letter', 'number'])
    tm.assert_frame_equal(result, exp)

    def check_index(index):
        data = ['A1', 'B2', 'C']
        index = index[:len(data)]
        result = Series(data, index=index).str.extract('(\\d)', expand=True)
        exp = DataFrame(['1', '2', np.nan], index=index)
        tm.assert_frame_equal(result, exp)
        result = Series(data, index=index).str.extract('(?P<letter>\\D)(?P<number>\\d)?', expand=True)
        e_list = [['A', '1'], ['B', '2'], ['C', np.nan]]
        exp = DataFrame(e_list, columns=['letter', 'number'], index=index)
        tm.assert_frame_equal(result, exp)
    i_funs = [tm.makeStringIndex, tm.makeUnicodeIndex, tm.makeIntIndex, tm.makeDateIndex, tm.makePeriodIndex, tm.makeRangeIndex]
    for index in i_funs:
        check_index(index())