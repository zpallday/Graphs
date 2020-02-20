import random


class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)











class User:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name

class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}



    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """

        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
            return False
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
            return False
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)
            return True



    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()



    def populate_graph(self, num_users, avg_friendships):
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
        # Add users
        # Create friendships
        for i in range(num_users):
            self.add_user(f"User {i+1}")

        # possible_friendship = []
        # for user_id in self.users:
        #     for friend_id in range(user_id + 1, self.last_id + 1):
        #         possible_friendship.append((user_id, friend_id))
        
        # random.shuffle(possible_friendship)
        # print("-----")
        # print(possible_friendship)
        # print("-----")

        # for i in range(num_users * avg_friendships // 2):
        #     friendship = possible_friendship[i]
        #     self.add_friendship(friendship[0], friendship[1])
        target_friendships = (num_users * avg_friendships)
        total_friendships = 0
        collisions = 0
        while total_friendships < target_friendships:
            user_id = random.randint(1, self.last_id)
            friend_id = random.randint(1, self.last_id)
            if self.add_friendship(user_id, friend_id):
                total_friendships += 2
            else:
                collisions += 1
        print(f'collisions: {collisions}')




    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument
        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.
        The key is the friend's ID and the value is the path.
        """
        q = Queue()
        visited = {} 
        q.enqueue([user_id])  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        while q.size() > 0:
            path = q.dequeue()
            v = path[-1]
            if v not in visited:
                visited[v] = path
                for friend_id in self.friendships[v]:
                    path_copy = path.copy()
                    path_copy.append(friend_id)
                    q.enqueue(path_copy)
        return visited





if __name__ == '__main__':
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print("-----")
    print(sg.users)
    print("-----")
    print(sg.friendships)
    connections = sg.get_all_social_paths(1)
    print("-----")
    print(connections)

    connection_lens = [len(v) for v in connections.values()]

    # print('The lengths of all social paths')
    # print(connection_lens)
    # print(sum(connection_lens) // len(connection_lens))