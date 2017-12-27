# -*- coding:utf-8
#!/usr/bin/python
# ----------------------------------------------
# boardSearch.py
# defining board object
# along with its various method
# (c) Jansen Simanullang, 17.12.2017 ~ 27.12.2017
# Medan, North Sumatra, Indonesia
# Surabaya, East Java, Indonesia
# ----------------------------------------------

class boardObject():
# ----------------------------------------------
# __init__(self):
# getDimension(self, board):
# getColumns(self, board):
# display(self, board):
# transpose(self, board)
# flip(self, board):
# lineSearch(self, word, aLine):
# horizontalSearch(self, word, board):
# verticalSearch(self, word, board):
# diagonalSearch(self, word, board):
# allSearch(self, word, board):

# ----------------------------------------------
	def __init__(self):
	# let's start by making sure uneven grid is handled
		cols = self.getColumns(board)
		for i in range(0, len(board)):
			d = cols - len(board[i])
			board[i] = board[i] + d * " "
		return
# ----------------------------------------------
	def getDimension(self, board):
		# get rows and columns length
		rows = len(board)
		cols = self.getColumns(board)
		return rows, cols
# ----------------------------------------------
	def getColumns(self, board):
		# column number should be simple but life is not always simple
		cols = len(board[0])
		# complex column number for an uneven grid
		colmax = lambda board: max([len(row) for row in board])
		cols = colmax(board)
		return cols
# ----------------------------------------------
	def display(self, board):
		# display the board object
		row, col = self.getDimension(board)
		for i in range(0, row):
			for j in range (0, col):
				print board[i][j],
			print ''
# ----------------------------------------------
	def transpose(self, board):
		# board can be transposed
		# transpose array row <--> col
		# horizontal line becomes vertical
		board = zip(*board)
		oBoardT = [''.join(b) for b in board]
		return oBoardT
# ----------------------------------------------
	def flip(self, board):
		# flip horizontally L <--> R
		fb = []
		for b in board:
			b = b[::-1]
			fb.append(''.join(b))
		return fb
# ----------------------------------------------
	def lineSearch(self, word, aLine):
		txtMatch = ''

		def searchFwd(word, aLine):
			o = 0
			ms = []
			me = []

			# search forward
			import re
			mi = re.finditer(word, aLine)
			for m in mi:
				ms.append(m.start())
				me.append(m.end())

			# search forward
			for i in range (0, len(ms)):
				for j in range(ms[i], me[i]):
					if word in aLine[j:j+len(word)]:
						o = o + 1
			#print "match: "+ word+" @("+str(j)+","+str(j+len(word))+")"
			return o

		def searchBwd(word, aLine):
			# search backward
			o = searchFwd(word, aLine[::-1])
			return o
		 
		# search forward from L --> R
		o = searchFwd(word, aLine)
		# search backward from R --> L
		o += searchBwd(word, aLine)
	 
		return o, txtMatch
# ----------------------------------------------
	def horizontalSearch(self, word, board):
		# search the board for word
		rows, cols = self.getDimension(board)
		nMatchWord = 0

		for i in range (0, rows):
			aLine = board[i]
			nMatch, txtMatch = self.lineSearch(word, aLine)
			#print i+1, str(nMatch)+" horizontal matches: ", txtMatch
			nMatchWord = nMatchWord + nMatch

		return nMatchWord
# ----------------------------------------------
	def verticalSearch(self, word, board):
		# horizontal board can be transposed to vertical board
		# vertical search is equal to horizontal search performed to transposed board
		nMatchWord = self.horizontalSearch(word, self.transpose(board))

		return nMatchWord
# ----------------------------------------------
	def diagonalSearch(self, word, board):
		# search the board for word in its diagonal
		rows, cols = self.getDimension(board)
		nMatchWord = 0

		# 1st diagonal: L --> R downward, \
		for i in range(0, cols):
			aLine = ''
			for j in range(0,rows):
				k = i + j
				if (k < cols):
					aLine = aLine + board[j][k]
			#print aLine
			nMatch, txtMatch = self.lineSearch(word, aLine)
			#print [i+1], str(nMatch)+" matches: ", txtMatch
			nMatchWord = nMatchWord + nMatch

		# 2nd diagonal: R --> L downward /
		for i in range(0, cols):
			aLine = ''
			for j in range(0,rows):
				k = i + j
				if (k < cols):
					aLine = aLine + self.flip(board)[j][k]
			#print aLine
			nMatch, txtMatch = self.lineSearch(word, aLine)
			#print [i+1], str(nMatch)+" matches: ", txtMatch
			nMatchWord = nMatchWord + nMatch

		return nMatchWord
# ----------------------------------------------
	def allSearch(self, word, board):
		# sum up all the eight (8) direction
		return self.horizontalSearch(word, board) +\
		self.verticalSearch(word, board) +\
		self.diagonalSearch(word, board)
# ----------------------------------------------
def solveInputFile(file_name):

	import os
	scriptDirectory = os.path.dirname(os.path.abspath(__file__)) + "/"
	file_path = scriptDirectory + "/" + file_name

	global board
	with open(file_path, 'r') as f:
		lines = f.readlines()
		lread = lambda ln : lines[ln].strip()
		# find the number of case T
		ln = 0
		T = int(lread(ln))
		#print "T = ", T
    
		for t in range(0, T):
			# find the number of rows R
			ln +=1
			R = int(lread(ln))
			#print "--------------------"
			#print "R = ", R
			# find the number of columns C
			ln +=1
			C = int(lread(ln))
			#print R, C
			#print "C = ", C
			# find board of words
			board = []
			for i in range(0, R):
				ln += 1
				board.append(lread(ln))
			ln += 1
			# find the word to seek
			W = lread(ln)
			oBoard = boardObject()
			#oBoard.display(board)
			#print W
			print "Case "+str(t+1)+":", oBoard.allSearch(W, board)
			#print "Horizontal: ", oBoard.horizontalSearch(W, board)
			#print "Vertikal: ", oBoard.verticalSearch(W, board)
			#print "Diagonal: ", oBoard.diagonalSearch(W, board)

solveInputFile("input1.in")
