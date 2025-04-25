data_1 = {'order': {'id': '1234',
                    'type': 'order.created',
                    'channel': 'eshop CZ'}}

data_2 = {'order': {'id': '1234',
                    'type': 'order.created',
                    'channel': ''}}

data_3 = {'order': {'id': '1234',
                    'type': 'order.created'}}


def vrat_zemi_objednavky(datovy_set):
    try:
        vystup = datovy_set['order']['channel'].split(' ')[1]
        1/0

    except KeyError:
        print('Data neobsahují hledaný atribut.')
    except IndexError:
        print('Neplatná hodnota pro "channel".')
    except Exception as error:  # ZeroDivisionError
        print('Objevila se další chyba')
        print(repr(error))
    else:
        print('Nalezená platná hodnota')
        return vystup


vystup_iso_kod = vrat_zemi_objednavky(datovy_set=data_1)