@pytest.mark.parametrize('version', [114, 117, 118, 119, None])
def test_timestamp_and_label(self, version):
    original = DataFrame([(1,)], columns=['variable'])
    time_stamp = datetime(2000, 2, 29, 14, 21)
    data_label = 'This is a data file.'
    with tm.ensure_clean() as path:
        original.to_stata(path, time_stamp=time_stamp, data_label=data_label, version=version)
        with StataReader(path) as reader:
            assert reader.time_stamp == '29 Feb 2000 14:21'
            assert reader.data_label == data_label