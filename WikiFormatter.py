from __future__ import print_function
import re

class WikiFormatter:
	text = ""
	regex = {
		"monospace_short":	(r'\`(.*)\`', r'<pre>\1</pre>'),
		"monospace_start":	(r'\{\{\{', r'<pre>'),
		"monospace_end":	(r'\}\}\}', r'</pre>'),
		"underline":		(r'\_\_(.*)\_\_', r'<ul>\1</ul>'),
		"strikethrough":	(r'~~(.*)~~', r'<strike>\1</strike>'),
		"superscript":		(r'\^([\w\S]+)\^', r'<sup>\1</sup>'),
		"subscript":		(r',,([\w\S]+),,', r'<sub>\1</sub>'),
		"linebreak":		(r'\[\[BR\]\]', r'<br/>'),
		"nowiki":			(r'(?<!#)!([\w\S]+)', r'<nowiki>\1</nowiki>')
			#With a fix for #!
		}

	def __init__(self, input_text):
		self.text = input_text.replace('\r\n', '\n') #Strip windows \r\n into \n

	def parse(self):
		self.parseUnorderedLists()
		self.parseNumberedLists()
		self.parseTables()
		self.parseLinks()
		for name, regex in self.regex.iteritems():
			self.text = re.sub(regex[0], regex[1], self.text)
		return self.text

	def parseLinks(self):
		#Some regex for thought
		# r'\[wiki:(\w\S)]' -> r'[[\1]]' matches basic wiki links
		# r'\[wiki:[\"](.+)[\"]\]' -> r'[[\1]]' matches custom pages
		# r'\[wiki:]
		return False


	def parseDefinitions(self):
		#Grab the iterator so we can get the next line when needed
		lines = self.text.split('\n').__iter__()
		output = ""
		for line in lines:
			if len(line) > 3:
				if line[0] == " " and line[-2:] == "::": #Matches " Word to define::"
					#we have a definition
					word = line[1:-2]
					definition = lines.next().strip()
					output += "\n; " + word
					output += "\n: " + definition
				else:
					output += "\n" + line
			else:
				output += "\n" + line
		self.text = output


	def parseUnorderedLists(self):
		depth = 0
		lineNumber = 0
		lineIndent = {}
		lineIndent.setdefault(0)
		output = ""
		for line in self.text.split('\n'):
			lineNumber += 1
			if line.startswith(' ') and line.find('*') > 0:
				#get position of first asterisk
				lineIndent[lineNumber] = line.find('*')
				if lineIndent[lineNumber] > lineIndent.get(lineNumber - 1):
					depth += 1
				elif lineIndent[lineNumber] < lineIndent.get(lineNumber - 1):
					depth -= 1
				line = "%s %s" % ("*" * depth, line[lineIndent[lineNumber]+2:])
			else:
				depth = 0
			

			output = "%s\n%s" % (output, line)
		self.text = output

	def parseNumberedLists(self):
		depth = 0
		lineNumber = 0
		lineIndent = {}
		lineIndent.setdefault(0)
		output = ""
		r = re.compile(r"[ai0-9][.]")
		for line in self.text.split('\n'):
			matches = r.findall(line)
			lineNumber += 1
			if len(matches):
				if line.startswith(" ") and line[:line.find(matches[0])].strip() == "":
					#we are in an ordered list!!!
					#Luckily(?) MediaWiki is simpler than Trac for these, so we can skip the details
					#Trac also ignores changes in the numbering, like 1. then a. on the same indentation.
					#So once again, we only handle indentation
					lineIndent[lineNumber] = line.find(matches[0])

					if lineIndent[lineNumber] > lineIndent.get(lineNumber - 1):
						depth += 1
					if lineIndent[lineNumber] < lineIndent.get(lineNumber - 1):
						depth -= 1
					line = ("#" * depth) + " " + line[line.find(matches[0])+len(matches[0]):]
				else:
					depth = 0
			output += "\n" + line
		self.text = output

	def parseTables(self):
		output = ""
		inTable = False
		for line in self.text.split('\n'):
			if line.strip().startswith("||"):
				if not inTable: #Start a new table
					inTable = True
					output += "\n{| class=\"wikitable\""
				else:
					output += "\n|-"
				row = line.split("||")[1:-1]
				for column in row:
					output += "\n| " + column
			else:
				if inTable:
					output += "\n|}"
					inTable = False
				output += "\n" + line
		self.text = output
		return output 




if __name__ == '__main__':
	import sys
	import argparse
	parser = argparse.ArgumentParser(description = "Wiki Formatting Convertor from Trac to MediaWiki")
	parser.add_argument('file', type=str, help="Trac source input file")
	parser.add_argument('-o', '--output', type=str, help="Output file, defaults to STDOUT", default=sys.stdout)
	args = parser.parse_args()
	if args.output != sys.stdout:
		args.output = open(args.output, 'w')
	output = args.output
	input_file = open(args.file, 'r')
	input_text = input_file.read()
	input_file.close()

	formatter = WikiFormatter(input_text)
	formatter.parseDefinitions()
	print(formatter.parse(), file=output)
