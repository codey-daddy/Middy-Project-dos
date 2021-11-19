#!/usr/bin/env python
# coding: utf-8

# ###### @author: Amir Akbari
# 

# # Starting with Python
# ## Installing Python
# Please search for **Download Anaconda Python** on Google, choose your Operating System (Windows, iOS, Linux), and follow the instructions to install Python version 3 via Anaconda. Anaconda is a distributor of Python and provides Python Interpreter (engine), Sypder IDE (editor), Jupyter (notebook), .... This makes the Python configuration on your computer seamless, however, some advanced users may prefer to install Python components separately, and for example work with a different editor such as PyCharm.
# 
# **Note**: To prevent potential glitches, avoid naming your folders with special characters. Likewise, it is also recommend to avoid a space in folder and file names. You may use the underscore key, `_`, instead. While this is not an issue for installing Python or Anaconda, it is an issue for IPython which looks in 
# `c:\user\username\.ipython` for configuration files. The solution is to define the HOME variable before launching
# IPython to a path that has only ASCII characters.
# 
# I use a Windows laptop and present the shortcut keys for Windows. On Mac, often there is a similar shortcut key and functionality using the command key instead of Ctrl. Of course, Mac users can search for the shortcut on the web too. The current Python version on my device is 3.8 and I work with Spyder version 5. If you use a different version (Python 3 and above) you may notice small visual differences but the functionality would be them same.
# 
# 

# ## Understanding the Sypder Environment
# 
# Spyder is an IDE (Integrated Development Environment) for Python. The IDE makes it easier to write codes in Python and later debug your code. Below, I introduce the basics of Spyder. You may find more information about it on its website at https://www.spyder-ide.org and on its YouTube channel at **Spder IDE**. 
# 
# **Note**: You may change the background color (aka theme) or font in the Editor and other windows in Spyder from `Tools -> Preferences -> Appearance`
# 
# Spyder has three windows:   
# ![alt text](Spyder3.png "Title") 
# $$\text{Figure 1. Spyder Windows. An example Screenshot}$$
# 
# 

# 1. **Editor**: where you write your codes.
#  
# This is where you write your codes before evaluating it. In the editor, your codes are color-coded for better readability. The executable codes are shown in black font. The reserved words (see  Section 4. Variable Names and Types below for details) are in blue. The text input values (those between `" "` or `' '`) and notes are in green. The gray font lines are comments. Notes and comments are similar concepts. These are lines which will not be executed but help to document, add clarification comments, and organize your code. Use `#` at the beginning of your text to comment out a line and use `"""` to open and close a few lines of notes.
#        
# Spyder has the tab completion feature: - After entering 1 or more characters, pressing the TAB button on your keyboard will bring up a list of functions, packages, and variables that match the typed text. This will reduce the chance of a typo in the syntax and is the recommended approach in coding, especially because **Python is case sensitive** (Python is also whitespace sensitive. So indentation, either spaces or tabs, affects how Python interprets files. We will talk about these more later). If the list of matches is large, pressing the TAB button again allows the arrow keys can be used to browse and select a completion. Also, when you write the function names in Spyder a window will pop up which shows its syntax, its input variables, and further information. A similar feature is in MS-Excel.
# 
# 
# The editor comes with a line number area, shown in the left side bar (see Figure 1). If Spyder spots an error in a line of your code it will show warnings and syntax errors, with a cross in a red circle beside that line. They can help you to detect potential problems before running your code. For instance, there is an error in line 16 in Figure 1 above. If I hover my mouse on the alert sign (the cross in a red circle) an window will pop up that reads `Code Analysis` `Undefined name "MIN"`. This occurs because Python is case sensitive and differentiates between `min` and `MIN` or `Min`. It does not know what `MIN` is so it gives the error.
# 
# Once you are done with your code, you can save it similar to an MS-Excel file and open it next time. Your codes will have a `.py` type. A Python program (aka `scripts`) is a collection of functions that can be run stand alone. You can open as many files you want in Spyder. They will be shown as a new tab beside each other. In Figure 1, I have two files open: `TeachingNote_Python.py` and `untitle0.py`.In Spyder, if you modify your codes and your file is not saved afterwards, you will see an asterisk (`*`) beside its name. In Figure 1, I have modified `untitle0.py` file but did not save it, so Spyder added a `*` to indicate that.
#   
#  2. **IPython Console**: where you run your code and see the outputs
# 
# This is where you can run Python code, either from the Editor or interactively. To run your code you have several options. The most commonly used ones are:
#    * you can execute your whole script by choosing `Run` from the `Run` drop menu in the toolbar (See Figure 2). Alternatively, you may press the green triangle icon (its shortcut key on Windows is `F5`).
#    * if you want to run one part of your script, first create a cell by adding `#%%` before and after that part. Then choose `Run Cell` from the `Run` drop menu. This will execute the codes in the active cell, the one that your mouse has last clicked in. Alternatively, click the icon with the green triangle in a rectangle (its shortcut key is `Ctrl+Enter`). If you want to serially run cells, one after another, you can use `Run cell and advance` or the icon with a double green triangle in a rectangle (its shortcut is `Shift+Enter`). 
#    * if you want to run a few lines of your code, you can select them and choose `Run selection or current line` from the `Run` drop menu, or use the icon with a green triangle beside I (its shortcut key is `F9`). Similarly, you can  write part of your code in the IPython Console window and press the `Enter` key to run only that part. For example, you can use it as a calculator. Try it!
# 
#    
# ![alt text](Run_Icons_Spyder3.png "Title") 
# $$\text{Figure 2. Run command}$$
# 
# The output of your code will be shown in the IPython Console. For instance, when I execute `print("Hello, World!")`, which asks Python to display the text "Hello World!", we see this text displayed in the IPython Console window (Figure 1). An input counter number beside each of your commands will be displayed too, e.g. $\color{blue}{\text{In [1]}}$ before $\color{blue}{\texttt{print }}(\color{green}{\texttt{"Hello, World!"}})$ in Figure 1. The counter for the next command increases serially. Also, if your code has an error, it will be shown here. For example, run `x2 = MIN(5,-1,100)` to see a `NameError`.
# 
# 
# You may access the history of all the codes you executed (ran) in `History` tab in this window too.
# 
#  3. **Source Window**: it has four panes
#     * VARIABLE EXPLORER: here you can see the variables you generated. In Figure 1, I executed `x1 = min(5,-1,100)`, and we see `x1` in the Variable Explorer window, whose value is `-1`. Its type is `int` (integer) and size is 1 (See Section 4. Variable Names and Types for more details on these).
#     * FILE EXPLORER: you can see all the files or folders in your working directory (see the upper right address bar in the Figure 1, which points to the folder `C:\Users\akbara23` on my device. Click on the folder icon beside this address bar and choose a folder for this course on your computers.
#     * HELP: you can see help and documentation on the functions. To access the help and documentation of each function, in the IPython console or in the Editor, select a function (double click on it) and press `Ctrl+I`. This will call the help on that function and show it in the Source window. You can also type `help(FUNCTION_NAME)` in the console or search for the function in the HELP pane.
#     * PLOTS: if your code generates a plot, it will be shown here (see Section 5.7. Matplotlib for details on plotting in Python).

# # Working with Python
# 
# Python is an interpreted high-level programming language for general-purpose programming. For finance related purposes, Python allows us to process data with complex formulas, similar to what VBA does in MS-Excel, but with fewer limitations and more access to predefined functions. In addition, it allows us to work with large tables and databases, that are difficult to manage with MS-Excel. Moreover, it helps us to run our analysis repeatedly on different databases automatically.
# 
# Python has an extensive set of built-in functions (similar to those of MS-Excel), but you can also work with more sophisticated  functions that others have written/developed, via importing those specific Python Libraries (_will talk about them shortly_). Of course, you can  define your own functions as well.
# 
# In this teaching note, for pedagogical reasons, I do my best to draw analogies between Python and MS-Excel. This undersells the vast capabilities in Python, but I believe will help you to better adapt to this programming language.
# 
# Functions are called similar to MS-Excel: `FUNCTION_NAME( input_variables)`. For example, the `print` function prints the value of the input in the IPython Console:

# In[1]:


print("Hello world!")


# More generally, functions can have multiple input variables (separated  with commas) and can generate multiple output variables. In general, the syntax is:
# 
# `out1, out2, out3, . . . = FUNCTION_NAME(in1, in2, in3, . . .)`.
# 
# In the example below, we are giving (parsing) 3 input variables to the `min` (minimum) function:

# In[2]:


min(5, -1, 100)


# To access the help and documentation of each function, in the IPython console or in the Editor, select a function (double click on it) and press `Ctrl+I`. This will call the help on that function and show it in the Source window. 
# You can also type `help(FUNCTION_NAME)` in the console. For example for the `min` function:

# In[3]:


help(min)


# You can also search for documentation for the function in the search bar in the HELP window. Lastly, help can also be shown automatically after writing a left parenthesis next to an object. You can activate this behavior in Preferences > Help.
# 
# Note that Python is case sensitive and if you type `Min`, you will receive a `NameError`, which means python cannot recognize this function.
# 

# In[4]:


#MIN(5, -1, 100)


# `NameError                                 Traceback (most recent call last)
# <ipython-input-207-451a873a8a93> in <module>
# ----> 1 MIN(5, -1, 100)
# NameError: name 'MIN' is not defined`
# 
# 

# ## Variable Names and Types
# 
# Python, similar to MS-Excel, needs to know the type of the variables it is working with. Recall in MS-Excel, we can set the data type of each cell to  _Number, Date, Text, Currency, ..._. A similar setting exists in Python.
# 
# The full details of these are easier to comprehend when we face an application. Below, I just list some important pointers so that you can start working with Python.
# 
# 
# ### Data Names
# 
# In MS-Excel, each cell is a variable (e.g. `A2` or `B17`). In Python, we directly give a name to the variables we use (this can also be done in MS-Excel too). For instance:

# In[5]:


A = 3
B = 5
C = A+B
print(A,B,C)


# You can also just type the name of the variable and run it. e.g.

# In[6]:


C


# In this document, I use both of these approaches to display the output values. 

# Variable names can take many forms, although

# * They can only contain numbers, letters (both upper and lower), and underscores. They cannot have special characters such as `$`.
# * Names must begin with a letter or an underscore. They cannot start, for instance, with a number.
# * Names are `CaSe SeNsItIve`. That is, variables `A` and `a` are different variables.
# * Reserved Words:  The following names are Python keywords. They have special meaning and shouldn't be used as variable names: $\color{blue}{\texttt{as, or, in, is, if, and, del, not, try, for, def, from, elif, with, else, exec,}}$ $\color{blue}{\texttt{pass, while, yield, break, print,class, raise, global, assert, except, import,}}$ $\color{blue}{\texttt{ lambda, return, continue, finally}}$
# 
# 
# If you define/use them in your code as a new variable, you'll get a syntax error. Therefore, the following codes will not execute:
# 
# `x: = 1.0`
# 
# `1X  = 1`
# 
# `X-1 = 1`
# 
# `for = 1`

# ### Data Types:
# 
# Some of the most commonly used variables are (_we will see the more complex ones later in the course_):
# 
# * <ins>Integer Numbers (aka INT)</ins>: 
# 
# Integers are numbers starting from $1, 2, 3, ...,\infty$. For example:

# **Caution**: Notice that large numbers never include commas. We can ask Python to show them with commas (e.g. 123,456,789) but we do not input them with commas (e.g. 123456789). In MS-Excel, if you input 123,456,789 in a cell, Excel guesses that this is a number and automatically stores it as a number without asking the user. 
# If you want to print numbers with commas use as below

# In[7]:


a = 123456789
print(a)
print(f'{a:,}')   # if you want to display the number comma-separated


# * <ins>Real Numbers (aka FLOAT)</ins>  
# 
# Real numbers are numbers with decimal values. You can ask Python to show only a few decimals of the number (similar to the MS-Excel Data Type)

# In[8]:


a = 13.56798
print(a)
print("%.2f" % a)   # if you want to display the data with 2 decimals


# * <ins>String (aka STR)</ins>
# 
# Strings are similar to the TEXT data type in MS-Excel. In order to make a string we may use a single quote sign `'` or double quotations `"`. Either works equally well. But if the string contains one, we need to use the other. For example
# 
# `x = "His name is Conan O'Brien"`
# 
# `x = 'My cat is named "Butters"`
# 
# If you need both a `'` and a `"` in your string, you can use the escape character \ which tells Python that the following character is to be taken as the literal character and is not a quote to delimit the string.  See it in action escaping the " below:
# 
# `x = "My cat's name is \"Butters\""`
# 
# **Example**: Let's see an example using `string` and `print` function

# In[9]:


x = "My cat's name is \"Butters\""
print(x)


# Recall, the syntax for each function is `FUNCTION_NAME(in1,in2,...)`. There are no commas between parentheses. So Python assumes there is one input. The input is not a number (integer or float) nor a string (it is not in `"` or `'`). So, Python concludes that you want to print the values of variable `x`.
# 
# **Note**: Going back to our initial example, `print("Hello world!")`, the input to the `print` function is the string "Hello world!". If we do not put this string in `"`, we receive a syntax error

# In[10]:


#print(Hello world!)


# ` File "<ipython-input-345-01a3c6a17cb8>", line 1
#     print(Hello world!)
#                 ^
# SyntaxError: invalid syntax`
# 
# 
# 
# The error message is pointing to `w` in `world`. Why? 
# Because you are not parsing a number or a string. So, Python concludes that you are parsing a variable to be printed but the name of this variable has space in it (before `world`), and spaces are not allowed for names. Ok, let's substitute space with an underscore `print(Hello_world!)`

# In[11]:


#print(Hello_world!)


# `  File "<ipython-input-572-a8b0d1e4f18c>", line 1
#     print(Hello_world!)
#                      ^
# SyntaxError: invalid syntax`
# 
# 
# 
# Again, we get a syntax error but this time it is pointing to `!`. Recall, variable names cannot have special characters such as `!`. Ok, let's remove it, `print(Hello_world)`
# 

# In[12]:


#print(Hello_world)


# `---------------------------------------------------------------------------
# NameError                                 Traceback (most recent call last)
# <ipython-input-692-fabb9b810891> in <module>
# ----> 1 print(Hello_world)
# NameError: name 'Hello_world' is not defined`
# 
# And now we get a Name Error, suggesting that we want to work with (print) a variable that we have not defined it before.

# * <ins>List (aka LIST)</ins> 
# 
# List allows you to have a group of variables in one variable. This is similar to selecting a series of cells (in a row or column) in MS-Excel. For example
# 
# List of characters: `x1 = ['a','b','c']`
# 
# List of numbers: `x2 = [1,5,23]`
# 
# List of characters and numbers: `x3 = ['ball', 3.14, -50, 'university', "course"]`
# 
# List of Lists: `newEngland=[["Massachusetts",6692824],["Connecticut",3596080],["Maine",1328302],["New Hampshire",1323459],["Rhode Island",1051511],["Vermont",626630]]`

# * <ins>Boolean (aka BOOL)</ins>
# 
# The Boolean variables are `0/1` or `True/False` variables. e.g.:

# In[13]:


x1 = True
y1 = False   


# Boolean variables are very useful in conditional statements, such as `IF` statements.

# ## Working with Numbers
# ### Basic arithmetic operations on numbers
# * Basic operators:
#   * +, -, *, /: These add, subtract, multiply, divide.
#   * **: This is for exponentiating (to the power).
#   * //: This is for integer divide (drops fractional part).
#   * %: This is to compute remainder on division for integers (MOD function in MS-Excel).

# In[14]:


a = 5
b = 2
x1 = a + b
x2 = a * b
x3 = a ** b
x4 = a / b
x5 = a // b
x6 = a % b

print("x1=",x1, "; x2=", x2, "; x3=",x3, "; x4=",x4, "; x5=",x5, "; x6=",x6)


# ### Priority of operations:
# The usual laws of arithmetic hold with respect to the priority of the operations. For example,
# 

# In[15]:


x7 = x1 + x2*x3**x4/x5
print(x7)


# $x_7 = x_1 + \frac{x_2 \; x_3^{x_4}}{x_5}$

# $\;\;\;\; = 7 + \frac{10 \; 25^{2.5}}{2}$

# $\;\;\;\; = 7 + \frac{10 \; 3125}{2}$

# $\;\;\;\; = 7 + 15625$

# $x_7 =  15632$
# 
# Of course, you can use parentheses to clarify the priority of operations:

# In[16]:


x7 = x1 + ((x2*(x3**x4))/x5)
print(x7)


# ## Working with Lists
# ### Accessing items of a list
# Consider the following example, where a list is called Alphabet:

# In[17]:


Alphabet = ["a","b","c","d","e","f"]


# To get the $i^{th}$ element of the list, we use the following syntax: `List_name[i-1]`. In Python, the index of a list (and array and matrix variables that we will see later) starts from 0. Example:
# 

# In[18]:


print ("The 1st item of Alphabet is: ", Alphabet[0]) 
print ("The 2nd item of Alphabet is: ", Alphabet[1]) 
print ("The Last item of Alphabet is: ", Alphabet[-1]) 


# This is equivalent to the `INDEX(array, row_num, [column_num])` function in MS-Excel, where you can access a cell by giving the row and column number of a cell to access it. For example, `INDEX(A4:C10, 2, 3)` returns cell `C5`.
# 
# 
# If you are interested in a few items, you can use a range

# In[19]:


print ("Items 2, 3, and 4 of Alphabet are: ", Alphabet[1:4]) # (Index 1,2,3 excluding 4)
print ("3 first items of Alphabet are: ", Alphabet[:3]) # (Index 0,1,2 excluding 3)
print ("Items 4 to end of Alphabet are: ", Alphabet[3:]) # (Index 3, 4, ...)


#  if for any reason you want to access to an empty list:

# In[20]:


x = []


# ### Functions of Lists
# * The `len()` function gives the length of a list variable (i.e. the number of items in the list). This is similar to the `COUNT()` function in MS-Excel, which helps us get the length of an array of cells.
#  e.g.

# In[21]:


x = len(Alphabet)
print("Alphabet has", x, "items.")


# * One can insert an item in the List, at a certain place with the `.insert` feature, 
# * add an item to the end of the list with the `.append` feature
# * If you want to remove an item from the list, use the `.remove` feature of the list:

# In[22]:


Alphabet.insert(2, 'Z') # add character `Z` as the 3rd item of Alphabet
Alphabet.append('B')    # add character `B` at the end of Alphabet
Alphabet.remove('f')    # remove character `f` from Alphabet

print(Alphabet)


# * If you are interested to find the index of an item on the list, use the `.index` feature of the list:

# In[23]:


print(Alphabet)
Alphabet.index('c')


# Similarly in MS-Excel, we can use the `ROW()` and `COLUMN()` functions to get the row and column indexes of a cell.

# * You can easily sort a list by `.sort` feature:

# In[24]:


A = [3,5,-1,2,0,10,11,0]
A.sort()
print("After sorting, A is:", A)


# In MS-Excel, we can use `Sort & Filter` option.

# **Note**,  `.sort` permanently change the order of your list. If you want to keep the original ordering of the list but you need to sort it, say for just printing, you can use the `sorted()` function:

# In[25]:


numlist = [67, 54, 39, 47, 38, 23, 99, 91, 91, 70]
print("sorted numlist is:",sorted(numlist))
print("But numlist stays as-is:",numlist)


# * use `in` feature to check if an item  belongs to a list. 
# For example, running this statement will return `True`, because Alphabet includes "a".

# In[26]:


"a" in Alphabet  


# In[27]:


# And running this statement will return False
"r" in Alphabet                  


# ### Copying Lists
# 
# Lists are mutable and so assignment does not create a simple copy. After the assignment the changes to either variable affect both.

# In[28]:


x    = [1, 2, 3]
y    = x
y[0] = 10


print("y = ", y)
print("x = ", x)


# This is because of the memory management of Python. Setting `y = x`, also sets the memory pointer of `y` equal to that of the `x`. Therefore, if you change `y`, you are also changing `x`. This makes  data management more efficient by Python (but we don't care about it in this class). 
# 
# However, slicing a list creates a copy of the list and any immutable types in the list – but not mutable elements in the list. This helps you preserve the value of `x`. In this way, simply copy the content of `x` to `y`:

# In[29]:


x    = [1, 2, 3]
y    = x[:]
y[0] = 10
print("y = ",y)
print("x = ",x)


# ## Converting Variable Types
# Similar to MS-Excel. Sometimes variables are stored in the wrong format and we need to change them.
# 
# * You can find the type a variable `x` by entering:

# In[30]:


type(Alphabet)


# In[31]:


x1 = 40
type(x1)


# * convert a string (character) to a number 

# In[32]:


x2 = "30"
print("type of the variable x2 is", type(x2))
# Similarly
x3 = str(x1) 
print("type of the variable x3 is",type(x3))


# In MS-Excel, the function `TEXT()` does a similar job.

# * convert a number which is stored as a string (character) back to a number 

# In[33]:


x4 = int(x2) 
print("type of the variable x4 is",type(x4))


# In[34]:


x5 = float(x2) 
print("type of the variable x5 is",type(x5))


# Knowing the data type of the variables you are working with is important. For example since `x2` and `x3` are stored as a string (character) then `x2+x3` is '3040' (not 70)!

# In[35]:


print(x2+x3)


# however, `int(x2)+int(x3)` is 70.

# In[36]:


x = int(x2)+int(x3)
print(x)


# # Conditional Statement
# ## IF statement
# 
# The concept of the `IF` statement is similar to the one in MS-Excel. There are three versions of the `IF` conditions: (1) if - then, (2)if-then-else, (3)if-then-elseif-then-else.
# 
# 
# In Python, the statement after the condition is considered the "then" statement of the `IF` statement and there is no need to include the  "then" argument. Simply add 4 spaces or 1 tab to open the "then" arguments.
#     
#  
# 1. Simple if-then statement: the syntax is as follows
#     
# `IF CONDITION :`
# 
# $\;\;\;\;$ `WHAT TO DO IF CONDITION HOLDS`
# 
# 
# For example:

# In[37]:


x = 5
if x > 0:
    print("x equals to", x)
    print("x is positive")


# 2. if- then- else     the syntax is as follows
#     
# `IF CONDITION :`
# 
# $\;\;\;\;$ `WHAT TO DO IF CONDITION HOLDS`
# 
# `ELSE:`
# 
# $\;\;\;\;$ `WHAT TO DO IF CONDITION DOES NOT HOLD`
# 
# For example:
#     

# In[38]:


y = 0   
if y > 0:
    print("y is positive")
else:
    print("y is not positive")


# 3. if- then- else if- then, ... Nested if statement can be implemented with `elif` command (shorten version of else if). The syntax is as follows
#     
# `IF CONDITION_1 :`
# 
# $\;\;\;\;$ `WHAT TO DO IF CONDITION_1 HOLDS`
# 
# `ELIF CONDITION_2 :`
#  
# $\;\;\;\;$ `WHAT TO DO IF CONDITION_2 HOLDS`
# 
# `ELSE:`
# 
# $\;\;\;\;$ `WHAT TO DO IF CONDITION_1 & CONDITION_2 DO NOT HOLD`
#     
# `elif` can be repeated as often as necessary. For example:    

# In[39]:


z = 0
if z > 0:
    print("z is positive")
elif z < 0:
    print("z is negative")
else:
    print("z must be 0")


# ## Logical Operators and Devices
# 
# Logical operators and devices are useful if you want to create (more complex) conditions. The core logical operators (besides `>` and `<`) are
# 
#   * `>=` :  Greater than or equal to
#   * `<=` :  Less than or equal to
#   * `==` :  Equal to
#   * `!=` :  Not equal to 
# 
# **Note:** Python uses `=` for assignment and `==` for testing equality. Whereas, in MS-Excel, you can use `=` in the `IF` statement for testing equality. There you can use `<>` to test for the `not equal` condition.  
# 
# 
# If you want to combine several conditions you use logical devices:
# 
# * `logical_and()`: Both logical expressions are True. Alternatively use `and` or `&` between conditions
# * `logical_or()` : Either of the logical expressions is True. Alternatively use `or ` between conditions 
# * `logical_not()`: Not True. Alternatively, use `not` or `~` between conditions
# 
# There are equivalent logical operators in MS-Excel such as `AND()`, `OR()`, and `NOT()` functions that can be used in the `IF` statement.
# 
# 
# * Special case: for lists you can also use the `in` feature to check if an item  belongs to it. 

# In[40]:


Team = ['T','e','a','m']
if ~('i' in Team): 
    print('There is no "i" in "Team"!')


# You can achieve similar functionality in MS-Excel too but it is less straightforward. You can use the `contain` search option in a column that is already `Filter`ed. 

# ## For statement
# A `FOR` loop, allows you to iterate an operation several times. The Python for statement iterates over the members of a sequence in order, executing the block each time. There is no easy to access alternative in MS-Excel for loops. Often, people use an index variable (say row 1 to 10), and copy the equation in multiple rows in the adjacent  column to mimic the loop functionality.
# This is simpler in Python. The syntax is
# 
# `FOR DEFINED_RANGE :`
# 
# $\;\;\;\;$ `WHAT TO DO IF CONDITION_1 HOLDS`

# For example, below, we ask Python to print "Financial Modeling is FUN with Python!"  10 times.
# We use the `RANGE` function to specify the number of iterations:

# In[41]:


# Example 1
for i in range(10):
    print("Financial Modeling is FUN with Python!" )


# The `RANGE(a,b,j)` function uses a start number `a`, a stop number `b` and a step size `j`. When not specified, `a=0` and `j=1`. For example, `range(10)` is equivalent  of `range(0,10,1)` and `range(2,10)` is equivalent  of `range(2,10,1)`.

# In[42]:


# Example 2
for i in range(2,10):
    print(i,end=' ') 
# the `end=' '` is used to avoid the enter at the end of each print.
# therefore the output is printed in one line:


# In[43]:


# Example 3
for ct in range(2,9,2):
    print(ct,end=' ')


# In[44]:


# Example 4
for ct in range(22,5,-3):
    print(ct,end=' ')


# We can define a specific range by using iterating in a list:

# In[45]:


# Example 5
for names in ["Sarah", "Ben","Moe"]:
    print(names)


# In[46]:


# a more advanced example of 5
Companies = ['TD','RBC','Goldman Sachs']
CEOs      = ['Bharat Masrani','David I. McKay','Lloyd Blankfein']

for i in range(len(Companies)):
    print('CEO of', Companies[i],'is',CEOs[i],'.' )
# here i gives the index of the loop for each iteration.


# Note that this is identical to the example below, where I use the `enumerate` function to also get the index number in the `CEOs` list and assign it to the variable `i`:

# In[47]:


# a more advanced example of 5
CEOs = ['Bharat Masrani','David I. McKay','Lloyd Blankfein']

for i,company_name in enumerate(['TD','RBC','Goldman Sachs']):
    print('CEO of', company_name,'is',CEOs[i],'.' )
# here i gives the index of the loop for each iteration.


# Loops can also be nested (a `FOR` loop inside another `FOR` loop). Pay attention to the spacing at the beginning  of each line, in each loose

# In[48]:


# Example 6
count = 0
x = range(10)
y = range(10)

for i in x:
    for j in y:
        count = count + j
print(count)


# **Important:** The iterable variable (in the above example `x` and `y`) should not be reassigned once inside the loop.

# A loop can be terminated early  using `break`. The `break` command is usually used after an `if` statement to terminate the
# loop prematurely if some condition has been met.

# In[49]:


# Example 7
x = range(10)
for i in x:
    print(i,end=' ')
    if i > 5:
        break


# A more readable implementation of the above example is with the use of `while` loops:
# 
# `WHILE CONDITION_HOLDS:`
# 
# $\;\;\;\;$ `WHAT TO DO IF CONDITION_1 HOLDS`
# 
# Contrast the `for` statement with the `while` loop, we check a condition for each iteration. For example:

# In[50]:


i = 0
while i < 10:
    print("Financial Modeling is FUN with Python!" )
    i = i+1


# # Define a Function:
# In Python, you can define your own function, in a separate file for example, and call it. This will help you with code-readability and debugging your code. You can test each function separately and then merge them all.
# 
# The syntax is as follows:
# 
# ` DEF FUNCTION_NAME(INPUT_VARIABLE):`
# 
# $\;\;\;\;$ `PROCESS INPUT_VARIABLE`
# 
# $\;\;\;\;$ `RETURN OUTPUT_VARIABLE (optional)`

# After defining your function, you should load it to Python. This way, Python learns about your newly defined function.
# Then you can parse any input variable you like to the function, as many times as you like. 
# There are two ways to do so
# 1. Simple: copy the function you wrote in the console and run it. 
# 2. Complete: save it in a .py file (e.g. MyFunctions.py). Then load it similar to a library (see the next section)
#     

# **Example:** Write a function that calculates the total grade of a student in Commerce-3FD3 Financial Modeling, from his/her grade in 5 weekly assignments (10% in total), 2 midterm exams (40% in total), final exam (40% in total), and class participation (10% in total)

# In[51]:


def Total_Grade_3FD3(Assignments,MidtermExams,FinalExam,ClassParticipation):
    # Input values: 
        # Assignments is a list of 5 marks, each with a 2% weight
        # MidtermExams, each with a 20% weight
        # FinalExam, each with a 40% weight
        # ClassParticipation, each with a 10% weight
    # Output
        # Total_Grade = 10% x Assignments + 40% x MidtermExams + 40% x FinalExam + 10% x ClassParticipation
    
    
    Total_Grade = 0.02 * sum(Assignments) + 0.20 * sum(MidtermExams) + 0.40 * FinalExam + 0.10 * ClassParticipation
    return Total_Grade


# Now that we have this function, we can run the above function to get the grade of any student. For example

# In[52]:


# Sarah's marks:
Total_Grade_3FD3([100,0,0,100,50],[80, 65],78, 80)


# In[53]:


# Rose's marks:
Total_Grade_3FD3([100,100,100,100,100],[80, 75],88, 100)


# I can now give the data for the whole class and get their total grade.

# In[54]:


# step 1. create the input data
Section_4_marks = [
    ["Sarah",[100,0,0,100,50],[80, 65],78, 80],
    ["Rose",[100,100,100,100,100],[80, 75],88, 100],
    ["Ben",[100,0,0,100,50],[80, 65],78, 80],
    ["John",[0,0,0,100,50],[50, 45],38, 20],
]
# step 2. calcualte the marks for wach student and print
for student_i in Section_4_marks:

    student_i_totalGrade = Total_Grade_3FD3(student_i[1],student_i[2],student_i[3],student_i[4])
    print("The total mark for", student_i[0], "is", student_i_totalGrade)


# I can further modify my codes to get the class average. 

# In[55]:


# step 1. create the input data
Section_4_marks = [
    ["Sarah",[100,0,0,100,50],[80, 65],78, 80],
    ["Rose",[100,100,100,100,100],[80, 75],88, 100],
    ["Ben",[100,0,0,100,50],[80, 65],78, 80],
    ["John",[0,0,0,100,50],[50, 45],38, 20]
]
# step 2. create the output
Section_4_totalGrades = []

# step 3. calcualte the marks for wach student
for i, student_i in enumerate(Section_4_marks):

    student_i_totalGrade = Total_Grade_3FD3(student_i[1],student_i[2],student_i[3],student_i[4])
    
    Section_4_totalGrades.append(student_i_totalGrade)

# step 4. print the class average
classAverage = sum(Section_4_totalGrades)/len(Section_4_totalGrades)
print("The class average is", classAverage)


# Furthermore, you can call a function inside another function. 

# # Libraries
# 
# In Python, many tools (functions) are not automatically loaded and are in modules called libraries. To be able to use the functions in a library, you first need to load the library. It is recommended to only load libraries that you need in each of your codes. In this way, you keep your programs smaller when they aren't needed. 
# 
# There are a large number of libraries available for Python. Often you need to search online to find the proper library and the proper functions in that library to get the desired job done.
# For the purpose of this class, I shortly introduce a set of widely used libraries and their functions that help us with financial modeling,  such as `NumPy`, `Pandas`, `MatPlotLib` and `SciPy`. These libraries are already installed on your devices once you install Python with Anaconda. There are two other libraries that we use frequently and are not already installed: `MumPy-Financial` and `Pandas_DataReader`. Below, I show how to install a library on Python.B
# 
# ## Install packages (library)
# There are several methods to install packages. The most common one is `pip install`:
# 
# On your computer, in Windows program files, search for `Anaconda Prompt(Anaconda3)`. In Mac iOs you can search within the Terminal search bar. This will open a black command window. Type
# `pip install numpy-financial` and press enter. This will install the `NumPy-Financial` library on your Python
# 
# ![alt text](pip_install.png "Title") 
# $$\text{Figure 3. PIP INSTALL with Anaconda Prompt}$$
# 
# Similarly, type `pip install pandas_datareader` to install this library.
# 
# ## Working with libraries
# 
# To get the documentation for a library,  go to docs.python.org/3/ and search for the name of  that library (say `NumPy`). Go to that library and review the functions there. You can alternatively, go to Help>Python Documentation in Spyder and search `NumPy` in the index.  You see the same thing.
# 
# 
# A typical way of loading a library is by using the `import LIBRARY_NAME`: e.g. 

# In[56]:


import numpy_financial # which will load the library named NumPy-Financial. or
import numpy_financial as npFin # you can assign a short name for the library too.


# Then you can call the functions inside the library (here the `NumPy-Financial` library) by `LIBRARY_NAME.FUNCTION_NAME(INPUT)`. This way, Python will not mix two functions with similar names that are in different libraries.
# 
# 
# You can use the `dir()` command to get the list of functions in each library. For example, after importing the library (say `NumPy-Financial`), in the IPython console type `dir(NumPy_Financial)` to get the list of functions in the Numpy library. ` For example

# In[57]:


import numpy_financial as npFin
dir(npFin) 
# this will give the list of some of the financial functions of NumPy


# These functions are equivalent to MS-Excel functions for time value of money. I will discuss them in the section for the NumPy-Financial library. 

# Below, I will introduce `NumPy` (which offers a series of mathematical calculation functions), `MumPy-Financial` (for its time value of money functions), `Pandas` (for data processing in the spreadsheet format), `Pandas_DataReader` (for downloading financial data from the web), `Matplotlib` (to plot graphs), `SciPy` (for optimization functions), and `Statsmodels` (for statistical analysis). This is a basic introduction so that you can start working with these libraries. You may need to consult their documentation webpages or online forums for a more indepth understanding.

# ## NumPy Library
# NumPy is a powerful library that allows data processing on large, multi-dimensional arrays and matrices. Moreover, it provides a large collection of high-level mathematical functions to operate in these arrays. Most other libraries use NumPy functions in the background. So, I start with it.
# 
# ### Data Types:
# NumPy works exclusively with numbers (`integer` and `float`). There is also `NaN`, or Not a Number, which happens if the input data has missing observations, similar to the blank cells in MS-Excel, or whenever a function produces a result that cannot be clearly evaluated to produce a number. There are also `inf`, which represents infinity, and `-inf`, which represents the negative infinity. These might happen, for instance, if you divide by a very very small number, closed to 0.

# NumPy provides the core data types for numerical analysis – **arrays** and **matrices**, which are both similar to lists, but arrays and matrices, unlike lists, are always rectangular so that all dimensions have the same
# number of elements. They resemble  the Tables/sheets in MS-Excel. We use mostly arrays in this class. Matrices are essentially a subset of arrays and behave in a virtually identical manner. The two important
# differences are:
# 
# * Matrices always have 2 dimensions, whereas Arrays can have 1, 2, 3 or more dimensions (although in this course we mostly use 2-dimensional arrays to be consistent with the MS-Excel examples)
#     * This means that a `1` by `n` vector stored as an array has `1` dimension and `n` elements, while the same vector stored as a matrix has 2-dimensions where the sizes of the dimensions are `1` and `n` (in either order).
# 
# * Matrices follow the rules of linear algebra for multiplication.     
#     * Standard mathematical operators on arrays operate element-by-element, similar to MS-Excel. This is not the case for matrices, where multiplication `(*)` follows the rules of linear algebra (this makes coding more concise).
# * The best practice is to use arrays and to use the `@` symbol for matrix (linear algebra) multiplication. 
# 
# ### Constructing Arrays
# 
# To create an array, from a list, use the `array()` function:

# In[58]:


import numpy as np
X = [0.0, 1, 2, 3, 4]
Y = np.array(X)
print("An example of a 1-row-4-column vector (1x4):")
print(Y)


# In[59]:


Y = np.array([[0.0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
print("An example of a 2-row-4-column matrix (2x4):")
print(Y)


# You can find the dimension of your array/ matrix with the `shape()` function:

# In[60]:


print(np.shape(Y))


# The first item indicates the number of rows and the second item indicates the number of columns.

# In[61]:


print("Y is an array of", np.shape(Y)[0], "by",np.shape(Y)[1] )


# ### Merging Two arrays (`concatenate`)
# use `concatenate()` function from the `NumPy` library can help you merge two arrays. This is similar to the `.append()` feature in lists. Use the `axis` option of the function to define the dimension of the merger:

# In[62]:


X = np.array([[1.0,2.5],[3.4,4.6]])
Y = np.array([[5.0,6.0],[7.1,8.9]])
Z1 = np.concatenate((X,Y),axis = 0) # stack x on top of y
print(Z1)


# In[63]:


Z2 = Z1 * 3 # create a new 4 by 2 array from z1
Z3 = Z1 * -2 # create a new 4 by 2 array from z1
Z = np.concatenate((Z1,Z2,Z3),axis = 1) # stack z2 beside z1
print(Z)


# In MS-Excel, you cannot automatically concatenate arrays or matrices. You can manually copy and paste the cells you want. This could be a very time consuming process, if you are working with several sheets. Also you might make mistakes. 

# ### Accessing elements of Arrays
# Similar to Lists, you can access each item of an array by indexing:

# In[64]:


print(Z[1,2]) # the item in row 2 and column 3 


# In[65]:


print(Z[2:4, 0:2 ])  # rows 3 to 4 (exclusive) and columns 1 to 2 (exclusive)


# In[66]:


print(Z[:2, ])  # rows 0 & 1  and all columns


# In[67]:


print(Z[1:,])  # rows 2 to end and all columns


# In[68]:


print(Z[:2,])  # rows 2 to end (every other row) and all columns


# You can reshape your array using the `reshape()` function, as follows:

# In[69]:


W = np.reshape(Z,(2,12))
print("W is a reshaped matrix of Z, which is", np.shape(W)[0],       "by",np.shape(W)[1] )
# I used \ sign to break a long line of code into two shorter ones.
print(W)


# ###  Quick look at arithmetic operations
# * Basic operators:
#   * `+, -, *, /`,
#   * `**`,
#   * `//`,
#   * `%`,
# * When  `x` and `y` are scalars, the behavior of these operators is obvious. 
# * When `x` and `y` are arrays the operation is element by element. Therefore, `x` and `y` should be the same size.
# 
# #### Matrix Multiplication
# * Matrix Multiplication is accessible with `@`. If `X` is a matrix with `N` rows and `M` columns (`N by M`) and `Y` is `M` by `L`, `Z = X @ Y` produces an array with `V[i,j] = sum X[i,m] Y[m,j]`, where `m=1 to M` and `X[i,m]` denotes the row `i` and column `m` value of the matrix `X`. 
# 

# In[70]:


V = X @ Y
print("X =")
print(X)

print("Y =")
print(Y)

print("V = X Matrix-multiply Y")
print(V)


# $$\begin{array}{lcl}
# V[0,0] &=& X[0,0] \times Y[0,0] \:+\: X[0,1] \times Y[1,0]\\
# &=& 1 \times 5 \:+\: 2 \times 7\\
# &=& 19 
# \end{array}$$
# 
# $$V[0,1] = X[0,0] \times Y[0,1] \:+\: X[0,1] \times Y[1,1]$$
# 
#  etc

# #### Sum, Product and Difference of an Array

# Similar to MS-Excel, in NumPy we have `sum()` and `product()` functions that allow us to get the sum/product of all elements of an array. Let's see some examples:

# Let's consider the array Z that we created above:

# In[71]:


print("Z = ")
print(Z)


# In[72]:


print(np.sum(Z))   # sum all elements of the array (output = 1 element)


# In[73]:


print(np.sum(Z, 0)) # sum the elements of each column, (output = 4 elements)


# In[74]:


print(np.sum(Z, 1)) # sum the elements of each row (output = 3 elements)


# `nansum()` is identical to `sum()`, except that NaNs are ignored. 

# Numpy also has a function to create the cumulative sum, called `cumsum`. This is very useful for financial applications, where each row is added with the above ones. You need to tell NumPy on which axis you want it to run the summation: 

# In[75]:


# cumulative sum, across the rows
print(np.cumsum(Z,0)) 


# In[76]:


# cumulative sum, across the columns
print(np.cumsum(Z,1)) 


# `prod()` and `cumprod()` behave similarly to `sum()` and `cumsum()` except that the product and cumulative product are
# returned. 

# `diff()` generates the difference between elements of an array. This is useful when you want to get how much a company has grown from the previous year, for example, or compute the stock returns. For instance,
# 
# `Q= np.diff(Z, 1, axis=0)` will give the 1st difference between elements of array `Z`. In this case, first row of `Q` is equal to the second row of `Z` minus the first row of `Z`. i.e.:
# $Q[0,] = Z[1,] - Z[0,]$
# and so on
# 

# In[77]:


Q= np.diff(Z, 1, axis=0)   
print(Q)


# In[78]:


# Double difference, column by column

print(np.diff(Z, 2, axis=0)) 


# #### Other Simple Math Functions for Array
# 
# Similar to MS-Excel:
# 
# * `exp()` returns the element-by-element exponential (e ^ x ) for an array.
# * `log()` returns the element-by-element natural logarithm (ln(x)) for an array.
# * `log10()` returns the element-by-element base-10 logarithm (log10 (x )) for an array.
# * `sqrt()` returns the element-by-element square root of x
# * `abs()` returns the element-by-element absolute value for an array.

# ### Descriptive Statistics
#  Python has `max()`, `min()`, `sum()` functions to generate some basic descriptive statistics. For other descriptive statistics, such as mean, median, standard deviation , variance, ... we can use functions in NumPy Library:
#  
#  * `mean()` and `nanmean()`. in MS-Excel, we have the `AVERAGE()` function
#  * `median()`, in MS-Excel, we have the `MEDIAN()` function
#  * `std()` and `nanstd()`. in MS-Excel we have `STDEV.P()` and `STDEV.S()`
#  * `var()` and `nanvar()`. in MS-Excel we have `VAR.P()` and `VAR.S()`
#  
#  These functions, similar to the `sum()` function allow you to choose the Axis or axes along which the statistics  are computed. The default is to compute the flattened array.
#  
# **Example:**

# In[79]:


# input variables:
nlist     = [2, 4, 13, 3, 7, 8, 5]
rlist     = [3.14, 2.71, -8.43, 5.25, 10.11, -23.78, 44.45]

print("the maximum of nlist is",max(nlist))
print("the minimum of nlist is",min(nlist))
print("sorted nlist is:",sorted(nlist),       ", the min is the first item:",sorted(nlist)[0],      ", and the max is the last item of the list:",  sorted(nlist)[-1])
print("the sum of nlist is",sum(nlist))


# In[80]:


avg_nlist = np.mean(nlist)
print("The average of nlist is ",avg_nlist)

avg_rlist = np.mean(rlist)
print("The average of rlist is ",avg_rlist)


# In[81]:


median_nlist = np.median(nlist)
print("The median of nlist is",median_nlist)
# alternative way to find the median is:
print("sorted nlist is :",sorted(nlist),       "and the median is the middle item:",sorted(nlist)[len(nlist)//2] )


# In[82]:


print("The standard deviation of rlist is",np.std(rlist))
print("The variance of rlist is",np.var(rlist))


# #### System of Equations
# * `solve()` solves the system of linear equations, 
# 
# **Example** Consider the following problem where we have 3 equations and 3 unknowns $(a, b, c)$
# 
# $$\begin{array}{lcl}
#         11 &=& a \: 1 + b \: 2 + c \: 4 \\
#         12.5 &=& a \: 3.4 + b \: 4.4 + c \: 9.1 \\
#         3.3 &=& a \: 2.2 + b \: 1.9 - c \: 0.5
# \end{array}$$
# 
# 
# To solve this, first define arrays $Y$, as vector of left-hand side $y_i$ variables, and $X$ as the matrix of right-hand side $x_{ij}$ variables. 
# $$\begin{array}{lcl}
#         y_1 &=& a \: x_{11} + b \:x_{21} + c \:x_{31} \\
#         y_2 &=& a \: x_{21} + b \:x_{22} + c \:x_{23} \\
#         y_3 &=& a \: x_{31} + b \:x_{32} + c \:x_{33} 
# \end{array}$$
# 
# where, 
# 
# \begin{equation*}
# Y = 
# \begin{bmatrix}
# 11 \\
# 12.5 \\
# 3.3
# \end{bmatrix}
# \end{equation*}
# 
# \begin{equation*}
# X = 
# \begin{bmatrix}
# 1 & 2 & 4 \\
# 3.4 & 4.4 & 9.1 \\
# 2.2 & 1.9 & -0.5
# \end{bmatrix}
# \end{equation*}
# 
# Then use the `solve` function from the linear algebra package of NumPy (`np.linalg`). As numerical, below I solve the above system of equations with the following values for $Y$ and $X$:
# 

# In[83]:


X = np.array([[1,2,4],[3.4,4.4,9.1],[2.2,1.9,-0.5]])
Y = np.array([[11],[12.5],[3.3]])
np.linalg.solve(X,Y)


# ### Random Variables
# In Python, you can generate random values with different distributions using the functions in the `NumPy` library ( for more advanced random number generators you may want to use the functions in the `RANDOM` library.) 
# 
# Most often we use 4 types of random variables:
# 
# * <ins>Uniform Distribution (real numbers)</ins>
# 
# This is the case if you want to generate a random number in a range (between `a` and `b`) with equal probability. Example:

# In[84]:


np.random.rand()
# This generates a random number between 0 and 1, each time you call it.


# In[85]:


np.random.rand(3,2)
#Create an array of the given shape (here a 3-by-2 matrix) 
# and populate it with random samples from a uniform distribution over [0, 1).


# * <ins>Uniform distribution (integer numbers)</ins>
# 
# if you want to generate a random INTEGER number in a range (between `a` and `b`) with equal probability. For example, you want to simulate rolling a six-faced dice  for 10 times:

# In[86]:


np.random.randint(1, high=6+1,size=10)
# This generates 10 random integers between 1 and 6, each time you call it.


# * <ins>Uniform distribution (from a set of options):</ins>
# 
# For example, if you want to simulate flipping a coin (Heads or Tails):

# In[87]:


coin   =["Head","Tail"]
np.random.choice(coin, size=10) # this will replicate 10 coin flipping


# In[88]:


# you can modify the chance (probability) of the Head or Tail events
# below I set the probability of a Head = 70% (therefore we get more Head outcomes)
np.random.choice(coin, size=10, p=[0.70, 0.30])


# * <ins>Normal distribution (bell curve)</ins>
# 
# Most random variables in the world are normally distributed (following central limit theorem). A normally distributed random variable is defined with its mean (the center of the bell curve) and its standard deviation (the dispersion around the mean of the bell curve).

# In[89]:


np.random.randn() 
# This generates a standard normal random value 
# with mean 0 and standard deviation 1
# the output ranges from -inf. to +inf. 


# In[90]:


np.random.randn(3,2) 
# This generates a matrix of 3_by_2 normal random values


# Let's experiment with random generating functions, as an example:
# 
# The following example builds a sentence using various parts of speech. It randomly chooses words from a list by using `np.random.choice()`. We have used a method of the string data type to capitalize the first letter of the sentence.
# 

# In[91]:


verbs   =["goes","cooks","shoots","faints","chews","screams"]
nouns   =["bear","lion","mother","baby","sister","car","bicycle","book"]
adverbs =["handily","sweetly","sourly","gingerly","forcefully","meekly"]
articles=["a","the","that","this"]

def sentence():
    article = np.random.choice(articles)    
    noun = np.random.choice(nouns)
    verb = np.random.choice(verbs)
    adverb = np.random.choice(adverbs)
    
    our_sentence = article + " " + noun + " " + verb + " " + adverb + "."
    our_sentence = our_sentence.capitalize()
    
    print(our_sentence)


# In[92]:


# call the function to print the random sentence:
sentence()


# ## NumPy-Financial
# The NumPy-Financial Python package is a collection of Time Value of Money functions. These functions were copied to this package from version 1.17 of NumPy. 
# 
# You need to first install this library as it is not included in the main package during the installation. Launch Anaconda Prompt (from the Start menu of Windows or the Mac equivalent) then type/run: `pip install numpy-financial`. It will download and install it on your machine.
# 
# The functions in this library are:

# In[93]:


import numpy_financial as npFin
dir(npFin)


# These are similar to the time value of money functions in MS-Excel. Let's see some examples:
# * <ins>`npv(rate, values)`</ins>
# 
# This is almost identical to the `NPV(rate,value1,[value2],...)` function in MS-Excel to calculate the net present value of a series of future cash flows, with this distinction that the first input cash flow is for today. In MS-Excel, the first input cash flow is for the next period and the user needs to manually subtract the initial cash flow to calculate the _net_ present value

# **Example** suppose you are asked to calculate the NPV of a project with initial investment of $ 10 Million. The cash flows in next 5 years are -2,1,3,10,20 million dollars. Your required rate of return is at least 10%:

# In[94]:


DiscountRate = 0.10
CashFlow = np.array([-10,-2,1,3,10,20])*1e6

NPV = npFin.npv(DiscountRate,CashFlow)
print('Net Prsent Value is ${:,.2f}'.format(NPV))  
# Notice that I am using a formatting command
# this changes the formatting of the output to currency, with 2 decimals.


#  * <ins>`pv(rate, nper, pmt, fv=0, when='end')`</ins>
#  
# Similarly, `pv()` calculates the present value of future cash flows. The cash flows could be an annuity payments (pmt) that are paid at certain dates (such as loan payments), or could be a lump sum payment (fv) paid at maturity (such as the principal of a zero coupon bond), or could be both (such as corporate bonds). 
# 
# Similar to the MS-Excel PV function, the argument `when` defines if it is an **Annuity due**, where the payments are at begins of each period (such as rent and insurance payments), or **Ordinary Annuity**, where payments are paid at the end of each period (such as mortgage and loan payments). Choose `when = {'begin', 1}` or `when = {'end', 0}` depending the application. The default value is `end`.
#  The default value of `fv` is `0`.

# **Example** Suppose you are leasing a car. The cash value of the car is \\$ 25,000 (after tax and fees). The car dealer offers you the following: monthly payments of \\$ 400 for 3 years, with an interest rate of 1.99% APR. After 3 years, you have the option to pay \$ 15,000 and own the car. Is this a good deal?

# In[95]:


PV = npFin.pv(0.0199/12, 3*12, 400, 15000, 1)
print('Present Value of his offer is ${:,}'.format(round(PV,2)))  
# this changes the formatting of the output to currency, with 2 decimals.


# That is, if you accept the dealer's offer, including the time value of money, you are paying more than \\$ 28,000 for a car which is worth only \$ 25,000`. So this is a bad deal.

# * `fv(rate, nper, pmt, pv, when='end')` calculates the future value of a stream of cash flows.
# 
# * `rate(nper, pmt, pv, fv, when='end', guess=None, tol=None, maxiter=100)`, finds the required rate of return. For this class, you can ignore the following arguments: `guess`, `tol`, and `maxiter`.
# 
# * `nper(rate, pmt, pv, fv=0, when='end')` computes the number of periodic payments of an annuity.
# * `pmt(rate, nper, pv, fv=0, when='end')` computes the payment against loan principal plus interest. Similarly, `ipmt()` computes the  interest portion of a payment and `ppmt()` computes the payment against loan principal.
# * `irr(CashFlows)` calculates the internal rate of return for a stream of future cash flows (the first element is the initial investment with a negative sign). `mirr()` is for modified IRR calculation.

# ## Pandas Library
# `Pandas` library is an increasingly important component of the Python scientific stack. It is a high-performance package that provides a comprehensive set of data structures for working with
# data. `pandas` also provides high-performance, robust methods for importing from and exporting to a wide range of formats, such as xlsx and csv files. Data structures in Pandas allow for labeling columns and rows, which is not available in NumPy. Moreover, it allows for relational-database operations (such as join), which are provided in MS-Access.

# In[96]:


import pandas as pd


# 
# ### Data Structures
# The most important data structures in `pandas` are Series and DataFrames. Series are the equivalent
# of 1-dimensional arrays. DataFrames are collections of Series and so are 2-dimensional (like MS-Excel spreadsheets). 
# 
# #### Series
# Series are the primary building block of the data structures in `pandas`, and in many ways a Series behaves
# similarly to `list` and can have both number and text.  

# In[97]:


# Panda Series
s = pd.Series([5.4, 6.6, 53, 'book',  4.5,"apple",1])
s


# As we see in the printed values in this example, `pandas` has automatically generated a label (index) for the series (the first column above) using the sequence 0, 1, . . . . This is similar to the row number in MS-Excel. You can use these indexes when printing or accessing the data.
# for example, print items with index 0 and 3:

# In[98]:


s[[0,3]]


# #### DataFrame
# `DataFrames` collect multiple series in the same way that a spreadsheet collects multiple columns of data.
# A `DataFrame` is composed of `Series` and each `Series` has its own data type, and so not all `DataFrames` are representable as homogeneous NumPy arrays.
# 
# A number of methods are available to initialize a DataFrame. The simplest method uses a homogeneous
# NumPy array.

# In[99]:


a = np.array([[7.0,8,9],[3,4,5]])
df = pd.DataFrame(a)
df


# A `DataFrame` contains column labels and row labels (similar to row number and column headings in MS-Excel). When none are
# provided, the numeric sequence 0, 1, . . . is used. In the above example, we have three columns that are labeled   `0`, `1` and `2`. There are also two rows labeled as `0` and `1`. 
# Labels are useful when working with large DataFrames, where you do not need to remember which column stores what values. We can assign column and row names by `columns` and `index` commands:

# **Example** Going back to our example for the grades in Section 4 of Commerce 3FD3:

# In[100]:


Section_4_marks = [
    [100,0,0,100,50,80, 65,78, 80],
    [100,100,100,100,100,80, 75,88, 100],
    [100,0,0,100,50,80, 65,78, 80],
    [0,0,0,100,50,50, 45,38, 20]
]
df = pd.DataFrame(Section_4_marks, columns=['A_1', 'A_2', 'A_3','A_4','A_5',                              'Mid_1','Mid_2','Final','Participation'],                     index=['Sarah', 'Rose', 'Ben','John'])

df 


# Then it is easier to access columns or rows of the DataFrame. You can select a column by giving its name in `[]`, for example:

# In[101]:


df['Mid_1']


# If you want to access a list of columns, say both `Mid_1` and `Mid_2`, put them in a list. e.g:

# In[102]:


df[['Mid_1','Mid_2']]


# To access a row, we can use the `.loc[row name]`:

# In[103]:


df.loc['Sarah']


# In[104]:


df.loc['Sarah','Final']


# If you don't know the index of an item, you can also access it via its row or column number via the `.iloc[]` feature:

# In[105]:


df.iloc[1,0]


#  or alternatively

# In[106]:


df.iloc[1]['A_1']


# You can define a new column for the DataFrame using `['new column name']`. For example, below I calculate the total grade for each student:

# In[107]:


df['total_grade'] = df['A_1']*0.02 + df['A_2']*0.02 + df['A_3']*0.02 +df['A_4']*0.02 +df['A_5']*0.02 + df['Mid_1'] * 0.20 + df['Mid_2']*0.20 + df['Final'] * 0.40 + df['Participation']*0.10  
df


# If you want to access the names of the columns:

# In[108]:


df.columns


# And if you want to access  the names of the rows (i.e. indexes)

# In[109]:


df.index


# #### Merge and Join DataFrames
# `merge` and `join` provide SQL-like operations for merging the DataFrames using row labels or the contents
# of columns. In MS-Excel, you can use the `XLOOKUP` function (or other similar lookup functions) for merging. 
# 
# The primary difference between the two is that `merge` by default uses column contents while
# `join` defaults to using index labels. Both commands take a large number of optional inputs. The important
# keyword arguments are:
# 
# * `how`, which must be one of 'left', 'right', 'outer', 'inner' describes which set of indices to use when performing the join. 
# 
#     * 'left' uses the indices of the DataFrame that is used to call the method and 'right' uses the DataFrame input into merge or join. 
# 
#     * 'outer' uses a union of all indices from both DataFrames and 'inner' uses an intersection from the two DataFrames.
# 
# * `on` is a single column name or list of column names to use in the merge. `on` assumes the names are common. If no value is given for `on` or `left_on/right_on`, then the common column names are used.
#     * `left_on` and `right_on` allow for a merge using columns with different names. When `left_on` and
# `right_on` contain the same column names, the behavior is the same as `on`.
# 
# * `left_index` and `right_index` indicate that the index labels are the join key for the left and right DataFrames.
# 
# Below, I try to explain each of these merges. First, I define two arbitrary DataFrames, called `df_left` and `df_right`.

# In[110]:


df_left = pd.DataFrame([['a','b'],['c','d'],['e','f'],['z','v']],columns=['one','two'])
print('df_left:')
print(df_left)

df_right = pd.DataFrame([['a','b'],['c','d'],['g','h']],columns=['one','three'])
print('df_right:')
print(df_right)


# Let's merge the two DataFrames, by putting the values of `df_right` beside the values of `df_left`, where the values of items in column ONE of the two DataFrame are the same (since column ONE is shared, it will not be repeated). This is called the `inner` join:

# In[111]:


df_left.merge(df_right,on='one') 


# Notice that by the `inner` join, we lost rows 2 and 3 of `df_left` and row 2 of `df_right`, because their values in column ONE are not shared.
# 
# `left` join allows us to keep the left DataFrame as-is and only add the values of `df_right` where there is a match. For missing values pandas puts NaN if cannot find the match

# In[112]:


df_left.merge(df_right,on='one', how='left')


# Similarly, with the `right` join, we keep the values of `df_right` and add the values of `df_left` if there is a match.

# In[113]:


df_left.merge(df_right,on='one', how='right')


# Lastly, we have the `outer` join, which merges all values and puts NaN if cannot find the match

# In[114]:


df_left.merge(df_right,on='one', how='outer')


# ### Importing and Exporting Data via Panda
# All of the data readers in pandas load data into a pandas `DataFrame`, which if need be you can transfer to a `NumPy` array. 
# In practice, the `DataFrame` is much more useful since it includes useful information such as column names read from the data source. 

# #### Import Excel files
# Excel files, both 97/2003 (xls) and 2007/10/13 (xlsx), can be imported using `read_excel()`. Two inputs are
# required to use `read_excel()`, the FILE_NAME and the SHEET_NAME containing the data. In this example, pandas
# makes use of the information in the Excel workbook that the first column contains dates and converts
# these to datetimes. 

# In[115]:


TSLA = pd.read_excel('VOO_TSLA_BTC_prices.xlsx',sheet_name='TSLA')
TSLA


# Other notable keyword arguments while importing include:
# 
# * `header`, an integer indicating which row to use for the column labels. The default is 0 (top) row, and if `skiprows` is used, this value is relative.
# * `skiprows`, typically an integer indicating the number of rows at the top of the sheet to skip before reading the file. The default is 0.
# * `skip_footer`, typically an integer indicating the number of rows at the bottom of the sheet to skip when reading the file. The default is 0.
# * `index_col`, an integer or column name indicating the column to use as the index. If not provided, a basic numeric index is generated.
# * `usecols=[0,1,2,3]`, only import columns 1 to 4.
# 

# #### Import CSV and other formatted text files
# Comma-separated value (CSV) files can be read using `read_csv()`. CSV files are text-based files and do not have Excel meta data (formatting embedded in cells; for example, they cannot have several sheets or cell formatting). Because of this, for many software programs they are easier to connect to, compared to Excel.
# In Windows, CSV files can be opened by NotePad or MS-Excel. With the latter, CSV files might look like an excel file but note that unlike excel files, CSV files cannot have multiple sheets. 

# In[116]:


TSLA_csv_data = pd.read_csv('TSLA_prices.csv')
TSLA_csv_data


# #### Export using Pandas
# Writing data from a Series or DataFrame is much simpler since the starting point (the Series or the DataFrame)
# is well understood by pandas. While the file writing methods all have a number of options, most can safely
# be ignored.

# In[117]:


# df.to_excel('FinancialModeling_marks.xlsx')
# df.to_excel('FinancialModeling_marks.xlsx', sheet_name='Section_4')
# df.to_csv('FinancialModeling_marks.csv')


# ### Manipulating Data in Pandas
# 
# Recall, to call a function from NumPy or base Python we type `FUNCTION_NAME(in1,in2,...)`. In pandas, we first type the input DataFrame (or on a set of its columns/rows), then call the function, i.e. `df.sum()`. Below, I introduce a few useful functions:
# 
# #### Summary 

# If you want to have a preview of your data you can use `head()` or `tail()` functions which return the first and last 5 rows of a DataFrame, respectively. This gives you a sense of the data at a glance and usually is the first step:

# In[118]:


TSLA_prices = pd.read_excel('VOO_TSLA_BTC_prices.xlsx',sheet_name = 'TSLA')
TSLA_prices.head()


# Similarly, you can use the `tail()` function to get the last 5 observations of a DataFrame.
# 
# Another useful function to get familiar with your datasets is the `dtype` feature; it gives the type of each column of the DataFrame. For example:

# In[119]:


TSLA_prices.dtypes


# #### Statistical Functions
# 
# Simple statistical functions such as `sum`, `mean`, `std`, `var`, `prod`, `median`, `quantile`, `abs`, `cumsum` (cumulative sum), and `cumprod` (cumulative product) are available for Series and DataFrame. DataFrame also supports `cov` and `corr` – the keyword argument axis determines the direction of the operation (0 for down columns, 1 for across rows). 
# 
# `describe()` returns a simple set of summary statistics (number of non-missing observations, average, standard deviation, ...). The output is a series where the index
# contains the names of the statistics computed.

# In[120]:


df = TSLA_prices[['Adj Close','Volume']]
df.describe()


# Notice that we can get each of the above separately too. For instance, to get the average values, you can use the `.mean()` function:

# In[121]:


df.mean()


# Similarly, use `.std()` to get the standard deviations, `.min()` and `.max()` to get minimum and maximum values of your DataFrame. `.count()` returns the number of non-null values – that is, those which are not NaN or another null value such as None or NaT (not a time, for datetimes). Use `.quantile([0.25,0.50,0.75])` to get the 25$^{th}$, 50$^{th}$, and 75$^{th}$ percentile values.

# #### Aggregation 
# The simplest application of `groupby` is to aggregate statistics such as group means or extrema. All aggregation
# functions will return a single value per column for each group. Many common aggregation functions
# have optimized versions provided by `pandas`. For example, `mean`, `sum`, `min`, `std`, and `count` can all be directly
# used on a `DataFrame GroupBy` object.
# 
# **Example** let's find the average price of Tesla's stocks per year in our sample:
# 
# First, create a column for the year (more on the date functions later)

# In[122]:


TSLA_prices['Year'] = TSLA_prices['Date'].dt.year


# If the DATE column was stored as a string (`str`), you can change it to Pandas Time-Date series, using `pd.to_datetime(GDP_data.DATE)`. Then you can work with the above `.dt` functions.
# 
# Second, Select the columns you are interested, and use the `groupby` function to group the data

# In[123]:


grouped_data = TSLA_prices[['Year','Open','High','Low','Close']].groupby('Year')


# Third, use the mean function to give the average values:

# In[124]:


grouped_data.mean()


# You can combine functions in DataFrame. For example, we can write second and thirds steps above in one line. Below, I do so, and compute the total volume of traded Tesla stocks in each year:

# In[125]:


TSLA_prices[['Year','Volume']].groupby('Year').sum()


# #### Delete columns of a DataFrame
# `.drop(list of columns,axis=1)` will return a DataFrame with the Series dropped without modifying the original DataFrame.

# In[126]:


TSLA_prices_2 = TSLA_prices.drop(['Low'],axis=1)
TSLA_prices_2.tail()


# `drop(labels)` drops rows based on the row labels in a label or list labels. For example, drop row 4 (California):

# In[127]:


TSLA_prices_3 = TSLA_prices_2.drop(2783)
TSLA_prices_3.tail()


# Finally, `drop_duplicates()` removes rows which are duplicates or other rows, and is used with the keyword argument `drop_duplicates(cols=col_list)` to only consider a subset of all columns when checking for duplicates.

# In[128]:


df = pd.DataFrame(np.array([[70,80, 5],[90,65,1],[74,95,3],[70,80,4]]) )
print('df = ')
df


# In[129]:


print('unique values of the first column of df = ',pd.unique(df[0]))

df_drop_duplicates = df.drop_duplicates([0,1])
print('drop rows with duplicate values in the first and second columns: ')
df_drop_duplicates


# #### Sort
# `sort_values` sorts the contents of the DataFrame along either axis using the contents of a single column or row. Passing a list of columns names or index values implements lexicographic search. `sort_index` will sort a DataFrame by the values in the index.
# Both support the keyword argument `ascending` to determine the direction of the sort (`ascending` by
# default). `ascending` can be used with a list to allow sorting in different directions for different sort variables.
# 
# **Example** Sort TSLA_prices by Volume and print the top 5 high volume days

# In[130]:


TSLA_prices.sort_values(by='Volume', ascending=False).head()


# Just before the COVID-19 crash, TSLA was trading heavily!

# ### Time-series Data
# A TimeSeries data is basically a series where the index contains datetimes index values (more formally
# the class `TimeSeries` inherits from `Series`), and the `Series` constructor will automatically promote a Series
# with datetime index values to a TimeSeries. 
# 
# TimeSeries have some useful indexing tricks. For instance, you can easily access all of the data for a particular year using `DataFrame_NAME.loc['yyyy-mm']` syntax where `yyyy` is the year and `mm` is the month.
# 
# **Example** Show the stock prices for Tesla in Feb. 2020:

# In[131]:


TSLA_prices.index = TSLA_prices['Date']     # use Date column as the index
TSLA_prices.drop('Date',axis=1,inplace=True)# drop the Date column. we don't need it any more now
print('Tesla Volume in Feb 2020:')
TSLA_prices.loc['2020-02']


# Similarly, you can access to a year, month, a date, or a period of time of a TimeSeries, for example:

# *  The data for year 2020: `TSLA_prices.loc['2020']`
# *  The data for the month Feb., 2020:`TSLA_prices.loc['2020-02']`
# *  The data for teh day Feb. 27th, 20200:`TSLA_prices.loc['2020-02-27']`
# * The data for the days in between Feb. 25th, 20200 and Mar. 20th, 20200: `TSLA_prices.loc['2020-02-25':'2020-03-20']`

# Once you have the time-series index, you can get the other date values. For example:

# In[132]:


TSLA_prices['Year'] = TSLA_prices.index.year
TSLA_prices['Quarter'] = TSLA_prices.index.quarter
TSLA_prices['Month'] = TSLA_prices.index.month
TSLA_prices['Day'] = TSLA_prices.index.day

TSLA_prices.head()


# If the DATE column was stored as a string (`str`), you can change it to Pandas Time-Date series, using `pd.to_datetime(GDP_data.DATE)`. Then you can work with the above `.dt` functions.

# #### Rate of Returns
# A more useful application of TimeSeries data is for financial time series, where we are interested in the growth rates (or rate of return) in a period. For example, in the dataset above, we can calculate the daily returns of stock price. Growth rates are computed using `pct_change()`. 
# $$R_t = \frac{P_t + D_t -P_{t-1}}{P_{t-1}}$$
# where, $P_t$ and $D_t$ are the closing price and dividends of the stock on period $t$, respectively. In Yahoo Finance data, the `Adj Close` column incorporates the effect of dividends and other distributions.

# In[133]:


TSLA_prices['daily_returns'] = TSLA_prices['Adj Close'].pct_change()
TSLA_prices.head()


# Notice that our stock price data starts from June 29, 2010. So, we do not have the return data for that date.
# 
# The `.pct_change()` function can also calculate growth rates over a longer period. The keyword argument periods constructs overlapping growth rates which are useful when using seasonal data. For example, in our dataset, which is at the daily frequency, you can get the annual growth rate, with respect to the 252 business days (the default value is 1)

# In[134]:


TSLA_prices['Adj Close'].pct_change(periods=252).tail() # a year has about 252 business days


# Alternatively, you can re-sample the daily price data to annual data (end of year) and then compute the annual returns:

# In[135]:


price_annual = TSLA_prices.resample("1y").bfill()
price_annual['Adj Close'].pct_change().tail()


# The `pct_change()` function is very useful for analyzing the stock returns. Most financial databases provide a time series for the price of a company and you can use this function to get the holding period returns.
# 
# The TimeSeries is also a useful data structure for plotting financial data. In the next sections, I will explain the basics of plotting with Python. 

# ## Pandas_datareader
# This library allows you to download data from several websites such as Yahoo Finance, Google Finance, Morningstar, St.Louis FED (FRED) and Kenneth French’s data library. Check the documentation of the library for more details here: https://pandas-datareader.readthedocs.io/en/latest/remote_data.html
# 
# 
# You need to first install this library as it is not included in the main package during the installation. Launch Anaconda Prompt (from the Start menu of Windows or the Mac equivalent) then type/run: `pip install pandas_datareader`. It will download and install it on your machine.
# 
# The main function in this library is called `DataReader` and its general syntax is: `.DataReader(Symbol, Data_Source, start_date, end_date)`. 
# * `Symbol` identifies what you want to download, 
# * `Data_Source` identifies the label (name) of the data vendor. See the library's documentation for the full list of vendors that are compatible with Pandas_datareader. 
# * `start_date` and `end_date` identify the data period to be downloaded. If not identified, it will be the last 5 years.
# 
# In this class, we mostly use this library to get stock prices from Yahoo Finance! website. But for financial modeling you may also want to download Macroeconomic data (such as GDP) from the central banks' website. Below, I list two examples:

# #### Stock Prices
# We can use Yahoo Finance, Google Finance, and Morningstar websites to get the stock prices of companies using their Ticker Symbols. The example below shows how to download the closing price for three companies:

# In[136]:


import pandas_datareader.data as pdr

# Define the instruments to download. We would like to see Apple, Microsoft and the S&P500 index.
tickers = ['AAPL', 'MSFT', '^GSPC']

# We would like all available data from 01/01/2000 until 12/31/2016.
start_date = '2020-12-31'
end_date = '2021-09-01'

# User pandas_reader.data.DataReader to load the 
# stock prices from Yahoo Finance. 

panel_data = pdr.DataReader(tickers, 'yahoo', start_date, end_date)
# panel_data = pdr.DataReader(tickers, 'morningstar', start_date, end_date)

# Yahoo Finance gives 'High', 'Low', 'Open', 'Close', 'Volume', 'Adj Close'.

Close_Price = panel_data['Close']
Close_Price.head()


# This will download data from Yahoo Finance, at the daily frequency. To get monthly data (prices at the end of each month), you need to re-sample from daily data every 1 month:

# In[137]:


Close_Price_monthly = Close_Price.resample("1m").ffill()
Close_Price_monthly.head()


# #### Economics Data
# We can use the website of the Federal Reserve Bank of St.Louis (FRED), the Bank of Canada, or World Bank. For example, below we can download US GDP data:

# In[138]:


import pandas_datareader.data as pdr
GDP_data = pdr.DataReader('GDP', 'fred', '2020-01-01', '2021-12-31')
GDP_data.head()


# #### Portfolio Data from Fama French
# We can access the datasets on the Fama/French Data Library (http://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html) via Pandas_datareader. There are many useful portfolios and asset pricing factors in this data library (it has more than 250 datasets). We will work with some of these in this class. 
# 
# The get the name of all datasets in this website, use `.get_available_datasets()` function. Below, we can see the 5 first datasets.

# In[139]:


import pandas_datareader.data as pdr
from pandas_datareader.famafrench import get_available_datasets

get_available_datasets()[:4]


# Let's dig in more deeply and choose '5_Industry_Portfolios' to get the data for the top 5 sectors in the US: Consumers, Manufacturing, High Tech., Health care, and others.

# In[140]:


Industry_Portfolios = pdr.DataReader('5_Industry_Portfolios', 'famafrench')


# In the _Variable Explorer_ tab click on  `Industry_Portfolios` and click on `DECR` to get the description of the data that you just downloaded.
# 
# This file was created by CMPT_IND_RETS using the 2021-June CRSP database (CRSP dataset is accessible from the WRDS portal- if you have not done so, you may get your credentials from https://wrds-www.wharton.upenn.edu/ and your MAC emails). It contains the value- and equal-weighted returns for 5 industry portfolios. The portfolios are constructed at the end of June. The annual returns are from January to December. Missing data are indicated by -99.99 or -999. Copyright 2021 Kenneth R. French
# 
# 
#     0 : Average Value Weighted Returns -- Monthly (96 rows x 5 cols) 
#     1 : Average Equal Weighted Returns -- Monthly (96 rows x 5 cols)
#     2 : Average Value Weighted Returns -- Annual (8 rows x 5 cols)
#     3 : Average Equal Weighted Returns -- Annual (8 rows x 5 cols)
#     4 : Number of Firms in Portfolios (96 rows x 5 cols)
#     5 : Average Firm Size (96 rows x 5 cols)
#     6 : Sum of BE / Sum of ME (8 rows x 5 cols)
#     7 : Value-Weighted Average of BE/ME (8 rows x 5 cols)
#   
# 
# 
# To compute the value-weighted average portfolio returns (index 0), the dataset uses the market capitalization of each firm as a weight
# 
# $$ R_{vw} = \sum w_i \: R_i $$

# In[141]:


Industry_Portfolios[0].head()


# ##  Matplotlib
# This is a complete plotting library capable of high-quality graphics. Here I cover the basics of producing
# plots. Further information is available on the `matplotlib` website (`https://matplotlib.org/`).
# 
# Another useful graphics library is `seaborn`, which is a Python data visualization library based on `matplotlib`. It provides a high-level interface for drawing attractive and informative statistical graphics. Refer to its documentation page (https://seaborn.pydata.org/) for more information.

# In[142]:


import matplotlib.pyplot as plt


# ### Line Plot
# The most basic, and often most useful 2D graphic is a line plot. Basic line plots are produced using `plot(INPUT_VARIABLE)` using a single input containing a 1-dimensional array. 
# 
# You may need to also call `.show()` function to see the generated plot, in the last step of your plotting.
# 
# **Example** plot the monthly returns for the High-Tech sector ('HiTec' in the Kenneth French Data Library datasets)

# In[143]:


df = Industry_Portfolios[0]
y  = df['HiTec'].to_numpy() # for teaching purposes, I convert it first to a NumPy Array object
plt.plot(y)
plt.show()


# You can modify the line color, line style or the marker on the graph by adding the Format strings, which may contain any of the following elements:
# 
# * Color 
#     * `b` for Blue  
#     * `g` for Green
#     * `r` for Red
#     * `c` for Cyan 
#     * `m` for Magenta 
#     * `y` for Yellow
#     * `k` for Black
#     * `w` for White 
# * Line Style
#     * `-` for Solid 
#     * `--` for Dashed
#     * `-.` for Dash-dot
#     * `:` for Dotted
# * Marker 
#     * `.` for Point
#     * `o` for Circle
#     * `s` for Square
#     * `d` for Thin Diamond
#     * `x` for Cross
#     * `+` for Plus
#     * `*` for Star
#     
# For example:

# In[144]:


# plot y in (r), use square markers (s), in dotted lines (:)  
plt.plot(y,'r*:')

# Add a title
plt.title("High Tech. Sectors", color='g')

# Add y-labes
plt.ylabel('HiTec monthly returns', color='b')

# Add the x-label
plt.xlabel('Observation', color='k')

# Add gridlines
plt.grid()

# plotting is finished. show it
plt.show()


# You can add multiple lines in a graph like below:

# In[145]:


x = Industry_Portfolios[0].to_numpy()

plt.plot(x[:,0],'b', label = 'Cnsmr')
plt.plot(x[:,1],'g.', label = 'Manuf')
plt.plot(x[:,2],'r:',label = 'HiTec')
plt.plot(x[:,3],'k-.', label = 'Hlth ')
plt.plot(x[:,4],'y--',label = 'other')

# Add legend
plt.legend(loc = 'lower right', frameon = True)
plt.show()


# You can have primary and secondary y-axises. This is a useful feature especially when the variables do not have the same scale and their order of magnitudes differ significantly.
# 
# **Example** Plot Apple's stock prices and monthly returns for the last 5 years.
# For this, we first download stock price data with the pandas_datareader library at the daily frequency. Then we re-sample at the monthly frequency to calculate monthly returns. In order to have primary and secondary y-axises, we need to define two (sub)plots, and tell python to share their x-axis. See below, where I define a plot and call it `ax1` and then create a twin copy of it and call it `ax2`. Once we have these, we can plot our graphs in each plot and Python will merge them.

# In[146]:


# 1. Download Price Data for Apple (AAPL).
import pandas_datareader.data as pdr
tickers = ['AAPL']
panel_data = pdr.DataReader(tickers, 'yahoo')
APPL_Price  = panel_data['Close'].resample("1m").ffill()
APPL_Return = panel_data['Adj Close'].resample("1m").ffill().pct_change()

# 2. In order to have two y-axis,
# 2.1. share the x axis between the two plots
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
# 2.2. plot the series
ax1.plot(APPL_Price,'g*-.')
ax2.plot(APPL_Return,'b')

# 2.3. Add y-labes
ax1.set_ylabel('Price', color='g')
ax2.set_ylabel('Monthly Return', color='b')

# 2.4. Add a title and the x-label
plt.title('APPL Stock Price and Return')
ax1.set_xlabel('Year')
plt.show()


# **Note** Above, I'm plotting a pandas DataFrame data (not NumPy Array), therefore I am able to use the time index.

# ### Scatter Plots
# Similarly, we can draw scatter plots with the `Matplotlib` library. This is when you want to plot the variable `y` in the vertical axis with respect to the variable `x` in the horizontal axis (you can also use `plt.plot(x,y)`). For instance, below I plot the monthly return of the High-tech sector, in the y-axis, with respect to the Manufacturing sector, in the x-axis

# In[147]:


df = Industry_Portfolios[0]

#plot y versus x, in (r), use square markers (s), in dotted lines (:)  
plt.scatter(x=df['Manuf'],y=df['HiTec'])

# Add a title
plt.title("High Tech. vs. Manufacturing Sectors")

# Add y-labes
plt.ylabel('HiTec monthly returns')

# Add the x-label
plt.xlabel('Manuf monthly returns')

# Add gridlines
plt.grid()

# plotting is finished. show it
plt.show()


# ### Bar Charts
# `bar` produces bar charts using two 1-dimensional arrays. The first specifies the left edge of the bars and
# the second the bar heights. 
# 
# **Example** Plot the average monthly return of the High Tech. sector per year in the last 5 years.

# In[148]:


df['Year'] = df.index.year
df_yr = df.groupby('Year').mean()
plt.bar(df_yr.index,df_yr['HiTec'])
plt.show()


# ### Pie Charts
# `pie` produces pie charts using a 1-dimensional array of data. The data can have any values, and does not
# need to sum to 1. 
# 
# **Example**: In which year the High Tech. sector experienced more positive return? Show with a pie chart
# 
# First, construct a column, indicating the observations with positive returns:

# In[149]:


df['Positive_HiTec'] = 1
df.loc[df['HiTec']<0,'Positive_HiTec'] = 0
df.head()


# Then count the number of observations in a year with positive returns:

# In[150]:


df_yr = df[['Year','Positive_HiTec']].groupby('Year').sum()
df_yr


# Lastly, plot the series. Also, add the relative size of each year's observation as a auto_percentage

# In[151]:


plt.pie(df_yr['Positive_HiTec'], labels = df_yr.index,  autopct='%1.1f%%')
plt.show()


# Pie charts can be modified using a large number of keyword arguments, including labels and custom
# colors. Exploded views of a pie chart can be produced by providing a vector of distances to the keyword argument explode.
# Note that `autopct = '%2.0f'` is using an old style format string to format the numeric labels. 

# ### Histograms
# Histograms can be produced using `hist`. Histograms show the frequency of repeated values in your data. See the example below, where, we plot the histogram for the monthly returns of the High Tech. sector. The height of each bin shows the number of months (observations) where the return falls in that bin. We can set the number of bins used in producing the histogram using the keyword argument bins.

# In[152]:


plt.hist(df['HiTec'], bins = 20)
plt.show()


# Histograms can be further modified using keyword arguments. In the next example, `cumulative=True` produces
# the cumulative histogram. 

# In[153]:


plt.hist(df['HiTec'], bins = 30, cumulative=True, color='r')
plt.show()


# ### Plots with Pandas
# `matplotlib` also sits on `pandas` library and you can directly call it from a DataFrame object. In this way, you can benefit from the date index of the time-series data.

# In[154]:


df = Industry_Portfolios[0]
df['HiTec'].plot()
plt.show()


# ## Statsmodels
# `statsmodels` library provides classes and functions for the estimation of many different statistical models, tests, data exploration. In this class, we use this library for linear regression application, using the ordinary least-square, or OLS, estimator. The online documentation is hosted at statsmodels.org.
# 
# In the example below, we use this library to find the three-year monthly market beta for the High Tech. sector. In the first step, we import the libraries we need and then download the data:

# In[155]:


# initialize
import pandas as pd
import statsmodels.api as sm
import pandas_datareader.data as pdr 

# data download
start_date = '2018-09-01'
end_date   = '2021-09-01'

Industry_Portfolios = pdr.DataReader('5_Industry_Portfolios', 'famafrench',start_date,end_date)
Market_Factors      = pdr.DataReader('F-F_Research_Data_Factors', 'famafrench',start_date,end_date)


# `Industry_Portfolios` dataset from `famafrench` data library contains several forms of the five sector portfolios. The value-weighted portfolios are stored in item `[0]`. `Market_Factors` dataset includes both monthly and annual data for the market, as well as the size and value factors. It also provides data for the risk free rate of returns. The monthly data is stored in item `[0]`.
# 
# In the next step, we merge the two datasets:

# In[156]:


# merge datasets
df = pd.merge(Market_Factors[0], Industry_Portfolios[0], on='Date')
df.head()


# According to the capital asset pricing model (CAPM), the expected excess asset return is linearly related to the market premium:
# $$E[R_i - R_f] = \beta_i E[R_m - R_f]$$ 
# Therefore, we can estimate market beta for asset $i$, denoted by $\beta_i$, using linear regressions:
# $$R_{i,t} - R_{f,t} = alpha_i + \beta_i (R_{m,t} - R_{f,t}) + e_{i,t}$$ 
# where, we include an intercept, $\alpha_i$ to capture the time-invariant effect of other (missing) factors. If CAPM holds in the data, the estimated $\alpha_i$ will be insignificant.k $e_{i,t}$ is the asset-specific noise, which is zero on average. 
# 
# In this model, the left-hand side variable (`Y`-axis variable) is the monthly returns of the Hight Tech. sector (`HiTec`) in excess of the risk free rate. The righ-hand side variables (the `X`-axis variable) are a constant (`const`) and the excess market return (`Mkt-RF`).

# In[157]:


Y = df['HiTec'] - df['RF']
X = sm.add_constant(df['Mkt-RF'])


# Now, we can estimate the model using the `.OLS()` function. Simply, give the left- and right-hand side variables and find the fitted values as follows:

# In[158]:


results  = sm.OLS(Y, X).fit()
print(results.summary())


# The above table, presents the analysis of variance information too. It reports the `R-squared`, estimated slope and intercept values (`coef`) and their 5\% confidence intervals (`[0.025   0.975]`). If you want to access each of these separately you can do so as follows:

# In[159]:


alpha_i = results.params[0]
beta_i  = results.params[1]
R2      = results.rsquared


# We observe that the High Tech. sector has a large beta (almost 1). Notice that in this example, the intercept, $\alpha_i$ is estimated non-zero. It is positive and statistically significant, suggesting that CAPM cannot explain the whole variation in these series.

# ## SciPy 
# `SciPy` library contains a number of routines to the find extremum (minimum or maximum) of a user-supplied objective function located in `scipy.optimize`. `SciPy` has more useful functions but for the sake of this class we only focus on the optimization and solver functions.

# In[160]:


import scipy.optimize as opt


# The steps are similar to the Solver add-on in MS-Excel. First we need to define an (objective) function that we want to minimize. For example, consider finding the minimum of the function $f(x) = x^2$. A function which
# allows the optimizer to work correctly has the form

# In[161]:


def optim_target1(x):
    return x**2


# Once an optimization target has been specified, the next step is to use one of the optimizers functions in SciPy to find the minimum values of this objective function. Optimizers are categorized into two main types: unconstrained and constrained optimizers. If the parameters in mind are limited in a range (for instance, only positive numbers), we use constrained optimizers. On the other hand, if the parameters of the objective function can take any value then use unconstrained optimizers.
# 
# An important application of optimizers in financial modeling is to find the optimal portfolio weights for an investor.

# ### Unconstrained Optimizers
# The basic structure of all of the unconstrained optimizers is `optimizer(f, x0)` where the `optimizer` is one of the `fmin_bfgs, fmin_cg, fmin_ncg or fmin_powell` functions in the SciPy library. `f` is your objective function and `x0` is a set of initial values used to start the algorithm. For this course, we mostly use `fmin_bfgs`, which is the simplest optimizer.
# Back to our example above:

# In[162]:


opt.fmin_bfgs(optim_target1, 1)


# The optimizer `fmin_bfgs` finds that at `x = -7.45036449e-09` our objective function ($f(x)=x^2$) reached to its minimum value, which is `Current function value: 0.000000`. 
# Notice that the correct theoretical answer is `x=0`, but numerically Python finds `x = -0.000000000745036449`, is accurate to 9 decimal places.

# We can modify our objective function to solve equations. Say we want to know at what value of `x` the objective function becomes 4. 
# The idea is to define a new objective function and find the minimum distance of the initial objective function: i.e. $f(x)= x^2 - 4$

# In[163]:


def optim_target2(x):
    return abs(x**2 - 4)

X_0 = opt.fmin_bfgs(optim_target2, 1) 
X_0


# The optimizer finds that at `X_0 = 1.99999999` our objective function ($f(x) = x^2-4 $) equals to its minimum value (i.e.`0.000000`). 
# Notice that the correct theoretical answer is `x=2`, and the numerical solution is accurate to 8 decimal places.

# **More Complex Cases**:
# Imagine the case where the objective function has multiple parameters (a parameter vector). In that case, define the  objective function in the following form

# In[164]:


def optim_target3(params):
    x, y = params
    return x**2 - 3*x + 3 + y*x -3*y + y**2


# Another case, would be to have an objective function that requires additional inputs, which are not parameters of interest. In this case, define the objective function in the following form:

# In[165]:


def optim_target4(params, hyperparams):
    x, y = params
    c1, c2, c3 = hyperparams
    return x**2 + c1*x + c2 + y*x + c3*y + y**2


# This form is especially useful when optimization targets require both parameters and data. Additional inputs can be passed to the optimization target using the keyword argument `args` and a
# tuple containing the input arguments in the correct order. In the above example, we have a single additional input, therefore the comma is necessary in `(hyperp,)` to let Python know that this is a `tuple`. E.g:

# In[166]:


# the syntax would be to include arg = (extra inputs,)
param0 = [1,2]
hyperparams = [5,0.1,3]
opt.fmin_bfgs(optim_target4, param0, args=(hyperparams,) )


# ### Constrained Optimization
# Constrained optimization is frequently encountered in financial problems where parameters are only meaningful in some particular range – for example, the weights in an investment portfolio must be positive (no short selling) or the weights cannot be larger than 10%.
# 
# More formally the constrained optimization problems can be formulated:
# 
# $$
# min_\theta \;\; f(\theta) \;\; \text{subject to} \\
# g(\theta) = 0 \;\; \text{(equality)} \\
# h(\theta) \ge 0 \;\;\; \text{(inequality)} \\
# \theta_L \le \theta \le \theta_H \;\; \text{(bounds)}\\
# $$
# 
# where the `f` is the objective function, `g` and `h` are the set of equations for the equality and inequality constraints on the parameters. 

# The function `fmin_slsqp` is the most general constrained optimizer and allows for equality, inequality and bounds constraints.
# Constraints (here the functions `g` and `h`) are provided either as a list of callable functions or as a single function which returns an array. The latter is simpler if there are multiple constraints, especially if the constraints can be easily calculated using linear
# algebra. 

# As an example, let's consider a simple consumption optimization. I want to buy ice cream and chocolate. Let's assume their joint utility (pleasure) is calculated with a  CRS Cobb-Douglas utility function:  $U(x_{i}, x_{c}) = x_{i}^\alpha \; x_{c} ^ {1-\alpha}$, where $x_i, x_c$ show the quantity of the ice cream and chocolate that I purchase. $\alpha$ is my personal preference for each item (e.g. my $\alpha = 0.33$ because I favor chocolate more than ice cream, by order of 2). I am subject to a budget constraint (say I have only `$15` to buy these): $p_{i} x_{i} + p_{c} x_{c} \le 15$, where $p$ shows the price of each item. Let's assume each scope of ice cream costs `$2`  and each chocolate bar costs `$10` (i.e. $p_i = 2 \;\; \text{and}\;\; p_c = 10 $). 
# Obviously the other constraint is that the quantity of each item I purchase cannot be negative. That is: $x_{i}\ge 0$ and $x_{c} \ge 0$). 

# We first need to specify the objective function

# In[167]:


def utility(x, p, alpha):
    return -1.0 * (x[0]**alpha)*(x[1]**(1-alpha))
# Notice that the optimizer finds the minimum, not maximum.
# So we multiply the output by -1 


# Then we need to define the 3 constraints (budget and non-negative purchases)

# In[168]:


def utility_constraints(x, p, alpha):
    return np.array([x[0], x[1], 15- p[0]*x[0]- p[1]*x[1]])


# Let's find out how many scoops of ice cream and how many bars of chocolate I should buy:

# In[169]:


p = np.array([2.0,10.])
alpha = 1.0/3
x0 = np.array([.4,.4])
opt.fmin_slsqp(utility, x0, f_ieqcons=utility_constraints, args=(p, alpha))


# That means my optimal decision is to buy 2.5 scoops of ice cream and 1 bar of chocolate.

# # Python Coding Conventions
# There are a number of common practices which can be adopted to produce Python code which looks
# more like code found in other modules:
# 
# 1. Use self-explanatory names for the variables and DataFrame. Something that you would quickly understand when you look at your codes
# 
# 1. Try to add sufficient comments and annotations to your codes so that you can understand your work later.
# 
# 1. Use 4 spaces to indent blocks – avoid using tab, except when an editor automatically converts tabs to 4 spaces
# 
# 2. Avoid more than 4 levels of nesting, if possible
# 
# 3. Limit lines to 79 characters. The `\` symbol can be used to break long lines
# 
# 4. Use two blank lines to separate functions, and one to separate logical sections in a function.
# 
# 5. Use ASCII mode in text editors, not UTF-8
# 
# 6. One module per import line
# 
# 7. Avoid `from` *module* `import * ` (for any module). Use either `from` *module* `import` *func1, func2* or `import` *module* `as` *shortname*.
# 
# 8. Follow the NumPy guidelines for documenting functions
# More suggestions can be found in *PEP8 Style Guide for Python Code* (`https://www.python.org/dev/peps/pep-0008/`)
# 
# # References and Python Resources
# Python is an increasingly popular programming  language. You can find numerous useful tutorials on it on the web. For this document, I personally consulted the following materials frequently:
# 
# * On www.Coursera.org, the "Python Programming: A Concise Introduction" online course by Bill Boyd
# 
# * On www.kevinsheppard.com, the "Introduction to Python for Econometrics, Statistics and Data Analysis" course by Kevin Sheppard
# 
# * On www.Linkedin.com/learning, the "Python: Data Analysis" and "Python Statistics Essential Training" courses, by Michele Valisneri
# 
# * Python forum on www.stackoverflow.com
# 
# * and, many tutorials on www.YouTube.com
# 
# ## Best Python Libraries/Packages for Finance and Financial Data Scientists
# 
# An article from Majid AliAkbar (https://www.linkedin.com/pulse/best-python-librariespackages-finance-financial-data-majid-aliakbar/), Published on March 28, 2017.
# 
# Finance professionals involved in data analytics and data science make use of R, Python and other programming languages to perform analysis on a variety of data sets. Python has been gathering a lot of interest and is becoming a language of choice for data analysis. Python also has a very active community which does not shy from contributing to the growth of python libraries. If you search on Github, a popular code hosting platform, you will see that there is a python package to do almost anything you want. This article provides a list of the best python packages and libraries used by finance professionals, quants, and financial data scientists.
# 
# * Numerical, Statistical & Data Structures
# 
#     * `numpy` – NumPy is the fundamental package for scientific computing with Python. It is a first-rate library for numerical programming and is widely used in academia, finance, and industry. NumPy specializes in basic array operations.
#     * `scipy` – SciPy supplements the popular Numeric module, Numpy. It is a Python-based ecosystem of open-source software for mathematics, science, and engineering. It is also used intensively for scientific and financial computation based on Python
#     * `pandas` – The pandas library provides high-performance, easy-to-use data structures and data analysis tools for the Python programming language. Pandas focus is on the fundamental data types and their methods, leaving other packages to add more sophisticated statistical functionality
#     * `quantdsl` – Quand DSL is domain specific language for quantitative analytics in finance and trading. Quant DSL is a functional programming language for modeling derivative instruments.
#     * `statistics` – This is a built-in Python library for all basic statistical calculations
# 
# * Financial Instruments
# 
#     * `pyfin` – Pyfin is a python library for performing basic options pricing in python
#     * `vollib` – vollib is a python library for calculating option prices, implied volatility and greeks using Black, Black-Scholes, and Black-Scholes-Merton. vollib implements both analytical and numerical greeks for each of the three pricing formulae.
#     * `QuantPy` – A framework for quantitative finance In python. Some current capabilities: Portfolio class that can import daily returns from Yahoo, Calculation of optimal weights for Sharpe ratio and efficient frontier, and event profiler
#     * `ffn` – A financial function library for Python. ffn is a library that contains many useful functions for those who work in quantitative finance. It stands on the shoulders of giants (Pandas, Numpy, Scipy, etc.) and provides a vast array of utilities, from performance measurement and evaluation to graphing and common data transformations.
#     * `pynance` – PyNance is open-source software for retrieving, analyzing and visualizing data from stock and derivatives markets. It includes tools for generating features and labels for machine learning algorithms.
#     * `tia` – TIA is a toolkit that provides Bloomberg data access, easier pdf generation, backtesting functionality, technical analysis functionality, return analysis and few windows utils.
# 
# * Trading & Backtesting
# 
#     * `TA-Lib` – TA-Lib is widely used by trading software developers requiring to perform technical analysis of financial market data. It has an open-source API for python.
#     * `trade` – trade is a Python framework for the development of financial applications. A trade app works like a service. The user informs the items he has in stock and a series of subsequent occurrences (purchases, sales, whatsoever) with those or other items. trade then calculates the effects of those occurrences and gives back the new amounts and costs of the items in stock.
#     * `zipline` – Zipline is a Pythonic algorithmic trading library. It is an event-driven system that supports both backtesting and live trading.
#     * `QuantSoftware Toolkit` – Python-based open source software framework designed to support portfolio construction and management. It is built the QSToolKit primarily for finance students, computing students, and quantitative analysts with programming experience.
#     * `quantitative` – Quantitative finance, and backtesting library. Quantitative is an event driven and versatile backtesting library.
#     * `analyzer` – Python framework for real-time financial and backtesting trading strategies
#     * `bt` – bt is a flexible backtesting framework for Python used to test quantitative trading strategies.
#     * `backtrader` – Python Backtesting library for trading strategies
#     * `pybacktest` – Vectorized backtesting framework in Python / pandas, designed to make your backtesting easier. It allows users to specify trading strategies using full power of pandas, at the same time hiding all boring things like manually calculating trades, equity, performance statistics and creating visualizations. Resulting strategy code is usable both in research and production setting.
#     * `pyalgotrade` – PyAlgoTrade is an event driven algorithmic trading Python library. Although the initial focus was on backtesting, paper trading is now possible
#     * `tradingWithPython` – A collection of functions and classes for Quantitative trading
#     * `pandas_talib` – A Python Pandas implementation of technical analysis indicators
#     * `algobroker` – This is an execution engine for algo trading. The idea is that this python server gets requests from clients and then forwards them to the broker API.
#     * `finmarketpy` – finmarketpy is a Python based library that enables you to analyze market data and also to backtest trading strategies using a simple to use API, which has prebuilt templates for you to define backtest.
# 
# * Risk Analysis
# 
#     * `pyfolio` – pyfolio is a Python library for performance and risk analysis of financial portfolios. It works well with the Zipline open source backtesting library.
#     * `empyrical` – Common financial risk and performance metrics. Used by zipline and pyfolio.
#     * `finance` – Financial Risk Calculations. Optimized for ease of use through class construction and operator overload.
#     * `qfrm` – Quantitative Financial Risk Management: awesome OOP tools for measuring, managing and visualizing risk of financial instruments and portfolios.
#     * `visualize-wealth` – A library built in Python to construct, backtest, analyze, and evaluate portfolios and their benchmarks.
#     * `VisualPortfolio` – This tool is used to visualize the performance of a portfolio
# 
# * Time Series
# 
#     * `ARCH` – ARCH and other tools for financial econometrics in Python
#     * `statsmodels` – Python module that allows users to explore data, estimate statistical models, and perform statistical tests.
#     * `dynts` – A statistic package for python with emphasis on time series analysis. Built around numpy, it provides several back-end time series classes including R-based objects via rpy2.
# 
