class Peer:
    def __init__(self, id, values):
        self.id = id
        self.values = values
        self.peers = []

    def remove_peer(self, peer):
        if peer in self.peers:
            self.peers.remove(peer)
            peer.remove_peer(self)

    def add_new_peer(self, peer):
        if peer not in self.peers:
            self.peers.append(peer)
            peer.add_new_peer(self)

    def find_values(self, target_values):
        res = {}
        for peer in self.peers:
            res[peer.id] = [x for x in peer.values if x in target_values]
        return res