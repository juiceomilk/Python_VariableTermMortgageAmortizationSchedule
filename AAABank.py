class CashBackCC:
    '''
    Create a AAA bank cash back credit card object/instance
    name: str. Has to be one the following: 'AAAVIC','AAAVC','AAANFVC','AAAMC'
    '''

    def __init__(self, name):
        
        if name == 'VIC':
            self.name = 'AAA Visa Infinite Card'
            self.type = 'Visa'
            self.fee = 99
            self.feature = ['4% Gas','2% Other']
        elif name == 'VC':
            self.name = 'AAA Visa Card'
            self.type = 'Visa'
            self.fee = 39
            self.feature = ['2% Gas', '1% Other']
        elif name == 'NFVC':
            self.name = 'AAA No-Fee Visa Card'
            self.type = 'Visa'
            self.fee = 0
            self.feature = ['1% Gas', '0.5% Other']
        elif name == 'NFMC':
            self.name = 'AAA No-Fee Mastercard Card'
            self.type = 'Mastercard'
            self.fee = 0
            self.feature = ['1% Gas', '0.5% Other']
        else:
            print('No such credit card!')
            
    def add_feature(self, feature):
        '''
        Add a new feature to the existing feature
        feature: string
        '''
        self.feature.append(feature)