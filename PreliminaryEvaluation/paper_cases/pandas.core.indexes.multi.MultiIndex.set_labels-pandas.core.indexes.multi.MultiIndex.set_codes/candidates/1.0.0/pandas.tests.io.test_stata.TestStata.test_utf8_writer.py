@pytest.mark.parametrize('version', [118, 119, None])
def test_utf8_writer(self, version):
    cat = pd.Categorical(['a', 'β', 'ĉ'], ordered=True)
    data = pd.DataFrame([[1.0, 1, 'ᴬ', 'ᴀ relatively long ŝtring'], [2.0, 2, 'ᴮ', ''], [3.0, 3, 'ᴰ', None]], columns=['a', 'β', 'ĉ', 'strls'])
    data['ᴐᴬᵀ'] = cat
    variable_labels = {'a': 'apple', 'β': 'ᵈᵉᵊ', 'ĉ': 'ᴎტჄႲႳႴႶႺ', 'strls': 'Long Strings', 'ᴐᴬᵀ': ''}
    data_label = 'ᴅaᵀa-label'
    data['β'] = data['β'].astype(np.int32)
    with tm.ensure_clean() as path:
        writer = StataWriterUTF8(path, data, data_label=data_label, convert_strl=['strls'], variable_labels=variable_labels, write_index=False, version=version)
        writer.write_file()
        reread_encoded = read_stata(path)
        data['strls'] = data['strls'].fillna('')
        tm.assert_frame_equal(data, reread_encoded)
        reader = StataReader(path)
        assert reader.data_label == data_label
        assert reader.variable_labels() == variable_labels
        data.to_stata(path, version=version, write_index=False)
        reread_to_stata = read_stata(path)
        tm.assert_frame_equal(data, reread_to_stata)