'''
method 만들기 연습
'''


# 은행계좌 만들기
class Account:
    """
    은행 계좌 클래스
    field(데이터) : 계좌번호(accountno), 잔액(balance)
    method(메소드) : 입금(deposit, 파라미터1 금액), 출금(withdraw, 파라미터1 금액), 이체(transfer, 파라미터1 금액, 파라미터2 다른계좌번호)
    """
    def __init__(self, accountno, balance=0):
        self.accountno = accountno
        self.balance = balance
        if self.balance < 0:
            raise ValueError('balance는 0 또는 양수여야 합니다')


    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return self.balance
        else:
            raise ValueError('금액은 0 이상이어야 합니다')


    def withdraw(self, amount):
        if amount > 0:
            self.balance -= amount
            return self.balance
        else:
            raise ValueError('금액은 0 이상이어야 합니다')


    def __eq__(self, other):
        return self.accountno == other.accountno


    def transfer(self, amount, other):
        self.balance -= amount
        other.balance += amount
        return f'{amount}만큼 {other.accountno}에 입금하셨습니다.'

if __name__ == '__main__':
    a1 = Account(123, 0)
    print(id(a1))
    print(a1.deposit(100000))

    a2 = Account(234, 0)
    print(id(a2))
    print(a2.deposit(100000))
    print(a1 == a2)

    print(a1.transfer(100, a2))
