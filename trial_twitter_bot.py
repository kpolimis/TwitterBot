# https://www.digitalocean.com/community/tutorials/how-to-create-a-twitterbot-with-python-3-and-the-tweepy-library

import time
import tweepy
import Tkinter
from Tkinter import *
from credentials import *
from cluster1 import *
from cluster2 import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print("bot for {0} account ({1})".format(user.name, user.screen_name))
print("user location: {}".format(user.location))

for follower in tweepy.Cursor(api.followers).items():
    follower.follow()

print("Followed everyone that is following: {}".format(user.name))
ids = []
for page in tweepy.Cursor(api.followers_ids, screen_name="jerawls21").pages():
    ids.extend(page)
    time.sleep(3)

print("total followers: {}".format(len(ids)))

def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(15 * 60)

print("cluster 1 accounts: {}".format(cluster_1))
print("cluster 2 accounts: {}".format(cluster_2))

# print detailed information about each followers
# for follower in limit_handled(tweepy.Cursor(api.followers).items()):
#     if follower.friends_count < 300:
#         print("follower {0}: {1}".format(follower, follower.screen_name))


root = Tkinter.Tk()

label1 = Label( root, text="Search")
E1 = Entry(root, bd =5)

label2 = Label( root, text="Number of Tweets")
E2 = Entry(root, bd =5)

label3 = Label( root, text="Response")
E3 = Entry(root, bd =5)

label4 = Label( root, text="Reply?")
E4 = Entry(root, bd =5)

label5 = Label( root, text="Retweet?")
E5 = Entry(root, bd =5)

label6 = Label( root, text="Favorite?")
E6 = Entry(root, bd =5)

label7 = Label( root, text="Follow?")
E7 = Entry(root, bd =5)

label8 = Label( root, text="Tweet?")
E8 = Entry(root, bd =5)

label9 = Label( root, text="Mass tweet?")
E9 = Entry(root, bd =5)

def getE1():
    return E1.get()

def getE2():
    return E2.get()

def getE3():
    return E3.get()

def getE4():
    return E4.get()

def getE5():
    return E5.get()

def getE6():
    return E6.get()

def getE7():
    return E7.get()

def getE8():
    return E8.get()

def getE9():
    return E9.get()

def mainFunction():
    getE1()
    search = getE1()

    getE2()
    numberOfTweets = 1

    # numberOfTweets = getE2()
    # numberOfTweets = float(numberOfTweets)

    getE3()
    phrase = getE3()

    getE4()
    reply = getE4()

    getE5()
    retweet = getE5()

    getE6()
    favorite = getE6()

    getE7()
    follow = getE7()

    if reply == "yes":
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                #Reply
                print('\nTweet by: @' + tweet.user.screen_name)
                print('ID: @' + str(tweet.user.id))
                tweetId = tweet.user.id
                username = tweet.user.screen_name
                api.update_status("@" + username + " " + phrase, in_reply_to_status_id = tweetId)
                print ("Replied with " + phrase)

            except tweepy.TweepError as e:
                print(e.reason)

            except StopIteration:
                break


    if retweet == "yes":
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                #Retweet
                tweet.retweet()
                print('Retweeted the tweet')

            except tweepy.TweepError as e:
                print(e.reason)

            except StopIteration:
                break

    if favorite == "yes":
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                #Favorite
                tweet.favorite()
                print('Favorited the tweet')

            except tweepy.TweepError as e:
                print(e.reason)

            except StopIteration:
                break

    if follow == "yes":
        for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
            try:
                #Follow
                tweet.user.follow()
                print('Followed the user')

            except tweepy.TweepError as e:
                print(e.reason)

            except StopIteration:
                break
    getE8()
    update_status = getE8()

    if update_status == "yes":
            try:
                api.update_status(phrase)
            except tweepy.TweepError as e:
                print(e.reason)

    getE9()
    mass_tweet = getE9()

    if mass_tweet == "yes":
        media_ids = []
        for follower in cluster_2:
            try:
                #Reply
                print(follower)
                #api.update_status(follower + " " + phrase)
                # https://stackoverflow.com/questions/43490332/sending-multiple-medias-with-tweepy
                # res = api.media_upload('NAP.png')
                res = api.media_upload('GROUP2.gif')
                media_ids.append(res.media_id)
                api.update_status(follower + " "+ phrase, media_ids=media_ids)
                print ("tweeted: " + phrase)

            except tweepy.TweepError as e:
                print(e.reason)

            except StopIteration:
                break


submit = Button(root, text ="Submit", command = mainFunction)

label1.pack()
E1.pack()
label2.pack()
E2.pack()
label3.pack()
E3.pack()
label4.pack()
E4.pack()
label5.pack()
E5.pack()
label6.pack()
E6.pack()
label7.pack()
E7.pack()
label8.pack()
E8.pack()
label9.pack()
E9.pack()
submit.pack(side =BOTTOM)

root.mainloop()
