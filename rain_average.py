#We have a list of annual rainfall recordings of cities.
#Each element in the list is of the form (c,r) where c is the city and r is the
#annual rainfall for a particular year.
#The list may have multiple entries for the same city,
#corresponding to rainfall recordings in different years.
#Write a Python function rainaverage(l) that takes as input a list of rainfall
#recordings and computes the avarage rainfall for each city. The output should be a list of pairs (c,ar)
#where c is the city and ar is the average rainfall for this city among the recordings in the input list.
#Note that ar should be of type float. The output should be sorted in dictionary order with respect to the city name


def rainaverage(l):
  raindata = {}
  for (c,r) in l:
    if c in raindata.keys():
      raindata[c].append(r)
    else:
      raindata[c] = [r]
  outputlist = []
  for c in sorted(raindata.keys()):
    thisaverage = sum(raindata[c])/len(raindata[c])
    outputlist.append((c,thisaverage))
  return(outputlist)
