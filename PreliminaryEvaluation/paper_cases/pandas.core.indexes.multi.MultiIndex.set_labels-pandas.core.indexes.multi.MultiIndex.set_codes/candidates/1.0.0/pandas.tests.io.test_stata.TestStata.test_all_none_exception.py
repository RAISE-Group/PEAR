@pytest.mark.parametrize('version', [114, 117, 118, 119, None])
def test_all_none_exception(self, version):
    output = [{'none': 'none', 'number': 0}, {'none': None, 'number': 1}]
    output = pd.DataFrame(output)
    output.loc[:, 'none'] = None
    with tm.ensure_clean() as path:
        with pytest.raises(ValueError, match='Column `none` cannot be exported'):
            output.to_stata(path, version=version)