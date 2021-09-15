import CellPhone


def main():
    man = input('Enter the manufacturer: ')
    mod = input('Enter the model number: ')
    retail = float(input('Enter the retail price: '))

    phone = CellPhone.cp(man, mod, retail)

    print('Here is the data that you entered:')
    print('Manufacturer:', phone.get_manufact())
    print('odel Number:', phone.get_model())
    print('Retail Price: $', phone.get_retail_price(), ',.2f', sep='')


main()
