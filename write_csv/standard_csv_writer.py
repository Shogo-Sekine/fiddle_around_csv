import csv

def main():
    # 文字列をとにかく1行ずつcsvに書き出す(生python wは上書き、aは追記)
    # with open('../data/sample2.csv', 'w') as f:
    # # with open('../data/sample2.csv', 'a') as f:
    #     for i in range(10):
    #         f.write(str(i + 1) + '行目1列目の書き込みです')
    #         f.write(',')  # csvなのでカンマで列を区切る
    #         f.write(str(i + 1) + '行目2列目の書き込みです')
    #         # 行の最後には改行を忘れないこと
    #         f.write('\n')

    # 文字列をとにかく1行ずつcsvに書き出す(csvモジュール wは上書き、aは追記)
    with open('../data/sample2.csv', 'w') as f:
    # with open('../data/sample2.csv', 'a') as f:
        writer = csv.writer(f, lineterminator='\n') # 改行コード（\n）を指定しておく
        for i in range(10):
            one_row = [str(i + 1) + '行目1列目の書き込みです', str(i + 1) + '行目2列目の書き込みです']
            writer.writerow(one_row)     # list（1次元配列）の場合
    '''
    output=>
        1行目1列目の書き込みです,1行目2列目の書き込みです
        2行目1列目の書き込みです,2行目2列目の書き込みです
        3行目1列目の書き込みです,3行目2列目の書き込みです
        4行目1列目の書き込みです,4行目2列目の書き込みです
        5行目1列目の書き込みです,5行目2列目の書き込みです
        6行目1列目の書き込みです,6行目2列目の書き込みです
        7行目1列目の書き込みです,7行目2列目の書き込みです
        8行目1列目の書き込みです,8行目2列目の書き込みです
        9行目1列目の書き込みです,9行目2列目の書き込みです
        10行目1列目の書き込みです,10行目2列目の書き込みです
    '''

    # cf:辞書形式でcsv出力する方法
    with open('../data/sample3.csv', 'w') as f:
        # ヘッダー名を最初に決める
        fieldnames = ['first_name', 'last_name', 'age']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow({'first_name': 'Baked', 'last_name': 'Beans', 'age': '20'})
        writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam', 'age': '56'})
        writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam', 'age': '65'})
        sample_dict = {'first_name': 'Fxxin', 'last_name': 'Spam', 'age': '312'}
        writer.writerow(sample_dict)

    '''
    output=>
        first_name,last_name,age
        Baked,Beans,20
        Lovely,Spam,56
        Wonderful,Spam,65
        Fxxin,Spam,312
    '''


if __name__ == '__main__':
    main()