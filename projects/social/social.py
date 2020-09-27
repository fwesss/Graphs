import random
from itertools import combinations
from typing import Dict, List
from collections import deque


class User:
    def __init__(self, name: str):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def add_friendship(self, user_id: int, friend_id: int) -> None:
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif (
            friend_id in self.friendships[user_id]
            or user_id in self.friendships[friend_id]
        ):
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name: str) -> None:
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users: int, avg_friendships: int) -> None:
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        users = [*range(num_users)]

        # Add users
        for num in users:
            self.add_user(f"Friend {num}")

        # Create friendships
        connections = list(combinations(self.users, 2))
        random.shuffle(connections)

        for connection in connections:
            if len(self.friendships[connection[0]]) < avg_friendships:
                self.add_friendship(connection[0], connection[1])

    def get_all_social_paths(self, user_id: int) -> Dict[int, List[int]]:
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        for user in self.friendships.keys():
            if user == user_id:
                visited[user] = [1]
            else:
                to_visit = deque()
                seen = set()

                to_visit.append([user_id])

                while len(to_visit):
                    path = to_visit.popleft()
                    vertex = path[-1]

                    if vertex == user:
                        visited[user] = path
                        break

                    if vertex not in seen:
                        seen.add(vertex)
                        for neighbor in [
                            neighbor for neighbor in self.friendships[vertex]
                        ]:
                            new_path = list(path) if path is not None else None
                            new_path.append(neighbor)
                            to_visit.append(new_path)

        return visited


if __name__ == "__main__":
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print(connections)
