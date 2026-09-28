@pytest.mark.parametrize('aggregation', ['min', 'max'])
def test_min_max_not_ordered_raises(self, aggregation):
    cat = Categorical(['a', 'b', 'c', 'd'], ordered=False)
    msg = 'Categorical is not ordered for operation {}'
    agg_func = getattr(cat, aggregation)
    with pytest.raises(TypeError, match=msg.format(aggregation)):
        agg_func()