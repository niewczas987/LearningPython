import json, requests
import re


class Requester:
    def __init__(self):
        self.url = 'http://127.0.0.1:5000'

    def request(self, method, endpoint, params=None):
        url = self.url + endpoint
        if method == 'GET':
            r = requests.get(url, params=params)
            return r.text
        else:
            r = requests.post(url, data=params)
            parsed = r.text
            parsed = re.sub('\W+', '', parsed)
            varJson = {}
            varJson['exists'] = parsed[6:]
            print('parsed',varJson)
            return varJson

    def login(self, username, real_name):
        endpoint = '/userExists'
        params = {'username': username}
        user_exists = self.request('POST', endpoint, params)
        return user_exists['exists']

    def create_account(self, username, real_name):
        endpoint = '/userExists'
        params = {'username': username}
        user_exists = self.request('POST', endpoint, params)
        print('user_exists',user_exists)
        if user_exists['exists']:
            return False
        endpoint = '/addUser'
        params['real_name'] = real_name
        self.request('POST', endpoint, params)
        return True

    def get_all_users(self):
        endpoint = '/getAllUsers'
        users = self.request('GET', endpoint)
        return json.loads(users)

    def prepare_conversation(self, user_one, user_two):
        endpoint = '/createConversationDb'
        params = {"user_one": user_one, "user_two": user_two}
        self.request("POST", endpoint, params)
        endpoint = "/get_message_history"
        history = self.request("POST", endpoint, params)
        return history

    def send_message(self, author, friend_name, message):
        endpoint = f"/sendMessage/{friend_name}"
        params = {"author": author, "message": message,}
        self.request("POST", endpoint, params)
        return True