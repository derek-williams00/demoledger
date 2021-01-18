from time import time as now

class Profile:
    def __init__(self, **kwargs):
        self.content = dict(kwargs)
        self.content['name'] = ''

    def __dict__(self):
        return self.content

    def sign(self, private_key, article):
        pass

    def verify(self, public_key, article):
        pass




class Event:
    def __init__(self, **kwargs):
        self.content = dict(kwargs)
        self.content['time'] = now()

    def __dict__(self):
        return self.content


class ProfileCreation(Event):
#    def __init__(self, time, name, number, public_key):

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        #TODO

class AccountOpening(AccountEvent):
    pass


class AccountClosing(AccountEvent):
    pass


class Transaction(Event):
    pass




class Transfer(Transaction):
    pass




class Payment(Transfer):
    pass




class Account:
    def __init__(self, **kwargs):
        self.content = dict(kwargs)
        self.content['name'] = ''

    def __dict__(self):
        return self.content




class CurrentAccount(Account):
    pass



class TitleAccount(Account):
    pass



class Ledger:
    def __init__(self, **kwargs):
        self.content = dict(kwargs)
        self.content['name'] = ''

    def __dict__(self):
        return self.content









