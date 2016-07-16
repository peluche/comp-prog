if __name__ == '__main__':
    for _ in range(int(raw_input())):
        n = int(raw_input())
        print '{}'.format('Chef' if n % 6 else 'Misha')
