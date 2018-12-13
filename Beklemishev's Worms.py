def W(n):
	k=1
	w=[n]
	while w:
		k+=1
		h=w[-1]
		w[-1]-=1
		i=len(w)-1
		while 0<h<=w[i-1]:i-=1
		w[i:]*=k*(h>0)
	return k-1
