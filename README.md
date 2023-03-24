# 作業2：文字計數

## 目標
已知附檔資料「hw2_data.txt」是一份近千行的字串資料。每一行只有一個英文字，且文字重複率很高。欲使用 hash 的資料結構，求：

1. 總共有多少個不重複的英文字
2. 每一個英文字出現之次數總和

## 操作
1. 將 `hw2_data.txt` 與主程式 `WordCounts.py` 置於相同目錄下。
2. 執行 `WordCounts.py`。

## 原理

步驟如下：

1. 將資料逐行讀取，取出單詞。
2. 條件判斷：單詞是否曾出現過。
	- 若不曾出現過，則單詞作為新的 key 值，value 為 1。
	- 若已經出現過，則單詞所作 key 值，其 value 增加 1。

## 程式碼逐行解釋

> 完整程式碼見 `WordCounts.py`。

### 取得檔案目錄

1. 引入 `os.path` 模組，處理檔案路徑用。
	```python
	import os.path
	```
2. 使用 `os.path.abspath` 取得主程式絕對路徑，再取出當下目錄。
	```python
	path = os.path.abspath(__file__)
	dir = os.path.dirname(path)
	```

### 建立儲存單詞 (key) 及次數 (value) 的 hash table
1. 建立空的辭典。
    ```python
    word_counts = {}
    ```
2. 使用 `open()` 讀取資料，並逐行取出單詞。
    ```python
    with open(dir + '\\hw2_data.txt', 'r') as f:
    for line in f:
        word = line.strip()
    ```
3. 以單詞為 key，若 key 已存在，則 value 增加 1。反之，則等於 1。
    ```python
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    ```
4. 先是不重複單詞總數，接著是單詞計數，依序 print out 結果。
    ```python
    print('Words: ', len(word_counts))
    print('Word Frequency: ', word_counts)
    ```
    輸出：
    ```
    Words:  10
    Word Frequency:  {'Cheese': 234, 'Pizza': 83, 'Coke': 145, 'Steak': 46, 'Burger': 196, 'Fries': 76, 'Rib': 33, 'Taco': 57, 'Pho': 19, 'Potato': 3}
    ```
