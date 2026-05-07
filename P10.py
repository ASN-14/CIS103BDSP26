# Albin Sanchez
def main():
    thetext = '''
       Python was conceived in the late 1980’s by Netherlands programmer
Guido Van Rossum and rolled out in 1991. Developing the language
was a hobby project for Van Rossum to keep him occupied over
Christmas, though he soon began implementing the language at
his employer Centrum Wiskunde & Informatica (CWI). The name of
the language was inspired by Monty Python’s Flying Circus, and
today users of this code often work in references to Monty Python.
Python is one of the most popular programming languages in the
world. As a scripting language that can automate a complex series
of tasks, Python is used on the back end of many web applications,
games, and digital and animated special effects. Sites like YouTube
and Instagram are among some of the titans that rely on this
language to support both front-end and back-end functionality.    
        '''
    print(thetext)
# ---------------------------------
    print('- '*18)
    print('Length of the text:',len(thetext))
    rspacetext = thetext.strip()
    print('New lenght of the text:',len(rspacetext))
    nbtext = thetext.count('the')
    print("count of the number 'the' found:", nbtext)
    wtext = 'little'
    if wtext in thetext:
        print("the word 'little' was found")
    else:
        print("the word 'little' was not found")
    wtext2 = 'titan'
    if wtext2 not in thetext:
        print("the word 'titan' was not found")
    else:
        print("the word 'titan' was found")
    nbtext2 = thetext.find('appl')
    print("Position number of 'appl':", nbtext2)
    thetext2 = thetext
    nbtext3 = thetext2.replace('Python','PYTHON')
    print(nbtext3)
    print('- '*18)
# ---------------------------------
    return
main()
