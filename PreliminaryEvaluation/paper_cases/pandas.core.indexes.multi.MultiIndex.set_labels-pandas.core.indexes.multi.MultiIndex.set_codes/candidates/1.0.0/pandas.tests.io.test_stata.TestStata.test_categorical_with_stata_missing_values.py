@pytest.mark.parametrize('version', [114, 117, 118, 119, None])
def test_categorical_with_stata_missing_values(self, version):
    values = [['a' + str(i)] for i in range(120)]
    values.append([np.nan])
    original = pd.DataFrame.from_records(values, columns=['many_labels'])
    original = pd.concat([original[col].astype('category') for col in original], axis=1)
    original.index.name = 'index'
    with tm.ensure_clean() as path:
        original.to_stata(path, version=version)
        written_and_read_again = self.read_dta(path)
        res = written_and_read_again.set_index('index')
        tm.assert_frame_equal(res, original, check_categorical=False)