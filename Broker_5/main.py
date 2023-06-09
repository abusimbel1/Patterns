from broker import Broker, Room


def upper_case(text):
    print(f'MANIPULATE {text.upper()}')


def lower_case(text):
    print(f'manipulate {text.lower()}')


if __name__ == '__main__':
    broker = Broker()

    loby_1 = 'Loby for even numbers'
    loby_2 = 'Loby for odd numbers'
    broker.add_room(loby_1, upper_case)
    broker.add_room(loby_1, lower_case)

    broker.add_room(loby_2, upper_case)
    broker.add_room(loby_2, lower_case)

    broker.post(loby_1, '2 4')
    broker.post(loby_2, '1 3')