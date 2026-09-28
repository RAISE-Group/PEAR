@pytest.mark.parametrize('version', [114, 117, 118, 119, None])
def test_write_variable_labels(self, version, mixed_frame):
    mixed_frame.index.name = 'index'
    variable_labels = {'a': 'City Rank', 'b': 'City Exponent', 'c': 'City'}
    with tm.ensure_clean() as path:
        mixed_frame.to_stata(path, variable_labels=variable_labels, version=version)
        with StataReader(path) as sr:
            read_labels = sr.variable_labels()
        expected_labels = {'index': '', 'a': 'City Rank', 'b': 'City Exponent', 'c': 'City'}
        assert read_labels == expected_labels
    variable_labels['index'] = 'The Index'
    with tm.ensure_clean() as path:
        mixed_frame.to_stata(path, variable_labels=variable_labels, version=version)
        with StataReader(path) as sr:
            read_labels = sr.variable_labels()
        assert read_labels == variable_labels