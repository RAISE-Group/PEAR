def test_getitem_boolean(self, float_string_frame, mixed_float_frame, mixed_int_frame, datetime_frame):
    d = datetime_frame.index[10]
    indexer = datetime_frame.index > d
    indexer_obj = indexer.astype(object)
    subindex = datetime_frame.index[indexer]
    subframe = datetime_frame[indexer]
    tm.assert_index_equal(subindex, subframe.index)
    with pytest.raises(ValueError, match='Item wrong length'):
        datetime_frame[indexer[:-1]]
    subframe_obj = datetime_frame[indexer_obj]
    tm.assert_frame_equal(subframe_obj, subframe)
    with pytest.raises(ValueError, match='Boolean array expected'):
        datetime_frame[datetime_frame]
    indexer_obj = Series(indexer_obj, datetime_frame.index)
    subframe_obj = datetime_frame[indexer_obj]
    tm.assert_frame_equal(subframe_obj, subframe)
    with tm.assert_produces_warning(UserWarning, check_stacklevel=False):
        indexer_obj = indexer_obj.reindex(datetime_frame.index[::-1])
        subframe_obj = datetime_frame[indexer_obj]
        tm.assert_frame_equal(subframe_obj, subframe)
    for df in [datetime_frame, float_string_frame, mixed_float_frame, mixed_int_frame]:
        if df is float_string_frame:
            continue
        data = df._get_numeric_data()
        bif = df[df > 0]
        bifw = DataFrame({c: np.where(data[c] > 0, data[c], np.nan) for c in data.columns}, index=data.index, columns=data.columns)
        for c in df.columns:
            if c not in bifw:
                bifw[c] = df[c]
        bifw = bifw.reindex(columns=df.columns)
        tm.assert_frame_equal(bif, bifw, check_dtype=False)
        for c in df.columns:
            if bif[c].dtype != bifw[c].dtype:
                assert bif[c].dtype == df[c].dtype