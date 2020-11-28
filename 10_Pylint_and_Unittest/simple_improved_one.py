'''
A very simple script
(Multiline comment at the begining of file describing it, helps with Pylint rating!)
'''

# Htting an enter after colon below causes sublime to use a tab instead of spaces.
# This causes us to have both spaces and tab mixed together, which is not good styling!
def myfunc():
	'''
	A simple function
	'''
	first = 1
	second = 2
	print(first)
	print(second)

myfunc()

'''
If you run this script by pylint, you'll get 0.00/12 score, which is better than -12.50/10.
But we still have a way to go. When you check more on Pylint results, you'll see:
mixed-indentation - 5 occurrences.
When you check at the beginning of the report, you,ll see:
************* Module simple_improved_one
simple_improved_one.py:9:0: W0312: Found indentation with tabs instead of spaces
simple_improved_one.py:12:0: W0312: Found indentation with tabs instead of spaces
simple_improved_one.py:13:0: W0312: Found indentation with tabs instead of spaces
simple_improved_one.py:14:0: W0312: Found indentation with tabs instead of spaces
simple_improved_one.py:15:0: W0312: Found indentation with tabs instead of spaces
simple_improved_one.py:17:0: C0304: Final newline missing (missing-final-newline)

So, we need to use spaces insted of tabs! We can fix this by removing tabs in myfunc() and replace
them with spaces. Please see another script: simple_improved_more.py for it.

'''