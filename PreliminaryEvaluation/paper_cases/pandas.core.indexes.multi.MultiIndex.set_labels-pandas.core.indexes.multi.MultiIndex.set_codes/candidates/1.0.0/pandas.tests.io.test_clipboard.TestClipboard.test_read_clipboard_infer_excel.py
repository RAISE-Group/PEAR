def test_read_clipboard_infer_excel(self, request, mock_clipboard):
    clip_kwargs = dict(engine='python')
    text = dedent('\n            John James\tCharlie Mingus\n            1\t2\n            4\tHarry Carney\n            '.strip())
    mock_clipboard[request.node.name] = text
    df = pd.read_clipboard(**clip_kwargs)
    assert df.iloc[1][1] == 'Harry Carney'
    text = dedent('\n            a\t b\n            1  2\n            3  4\n            '.strip())
    mock_clipboard[request.node.name] = text
    res = pd.read_clipboard(**clip_kwargs)
    text = dedent('\n            a  b\n            1  2\n            3  4\n            '.strip())
    mock_clipboard[request.node.name] = text
    exp = pd.read_clipboard(**clip_kwargs)
    tm.assert_frame_equal(res, exp)