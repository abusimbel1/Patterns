from broker import Broker, Room


def handle_big(sound):
    print(f'HANDLE {sound.upper()}')


def handle_small(sound):
    print(f'handle {sound.lower()}')


if __name__ == '__main__':
    broker = Broker()

    room_1 = 'Room for cats'
    room_2 = 'Room for dogs'
    broker.add_room(room_1, handle_big)
    broker.add_room(room_1, handle_small)

    broker.add_room(room_2, handle_small)
    broker.add_room(room_2, handle_small)

    broker.post(room_1, 'meow meow')
    broker.post(room_1, 'bark bark')