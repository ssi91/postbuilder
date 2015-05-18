__author__ = 'ssi'


class MD:
	def __init__(self, octoPath):
		self.octoPath = octoPath
		self.sourcePath = octoPath + "source/"

	def createMarkdown(self, filetitle, type = 'post'):
		import datetime

		sourse = self.sourcePath
		if (type == "post"):
			sourse += "_posts/"
		now_time = datetime.datetime.now()
		filename = now_time.strftime("%Y-%m-%d") + '-' + filetitle + '.markdown'
		f = open(sourse + filename, 'w')
		f.close()
		self.filename = sourse + filename

	def writeMeta(self, title, categories = [], type = 'post'):
		if self.filename:
			import datetime

			f = open(self.filename, 'w')
			f.write('---\n')
			f.write('layout: ' + type + '\n')
			f.write('title: \"' + title + '\"\n')
			f.write('date: ' + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' +0600\n')
			f.write('comments: true\n')
			f.write('categories:\n')

			for cat in categories:
				f.write('- ' + cat + '\n')

			f.write('---\n')
			f.close()
			self.isMetaMetaWrited = True

	def addPost(self, type = 'post'):
		if self.isMetaMetaWrited:
			sourse = self.sourcePath
			if (type == "post"):
				sourse += "_posts/"
			f = open("post.md", 'r')
			post = f.read()
			f.close()
			f = open(self.filename, 'a')
			f.write(post)
			f.close()

	def addCommentForm(self, type = "post"):
		if self.isMetaMetaWrited:
			sourse = self.sourcePath
			if (type == "post"):
				sourse += "_posts/"
			f = open("commentform.html", 'r')
			commentForm = f.read()
			f.close()
			f = open(self.filename, 'a')
			f.write(commentForm)
			f.close()
