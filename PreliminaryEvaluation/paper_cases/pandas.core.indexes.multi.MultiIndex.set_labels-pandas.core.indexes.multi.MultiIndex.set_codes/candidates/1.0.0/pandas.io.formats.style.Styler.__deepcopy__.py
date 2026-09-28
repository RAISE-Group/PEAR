def __deepcopy__(self, memo):
    return self._copy(deepcopy=True)