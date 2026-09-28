@Appender('\n        Examples\n        --------\n        >>> df = pd.DataFrame(\n        ...     data={"animal_1": ["elk", "pig"], "animal_2": ["dog", "quetzal"]}\n        ... )\n        >>> print(df.to_markdown())\n        |    | animal_1   | animal_2   |\n        |---:|:-----------|:-----------|\n        |  0 | elk        | dog        |\n        |  1 | pig        | quetzal    |\n        ')
@Substitution(klass='DataFrame')
@Appender(_shared_docs['to_markdown'])
def to_markdown(self, buf: Optional[IO[str]]=None, mode: Optional[str]=None, **kwargs) -> Optional[str]:
    kwargs.setdefault('headers', 'keys')
    kwargs.setdefault('tablefmt', 'pipe')
    tabulate = import_optional_dependency('tabulate')
    result = tabulate.tabulate(self, **kwargs)
    if buf is None:
        return result
    buf, _, _, _ = get_filepath_or_buffer(buf, mode=mode)
    assert buf is not None
    buf.writelines(result)
    return None