def findDecision(obj): #obj[0]: age, obj[1]: sex, obj[2]: cp, obj[3]: trtbps, obj[4]: chol, obj[5]: fbs, obj[6]: restecg, obj[7]: thalachh, obj[8]: exng, obj[9]: oldpeak, obj[10]: slp, obj[11]: caa, obj[12]: thall
	# {"feature": "cp", "instances": 242, "metric_value": 0.9976, "depth": 1}
	if obj[2]>0:
		# {"feature": "trtbps", "instances": 128, "metric_value": 0.7856, "depth": 2}
		if obj[3]<=182.62362130489413:
			# {"feature": "oldpeak", "instances": 127, "metric_value": 0.7751, "depth": 3}
			if obj[9]<=2.562123466061027:
				# {"feature": "age", "instances": 120, "metric_value": 0.7219, "depth": 4}
				if obj[0]>44.76894247609949:
					# {"feature": "thall", "instances": 97, "metric_value": 0.8072, "depth": 5}
					if obj[12]>1:
						# {"feature": "sex", "instances": 93, "metric_value": 0.7706, "depth": 6}
						if obj[1]>0:
							# {"feature": "thalachh", "instances": 55, "metric_value": 0.9121, "depth": 7}
							if obj[7]>103:
								# {"feature": "caa", "instances": 54, "metric_value": 0.8987, "depth": 8}
								if obj[11]<=3:
									# {"feature": "chol", "instances": 52, "metric_value": 0.9118, "depth": 9}
									if obj[4]>126:
										# {"feature": "slp", "instances": 51, "metric_value": 0.9183, "depth": 10}
										if obj[10]>1:
											# {"feature": "fbs", "instances": 28, "metric_value": 0.7496, "depth": 11}
											if obj[5]<=0:
												# {"feature": "exng", "instances": 21, "metric_value": 0.8631, "depth": 12}
												if obj[8]<=0:
													# {"feature": "restecg", "instances": 19, "metric_value": 0.8997, "depth": 13}
													if obj[6]>0:
														return 'more'
													elif obj[6]<=0:
														return 'more'
													else: return 'more'
												elif obj[8]>0:
													return 'more'
												else: return 'more'
											elif obj[5]>0:
												return 'more'
											else: return 'more'
										elif obj[10]<=1:
											# {"feature": "fbs", "instances": 23, "metric_value": 0.9986, "depth": 11}
											if obj[5]<=0:
												# {"feature": "restecg", "instances": 18, "metric_value": 1.0, "depth": 12}
												if obj[6]<=0:
													# {"feature": "exng", "instances": 12, "metric_value": 0.9799, "depth": 13}
													if obj[8]<=0:
														return 'less'
													elif obj[8]>0:
														return 'more'
													else: return 'more'
												elif obj[6]>0:
													# {"feature": "exng", "instances": 6, "metric_value": 0.9183, "depth": 13}
													if obj[8]<=0:
														return 'less'
													elif obj[8]>0:
														return 'less'
													else: return 'less'
												else: return 'less'
											elif obj[5]>0:
												# {"feature": "restecg", "instances": 5, "metric_value": 0.971, "depth": 12}
												if obj[6]<=0:
													# {"feature": "exng", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[8]<=0:
														return 'more'
													elif obj[8]>0:
														return 'less'
													else: return 'less'
												elif obj[6]>0:
													return 'more'
												else: return 'more'
											else: return 'more'
										else: return 'more'
									elif obj[4]<=126:
										return 'more'
									else: return 'more'
								elif obj[11]>3:
									return 'more'
								else: return 'more'
							elif obj[7]<=103:
								return 'less'
							else: return 'less'
						elif obj[1]<=0:
							# {"feature": "thalachh", "instances": 38, "metric_value": 0.3985, "depth": 7}
							if obj[7]>114.68001030955222:
								# {"feature": "caa", "instances": 36, "metric_value": 0.3095, "depth": 8}
								if obj[11]<=0:
									return 'more'
								elif obj[11]>0:
									# {"feature": "slp", "instances": 13, "metric_value": 0.6194, "depth": 9}
									if obj[10]>1:
										# {"feature": "chol", "instances": 12, "metric_value": 0.4138, "depth": 10}
										if obj[4]<=318:
											return 'more'
										elif obj[4]>318:
											# {"feature": "fbs", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[5]<=1:
												# {"feature": "restecg", "instances": 2, "metric_value": 1.0, "depth": 12}
												if obj[6]<=0:
													# {"feature": "exng", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8]<=0:
														return 'less'
													else: return 'less'
												else: return 'less'
											else: return 'less'
										else: return 'less'
									elif obj[10]<=1:
										return 'less'
									else: return 'less'
								else: return 'more'
							elif obj[7]<=114.68001030955222:
								# {"feature": "chol", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[4]>178:
									return 'less'
								elif obj[4]<=178:
									return 'more'
								else: return 'more'
							else: return 'less'
						else: return 'more'
					elif obj[12]<=1:
						# {"feature": "thalachh", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[7]<=142:
							return 'less'
						elif obj[7]>142:
							return 'more'
						else: return 'more'
					else: return 'less'
				elif obj[0]<=44.76894247609949:
					return 'more'
				else: return 'more'
			elif obj[9]>2.562123466061027:
				# {"feature": "slp", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[10]>0:
					return 'less'
				elif obj[10]<=0:
					return 'more'
				else: return 'more'
			else: return 'less'
		elif obj[3]>182.62362130489413:
			return 'less'
		else: return 'less'
	elif obj[2]<=0:
		# {"feature": "trtbps", "instances": 114, "metric_value": 0.8315, "depth": 2}
		if obj[3]>100:
			# {"feature": "caa", "instances": 113, "metric_value": 0.8216, "depth": 3}
			if obj[11]>0:
				# {"feature": "oldpeak", "instances": 64, "metric_value": 0.3955, "depth": 4}
				if obj[9]>0.45986212448770014:
					# {"feature": "age", "instances": 51, "metric_value": 0.1392, "depth": 5}
					if obj[0]<=63:
						return 'less'
					elif obj[0]>63:
						# {"feature": "chol", "instances": 9, "metric_value": 0.5033, "depth": 6}
						if obj[4]<=254:
							return 'less'
						elif obj[4]>254:
							# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[1]<=0:
								return 'more'
							elif obj[1]>0:
								return 'less'
							else: return 'less'
						else: return 'more'
					else: return 'less'
				elif obj[9]<=0.45986212448770014:
					# {"feature": "sex", "instances": 13, "metric_value": 0.8905, "depth": 5}
					if obj[1]>0:
						# {"feature": "thalachh", "instances": 11, "metric_value": 0.684, "depth": 6}
						if obj[7]>105:
							# {"feature": "fbs", "instances": 10, "metric_value": 0.469, "depth": 7}
							if obj[5]<=0:
								return 'less'
							elif obj[5]>0:
								# {"feature": "chol", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[4]>233:
									return 'less'
								elif obj[4]<=233:
									return 'more'
								else: return 'more'
							else: return 'less'
						elif obj[7]<=105:
							return 'more'
						else: return 'more'
					elif obj[1]<=0:
						return 'more'
					else: return 'more'
				else: return 'less'
			elif obj[11]<=0:
				# {"feature": "thall", "instances": 49, "metric_value": 0.9997, "depth": 4}
				if obj[12]<=2:
					# {"feature": "exng", "instances": 27, "metric_value": 0.7642, "depth": 5}
					if obj[8]<=0:
						return 'more'
					elif obj[8]>0:
						# {"feature": "restecg", "instances": 11, "metric_value": 0.994, "depth": 6}
						if obj[6]>0:
							# {"feature": "slp", "instances": 8, "metric_value": 0.8113, "depth": 7}
							if obj[10]<=1:
								return 'less'
							elif obj[10]>1:
								return 'more'
							else: return 'more'
						elif obj[6]<=0:
							return 'more'
						else: return 'more'
					else: return 'less'
				elif obj[12]>2:
					# {"feature": "oldpeak", "instances": 22, "metric_value": 0.5746, "depth": 5}
					if obj[9]>0.5:
						return 'less'
					elif obj[9]<=0.5:
						# {"feature": "age", "instances": 8, "metric_value": 0.9544, "depth": 6}
						if obj[0]<=57:
							# {"feature": "chol", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[4]>211:
								return 'less'
							elif obj[4]<=211:
								# {"feature": "restecg", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[6]>0:
									return 'more'
								elif obj[6]<=0:
									return 'less'
								else: return 'less'
							else: return 'more'
						elif obj[0]>57:
							return 'more'
						else: return 'more'
					else: return 'less'
				else: return 'less'
			else: return 'less'
		elif obj[3]<=100:
			return 'more'
		else: return 'more'
	else: return 'less'
