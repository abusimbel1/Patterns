import unittest
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from peer import Peer


class TestPeer(unittest.TestCase):

    def test_find_value(self):
        peer_1 = Peer('first peer', [])
        peer_2 = Peer('second peer', [1, 2])
        peer_3 = Peer('third peer', [1, 2, 3])
        peer_4 = Peer('4th peer', [4, 7, 17])
        peer_5 = Peer('5th peer', [111, 222, 333])

        peer_1.add_new_peer(peer_2)
        peer_1.add_new_peer(peer_3)
        peer_1.add_new_peer(peer_4)
        peer_1.add_new_peer(peer_5)
        self.assertDictEqual(peer_1.find_values([1]), {'4th peer': [], '5th peer': [], 'second peer': [1], 'third peer': [1]})
        self.assertDictEqual(peer_1.find_values([1, 2]), {'4th peer': [], '5th peer': [], 'second peer': [1, 2], 'third peer': [1, 2]})
        self.assertDictEqual(peer_1.find_values([]), {'4th peer': [], '5th peer': [], 'second peer': [], 'third peer': []})
        self.assertDictEqual(peer_1.find_values([1, 2, 3, 4, 222, 333, 17, 7]), {'second peer': [1, 2], 'third peer': [1, 2, 3], '4th peer': [4, 7, 17], '5th peer': [222, 333]})

    def test_remove_peers(self):
        peer_1 = Peer('second peer', [])
        peer_2 = Peer('first peer', [])

        peer_1.add_new_peer(peer_2)
        self.assertEqual(len(peer_1.peers), 1)

        peer_1.remove_peer(peer_2)
        self.assertEqual(len(peer_1.peers), 0)

    def test_adds_peers(self):
        peer_1 = Peer('second peer', [])
        peer_2 = Peer('first peer', [])

        self.assertEqual(len(peer_1.peers), 0)
        self.assertEqual(len(peer_2.peers), 0)

        peer_1.add_new_peer(peer_2)

        self.assertEqual(len(peer_1.peers), 1)
        self.assertEqual(len(peer_2.peers), 1)


if __name__ == "__main__":
    unittest.main()