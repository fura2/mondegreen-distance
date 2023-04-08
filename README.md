# Mondegreen Distance

日本語の響きの近さを測るモジュール

- Webアプリはこちら https://mondegreen-search.streamlit.app/
- 解説はこちら https://zenn.dev/articles/c97c8a59f3cc19

## インストール
```bash
pip3 install -r requirements.txt
pip3 install .
```

## 使い方
```python
from mondegreen_distance import distance
print(distance('さよなら', 'さよなら'))    # output: 0.0
print(distance('おはよう', 'さよなら'))    # output: 2.9095890410958907
print(distance('ぴあならー', 'さよなら'))  # output: 1.0997260273972604
```

## デモ
入力した単語に最も響きが近い単語を辞書ファイルから検索する。
辞書ファイルの詳細は[resource](resource)を参照。
```bash
python3 demo/search.py resource/db_mtg.csv
```
