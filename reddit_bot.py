import praw
import config


def bot_login():
		print("Logging in...")
		r= praw.Reddit(username = config.username,
					password = config.password,
					client_id = config.client_id,
					client_secret = config.client_secret,
					user_agent = "spyd3r's dog comment responder v0.1" )
		print("Logged in...")


		return r;

def run_bot(r):
	print("Obtaining 25 comments")
	for comment in r.subreddit("test").comments(limit=25): 					
		if "dog" in comment.body:
			print ("String with \"dog\" found in comment" + comment.id)
			comment.reply("Hey! I also Love Dogs! [Here](https://i.ibb.co/w00hZb5/my-Dog.jpg) is an image of one!")
			print("Replied to comment" +  comment.id)


r = bot_login()


run_bot(r)

