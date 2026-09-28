@pytest.mark.slow
def test_subplot_titles(self, iris):
    df = iris.drop('Name', axis=1).head()
    title = list(df.columns)
    plot = df.plot(subplots=True, title=title)
    assert [p.get_title() for p in plot] == title
    msg = 'The length of `title` must equal the number of columns if using `title` of type `list` and `subplots=True`'
    with pytest.raises(ValueError, match=msg):
        df.plot(subplots=True, title=title + ['kittens > puppies'])
    with pytest.raises(ValueError, match=msg):
        df.plot(subplots=True, title=title[:2])
    msg = 'Using `title` of type `list` is not supported unless `subplots=True` is passed'
    with pytest.raises(ValueError, match=msg):
        df.plot(subplots=False, title=title)
    plot = df.drop('SepalWidth', axis=1).plot(subplots=True, layout=(2, 2), title=title[:-1])
    title_list = [ax.get_title() for sublist in plot for ax in sublist]
    assert title_list == title[:3] + ['']