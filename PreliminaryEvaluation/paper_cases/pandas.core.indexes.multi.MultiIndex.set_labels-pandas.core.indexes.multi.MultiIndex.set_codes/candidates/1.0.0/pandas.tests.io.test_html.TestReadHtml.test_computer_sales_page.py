def test_computer_sales_page(self, datapath):
    data = datapath('io', 'data', 'html', 'computer_sales_page.html')
    msg = 'Passed header=\\[0,1\\] are too many rows for this multi_index of columns'
    with pytest.raises(ParserError, match=msg):
        self.read_html(data, header=[0, 1])
    data = datapath('io', 'data', 'html', 'computer_sales_page.html')
    assert self.read_html(data, header=[1, 2])