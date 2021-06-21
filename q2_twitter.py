import os
import uuid


"""
1. What technologies would you use to build out this platform? Please tell us the
languages, databases, tools / servers you would use to build out the above platform.

Languages : Golang, Python
Database : Cassandra(used for high velocity writes, and lower velocity reads.)
,Hadoop(used to process unstructured and large datasets, hundreds of billions of rows.)
,MySQL ( UserInfoMetadata), 
Redis ( Inmemory storage)
,Vertica (used for analytics and large aggregations and joins so they don’t have to write MapReduce jobs.)

Tools:
-----
Zookeeper, Load Balancers, APi Server, 

2. Write the schema of your database that is going to store the data. We want to see this in
detail to see where the all the different information will be stored

Tweet Table:
TweetID : int, PK
UserID : int
Content: varchar(140)
TweetLatitude : int
TweetLongitude : int
UserLatitude : int
UserLongitude: int
CreationDate : datetime

User Table:
UserID: int,PK
Name : varchar(20)
Email : varchar(32)
DOB : datetime
CreationDate : datetime
LastLogin : datetime

UserFollow:
UserId1 : int,PK
UserId2 : int,PK

4. How much can the system you have built scale up to? What are the limiting factors of
your system and when will it start failing?

Load Estimation
---------------
Let's assume we have 1 billion users, with 200 million daily active users (DAU). 
Also assume we have 100 million new tweets every day, and on average each user follows 200 people.

How many total tweet-views? Let's assume on average a user visits their timeline twice a day and visits 5 other people's pages.
On each page if a user sees 20 tweets, then the no. of views our system will generate is: 200M DAU * ((2 + 5) * 20 tweets) => 28B/day

Storage Estimates
-----------------

Let's say each tweet has 140 characters and we need two bytes to store a character without compression.
 Assume we need 30 bytes to store metadata with each tweet (like ID, timestamps, etc.). Total storage we would need is:
100M new daily tweets * ((140 * 2) + 30) bytes => ~28 GB/day



Bandwidth Estimates
-------------------
Since total ingress is 28TB per day, then it will translate to:
28TB / (24 * 60 * 60) ~= 32 MB/sec

Limitations :
-----------

1. What if a user becomes hot? There will be lots of queries on the server holding that user. 
This high load will affect the service's performance.
2 .Over time, some users will have more data compared to others. Maintaining a uniform distribution of growing data 
is quite difficult.
"""
class NotFound(Exception):
    pass

class User:

    def __init__(self):
        self._name = None
        self._user_id = None
        self._user_map = {}

    @property
    def user_name(self):
        return self._name

    @user_name.setter
    def user_name(self, name):
        if len(name) == 0:
            raise ValueError("Name cannot be empty")
        self._name =name
        self._user_id = str(uuid.uuid3(uuid.NAMESPACE_DNS, self.user_name))
        self._user_map[self.user_id] = self.user_name

    @property
    def user_id(self):
        return self._user_id

    def __str__(self):
        return "{}".format(
            self._user_map
        )

    @property
    def user_map(self):
        return self._user_map

    def _get_user_name(self, user_id):
        if user_id not in self.user_map:
            raise NotFound("user id doesn't exist")

        return self.user_map[user_id]
        
    def _get_user_id(self, user_name):
        for key, value in self.user_map.items():
            if value == user_name:
                name = key
                break
        else:
            raise NotFound("User doesn't exist")

        return name

class Follow(User):
    def __init__(self):
        super(Follow,self).__init__()
        self._follow_map = {}
        self._from_user_id = None
        self._to_user_id = None
    @property
    def from_user_id(self):
        return self._from_user_id

    @property
    def to_user_id(self):
        return self._to_user_id
    
    @property
    def follow_map(self):
        return self._follow_map
        
    def follow(self,from_user_name,to_user_name,user):
        self._from_user_id = user._get_user_id(from_user_name)
        self._to_user_id = user._get_user_id(to_user_name)
        if self.from_user_id not in self.follow_map:
            self.follow_map[self._from_user_id] = []
            self.follow_map[self._from_user_id].append(self._to_user_id)
        else:
            self.follow_map[self._from_user_id].append(self._to_user_id)


    def __str__(self):
        return '{}'.format(self._follow_map)


class Post:
    def __init__(self):
        pass


if __name__ == "__main__":
    USER = User()
    USER.user_name = "Bhargav"
    USER.user_name = "Ravi"
    USER.user_name = "Rajeev"
    FOLLOW = Follow()
    FOLLOW.follow("Bhargav","Ravi",USER)
    FOLLOW.follow("Bhargav","Rajeev",USER)
    FOLLOW.follow("Ravi","Rajeev",USER)
    FOLLOW.follow("Rajeev","Bhargav",USER)

    print(FOLLOW)
