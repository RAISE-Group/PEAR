def apply_broadcast(self, target: 'DataFrame') -> 'DataFrame':
    result_values = np.empty_like(target.values)
    result_compare = target.shape[0]
    for i, col in enumerate(target.columns):
        res = self.f(target[col])
        ares = np.asarray(res).ndim
        if ares > 1:
            raise ValueError('too many dims to broadcast')
        elif ares == 1:
            if result_compare != len(res):
                raise ValueError('cannot broadcast result')
        result_values[:, i] = res
    result = self.obj._constructor(result_values, index=target.index, columns=target.columns)
    return result