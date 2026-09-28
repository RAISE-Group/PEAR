def test_roundtrip(self, gbq_dataset):
    destination_table = gbq_dataset
    test_size = 20001
    df = make_mixed_dataframe_v2(test_size)
    df.to_gbq(destination_table, _get_project_id(), chunksize=None, credentials=_get_credentials())
    result = pd.read_gbq(f'SELECT COUNT(*) AS num_rows FROM {destination_table}', project_id=_get_project_id(), credentials=_get_credentials(), dialect='standard')
    assert result['num_rows'][0] == test_size