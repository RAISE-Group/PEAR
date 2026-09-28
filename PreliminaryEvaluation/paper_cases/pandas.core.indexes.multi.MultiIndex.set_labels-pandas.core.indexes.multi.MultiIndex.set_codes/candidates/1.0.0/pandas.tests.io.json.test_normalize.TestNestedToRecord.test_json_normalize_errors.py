def test_json_normalize_errors(self, missing_metadata):
    msg = "Try running with errors='ignore' as key 'name' is not always present"
    with pytest.raises(KeyError, match=msg):
        json_normalize(data=missing_metadata, record_path='addresses', meta='name', errors='raise')