# -*- coding:utf-8
#!/usr/bin/python
# ------------------
# myBoardSolver.py
# ------------------

class boardSolver():

	def getDimension(self, board):
		rows = len(board)
		cols = len(board[0])
		return rows, cols


	def display(self, board):
		row, col = self.getDimension(board)
		for i in range(0, row):
			for j in range (0, col):
				print board[i][j],
			print ''


	def transpose(self, board):
		board = zip(*board)
		tboard = [''.join(i) for i in board]
		return tboard


	def linearSearch(self, word, strLine):
		txtMatch  = ''
		readL = []
		readR = []
		# search from RIGHT
		import re
		matchesR = re.finditer(word, strLine)
		for match in matchesR:
			iTuple = (match.start(), match.end())
			readR = readR + [iTuple]
		# search from LEFT
		matchesL = re.finditer(word[::-1], strLine)
		for match in matchesL:
			iTuple = ((match.start(), match.end()))
			readL = (readL) + [iTuple]
		# remove duplicates
		reads = set(readR + readL)
		nMatch = len(reads)
		# see location of matches
		for read in reads:
			txtMatch =  txtMatch  + word + " @(%s, %s) " % read
		return nMatch, txtMatch


	def search_horizon_all(self, word, board):
		rows, cols = self.getDimension(board)
		nMatchLinear = 0
		for i in range (0, rows):
			strLine = board[i]
			nMatch, txtMatch = self.linearSearch(word, strLine)
			print i+1, str(nMatch)+" matches: ", txtMatch
			nMatchLinear = nMatchLinear + nMatch
		return nMatchLinear


	def search_vertic_all(self, word, board):
		# vertical search is equal to linear search to transposed board
		board = self.transpose(board)
		nMatch = self.search_horizon_all(word, board)
		return nMatch

	def search_diagon(self, word, board):
		rows, cols = self.getDimension(board)
		# moving diagonally left to right:
		# moving through each column
		# dword = board[0][0] + board[1][1] + board[2][2] + board[3][3]
		# dword = board[0][1] + board[1][2] + board[2][3] + board[3][4]
		# dword = board[0][2] + board[1][3] + board[2][4] + board[3][5]
		# dword = board[0][2] + board[1][3] + board[2][4] + board[3][5]
		nMatchLinear = 0

		# search from LEFT DIAGONAL
		for i in range(0, rows-1):
			dword = ''
			#print i, '----------------'
			for j in range(0, cols-1):
				dword = ''
				for k in range(0, rows):
					try:
						dword = dword + board[i+k][j+k]
					except:
						continue
				nMatch, txtMatch = self.linearSearch(word, dword)
				nMatchLinear = nMatchLinear + nMatch
				#print (i+1,j+1), str(nMatch)+" matches: ", txtMatch

		# moving diagonally right to left:
		# TODO: below here
		# moving through each column
		# dword = board[0][0] + board[1][1] + board[2][2] + board[3][3]
		# dword = board[0][1] + board[1][2] + board[2][3] + board[3][4]
		# dword = board[0][2] + board[1][3] + board[2][4] + board[3][5]
		# dword = board[0][2] + board[1][3] + board[2][4] + board[3][5]

		# search from RIGHT DIAGONAL to left downward
		for i in range(0, rows-1):
			dword = ''
			for j in range(0, cols-1):
				dword = ''
				for k in range(0, rows):
					try:
						dword = dword + board[j+k][i+k]
					except:
						continue
				nMatch, txtMatch = self.linearSearch(word, dword)
				nMatchLinear = nMatchLinear + nMatch
				print (i+1,j+1), str(nMatch)+" matches: ", txtMatch


		return nMatchLinear

		
			
#------------------------------------------------------------------------
# G E E K S F O R G E E K S 
# G E E K S Q U I Z G E E K 
# I D E Q A P R A C T I C E 
# A B C G E E K S B C A G E 
#------------------------------------------------------------------------
board = [  "GEEKSFORGEEKS",\
			"GEEKSQUIZGEEK",\
			"IDEQAPRACTICE","ABCGEEKSBCAGE"]
#------------------------------------------------------------------------
dBoard = boardSolver()
dBoard.display(board)
#print dBoard.getDimension(board)
print dBoard.linearSearch('EE', board[0])
#print dBoard.linearSearch('EE', board, 1)
#print dBoard.search_horizon_all('EE', board)
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
print dBoard.search_diagon('GDC',board)
