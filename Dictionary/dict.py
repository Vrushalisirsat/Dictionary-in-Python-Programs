# Dictionary :-  represents a collection of  "key:value" pairs.

#Dictionary can created by using following ways :-
'''
# Way-1 :- dict_obj={}   --> It will create an empty dictionary.
# Example-1 :-

#__main__
x={}
print("x =,x)
print("DataType of x =",type(x))
x['A']=20
X['B']=30
print("x =",x)
#end of __main__


# Way-2 :- dict_obj={key:value , key:value,...........}


#Way-3 :-  dict_obj=dict9tuple/list/set/dictionary)
# Example :-

from array import *
#__main__
t=(["A",65] , (20,30) , {1.1 , 2.2} , {'a':97,'b':98},array("i",[40,50]))
d=dict(t)
print("d =",d)
#end of __main__


#Way-4 :-  dict_obj = dict(**keyword_arguments)

# Example :-
#__main__
d=dict(A=10,B=20,C=30)
print("d =",d)
#end of __main__




#Way-5:-  dict_obj = dict(zip(Iterable1,Iterable2))

# Example :-
#__main__
z=zip(['A','B','C'],(11,22,33))
d=dict(z)
print("d =",d)
#end of __main__

#--------------------------------------------------------------------------------------------------------------------

# Accessing Elements in Dictionary :-    Syntax:- dict_obj[key]

# Example :-
#__main__
d={'a':97,'b':98,'c':99}
print("d['a'] =",d['a'])
print("d['b'] =",d['b'])
print("d['c'] =",d['c'])
#end of __main__

#------------------------------------------------------------------------------------------------------------

#To check wheather the dictionary is mutable or not.

#__main__
d={'A':65,'B':66,'C':67}
del d['B']
d['D']=40
d['A']=90
print("d =",d)
#end of __main__

#------------------------------------------------------------------------------------------------------------

# Retriving values in the dictionary by using for-in loop.

# Example-1:-
#__main__
d={'A':65,'B':66,'C':67}
for x in d:
    print("x =",x)
    print(d[x])
#end of loop

for x in d.values():
    print("x =",x)
#end of loop
#end of __main__


# Example-2:-

#__main__
d={'A':65,'B':66,'C':67}
print(d.items())

for k,v in d.items():
    print("key =",k , "value =",v)
# end of __main__
#end of __main__

'''

# Example :-
# To map multiple values related with single values

#__main__

d={
   1111:{"name":"JACK","java":90,"cpp":50},
   2222:{"name":"JAMES","java":60,"cpp":80}
  }

for x in d:
    print("\nRoll Number =",x)
    print("Student Name =",d[x]["name"])
    print("Marks in JAVA =",d[x]["java"])
    print("Marks in Cpp =",d[x]["cpp"])











