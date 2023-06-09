import sys
import os
import unittest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from broker import Broker, Room


def test_handler(v):
    return v

class TestBroker(unittest.TestCase):

    def test_adds_room(self):
        broker = Broker()
        room = Room('some_test_room')
        room_2 = Room('some_second_test_room')

        self.assertEqual(len(broker.rooms.keys()), 0)
        broker.add_room(room, test_handler)
        self.assertEqual(len(broker.rooms.keys()), 1)
        broker.add_room(room_2, test_handler)
        self.assertEqual(len(broker.rooms.keys()), 2)

    def test_remove_rooms(self):
        broker = Broker()
        room = Room('test')
        room_2 = Room('test_room_2')
        room_3 = Room('test_room_3')

        self.assertEqual(len(broker.rooms.keys()), 0)
        broker.add_room(room, test_handler)
        broker.add_room(room_2, test_handler)
        broker.add_room(room_3, test_handler)
        self.assertEqual(len(broker.rooms.keys()), 3)

class TestRoom(unittest.TestCase):

    def test_adds_receivers(self):
        room = Room('some_test_room')
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



if __name__ == "__main__":
    unittest.main()