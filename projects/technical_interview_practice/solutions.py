##########################################
######## Function Implementations ########
##########################################


from collections import Counter

#### Function implementation for question 1 ####
def question1(s, t):
	
  cnt = Counter()

  # count the number of each characters in s
  for c in s:
  	cnt[c] += 1

	for c in t:
	  # no more character c in the cnt
	  if cnt[c] == 0:
	    return False

	  cnt[c] -= 1

  return True


#### Function implementation for question 4 ####
def question4(T, r, n1, n2):
  
  while 1:
    children = [i for i,x in enumerate(T[r]) if x == 1]
    left_child = min(children)
    right_child = max(children)

    if r == n1 or r == n2:
      return r
    elif r < n1 and r < n2:
  	  r = right_child
    elif r > n1 and r > n2:
  	  r = left_child
    else:
  	  return r

#### Function implementation for question 5 ####
class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None

def question5(ll, m):
  
  if ll == None:
    return

  slow = ll
  fast = ll
    
  for i in range(m):
  	fast = fast.next
  	# m greater than the length of the list
  	if fast == None and i < m - 1:
  	  return None

  while fast != None:
  	slow = slow.next
  	fast = fast.next

  return slow.data





############################
######## Test Cases ########
############################

#### Test Cases for question 1 ####

print "Question 1 Test Cases"
# Case 1: s is an empty string
s = ''
t = 'dbca'
print question1(s, t)
# expected output: False

# Case 2: t is an empty string
s = 'ab'
t = ''
print question1(s, t)
# expected output: True

# Case 3: t is a permutation of a substring of s
s = 'abcd'
t = 'ba'
print question1(s, t)
# expected output: True

# Case 4: some letter in t does not appear in s
s = 'acdb'
t = 'va'
print question1(s, t)
# expected output: False

# Case 5: The number of a letter in t exceeds 
#         the number of the letter in s
s = 'acbcdb'
t = 'babcdb'
print question1(s, t)
# expected output: False


#### Test Cases for question 4 ####

print "Question 4 Test Cases"

print question4([[0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0],
                 [1, 0, 0, 0, 1, 0, 1],
                 [0, 0, 0, 0, 0, 0, 0]],
                3,
                6,
                4)


#### Test Cases for question 5 ####

print "Question 5 Test Cases"

# Case 1: empty list
head = None
print question5(head, 1)
# expected output: None

# Case 2: m too large
head = Node(1)
print question5(head, 2)
# expected output: None

# Case 3: one-element list
head = Node(1)
print question5(head, 1)
# expected output: 1

# Case 4: Multi-element list
head = Node(3)
a = Node(1)
b = Node(4)
c = Node(2)
head.next = a
a.next = b
b.next = c

print question5(head, 1)
# expected output: 2

print question5(head, 2)
# expected output: 4

print question5(head, 4)
# expected output: 3

print question5(head, 5)
# expected output: None