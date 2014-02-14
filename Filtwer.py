print ""
print "***********************************************************"
print "*  ______   ______   ______   ______   _______   __       *"
print "* |  ____| |  __  | |   ___| |__  __| |  ___  | |  |      *"
print "* | |____  | |  | | |  |        ||    | |   | | |  |      *"
print "* |_____ | | |  | | |  |        ||    | |___| | |  |      *"
print "*  _____ | | |__| | |  |___   __||__  | |   | | |  |____  *"
print "* |______| |______| |______| |______| |_|   |_| |_______| *"
print "*                                                         *"
print "*      F I L T W E R                                      *"
print "*                                                         *"
print "***********************************************************"
print "                                                       "
print "Python Script written by Adam Rapley (Red Dot Innovations)"
print "@AutomatedRandom // me [at] adamrapley [dot] com"
print "                                                       "
print "***********************************************************"
print ""

import twitter
api = twitter.Api(consumer_key='<redacted>',
				  consumer_secret='<redacted>',
				  access_token_key='<redacted>',
				  access_token_secret='<redacted>')

while True:
		menu1select = raw_input("1. You\n2. Others\n> ")
		if menu1select in ["1","2"]: break
		print "Please enter a valid entry!"

if menu1select == "1":
	while True:
		menu2select = raw_input("1. Tweet\n2. Last 5 Tweets\n3. Search last 200 tweets by keyword\n> ")
		if menu2select in ["1","2","3"]: break
		print "Please enter a valid entry!"

	if "1" == menu2select:
		statusinput = raw_input("Tweet: ")
		status = api.PostUpdate(statusinput)
		print "Sucessfully tweeted!"

	elif "2" == menu2select:
		hometweet = api.GetHomeTimeline()
		for i in (0, len(hometweet)):
			print hometweet[i]

	else:
		keyword = raw_input("keyword: ")

def returnFormattedTweet(tweetid):
	print [tweet.GetName]
	print 


#Additional functionality ID
#Tweets by user ID