
class Account:
    def number(self) -> int:
        pass

    def gross_credits(self) -> int:
        pass #TODO

    def gross_debits(self) -> int:
        pass #TODO

    def net_credits(self) -> int:
        pass #TODO

    def net_debits(self) -> int:
        pass #TODO

    def verify(self, txn):
        

#NOTE: only account 0 can have more debits than credits

class Event:
    '''
        Possible kinds of events include:
            * Funds transfer
            * Create Account
            * Change Account info
    '''
    pass


class Transaction:
    ''' Transfer of funds from one account to another. '''

    def __init__(self, time, amount, payer_n, recipient_n):
        self.time = time
        self.amount = amount
        self.payer_n = payer_n
        self.recipient_n = recipient_n

    def time(self):
        return self.time

    def amount(self) -> int:
        return self.amount

    def payer_n(self) -> int:
        return self.payer_n

    def recipient_n(self) -> int:
        return self.recipient_n

    def counterparties(self): -> list[int]:
        return [self.payer_n, self.recipient_n]


class Ledger:
    '''
        Local model of a ledger manaaged on an individual machine.
        Other nodes host local copies and synchronize with eachother.
    '''
    def __init__(self, **kwargs):
        self.time_founded = kwargs.get('time', default=0)
        # List of account objects where index cooresponds
        #   to account number.
        #   The ledger's treasury account is number 0.
        self.accounts = [Account()]
        #
        # Maps user names to numbers
        self.user_numbers = dict()

    def time_founded(self):
        pass #TODO

    def n_accounts(self) -> int:
        return len(self.accounts)

    def using_account_n(self, number) -> bool:
        return self.n_accounts

    def account_by_n(self, number) -> Account:
        return self.accounts[number]

    def txn_is_valid(self, txn) -> bool:
        ''' For a txn to be valid, all counterparties must sign '''
        return True #TODO






