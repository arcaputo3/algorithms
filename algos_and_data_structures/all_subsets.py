# parameter s is a list
# returns a list of all subsets of s including [] and the s itself
def subsets(s):
	# base case
	if len(s) == 0:
		return [[]]
	# the input set is not empty, divide and conquer!
	h, t = s[0], s[1:]
	ss_excl_h = subsets(t)
	ss_incl_h = [([h] + ss) for ss in ss_excl_h]
	return ss_incl_h + ss_excl_h

print(subsets([1,2,3]))
