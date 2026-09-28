def test_replace_period(self):
    d = {'fname': {'out_augmented_AUG_2011.json': pd.Period(year=2011, month=8, freq='M'), 'out_augmented_JAN_2011.json': pd.Period(year=2011, month=1, freq='M'), 'out_augmented_MAY_2012.json': pd.Period(year=2012, month=5, freq='M'), 'out_augmented_SUBSIDY_WEEK.json': pd.Period(year=2011, month=4, freq='M'), 'out_augmented_AUG_2012.json': pd.Period(year=2012, month=8, freq='M'), 'out_augmented_MAY_2011.json': pd.Period(year=2011, month=5, freq='M'), 'out_augmented_SEP_2013.json': pd.Period(year=2013, month=9, freq='M')}}
    df = pd.DataFrame(['out_augmented_AUG_2012.json', 'out_augmented_SEP_2013.json', 'out_augmented_SUBSIDY_WEEK.json', 'out_augmented_MAY_2012.json', 'out_augmented_MAY_2011.json', 'out_augmented_AUG_2011.json', 'out_augmented_JAN_2011.json'], columns=['fname'])
    assert set(df.fname.values) == set(d['fname'].keys())
    expected = DataFrame({'fname': [d['fname'][k] for k in df.fname.values]}, dtype=object)
    result = df.replace(d)
    tm.assert_frame_equal(result, expected)