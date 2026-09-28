def test_from_records_set_index_name(self):

    def create_dict(order_id):
        return {'order_id': order_id, 'quantity': np.random.randint(1, 10), 'price': np.random.randint(1, 10)}
    documents = [create_dict(i) for i in range(10)]
    documents.append({'order_id': 10, 'quantity': 5})
    result = DataFrame.from_records(documents, index='order_id')
    assert result.index.name == 'order_id'
    result = DataFrame.from_records(documents, index=['order_id', 'quantity'])
    assert result.index.names == ('order_id', 'quantity')