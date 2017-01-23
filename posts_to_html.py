import sys, os, re
from bs4 import BeautifulSoup
import json
from jinja2 import Template

f = open('posts.json')
posts = json.loads(f.read())

template = open('post.html').read()

for i, post in enumerate(posts):
  
  type = post['type']
  if type in ['photo', 'link']:
    continue
  
  id = post['id']
  slug = post['slug']
  url = post['post_url']
  
  print("Trying to parse {}: {}".format(i, url))
  
  body = None
  try:
    body = post['content']
  except:
    try:
      body = post['body']
    except:
      try:
        body = post['trail'][0]['content']
      except:
        pass

  path_parts = url.split("/")
  base_path = "/".join(path_parts[3:5])
  full_path = "/".join(path_parts[3:])
  
  os.system("mkdir -p {}".format(full_path))

  base_html_path = base_path + "/index.html"
  base_file = open(base_html_path, "w")

  full_html_path = full_path + "/index.html"
  full_file = open(full_html_path, "w")
  
  t = Template(template)
  output = t.render(body=body)
  
  base_file.write(output)
  full_file.write(output)
  
  print("Write {} and {} with post...".format(base_html_path, full_html_path))
