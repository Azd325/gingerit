Little Client around [GingerSoftware](https://rapidapi.com/ginger-software-ginger-software-default/api/ginger4/details)
----

[![codecov](https://codecov.io/gh/Azd325/gingerit/graph/badge.svg?token=XAZK1SVQZM)](https://codecov.io/gh/Azd325/gingerit)


> [!NOTE]
> You have to set your API key from RapidAPI as enviroment variable

```bash
export GINGER_IT_API_KEY = your-key
```


```python
from gingerit.gingerit import GingerIt
text = "The smelt of fliwers bring back memories."
output = GingerIt().parse(text)
```
