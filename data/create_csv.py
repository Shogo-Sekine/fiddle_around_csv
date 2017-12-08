import csv

def main():
    row = 10
    column = 10
    with open('sample.csv', 'w') as f:
        f.write('BLANK_,')
        for i in range(column):
            f.write('HEADER_' + str(i + 1))
            if (i + 1) != column:
                f.write(',')
        f.write('\n')

        for i in range(row):
            f.write('INDEX_' + str(i + 1))
            f.write(',')
            for j in range(column):
                f.write(str(i+1) + '_' + str(j+1))
                if (j + 1) != column:
                    f.write(',')
            f.write('\n')

if __name__ == '__main__':
    main()