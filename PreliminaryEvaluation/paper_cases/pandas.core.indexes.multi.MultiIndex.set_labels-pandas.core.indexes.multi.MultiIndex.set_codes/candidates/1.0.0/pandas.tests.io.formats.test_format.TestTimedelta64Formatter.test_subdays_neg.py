def test_subdays_neg(self):
    y = pd.to_timedelta(list(range(5)) + [pd.NaT], unit='s')
    result = fmt.Timedelta64Formatter(-y, box=True).get_result()
    assert result[0].strip() == "'00:00:00'"
    assert result[1].strip() == "'-1 days +23:59:59'"