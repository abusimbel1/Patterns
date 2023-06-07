from peer import Peer

if __name__ == "__main__":
    example_peer = Peer('example', [])

    peer_1 = Peer('1', [1, 2, 3])
    peer_2 = Peer('2', [4, 5, 6])
    peer_3 = Peer('3', [7, 8, 9])

    example_peer.add_peer(peer_1)
    example_peer.add_peer(peer_2)
    example_peer.add_peer(peer_3)
    print('result for biggest peer:',
          example_peer.find_values([1, 3, 5, 4, 7]))

    peer_1.add_peer(peer_2)
    print('result for small peer:',
          peer_1.find_values([1, 3, 5, 4, 7]))