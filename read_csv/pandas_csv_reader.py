import pandas as pd

def main():
  # DataFrame型でcsvを読み込む
  # reader = pd.read_csv('../data/sample.csv')
  # print(reader)

  """
            BLANK_ HEADER_1 HEADER_2 HEADER_3 HEADER_4 HEADER_5 HEADER_6 HEADER_7  \
      0   INDEX_1      1_1      1_2      1_3      1_4      1_5      1_6      1_7
      1   INDEX_2      2_1      2_2      2_3      2_4      2_5      2_6      2_7
      2   INDEX_3      3_1      3_2      3_3      3_4      3_5      3_6      3_7
      3   INDEX_4      4_1      4_2      4_3      4_4      4_5      4_6      4_7
      4   INDEX_5      5_1      5_2      5_3      5_4      5_5      5_6      5_7
      5   INDEX_6      6_1      6_2      6_3      6_4      6_5      6_6      6_7
      6   INDEX_7      7_1      7_2      7_3      7_4      7_5      7_6      7_7
      7   INDEX_8      8_1      8_2      8_3      8_4      8_5      8_6      8_7
      8   INDEX_9      9_1      9_2      9_3      9_4      9_5      9_6      9_7
      9  INDEX_10     10_1     10_2     10_3     10_4     10_5     10_6     10_7

        HEADER_8 HEADER_9 HEADER_10
      0      1_8      1_9      1_10
      1      2_8      2_9      2_10
      2      3_8      3_9      3_10
      3      4_8      4_9      4_10
      4      5_8      5_9      5_10
      5      6_8      6_9      6_10
      6      7_8      7_9      7_10
      7      8_8      8_9      8_10
      8      9_8      9_9      9_10
      9     10_8     10_9     10_10
      
  """
      # chunksizeで行数を決定して自動的にイテレーションによる読み込みを実施する
      # reader = pd.read_csv('../data/sample.csv', chunksize=1)
      # for r in reader:
      #   print(r)

  """
        BLANK_ HEADER_1 HEADER_2 HEADER_3 HEADER_4 HEADER_5 HEADER_6 HEADER_7  \
    0  INDEX_1      1_1      1_2      1_3      1_4      1_5      1_6      1_7

      HEADER_8 HEADER_9 HEADER_10
    0      1_8      1_9      1_10
        BLANK_ HEADER_1 HEADER_2 HEADER_3 HEADER_4 HEADER_5 HEADER_6 HEADER_7  \
    1  INDEX_2      2_1      2_2      2_3      2_4      2_5      2_6      2_7

      HEADER_8 HEADER_9 HEADER_10
    1      2_8      2_9      2_10
        BLANK_ HEADER_1 HEADER_2 HEADER_3 HEADER_4 HEADER_5 HEADER_6 HEADER_7  \
    2  INDEX_3      3_1      3_2      3_3      3_4      3_5      3_6      3_7

      HEADER_8 HEADER_9 HEADER_10
    2      3_8      3_9      3_10
        BLANK_ HEADER_1 HEADER_2 HEADER_3 HEADER_4 HEADER_5 HEADER_6 HEADER_7  \
    3  INDEX_4      4_1      4_2      4_3      4_4      4_5      4_6      4_7

      HEADER_8 HEADER_9 HEADER_10
    3      4_8      4_9      4_10
        BLANK_ HEADER_1 HEADER_2 HEADER_3 HEADER_4 HEADER_5 HEADER_6 HEADER_7  \
    4  INDEX_5      5_1      5_2      5_3      5_4      5_5      5_6      5_7

      HEADER_8 HEADER_9 HEADER_10
    4      5_8      5_9      5_10
        BLANK_ HEADER_1 HEADER_2 HEADER_3 HEADER_4 HEADER_5 HEADER_6 HEADER_7  \
    5  INDEX_6      6_1      6_2      6_3      6_4      6_5      6_6      6_7

      HEADER_8 HEADER_9 HEADER_10
    5      6_8      6_9      6_10
        BLANK_ HEADER_1 HEADER_2 HEADER_3 HEADER_4 HEADER_5 HEADER_6 HEADER_7  \
    6  INDEX_7      7_1      7_2      7_3      7_4      7_5      7_6      7_7

      HEADER_8 HEADER_9 HEADER_10
    6      7_8      7_9      7_10
        BLANK_ HEADER_1 HEADER_2 HEADER_3 HEADER_4 HEADER_5 HEADER_6 HEADER_7  \
    7  INDEX_8      8_1      8_2      8_3      8_4      8_5      8_6      8_7

      HEADER_8 HEADER_9 HEADER_10
    7      8_8      8_9      8_10
        BLANK_ HEADER_1 HEADER_2 HEADER_3 HEADER_4 HEADER_5 HEADER_6 HEADER_7  \
    8  INDEX_9      9_1      9_2      9_3      9_4      9_5      9_6      9_7

      HEADER_8 HEADER_9 HEADER_10
    8      9_8      9_9      9_10
        BLANK_ HEADER_1 HEADER_2 HEADER_3 HEADER_4 HEADER_5 HEADER_6 HEADER_7  \
    9  INDEX_10     10_1     10_2     10_3     10_4     10_5     10_6     10_7

      HEADER_8 HEADER_9 HEADER_10
    9     10_8     10_9     10_10

  """

  # # 列単位で取得
  # reader = pd.read_csv('../data/sample.csv', chunksize=5)
  # for r in reader:
  #   for index, row in r.iteritems():
  #     print(index, row)

  """
      BLANK_ 0    INDEX_1
    1    INDEX_2
    2    INDEX_3
    3    INDEX_4
    4    INDEX_5
    Name: BLANK_, dtype: object
    HEADER_1 0    1_1
    1    2_1
    2    3_1
    3    4_1
    4    5_1
    Name: HEADER_1, dtype: object
    HEADER_2 0    1_2
    1    2_2
    2    3_2
    3    4_2
    4    5_2
    Name: HEADER_2, dtype: object
    HEADER_3 0    1_3
    1    2_3
    2    3_3
    3    4_3
    4    5_3
    Name: HEADER_3, dtype: object
    HEADER_4 0    1_4
    1    2_4
    2    3_4
    3    4_4
    4    5_4
    Name: HEADER_4, dtype: object
    HEADER_5 0    1_5
    1    2_5
    2    3_5
    3    4_5
    4    5_5
    Name: HEADER_5, dtype: object
    HEADER_6 0    1_6
    1    2_6
    2    3_6
    3    4_6
    4    5_6
    Name: HEADER_6, dtype: object
    HEADER_7 0    1_7
    1    2_7
    2    3_7
    3    4_7
    4    5_7
    Name: HEADER_7, dtype: object
    HEADER_8 0    1_8
    1    2_8
    2    3_8
    3    4_8
    4    5_8
    Name: HEADER_8, dtype: object
    HEADER_9 0    1_9
    1    2_9
    2    3_9
    3    4_9
    4    5_9
    Name: HEADER_9, dtype: object
    HEADER_10 0    1_10
    1    2_10
    2    3_10
    3    4_10
    4    5_10
    Name: HEADER_10, dtype: object
    BLANK_ 5     INDEX_6
    6     INDEX_7
    7     INDEX_8
    8     INDEX_9
    9    INDEX_10
    Name: BLANK_, dtype: object
    HEADER_1 5     6_1
    6     7_1
    7     8_1
    8     9_1
    9    10_1
    Name: HEADER_1, dtype: object
    HEADER_2 5     6_2
    6     7_2
    7     8_2
    8     9_2
    9    10_2
    Name: HEADER_2, dtype: object
    HEADER_3 5     6_3
    6     7_3
    7     8_3
    8     9_3
    9    10_3
    Name: HEADER_3, dtype: object
    HEADER_4 5     6_4
    6     7_4
    7     8_4
    8     9_4
    9    10_4
    Name: HEADER_4, dtype: object
    HEADER_5 5     6_5
    6     7_5
    7     8_5
    8     9_5
    9    10_5
    Name: HEADER_5, dtype: object
    HEADER_6 5     6_6
    6     7_6
    7     8_6
    8     9_6
    9    10_6
    Name: HEADER_6, dtype: object
    HEADER_7 5     6_7
    6     7_7
    7     8_7
    8     9_7
    9    10_7
    Name: HEADER_7, dtype: object
    HEADER_8 5     6_8
    6     7_8
    7     8_8
    8     9_8
    9    10_8
    Name: HEADER_8, dtype: object
    HEADER_9 5     6_9
    6     7_9
    7     8_9
    8     9_9
    9    10_9
    Name: HEADER_9, dtype: object
    HEADER_10 5     6_10
    6     7_10
    7     8_10
    8     9_10
    9    10_10
    Name: HEADER_10, dtype: object

  """

  # 行単位で取得
  reader = pd.read_csv('../data/sample.csv', chunksize=1)
  for r in reader:
    # row_index部分は本来のインデックスの番号が入る(INDEX_とは別)
    # row[0]に「INDEX_」、row[1]~には1_1 ~ 1_10と入っている(行数分イテレーションされる)
    for row_index, row in r.iterrows(): 
      for element in row[1:]: # row[0]以外でイテレーションすると各要素を取り出せる
        print(element)
  """
    1_1
    1_2
    1_3
    1_4
    1_5
    1_6
    1_7
    1_8
    1_9
    1_10
    2_1
    2_2
    2_3
    2_4
    2_5
    2_6
    2_7
    2_8
    2_9
    2_10
    3_1
    3_2
    3_3
    3_4
    3_5
    3_6
    3_7
    3_8
    3_9
    3_10
    4_1
    4_2
    4_3
    4_4
    4_5
    4_6
    4_7
    4_8
    4_9
    4_10
    5_1
    5_2
    5_3
    5_4
    5_5
    5_6
    5_7
    5_8
    5_9
    5_10
    6_1
    6_2
    6_3
    6_4
    6_5
    6_6
    6_7
    6_8
    6_9
    6_10
    7_1
    7_2
    7_3
    7_4
    7_5
    7_6
    7_7
    7_8
    7_9
    7_10
    8_1
    8_2
    8_3
    8_4
    8_5
    8_6
    8_7
    8_8
    8_9
    8_10
    9_1
    9_2
    9_3
    9_4
    9_5
    9_6
    9_7
    9_8
    9_9
    9_10
    10_1
    10_2
    10_3
    10_4
    10_5
    10_6
    10_7
    10_8
    10_9
    10_10
  """

if __name__ == '__main__':
  main()