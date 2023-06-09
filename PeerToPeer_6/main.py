from peer import Peer

if __name__ == "__main__":
    example_peer = Peer('Mock', [])

    peer_1 = Peer('First', [2, 14, 44])
    peer_2 = Peer('Second', [64, 53, 90])
    peer_3 = Peer('Third', [567, 866, 999])

    example_peer.add_new_peer(peer_1)
    example_peer.add_new_peer(peer_2)
    example_peer.add_new_peer(peer_3)

    print('Biggest peer:',
          example_peer.find_values([14, 90, 53, 567, 866]))

    peer_1.add_new_peer(peer_2)
    print('Smaller peer:',
          peer_1.find_values([2, 53, 14, 90, 64]))