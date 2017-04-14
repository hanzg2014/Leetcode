#coding: utf8
#!/usr/bin/python
import pickle
if __name__=='__main__':

    #############
    #   Help    #
    #############
    #    help(5)

    ################
    #   Grammar    #
    ################
    print "\n#   Grammar    \n#"
    var = 4
    string = "Hello"
    string+= "World" 
    print string
    var, string = string, var
    print var, string


    ##################
    #   Data Type    #
    ##################
    print "\n#   Data Type    #\n"
    #change the increment into 2
    mylist = ["List item 1", 2, 3.14]
    print mylist[::2]

    ###############
    #   String    #
    ###############
    print "\n#   String    #\n"
    sample = [1, ["another", "list"], ("a", "tuple")]
    print sample[:-1]
    #multiline string
    strString = """This is
    a multiline
    string."""
    print strString

    #dictionary
    print "This %(verb)s a %(noun)s." % {"noun": "test", "verb": "is"}
        
    #
    print "Name: %s\Number: %s\String: %s" % ("Poromenos", 3, 3 * "-")


    #####################
    #   Flow Control    #
    #####################
    print "\n#   Flow Control    #\n"
    rangelist = range(10)
    print rangelist

    for number in rangelist:
    # Check if number is one of
    # the numbers in the tuple.
        if number in (3, 4, 7, 9):
        # "Break" terminates a for without
        # executing the "else" clause.
            print "bingo"
            break
        # "Continue" starts the next iteration
        # of the loop. It's rather useless here,
        # as it's the last statement of the loop.

    #################
    #   Function    #
    #################
    print "#\n   Function    #\n"
    funcvar = lambda x: x + 1
    print funcvar(1)

    def passing_example(a_list, an_int=2, a_string="A default string"):
        a_list.append("A new item")
        an_int = 4
        return a_list, an_int, a_string

    my_list = [1, 2, 3]
    my_int = 10
    print passing_example(my_list, my_int)
            
    ##############
    #   class    #
    ##############
    print "\n#   class    #\n"
    class MyClass(object):
        common = 10
        def __init__(self):
            self.myvariable = 3
        def myfunction(self, arg1, arg2):
            return self.myvariable
    # This is the class instantiation
    myclass1 = MyClass()
    print myclass1.common
    print myclass1.myfunction(1,2)
    myclass2 = MyClass()
    MyClass.common = 30
    print myclass2.common
    myclass2.common = 50
    MyClass.common = 40
    # This has not changed, because "common" is
    # now an instance variable.
    print myclass1.common
    print myclass2.common

    class OtherClass(MyClass):
        def __init__(self, arg1):
            self.myvariable = 3
            print arg1

    myclass3 =  OtherClass("why")
    myclass3.test = 10
    print myclass3.test

    #################
    #   Exception   #
    ################# 
    print "#\n   Exception   \n#"
    try:
            # Division by zero raises an exception
        10 / 0
    except ZeroDivisionError:
        print "Oops, invalid."
    else:
                # Exception didn't occur, we're good.
        pass
    finally:
                # This is executed after the code block is run
                # and all exceptions have been handled, even
                # if a new exception is raised while handling.
        print "We're done with that."

    ##############
    #   Import   #
    ##############
    print "\n#   Import   #\n"
    mylist = ["This", "is", 4, 13327]
    myfile = open("./test.dat","w")
    pickle.dump(mylist,myfile)
    #myfile.close()
    myfile = open("./test.dat")
    print myfile.read()
    myfile.close()
        
    #myfile = open("./test.dat", "w")
    #myfile.write("This is a sample string")
    myfile.close()
    myfile = open("./test.dat")
    #print myfile.read()
    loadedlist = pickle.load(myfile)
    myfile.close()
    print loadedlist

    ##############
    #   Others   #
    ##############
    print "\n#   Others   #\n"
    lst1 = [1, 2, 3]
    lst2 = [3, 4, 5]
    print [x * y for x in lst1 for y in lst2]
    print [x for x in lst1 if 4 > x > 1]
    print any([i % 3 for i in [3, 3, 3, 2]])
    print sum(1 for i in [3, 4, 4, 4, 3] if i == 4)
    print sum([2,3,4,5])

    del lst1[0]
    print lst1
    del lst1
    

