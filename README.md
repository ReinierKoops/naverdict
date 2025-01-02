# Introduction

Search of both English-Korean and Korean-English dictionaries of endic.naver.com

Based on the [NDic](https://github.com/jupiny/ndic) repository by [SeunghwanJoo](https://github.com/jupiny).

# Installation

Install via pip:

```cmd
    pip install naverdic
```

# How to use

Using this as a Python package you can use:

```python
    from naverdic.search import search

    search("하다")
```
```
["do", "have", "give", "make", "play"]
```

Using this as a CMD you can use:

```bash
    naverdic 하다
```