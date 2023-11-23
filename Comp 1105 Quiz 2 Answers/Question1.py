# Write a function that given a string as its parameter, returns the string into a set.
# The "word" must be more than 1 letter, not case sensitive
# i.e. 1. Click submit to proceed.  2.click Submit and (3)Create Another to save this question and create another-- of the same type!!...
# set = [click, submit, to, proceed, and, create, another, save, this, question, of, the, type]

def Q1(inpStr):
    ls = inpStr.lower().split()
    theSet = set()
    for w in ls:
        w = clean(w)
        if w != '':
            theSet.add(w)
    return list(theSet)


def clean(word):
    return word.strip('0123456789.!@#$%^&*()_+=-~":;?><,')


# testing the function
print(Q1("1. Click submit to proceed.  2.click Submit and (3)Create Another to save this question and create another-- of the same type!!..."))
