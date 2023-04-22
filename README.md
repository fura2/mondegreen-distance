# Mondegreen Distance
[![Actions Status](https://github.com/fura2/mondegreen-distance/actions/workflows/python-package.yml/badge.svg)](https://github.com/fura2/mondegreen-distance/actions)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)

日本語の響きの近さを測るモジュール

- 📝 解説 https://zenn.dev/articles/c97c8a59f3cc19
- Webアプリ [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://mondegreen-search.streamlit.app)

## インストール
```bash
pip3 install -r requirements.txt
pip3 install .
```

## 使い方
```python
from mondegreen_distance import distance
print(distance('からあげ', 'からあげ'))  # output: 0.0
print(distance('やきとり', 'からあげ'))  # output: 2.4189041095890413
print(distance('からおけ', 'からあげ'))  # output: 0.4134246575342466
```

## デモ
入力した単語に最も響きが近い単語を辞書ファイルから検索する。
辞書ファイルの詳細は[resource](resource)を参照。
```bash
python3 demo/search.py resource/db_mtg.csv
```
