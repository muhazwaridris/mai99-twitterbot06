import tweepy
import time

print ('Loading mai99-twitterbot06 program...')

consumer_key = 'xxxxxxxxx'
consumer_secret = 'xxxxxxxxx'
access_token = 'xxxxxxxxx'
access_token_secret = 'xxxxxxxxx'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Last Saved Follower ID for testing.
FILE_NAME = 'last_follower.txt'
your_account = api.me()
follower = api.followers_ids(your_account)
friends = api.friends_ids(your_account)

def retrieve_last_follower(file_name):
    f_read = open(file_name, 'r')
    last_follower = f_read.read().strip()
    f_read.close()
    return last_follower

def store_last_follower(last_follower, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_follower))
    f_write.close()
    return

def capture():
    for last_f in follower:
        last_follower = (api.get_user(last_f))
        store_last_follower(last_follower.screen_name, FILE_NAME)
        print ('Your last follower is @'+last_follower.screen_name)
        break

def send_message():
    last_follower = retrieve_last_follower(FILE_NAME)
    for last_f in follower:
        last_follower = (api.get_user(last_f))
        dm_text = ('Hai @'+ last_follower +', Thank you for following!')
        if last_follower == last_follower.screen_name:
            break
        else:
            api.send_direct_message(screen_name=last_follower, text=dm_text)
            print ('Direct Message has been sent to @'+last_follower.screen_name)

def execute():
    if program == '1':
        send_message()
        print ('The mai99-twitterbot06 program will be terminated!')
        print ('<=============================================================>')
        time.sleep(3)
        exit()
    elif program == '9':
        capture()
        print ('The mai99-twitterbot06 program will be terminated!')
        print ('<=============================================================>')
        time.sleep(3)
        exit()
    elif program == '0':
        print ('The mai99-twitterbot06 program will be terminated!')
        print ('<=============================================================>')
        time.sleep(3)
        exit()
    else:
        print('Input error, please try again!')
        print ('<=============================================================>')
        time.sleep(3)

while True:
    print ('Enter 1 to send a message to new follower')
    print ('Enter 9 to capture your last follower')
    print ('Enter 0 to terminate mai99-twitterbot06 program')
    program = input('Program to be execute: ')
    execute()