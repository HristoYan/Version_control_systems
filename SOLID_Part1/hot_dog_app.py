from model import HotDogOne, HotDogTwo, HotDogThree, CustomHodDog


def mian():
    money = []
    while True:
        print('Hello and Welcome to my Hod Dog Shop!')
        print('What would be for you today? We offer three standard recipes:'
              ' "Recipe One", "Recipe Two" and "Recipe Three". You can also create your own recipe.')

        while True:
            try:
                count = int(input('How meny Hot dogs would you like to order today? '
                                  'There is a discount if you order more. press 13 to exit.\n-> '))
                if count == 13:
                    exit()
                if count < 1:
                    raise ValueError('Invalid input. Your order must be an positive integer higher then zero.')
            except ValueError as e:
                print(e)
            orders = []
            total = 0
            for i in range(count): # noqa
                print(f'For hod dog # {i + 1}...')
                try:
                    choice = input('1 - Recipe One\n2 - Recipe Two\n3 - Recipe Three\n4 - Custom Recipe\n-> ')

                    if choice not in ['1', '2', '3', '4']:
                        raise ValueError('Invalid input! choose a number between 1 and 4.')

                except ValueError as e:
                    print(e)

                if choice == '1': # noqa
                    sauce, topping = sauce_topping()
                    hot_dog = HotDogOne(sauce, topping)
                    total += hot_dog.price
                    hot_dog_info = hot_dog.ingredients()
                elif choice == '2':
                    sauce, topping = sauce_topping()
                    hot_dog = HotDogTwo(sauce, topping)
                    total += hot_dog.price
                    hot_dog_info = hot_dog.ingredients()
                elif choice == '3':
                    sauce, topping = sauce_topping()
                    hot_dog = HotDogThree(sauce, topping)
                    total += hot_dog.price
                    hot_dog_info = hot_dog.ingredients()
                elif choice == '4':
                    bread = input('Choose your bread. We have: white, whole grain and dark\n-> ')
                    sausage = input('Choose your sausage. We have: white, macedonian and wurst\n-> ')
                    sauce, topping = sauce_topping()
                    hot_dog = CustomHodDog(bread, sausage, sauce, topping)
                    total += hot_dog.price
                    hot_dog_info = hot_dog.ingredients()

                orders.append(hot_dog_info) # noqa

            else:
                break

        if count >= 3:
            print(f'Price before discount: {total}')

        display_order(orders)
        if 3 <= count < 6:
            total *= 0.9
        elif count >= 6:
            total *= 0.8

        print(f'Total price: {total:.2f}')
        money.append(float(total))
        save_order(orders, total)

        more = input('Next customer? (y/n) -> ')
        if more == 'y':
            continue
        else:
            break
    all_orders = input('See all orders so far (y/n) -> ')
    if all_orders == 'y':
        print(f'All Orders for the day:\n'
              f'Hot dog One ordered {HotDogOne.counter} times.\n'
              f'Hot dog Two ordered {HotDogTwo.counter} times\n'
              f'Hot dog Three ordered {HotDogThree.counter} times\n'
              f'Custom Hot dog ordered {CustomHodDog.counter} times\n')
        print(f'Total income for the day: {sum(money):.2f}')

    if HotDogOne.counter > 20:
        print('You are running out of Bread One and Sausage One. You better stock pile it.')
    if HotDogTwo.counter > 20:
        print('You are running out of Bread Two and Sausage Two. You better stock pile it.')
    if HotDogThree.counter > 20:
        print('You are running out of Bread Three and Sausage Three. You better stock pile it.')
    if CustomHodDog.counter > 20:
        print('You are running out of Custom Breads and Custom Sausages. You better stock pile it.')


def sauce_topping():
    sauce = input('Choose you sauce. We have: mayonnaise, mustard, ketchup\n-> ')
    topping = input('Choose you topping. We have: sweet onions, jalapenos, chile, pickles\n-> ')
    return sauce, topping


def display_order(orders):
    print('Your order is:')
    for order in orders:
        print(order)


def save_order(orders, total):
    with open('order_log.txt', 'a') as f:
        for order in orders:
            f.write(f'{order}\n')
        f.write(f'\nTotal price: {total:.2f}\n')
        f.write('\n-------------------\n')


if __name__ == '__main__':
    mian()
