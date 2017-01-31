import pytumblr
import json

BLOG_NAME = 'rjurney'
client = pytumblr.TumblrRestClient(
  'foo',
  'bar',
  'foo2',
  'bar2'
)

all_posts = []
for i in range(0,9):
  posts = client.posts(BLOG_NAME, filter='HTML', limit=20, offset=20*i)
  all_posts += posts['posts']

f = open('posts.json')
j = json.dumps(all_posts)
f.write(j)
f.close()
