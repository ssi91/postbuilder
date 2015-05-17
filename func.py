__author__ = 'ssi'


def addCommentForm(markdown, type = "post"):
	sourse = ""
	if (type == "post"):
		sourse = "_post/"
	f = open("commentform.html", 'r')
	commentForm = f.read()
	f.close()
	f = open(sourse + markdown, 'a')
	f.write(commentForm)
	f.close()


def addPost(markdown, type = 'post'):
	sourse = ""
	if (type == "post"):
		sourse = "_post/"
	f = open("post.html", 'r')
	post = f.read()
	f.close()
	f = open(sourse + markdown, 'a')
	f.write(post)
	f.close()


def createMarkdown(filetitle, type = 'post'):
	import datetime

	sourse = ""
	if (type == "post"):
		sourse = "/home/ssi/octopress/source/_posts/"
	now_time = datetime.datetime.now()
	filename = now_time.strftime("%Y-%m-%d") + '-' + filetitle + '.markdown'
	print (filename)
	f = open(sourse + filename, 'w')
	f.close()
