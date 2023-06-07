import unittest
from broker import Broker, Room


def test_handler(v):
    return v


class TestRoom(unittest.TestCase):

    def test_adds_receivers(self):
        room = Room('test')
        self.assertEqual(len(room.receivers), 0)
        room.add_receiver(test_handler)
        self.assertEqual(len(room.receivers), 1)

    def test_remove_receivers(self):
        room = Room('test')
        self.assertEqual(len(room.receivers), 0)
        room.add_receiver(test_handler)
        self.assertEqual(len(room.receivers), 1)
        room.remove_receiver(test_handler)
        self.assertEqual(len(room.receivers), 0)


class TestBroker(unittest.TestCase):

    def test_adds_room(self):
        broker = Broker()
        room = Room('test')

        self.assertEqual(len(broker.rooms.keys()), 0)
        broker.add_room(room, test_handler)
        self.assertEqual(len(broker.rooms.keys()), 1)

    def test_remove_rooms(self):
        broker = Broker()
        room = Room('test')

        self.assertEqual(len(broker.rooms.keys()), 0)
        broker.add_room(room, test_handler)
        self.assertEqual(len(broker.rooms.keys()), 1)


if __name__ == "__main__":
    unittest.main()