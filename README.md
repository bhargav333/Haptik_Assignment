# Haptik Assignment
#### Q1 : You can find a file called chats.txt here, the file contains a group conversation among a group of people.. Write a function that reads from the file and returns the 3 most active users in the conversation.
```sh
python q1_most_active_users.py --Url "https://s3.ap-south-1.amazonaws.com/haptikinterview/chats.txt"
```

#### Q3 : Write a function that given a list of strings and an input string will return True if you can create the input string from the list of strings and will return False if you cannot create the string from the list.
```sh
python q3_can_create.py --list back end front end tree --inputStr frontend
```

#### Q2 : Twitter is a micro blogging platform where users post “tweets” which are ristricted to 140 characters. In this question we want you to build twitter as a platform.
-------
 1. What technologies would you use to build out this platform? Please tell us the
languages, databases, tools / servers you would use to build out the above platform.
''
''
Languages : Golang, Python
Database : Cassandra(used for high velocity writes, and lower velocity reads.)
          ,Hadoop(used to process unstructured and large datasets, hundreds of billions of rows.)
,MySQL ( UserInfoMetadata), Redis ( Inmemory storage),Vertica (used for analytics and large aggregations and joins so they don’t have to write MapReduce jobs.)
Tools: Zookeeper, Load Balancers, APi Server, 
''
-----------------
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
\
User Table:
UserID: int,PK
Name : varchar(20)
Email : varchar(32)
DOB : datetime
CreationDate : datetime
LastLogin : datetime
\
UserFollow:
UserId1 : int,PK
UserId2 : int,PK
-----------------
 4. How much can the system you have built scale up to? What are the limiting factors of
your system and when will it start failing?

Load Estimation: 

Let's assume we have 1 billion users, with 200 million daily active users (DAU). 
Also assume we have 100 million new tweets every day, and on average each user follows 200 people.
How many total tweet-views? Let's assume on average a user visits their timeline twice a day and visits 5 other people's pages.
On each page if a user sees 20 tweets, then the no. of views our system will generate is: 200M DAU * ((2 + 5) * 20 tweets) => 28B/day


Storage Estimates:

Let's say each tweet has 140 characters and we need two bytes to store a character without compression.
 Assume we need 30 bytes to store metadata with each tweet (like ID, timestamps, etc.). Total storage we would need is:
100M new daily tweets * ((140 * 2) + 30) bytes => ~28 GB/day
Bandwidth Estimates:-
Since total ingress is 28TB per day, then it will translate to:
28TB / (24 * 60 * 60) ~= 32 MB/sec

Limitations :
- What if a user becomes hot? There will be lots of queries on the server holding that user. 
This high load will affect the service's performance.
- Over time, some users will have more data compared to others. Maintaining a uniform distribution of growing data 
is quite difficult.
