def test_constructor_dict_timedelta64_index(self):
    td_as_int = [1, 2, 3, 4]

    def create_data(constructor):
        return {i: {constructor(s): 2 * i} for i, s in enumerate(td_as_int)}
    data_timedelta64 = create_data(lambda x: np.timedelta64(x, 'D'))
    data_timedelta = create_data(lambda x: timedelta(days=x))
    data_Timedelta = create_data(lambda x: Timedelta(x, 'D'))
    expected = DataFrame([{0: 0, 1: None, 2: None, 3: None}, {0: None, 1: 2, 2: None, 3: None}, {0: None, 1: None, 2: 4, 3: None}, {0: None, 1: None, 2: None, 3: 6}], index=[Timedelta(td, 'D') for td in td_as_int])
    result_timedelta64 = DataFrame(data_timedelta64)
    result_timedelta = DataFrame(data_timedelta)
    result_Timedelta = DataFrame(data_Timedelta)
    tm.assert_frame_equal(result_timedelta64, expected)
    tm.assert_frame_equal(result_timedelta, expected)
    tm.assert_frame_equal(result_Timedelta, expected)