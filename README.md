
# Royal-Calc-API

My first simple flask api used to do simple mathematical calculations.

`Note: This project is only for learning purpose.`


## Documentation

### API link details:

For adding two number api link:
```
https://royal-calc.herokuapp.com/sum/5,4
```
For subtracting two number api link:
```
https://royal-calc.herokuapp.com/subtract/5,4
```
For multipling two number api link:
```
https://royal-calc.herokuapp.com/multiply/5,4
```
For dividing two number api link:
```
https://royal-calc.herokuapp.com/divide/32,4
```

### For using this api with python:

```python
import requests
import json
response_API = requests.get('Api link')
data = response_API.text
parse_json = json.loads(data)
print(prase_json)
```

### For using this api with javascript:

```javascript
fetch('Api link')
  .then(response => response.json())
  .then(json => console.log(json))
```

