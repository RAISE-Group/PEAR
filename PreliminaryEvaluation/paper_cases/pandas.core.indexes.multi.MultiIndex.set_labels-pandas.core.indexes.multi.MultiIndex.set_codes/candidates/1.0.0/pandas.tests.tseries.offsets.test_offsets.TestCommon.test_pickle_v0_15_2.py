def test_pickle_v0_15_2(self, datapath):
    offsets = {'DateOffset': DateOffset(years=1), 'MonthBegin': MonthBegin(1), 'Day': Day(1), 'YearBegin': YearBegin(1), 'Week': Week(1)}
    pickle_path = datapath('tseries', 'offsets', 'data', 'dateoffset_0_15_2.pickle')
    tm.assert_dict_equal(offsets, read_pickle(pickle_path))