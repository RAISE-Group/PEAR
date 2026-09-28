def insert(self, chunksize=None, method=None):
    if method is None:
        exec_insert = self._execute_insert
    elif method == 'multi':
        exec_insert = self._execute_insert_multi
    elif callable(method):
        exec_insert = partial(method, self)
    else:
        raise ValueError(f'Invalid parameter `method`: {method}')
    keys, data_list = self.insert_data()
    nrows = len(self.frame)
    if nrows == 0:
        return
    if chunksize is None:
        chunksize = nrows
    elif chunksize == 0:
        raise ValueError('chunksize argument should be non-zero')
    chunks = int(nrows / chunksize) + 1
    with self.pd_sql.run_transaction() as conn:
        for i in range(chunks):
            start_i = i * chunksize
            end_i = min((i + 1) * chunksize, nrows)
            if start_i >= end_i:
                break
            chunk_iter = zip(*[arr[start_i:end_i] for arr in data_list])
            exec_insert(conn, keys, chunk_iter)