import math
import os
import re
import sys
import itertools
import random
from random import choice
import numpy as np
import sympy
from itertools import combinations

class lattice(object):
	def __init__(self, L , J=1, alpha=1.50):
		self.lattice = [choice([1,-1]) for _ in range(L)]
		self.length = L
		self.alpha = alpha
		self.J = J
		self.m = self.TotalMagnet()
		self.e = self.TotalEnergy()
	def TotalEnergy(self):
		e = 0
		for i,j in list(combinations(list(range(self.length)),2)):
			e += self.lattice[i]*self.lattice[j]/(pow(abs(i-j),self.alpha))
		return -self.J * e	
	def TotalMagnet(self):
		return sum(self.lattice)
	def UpdateSite(self,i):
		self.lattice[i]*=-1
		self.m = self.m + 2*self.lattice[i]
	def printLattice(self):
		s = ":" 
		for site in self.lattice:
			s+="({}):".format(site)
		print(s)	
	def Metropolis(self):
		for i in range(self.length):
			#print(self.lattice[i])
			self.UpdateSite(i)
			#print(self.lattice[i])
			DE = self.TotalEnergy() - self.e
			if DE<0:
				self.e = self.e +DE
				#print("updated!") 
			else:
				ptest = random.random()
				if ptest < math.exp(-self.J*DE):
					self.e += DE
					#print("Updated!")
				else:
					self.UpdateSite(i)
					#print("notUpdated!")
			#print(self.lattice[i])
if __name__ == '__main__':
	
	L= int(input())
	N = int(input())
	nsample = int(input())
	J = float(input())
	f = open("1DLongRangeIsingSizeEq{}.csv".format(L),"a+")
	for _ in range(2):
		J = J + 0.01
		grid = lattice(L,J)
		data = []
		for sample in range(nsample):
			for itr in range(N):
				grid.Metropolis()
			data.append(abs(float(grid.m)/float(L)))
		meanM = np.mean(data)
		stdM = np.std(data)
		f.write("{},{},{}\n".format(J,meanM,stdM))
	f.close()
	
