import praw  

#Unique username
r = praw.Reddit(user_agent='contentPlease!')
#Subreddit we are looking through
sub="aww"
#Number of submissions we want to get
items=20
submissions = r.get_subreddit(sub).get_top(limit=items)

#hard coded string
hcs="{{"
 
for item in submissions:
    hcs+="\""
    hcs+=str(item.url)
    hcs+="\","
    print (item.url)
	
hcs+="\"\"}}"
print(hcs)