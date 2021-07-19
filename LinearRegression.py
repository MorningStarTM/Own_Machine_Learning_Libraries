
import math
class LinearRegression:
	def fit(set):
		mean_x = 0
		mean_y = 0
		sigma_x = 0
		sigma_y = 0
		sigma_xy = 0
		sigma_XX = 0
		
		for i in set:
			sigma_y += i[1]
		for i in set:
			sigma_x += i[0]
		mean_y = sigma_y/len(set)
		mean_x = sigma_x/len(set)
		for i,j in set:
			sigma_xy = sigma_xy + (i*j)
		for i in set:
			sigma_XX += i[0]**2
		
		LinearRegression.fit.m = (sigma_xy - ((sigma_x*sigma_y)/len(set)))/(sigma_XX-((sigma_x*sigma_x)/len(set)))
		LinearRegression.fit.b = (1/len(set))*(sigma_y-(LinearRegression.fit.m*sigma_x))

	def predict(value):
		m = LinearRegression.fit.m
		b = LinearRegression.fit.b
		x = value
		y = (m*x)+b
		return y

	def score(set):
		X_X = []
		Y_Y = []
		sigmaX_Y = 0
		squareX_X = []
		squareY_Y = []
		mean_x = 0
		mean_y = 0
		sigma_x = 0
		sigma_y = 0
		sigma_XX = 0
		sigma_YY = 0
		sigma_x_x = 0
		sigma_y_y = 0

		for i in set:
			sigma_y += i[1]
		for i in set:
			sigma_x += i[0]
		mean_y = sigma_y/len(set)
		mean_x = sigma_x/len(set)
		for i in set:
			sigma_XX += i[0]**2
		for i in set:
			sigma_YY += i[1]**2
		for i in set:
			sigma_x_x += (i[0] - mean_x)
			X_X.append(round(i[0] - mean_x,3))
		for i in set:
			sigma_y_y += (i[1] - mean_y)
			Y_Y.append(round(i[1] - mean_y,3))

		for i in X_X:
			squareX_X.append(i**2)
		for i in Y_Y:
			squareY_Y.append(i**2)

		for i in range(len(X_X)):
			sigmaX_Y+=(X_X[i]*Y_Y[i])
	
		r_partial = (sigma_XX-((sigma_x**2)/len(set)))
		r_partial_2 = (sigma_YY-((sigma_y**2)/len(set)))	
		r_divider = (r_partial*r_partial_2)
		r_divider = math.sqrt(r_divider)
		r = sigmaX_Y/r_divider
		return r
		

		
		
