def findDecision(obj): #obj[0]: age, obj[1]: sex, obj[2]: cp, obj[3]: trtbps, obj[4]: chol, obj[5]: fbs, obj[6]: restecg, obj[7]: thalachh, obj[8]: exng, obj[9]: oldpeak, obj[10]: slp, obj[11]: caa, obj[12]: thall
	# {"feature": "cp", "instances": 303, "metric_value": 0.9943, "depth": 1}
	if obj[2]>0:
		# {"feature": "thall", "instances": 160, "metric_value": 0.7462, "depth": 2}
		if obj[12]<=2:
			# {"feature": "caa", "instances": 121, "metric_value": 0.5635, "depth": 3}
			if obj[11]<=0:
				# {"feature": "thalachh", "instances": 86, "metric_value": 0.3651, "depth": 4}
				if obj[7]>160.62790697674419:
					return 'more'
				elif obj[7]<=160.62790697674419:
					# {"feature": "sex", "instances": 36, "metric_value": 0.65, "depth": 5}
					if obj[1]>0:
						# {"feature": "chol", "instances": 20, "metric_value": 0.8813, "depth": 6}
						if obj[4]<=262:
							# {"feature": "oldpeak", "instances": 17, "metric_value": 0.6723, "depth": 7}
							if obj[9]<=2.3:
								# {"feature": "trtbps", "instances": 15, "metric_value": 0.3534, "depth": 8}
								if obj[3]>108:
									return 'more'
								elif obj[3]<=108:
									# {"feature": "age", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[0]>47:
										return 'more'
									elif obj[0]<=47:
										return 'less'
									else: return 'less'
								else: return 'more'
							elif obj[9]>2.3:
								return 'less'
							else: return 'less'
						elif obj[4]>262:
							return 'less'
						else: return 'less'
					elif obj[1]<=0:
						return 'more'
					else: return 'more'
				else: return 'more'
			elif obj[11]>0:
				# {"feature": "slp", "instances": 35, "metric_value": 0.8631, "depth": 4}
				if obj[10]>1:
					# {"feature": "chol", "instances": 25, "metric_value": 0.6343, "depth": 5}
					if obj[4]>149:
						# {"feature": "age", "instances": 24, "metric_value": 0.5436, "depth": 6}
						if obj[0]<=54:
							return 'more'
						elif obj[0]>54:
							# {"feature": "sex", "instances": 11, "metric_value": 0.8454, "depth": 7}
							if obj[1]<=0:
								# {"feature": "fbs", "instances": 9, "metric_value": 0.5033, "depth": 8}
								if obj[5]<=0:
									return 'more'
								elif obj[5]>0:
									# {"feature": "trtbps", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[3]>110:
										# {"feature": "thalachh", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[7]>152:
											return 'more'
										elif obj[7]<=152:
											return 'less'
										else: return 'less'
									elif obj[3]<=110:
										return 'more'
									else: return 'more'
								else: return 'more'
							elif obj[1]>0:
								return 'less'
							else: return 'less'
						else: return 'more'
					elif obj[4]<=149:
						return 'less'
					else: return 'less'
				elif obj[10]<=1:
					# {"feature": "oldpeak", "instances": 10, "metric_value": 0.971, "depth": 5}
					if obj[9]<=0.5:
						# {"feature": "thalachh", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[7]>120:
							# {"feature": "chol", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[4]>236:
								return 'more'
							elif obj[4]<=236:
								# {"feature": "age", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[0]>57:
									return 'more'
								elif obj[0]<=57:
									return 'less'
								else: return 'less'
							else: return 'more'
						elif obj[7]<=120:
							return 'less'
						else: return 'less'
					elif obj[9]>0.5:
						return 'less'
					else: return 'less'
				else: return 'less'
			else: return 'more'
		elif obj[12]>2:
			# {"feature": "oldpeak", "instances": 39, "metric_value": 0.9957, "depth": 3}
			if obj[9]<=1.9:
				# {"feature": "slp", "instances": 32, "metric_value": 0.9544, "depth": 4}
				if obj[10]<=1:
					# {"feature": "thalachh", "instances": 19, "metric_value": 0.998, "depth": 5}
					if obj[7]>132:
						# {"feature": "trtbps", "instances": 15, "metric_value": 0.971, "depth": 6}
						if obj[3]>125:
							# {"feature": "age", "instances": 8, "metric_value": 0.9544, "depth": 7}
							if obj[0]<=64:
								# {"feature": "chol", "instances": 6, "metric_value": 1.0, "depth": 8}
								if obj[4]>227:
									# {"feature": "restecg", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[6]>0:
										# {"feature": "fbs", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[5]<=0:
											# {"feature": "caa", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[11]>1:
												return 'more'
											elif obj[11]<=1:
												return 'less'
											else: return 'less'
										elif obj[5]>0:
											return 'more'
										else: return 'more'
									elif obj[6]<=0:
										return 'less'
									else: return 'less'
								elif obj[4]<=227:
									return 'more'
								else: return 'more'
							elif obj[0]>64:
								return 'less'
							else: return 'less'
						elif obj[3]<=125:
							# {"feature": "age", "instances": 7, "metric_value": 0.5917, "depth": 7}
							if obj[0]>48:
								return 'more'
							elif obj[0]<=48:
								# {"feature": "chol", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[4]>229:
									return 'more'
								elif obj[4]<=229:
									return 'less'
								else: return 'less'
							else: return 'more'
						else: return 'more'
					elif obj[7]<=132:
						return 'less'
					else: return 'less'
				elif obj[10]>1:
					# {"feature": "trtbps", "instances": 13, "metric_value": 0.6194, "depth": 5}
					if obj[3]<=172:
						# {"feature": "thalachh", "instances": 12, "metric_value": 0.4138, "depth": 6}
						if obj[7]>141:
							return 'more'
						elif obj[7]<=141:
							# {"feature": "age", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[0]>57:
								return 'more'
							elif obj[0]<=57:
								return 'less'
							else: return 'less'
						else: return 'more'
					elif obj[3]>172:
						return 'less'
					else: return 'less'
				else: return 'more'
			elif obj[9]>1.9:
				# {"feature": "trtbps", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[3]<=160:
					return 'less'
				elif obj[3]>160:
					return 'more'
				else: return 'more'
			else: return 'less'
		else: return 'more'
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
				# {"feature": "exng", "instances": 38, "metric_value": 0.7897, "depth": 4}
				if obj[8]<=0:
					# {"feature": "thalachh", "instances": 24, "metric_value": 0.4138, "depth": 5}
					if obj[7]>71:
						# {"feature": "chol", "instances": 23, "metric_value": 0.258, "depth": 6}
						if obj[4]<=298.7745524473303:
							return 'more'
						elif obj[4]>298.7745524473303:
							# {"feature": "oldpeak", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[9]>0.0:
								return 'more'
							elif obj[9]<=0.0:
								return 'less'
							else: return 'less'
						else: return 'more'
					elif obj[7]<=71:
						return 'less'
					else: return 'less'
				elif obj[8]>0:
					# {"feature": "restecg", "instances": 14, "metric_value": 1.0, "depth": 5}
					if obj[6]>0:
						# {"feature": "slp", "instances": 10, "metric_value": 0.8813, "depth": 6}
						if obj[10]<=1:
							# {"feature": "trtbps", "instances": 8, "metric_value": 0.5436, "depth": 7}
							if obj[3]>110:
								return 'less'
							elif obj[3]<=110:
								return 'more'
							else: return 'more'
						elif obj[10]>1:
							return 'more'
						else: return 'more'
					elif obj[6]<=0:
						return 'more'
					else: return 'more'
				else: return 'more'
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
