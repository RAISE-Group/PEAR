@pytest.mark.parametrize('if_exists, expected_num_rows, expectation', [('append', 300, does_not_raise()), ('fail', 200, pytest.raises(pandas_gbq.gbq.TableCreationError)), ('replace', 100, does_not_raise())])
def test_gbq_if_exists(self, if_exists, expected_num_rows, expectation, gbq_dataset):
    destination_table = gbq_dataset
    test_size = 200
    df = make_mixed_dataframe_v2(test_size)
    df.to_gbq(destination_table, _get_project_id(), chunksize=None, credentials=_get_credentials())
    with expectation:
        df.iloc[:100].to_gbq(destination_table, _get_project_id(), if_exists=if_exists, chunksize=None, credentials=_get_credentials())
    result = pd.read_gbq(f'SELECT COUNT(*) AS num_rows FROM {destination_table}', project_id=_get_project_id(), credentials=_get_credentials(), dialect='standard')
    assert result['num_rows'][0] == expected_num_rows