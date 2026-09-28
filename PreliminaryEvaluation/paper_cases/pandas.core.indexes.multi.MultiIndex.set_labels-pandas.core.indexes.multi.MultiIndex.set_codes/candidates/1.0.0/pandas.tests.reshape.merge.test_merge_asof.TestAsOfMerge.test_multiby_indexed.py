def test_multiby_indexed(self):
    left = pd.DataFrame([[pd.to_datetime('20160602'), 1, 'a'], [pd.to_datetime('20160602'), 2, 'a'], [pd.to_datetime('20160603'), 1, 'b'], [pd.to_datetime('20160603'), 2, 'b']], columns=['time', 'k1', 'k2']).set_index('time')
    right = pd.DataFrame([[pd.to_datetime('20160502'), 1, 'a', 1.0], [pd.to_datetime('20160502'), 2, 'a', 2.0], [pd.to_datetime('20160503'), 1, 'b', 3.0], [pd.to_datetime('20160503'), 2, 'b', 4.0]], columns=['time', 'k1', 'k2', 'value']).set_index('time')
    expected = pd.DataFrame([[pd.to_datetime('20160602'), 1, 'a', 1.0], [pd.to_datetime('20160602'), 2, 'a', 2.0], [pd.to_datetime('20160603'), 1, 'b', 3.0], [pd.to_datetime('20160603'), 2, 'b', 4.0]], columns=['time', 'k1', 'k2', 'value']).set_index('time')
    result = pd.merge_asof(left, right, left_index=True, right_index=True, by=['k1', 'k2'])
    tm.assert_frame_equal(expected, result)
    with pytest.raises(MergeError):
        pd.merge_asof(left, right, left_index=True, right_index=True, left_by=['k1', 'k2'], right_by=['k1'])