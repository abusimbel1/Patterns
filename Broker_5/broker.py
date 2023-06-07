class Room:
    def __init__(self, name) -> None:
        self.name = name
        self.receivers = []

    def add_receiver(self, receiver):
        self.receivers.append(receiver)

    def remove_receiver(self, receiver):
        self.receivers.remove(receiver)

    def post(self, data):
        for receiver in self.receivers:
            receiver(data)


class Broker:
    def __init__(self):
        self.rooms = {}

    def add_room(self, room, handler):
        if room not in self.rooms:
            self.rooms[room] = Room(room)
        self.rooms[room].add_receiver(handler)

    def remove_room(self, room, handler):
        if room in self.rooms:
            self.rooms[room].remove_receiver(handler)

    def post(self, room, data):
        if room in self.rooms:
            self.rooms[room].post(data)