from urllib.request import Request, urlopen
from urllib.parse import urlparse
from urllib.error import URLError, HTTPError
from re import match
import argparse
'''
Example Usage : python q1_most_active_users.py --Url "https://s3.ap-south-1.amazonaws.com/haptikinterview/chats.txt"

'''
class Url:
    r"""Url parent class to validate input Url
    Args: 
    url : input chat Url
    """
    def __init__(self, url):
        self._url = url

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        if not urlparse(url):
            raise ValueError("Not a valid url")
        self._url = url
class FileException(Exception):
    pass
class FileValidator(Url):
    def __init__(self, url):
        super(FileValidator,self).__init__(url)
        if not self.url:
            raise FileNotFoundError("Please provide a text Url")
        if self.url[-3:] != "txt":
            raise FileException("Provided Url is not text Url")
        
        
class ActiveUsers(FileValidator):

    def __init__(self, url):
        self.user_hashmap = {}
        super(ActiveUsers, self).__init__(url)

    def __user_map(self, line: str) -> str:
        isusermatch = match(r"((<)(\w+)(>)(:))", line)
        matcheduser = ""
        if isusermatch is not None:
            matcheduser = list(filter(None, isusermatch.groups()))
        return matcheduser[2]

    
    def get_top_users(self):
        try:
            request = Request(self.url)
            chat_file = urlopen(request)
            for line in chat_file:
                if len(line.strip()) != 0:
                    decoded_line = line.decode("utf-8")
                    user = self.__user_map(decoded_line)
                    if user in self.user_hashmap:
                        self.user_hashmap[user] += 1
                    else:
                        self.user_hashmap[user] = 1
            sorted_list = sorted(
                self.user_hashmap, key=self.user_hashmap.get, reverse=True
            )[:3]
            return "Top 3 Active Users are : {}, {} and {}".format(
                sorted_list[0], sorted_list[1], sorted_list[2]
            )

        except HTTPError as err:
            print("The server couldn't fullfill the request.")
            print("Error code: ", err.code)
        except URLError as err:
            print("Failed to reach server.")
            print("Error Reason :", err.reason)


if __name__ == "__main__":
    # Create the parser
    my_parser = argparse.ArgumentParser(description='Program to provide top 3 Active Users')
    my_parser.add_argument('--Url',metavar='url',
                       type=str,
                       nargs="?",
                       default = "https://s3.ap-south-1.amazonaws.com/haptikinterview/chats.png",
                       help='chat text Url')
    args = my_parser.parse_args()
    input_url = args.Url
    TOPUSERS = ActiveUsers(
       url = input_url
    )
    print(TOPUSERS.get_top_users())
