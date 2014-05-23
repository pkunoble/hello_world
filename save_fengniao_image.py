#!/usr/bin/python

import os.path
import urllib2
import urlparse
import re
import sys


def GetImageFileName(image_url):
  parsed = urlparse.urlparse(image_url)
  return os.path.basename(parsed.path)


kImageUrlPattern = re.compile(r'var gbig_pic = "(.+)"')

def GetImageUrl(page_url):
  page = urllib2.urlopen(page_url).read()
  matched = kImageUrlPattern.search(page)
  if matched:
    return matched.group(1)
  else:
    return ""


def SaveImage(page_url):
  image_url = GetImageUrl(page_url)
  if not image_url:
    return False

  image_data = urllib2.urlopen(image_url).read()
  writer = open(GetImageFileName(image_url), "wb")
  writer.write(image_data)
  return True


if __name__ == "__main__":
  if len(sys.argv) == 1:
    print "save_fengniao_image.py url1 url2 ..."
    sys.exit(1)

  for url in sys.argv[1:]:
    print url, "ok" if SaveImage(url) else "failed"
