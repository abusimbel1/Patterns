class Peer:
    def __init__(self, id, values):
        self.id = id
        self.values = values
        self.peers = []

    def add_peer(self, peer):
        if peer not in self.peers:
            self.peers.append(peer)
            peer.add_peer(self)

    def remove_peer(self, peer):
        if peer in self.peers:
            self.peers.remove(peer)
            peer.remove_peer(self)

    def find_values(self, target_values):
        result = {}
        for peer in self.peers:
            result[peer.id] = [x for x in peer.values if x in target_values]
        return result