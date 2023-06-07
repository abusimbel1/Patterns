import unittest
from peer import Peer


class TestPeer(unittest.TestCase):

    def test_adds_peers(self):
        peer_1 = Peer('peer 2', [])
        peer_2 = Peer('peer 1', [])

        self.assertEqual(len(peer_1.peers), 0)
        self.assertEqual(len(peer_2.peers), 0)

        peer_1.add_peer(peer_2)

        self.assertEqual(len(peer_1.peers), 1)
        self.assertEqual(len(peer_2.peers), 1)

    def test_remove_peers(self):
        peer_1 = Peer('peer 2', [])
        peer_2 = Peer('peer 1', [])

        peer_1.add_peer(peer_2)
        self.assertEqual(len(peer_1.peers), 1)

        peer_1.remove_peer(peer_2)
        self.assertEqual(len(peer_1.peers), 0)

    def test_find_value(self):
        peer_1 = Peer('peer 1', [])
        peer_2 = Peer('peer 2', [1, 2])

        peer_1.add_peer(peer_2)
        self.assertDictEqual(peer_1.find_values([1]), {"peer 2": [1]})
        self.assertDictEqual(peer_1.find_values([1, 2]), {"peer 2": [1, 2]})
        self.assertDictEqual(peer_1.find_values([]), {"peer 2": []})
        self.assertDictEqual(peer_1.find_values(
            [1, 2, 3, 4]), {"peer 2": [1, 2]})


if __name__ == "__main__":
    unittest.main()