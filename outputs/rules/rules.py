def findDecision(obj): #obj[0]: age, obj[1]: sex, obj[2]: cp, obj[3]: trtbps, obj[4]: chol, obj[5]: fbs, obj[6]: restecg, obj[7]: thalachh, obj[8]: exng, obj[9]: oldpeak, obj[10]: slp, obj[11]: caa, obj[12]: thall
	# {"feature": "cp", "instances": 303, "metric_value": 0.9943, "depth": 1}
	if obj[2]>0:
		# {"feature": "trtbps", "instances": 160, "metric_value": 0.7462, "depth": 2}
		if obj[3]<=182.49734270893063:
			# {"feature": "oldpeak", "instances": 159, "metric_value": 0.7368, "depth": 3}
			if obj[9]<=2.583613524265049:
				# {"feature": "thall", "instances": 150, "metric_value": 0.6801, "depth": 4}
				if obj[12]<=2:
					# {"feature": "caa", "instances": 116, "metric_value": 0.5061, "depth": 5}
					if obj[11]<=0:
						# {"feature": "thalachh", "instances": 82, "metric_value": 0.2812, "depth": 6}
						if obj[7]>161.109756097561:
							return 'more'
						elif obj[7]<=161.109756097561:
							# {"feature": "chol", "instances": 34, "metric_value": 0.5226, "depth": 7}
							if obj[4]<=235.55882352941177:
								return 'more'
							elif obj[4]>235.55882352941177:
								# {"feature": "sex", "instances": 15, "metric_value": 0.8366, "depth": 8}
								if obj[1]>0:
									# {"feature": "age", "instances": 8, "metric_value": 1.0, "depth": 9}
									if obj[0]<=64:
										# {"feature": "fbs", "instances": 7, "metric_value": 0.9852, "depth": 10}
										if obj[5]<=0:
											# {"feature": "slp", "instances": 6, "metric_value": 0.9183, "depth": 11}
											if obj[10]>1:
												# {"feature": "restecg", "instances": 5, "metric_value": 0.971, "depth": 12}
												if obj[6]>0:
													# {"feature": "exng", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[8]<=0:
														return 'less'
													else: return 'less'
												elif obj[6]<=0:
													# {"feature": "exng", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[8]<=0:
														return 'more'
													else: return 'more'
												else: return 'more'
											elif obj[10]<=1:
												return 'less'
											else: return 'less'
										elif obj[5]>0:
											return 'more'
										else: return 'more'
									elif obj[0]>64:
										return 'more'
									else: return 'more'
								elif obj[1]<=0:
									return 'more'
								else: return 'more'
							else: return 'more'
						else: return 'more'
					elif obj[11]>0:
						# {"feature": "chol", "instances": 34, "metric_value": 0.8338, "depth": 6}
						if obj[4]>149:
							# {"feature": "thalachh", "instances": 33, "metric_value": 0.799, "depth": 7}
							if obj[7]>120:
								# {"feature": "slp", "instances": 32, "metric_value": 0.7579, "depth": 8}
								if obj[10]>1:
									# {"feature": "age", "instances": 24, "metric_value": 0.5436, "depth": 9}
									if obj[0]<=54:
										return 'more'
									elif obj[0]>54:
										# {"feature": "sex", "instances": 11, "metric_value": 0.8454, "depth": 10}
										if obj[1]<=0:
											# {"feature": "fbs", "instances": 9, "metric_value": 0.5033, "depth": 11}
											if obj[5]<=0:
												return 'more'
											elif obj[5]>0:
												# {"feature": "restecg", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[6]<=0:
													# {"feature": "exng", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[8]<=0:
														return 'more'
													else: return 'more'
												else: return 'more'
											else: return 'more'
										elif obj[1]>0:
											return 'less'
										else: return 'less'
									else: return 'more'
								elif obj[10]<=1:
									# {"feature": "age", "instances": 8, "metric_value": 1.0, "depth": 9}
									if obj[0]>54:
										# {"feature": "restecg", "instances": 6, "metric_value": 0.9183, "depth": 10}
										if obj[6]<=0:
											# {"feature": "exng", "instances": 5, "metric_value": 0.971, "depth": 11}
											if obj[8]<=0:
												# {"feature": "sex", "instances": 4, "metric_value": 1.0, "depth": 12}
												if obj[1]>0:
													# {"feature": "fbs", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[5]<=1:
														return 'more'
													else: return 'more'
												elif obj[1]<=0:
													# {"feature": "fbs", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[5]<=0:
														return 'more'
													else: return 'more'
												else: return 'more'
											elif obj[8]>0:
												return 'less'
											else: return 'less'
										elif obj[6]>0:
											return 'less'
										else: return 'less'
									elif obj[0]<=54:
										return 'more'
									else: return 'more'
								else: return 'more'
							elif obj[7]<=120:
								return 'less'
							else: return 'less'
						elif obj[4]<=149:
							return 'less'
						else: return 'less'
					else: return 'more'
				elif obj[12]>2:
					# {"feature": "thalachh", "instances": 34, "metric_value": 0.9774, "depth": 5}
					if obj[7]>114.90166216319932:
						# {"feature": "age", "instances": 32, "metric_value": 0.9544, "depth": 6}
						if obj[0]<=68:
							# {"feature": "slp", "instances": 31, "metric_value": 0.9383, "depth": 7}
							if obj[10]<=1:
								# {"feature": "sex", "instances": 19, "metric_value": 0.998, "depth": 8}
								if obj[1]>0:
									# {"feature": "caa", "instances": 18, "metric_value": 0.9911, "depth": 9}
									if obj[11]<=3:
										# {"feature": "chol", "instances": 17, "metric_value": 0.9774, "depth": 10}
										if obj[4]>188:
											# {"feature": "fbs", "instances": 16, "metric_value": 0.9887, "depth": 11}
											if obj[5]<=0:
												# {"feature": "restecg", "instances": 13, "metric_value": 0.9612, "depth": 12}
												if obj[6]<=0:
													# {"feature": "exng", "instances": 8, "metric_value": 1.0, "depth": 13}
													if obj[8]<=0:
														return 'less'
													elif obj[8]>0:
														return 'more'
													else: return 'more'
												elif obj[6]>0:
													# {"feature": "exng", "instances": 5, "metric_value": 0.7219, "depth": 13}
													if obj[8]<=0:
														return 'less'
													elif obj[8]>0:
														return 'less'
													else: return 'less'
												else: return 'less'
											elif obj[5]>0:
												# {"feature": "restecg", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[6]>0:
													return 'more'
												elif obj[6]<=0:
													return 'less'
												else: return 'less'
											else: return 'more'
										elif obj[4]<=188:
											return 'less'
										else: return 'less'
									elif obj[11]>3:
										return 'more'
									else: return 'more'
								elif obj[1]<=0:
									return 'more'
								else: return 'more'
							elif obj[10]>1:
								# {"feature": "chol", "instances": 12, "metric_value": 0.4138, "depth": 8}
								if obj[4]<=232:
									return 'more'
								elif obj[4]>232:
									# {"feature": "sex", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[1]>0:
										# {"feature": "caa", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[11]<=0:
											# {"feature": "fbs", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[5]<=0:
												# {"feature": "restecg", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[6]<=1:
													# {"feature": "exng", "instances": 3, "metric_value": 0.9183, "depth": 13}
													if obj[8]<=0:
														return 'more'
													else: return 'more'
												else: return 'more'
											else: return 'more'
										elif obj[11]>0:
											return 'more'
										else: return 'more'
									elif obj[1]<=0:
										return 'more'
									else: return 'more'
								else: return 'more'
							else: return 'more'
						elif obj[0]>68:
							return 'less'
						else: return 'less'
					elif obj[7]<=114.90166216319932:
						return 'less'
					else: return 'less'
				else: return 'more'
			elif obj[9]>2.583613524265049:
				# {"feature": "slp", "instances": 9, "metric_value": 0.9183, "depth": 4}
				if obj[10]>0:
					return 'less'
				elif obj[10]<=0:
					return 'more'
				else: return 'more'
			else: return 'less'
		elif obj[3]>182.49734270893063:
			return 'less'
		else: return 'less'
	elif obj[2]<=0:
		# {"feature": "caa", "instances": 143, "metric_value": 0.8454, "depth": 2}
		if obj[11]>0:
			# {"feature": "oldpeak", "instances": 78, "metric_value": 0.3435, "depth": 3}
			if obj[9]>0.33210234361082636:
				# {"feature": "sex", "instances": 59, "metric_value": 0.1239, "depth": 4}
				if obj[1]>0:
					return 'less'
				elif obj[1]<=0:
					# {"feature": "age", "instances": 13, "metric_value": 0.3912, "depth": 5}
					if obj[0]<=63:
						return 'less'
					elif obj[0]>63:
						# {"feature": "trtbps", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[3]>130:
							return 'less'
						elif obj[3]<=130:
							return 'more'
						else: return 'more'
					else: return 'less'
				else: return 'less'
			elif obj[9]<=0.33210234361082636:
				# {"feature": "sex", "instances": 19, "metric_value": 0.7425, "depth": 4}
				if obj[1]>0:
					# {"feature": "thalachh", "instances": 17, "metric_value": 0.5226, "depth": 5}
					if obj[7]>105:
						# {"feature": "trtbps", "instances": 16, "metric_value": 0.3373, "depth": 6}
						if obj[3]>108:
							return 'less'
						elif obj[3]<=108:
							# {"feature": "age", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[0]<=52:
								return 'more'
							elif obj[0]>52:
								return 'less'
							else: return 'less'
						else: return 'more'
					elif obj[7]<=105:
						return 'more'
					else: return 'more'
				elif obj[1]<=0:
					return 'more'
				else: return 'more'
			else: return 'less'
		elif obj[11]<=0:
			# {"feature": "thall", "instances": 65, "metric_value": 0.9985, "depth": 3}
			if obj[12]<=2:
				# {"feature": "fbs", "instances": 38, "metric_value": 0.7897, "depth": 4}
				if obj[5]<=0:
					# {"feature": "restecg", "instances": 37, "metric_value": 0.7532, "depth": 5}
					if obj[6]<=1:
						# {"feature": "thalachh", "instances": 36, "metric_value": 0.7107, "depth": 6}
						if obj[7]>71:
							# {"feature": "slp", "instances": 35, "metric_value": 0.661, "depth": 7}
							if obj[10]>0:
								# {"feature": "exng", "instances": 34, "metric_value": 0.6024, "depth": 8}
								if obj[8]<=0:
									# {"feature": "chol", "instances": 23, "metric_value": 0.258, "depth": 9}
									if obj[4]<=298.7745524473303:
										return 'more'
									elif obj[4]>298.7745524473303:
										# {"feature": "oldpeak", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[9]>0.0:
											return 'more'
										elif obj[9]<=0.0:
											return 'less'
										else: return 'less'
									else: return 'more'
								elif obj[8]>0:
									# {"feature": "age", "instances": 11, "metric_value": 0.9457, "depth": 9}
									if obj[0]>42:
										# {"feature": "chol", "instances": 10, "metric_value": 0.8813, "depth": 10}
										if obj[4]>197:
											# {"feature": "trtbps", "instances": 9, "metric_value": 0.7642, "depth": 11}
											if obj[3]<=140:
												return 'more'
											elif obj[3]>140:
												# {"feature": "oldpeak", "instances": 3, "metric_value": 0.9183, "depth": 12}
												if obj[9]<=0.0:
													# {"feature": "sex", "instances": 2, "metric_value": 1.0, "depth": 13}
													if obj[1]<=0:
														return 'more'
													else: return 'more'
												elif obj[9]>0.0:
													return 'less'
												else: return 'less'
											else: return 'less'
										elif obj[4]<=197:
											return 'less'
										else: return 'less'
									elif obj[0]<=42:
										return 'less'
									else: return 'less'
								else: return 'more'
							elif obj[10]<=0:
								return 'less'
							else: return 'less'
						elif obj[7]<=71:
							return 'less'
						else: return 'less'
					elif obj[6]>1:
						return 'less'
					else: return 'less'
				elif obj[5]>0:
					return 'less'
				else: return 'less'
			elif obj[12]>2:
				# {"feature": "oldpeak", "instances": 27, "metric_value": 0.6913, "depth": 4}
				if obj[9]>0.5:
					return 'less'
				elif obj[9]<=0.5:
					# {"feature": "age", "instances": 10, "metric_value": 1.0, "depth": 5}
					if obj[0]>41:
						# {"feature": "chol", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[4]<=234:
							return 'more'
						elif obj[4]>234:
							return 'less'
						else: return 'less'
					elif obj[0]<=41:
						return 'less'
					else: return 'less'
				else: return 'more'
			else: return 'less'
		else: return 'more'
	else: return 'less'
