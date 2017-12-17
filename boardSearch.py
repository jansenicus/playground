# -*- coding:utf-8
#!/usr/bin/python
# ----------------------------------------------
# boardSearch.py
# defining board object
# along with its various method
# (c) Jansen Simanullang, 17.12.2017
# Medan, North Sumatra, Indonesia
# Surabaya, East Java, Indonesia
# ----------------------------------------------


class boardObject():

 def getDimension(self, board):
 # get rows and columns length
		rows = len(board)
		cols = len(board[0])
		return rows, cols

 def display(self, board):
 # display the board object
		row, col = self.getDimension(board)
		for i in range(0, row):
			for j in range (0, col):
				print board[i][j],
			print ''

 def transpose(self, board):
 # board can be transposed
 # transpose array row <--> col
 # horizontal line becomes vertical
		board = zip(*board)
		tboard = [''.join(b) for b in board]
		return tboard
		
 def flip(self, board):
 # flip horizontally L <--> R
  fb = []
  for b in board:
   b = b[::-1]
   fb.append(''.join(b))
  return fb

 def lineSearch(self, word, aLine):
		txtMatch = ''
		matchLR = []
		matchRL = []
		
		# search forward from L --> R
		import re
		findLR = re.finditer(word, aLine)

		for match in findLR:
			matchIdx = (match.start(), match.end())
			matchLR = matchLR + [matchIdx]

		# search backward from R --> L
		findRL = re.finditer(word[::-1], aLine)

		for match in findRL:
			matchIdx = ((match.start(), match.end()))
			matchLR = (matchLR) + [matchIdx]

		# remove duplicates
		# they may contain palindromes
		# which counted twice of the same word
		matchSet = set(matchRL + matchLR)
		nMatch = len(matchSet)

		# see location of matches
		for match in matchSet:
			txtMatch = txtMatch + word + " @(%s, %s) " % match

		return nMatch, txtMatch


 def horizontalSearch(self, word, board):
 # search the board for word
		rows, cols = self.getDimension(board)
		nMatchWord = 0

		for i in range (0, rows):
			aLine = board[i]
			nMatch, txtMatch = self.lineSearch(word, aLine)
			print i+1, str(nMatch)+" matches: ", txtMatch
			nMatchWord = nMatchWord + nMatch

		return nMatchWord



 def verticalSearch(self, word, board):
  # horizontal board can be transposed to vertical board
		# vertical search is equal to horizontal search performed to transposed board
		nMatchWord = self.horizontalSearch(word, self.transpose(board))

		return nMatchWord


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
		  print aLine
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
		  print aLine
		  nMatch, txtMatch = self.lineSearch(word, aLine)
		  #print [i+1], str(nMatch)+" matches: ", txtMatch
		  nMatchWord = nMatchWord + nMatch

		return nMatchWord
		
 def allSearch(self, word, board):
 # sum up all the eight (8) direction
   return self.horizontalSearch(word, board) +\
   self.verticalSearch(word, board) +\
   self.diagonalSearch(word,board)




#------------------------------------------------------------------------
# G E E K S F O R G E E K S 
# G E E K S Q U I Z G E E K 
# I D E Q A P R A C T I C E 
# A B C G E E K S B C A G E 
#------------------------------------------------------------------------
board = [ "GEEKSFORGEEKS",\
			"GEEKSQUIZGEEK",\
			"IDEQAPRACTICE","ABCGEEKSBCAGE"]
#------------------------------------------------------------------------
dBoard = boardObject()
dBoard.display(board)
print "---"
fb = dBoard.flip(board)
#dBoard.display(fb)
#print dBoard.getDimension(board)
#print dBoard.lineSearch('EE', board[0])
#print dBoard.lineSearch('EE', board[1])
#print dBoard.horizontalSearch('EE', board)

tboard = dBoard.transpose(board)

# G G I A 
# E E D B 
# E E E C 
# K K Q G 
# S S A E 
# F Q P E 
# O U R K 
# R I A S 
# G Z C B 
# E G T C 
# E E I A 
# K E C G 
# S K E E 

dBoard.display(tboard)
#print dBoard.search_vertic_all('EE', board)
#print dBoard.diagonalSearch('EE',board)
print dBoard.allSearch('EE', board)
