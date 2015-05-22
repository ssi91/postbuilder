__author__ = 'ssi'
import sys
import argparse
import buildmd
import subprocess
import os


def getParser():
	parser = argparse.ArgumentParser()
	parser.add_argument('-cat', '--categories', nargs = '+')
	parser.add_argument('-t', '--type', choices = ['post', 'page'], default = 'post')
	parser.add_argument('-page', action = 'store_const', const = True)
	parser.add_argument('-c', action = 'store_const', const = True)
	parser.add_argument('-g', '--generate', action = 'store_const', const = True)
	parser.add_argument('-d', '--deploy', action = 'store_const', const = True)
	parser.add_argument('-ft', '--filetitle', required = True)
	parser.add_argument('-pt', '--posttitle', required = True)

	return parser


if __name__ == '__main__':
	parser = getParser()
	namespace = parser.parse_args(sys.argv[1:])

	octoDir = '/home/ssi/octopress/'

	md = buildmd.MD(octoDir)
	md.createMarkdown(namespace.filetitle, namespace.type)
	md.writeMeta(namespace.posttitle, namespace.categories, namespace.type)

	md.addPost()
	if namespace.c:
		md.addCommentForm()

	if namespace.generate:
		os.chdir(octoDir)
		subprocess.call("cd ~/octopress", shell = True)
		subprocess.call("rake generate", shell = True)
		if namespace.deploy:
			subprocess.call("rake deploy", shell = True)
