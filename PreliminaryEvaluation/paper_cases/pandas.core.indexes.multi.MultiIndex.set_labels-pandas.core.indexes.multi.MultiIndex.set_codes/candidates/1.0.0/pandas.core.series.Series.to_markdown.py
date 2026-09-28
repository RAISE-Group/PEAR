@Appender('\n        Examples\n        --------\n        >>> s = pd.Series(["elk", "pig", "dog", "quetzal"], name="animal")\n        >>> print(s.to_markdown())\n        |    | animal   |\n        |---:|:---------|\n        |  0 | elk      |\n        |  1 | pig      |\n        |  2 | dog      |\n        |  3 | quetzal  |\n        ')
@Substitution(klass='Series')
@Appender(generic._shared_docs['to_markdown'])
def to_markdown(self, buf: Optional[IO[str]]=None, mode: Optional[str]=None, **kwargs) -> Optional[str]:
    return self.to_frame().to_markdown(buf, mode, **kwargs)