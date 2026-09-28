@pytest.mark.parametrize('version', [114, 117, 118, 119, None])
@pytest.mark.filterwarnings('ignore:\\nStata value:pandas.io.stata.ValueLabelTypeMismatch')
def test_categorical_writing(self, version):
    original = DataFrame.from_records([['one', 'ten', 'one', 'one', 'one', 1], ['two', 'nine', 'two', 'two', 'two', 2], ['three', 'eight', 'three', 'three', 'three', 3], ['four', 'seven', 4, 'four', 'four', 4], ['five', 'six', 5, np.nan, 'five', 5], ['six', 'five', 6, np.nan, 'six', 6], ['seven', 'four', 7, np.nan, 'seven', 7], ['eight', 'three', 8, np.nan, 'eight', 8], ['nine', 'two', 9, np.nan, 'nine', 9], ['ten', 'one', 'ten', np.nan, 'ten', 10]], columns=['fully_labeled', 'fully_labeled2', 'incompletely_labeled', 'labeled_with_missings', 'float_labelled', 'unlabeled'])
    expected = original.copy()
    original = pd.concat([original[col].astype('category') for col in original], axis=1)
    expected['incompletely_labeled'] = expected['incompletely_labeled'].apply(str)
    expected['unlabeled'] = expected['unlabeled'].apply(str)
    expected = pd.concat([expected[col].astype('category') for col in expected], axis=1)
    expected.index.name = 'index'
    with tm.ensure_clean() as path:
        original.to_stata(path, version=version)
        written_and_read_again = self.read_dta(path)
        res = written_and_read_again.set_index('index')
        tm.assert_frame_equal(res, expected, check_categorical=False)