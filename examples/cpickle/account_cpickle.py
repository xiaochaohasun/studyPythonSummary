#!/usr/bin/env python

import os
import cPickle as p
import time


def save_money(wallet_file, record_file,amount,comment):
    date = time.strftime('%Y-%m-%d')

    with open(wallet_file) as fobj:
        balance = p.load(fobj) + amount
    with open(wallet_file,'w') as fobj:
        p.dump(balance,fobj)
    with open(record_file, 'a') as fobj:
        fobj.write(
            '%-12s%-8s%-8s%-10s%-20s' % \
            (date, amount, 'n/a', balance, comment)
        )


def cost_money(wallet_file, record_file,amount,comment):
    date = time.strftime('%Y-%m-%d')

    with open(wallet_file) as fobj:
        balance = p.load(fobj) - amount
    with open(wallet_file,'w') as fobj:
        p.dump(balance, fobj)
    with open(record_file, 'a') as fobj:
        fobj.write(
            '%-12s%-8s%-8s%-10s%-20s\n' % \
            (date, 'n/a', amount, balance, comment)
        )


def query(wallet_file, record_file):
    print '%-12s%-8s%-8s%-10s%-20s' % \
          ('date','save','cost','balance','comment')
    with open(record_file) as fobj:
        for line in fobj:
            print line,
    with open(wallet_file) as fobj:
        print '\nNew Balance: \033[31;1m%s\033[0m' % p.load(fobj)

def main():
    cmds = {'0': save_money, '1': cost_money, '2': query}
    wallet_file = 'wallet.data'
    record_file = 'record.txt'
    prompt = '''(0) save money
(1)cost money
(2)query history
(3)quit
please input your choice(0/1/2/3): '''
    if not os.path.exists(wallet_file):
        with open(wallet_file, 'w') as fobj:
            p.dump(10000, fobj)
    if not os.path.exists(record_file):
        os.mknod(record_file)

    while True:
        try:
            choice = raw_input(prompt).strip()[0]
        except IndentationError:
            continue
        except (KeyboardInterrupt,EOFError):
            choice='3'
        if choice not in '0123':
            print 'Invalid choice.Try again.'
            continue
        if choice == '3':
            print '\nBye-bye'
            break
        args=(wallet_file, record_file)
        if choice in '01':
            try:
                amount=int(raw_input('amount: '))
                comment=raw_input('comment: ')
            except ValueError:
                print '\033[31;1mInvalid amount,Try again.\033[0m'
                continue
            except (KeyboardInterrupt,EOFError):
                print '\nBye-bye'
                break
            args=(wallet_file, record_file,amount,comment)
        cmds[choice](*args)


if __name__ == '__main__':
    main()
