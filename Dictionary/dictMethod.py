# Dictionary Methods :-

'''
# 1) dict_obj.clear()

# Examples :

#__main__
d={"A":10 , "B":20 ,"C":30}
d.clear()
print("d =",d)
#end of __main__


# 2) new_dict_obj = dict_obj.copy()

d={'a':97,'b':98,'c':99}
x=d.copy()
print("d =",d)
print("id of d =",id(d))

print("x =",x)
print("id of x =",id(x))



# 3) new_dict_obj = dict.fromkeys(Iterable[,values])

#Example

#__main__
x=[10,20,30]
d=dict.fromkeys(x)
print("d =",d)

d=dict.fromkeys(x,(1.1,3.4))
print("d =",d)

d=dict.fromkeys(x,'A')
print("d =",d)

x={'A':10,'B':20,'C':30}
d=dict.fromkeys(x)
print("d =",d)
# end of __main__

'''

# 4) value=dict_obj.get(key[,default_value])

d={'A':10,'B':20,'C':30}

x=d.get("A",0)
print("x =",x)

Y=d.get("D")
print("Y =",Y)

Z=d.get("D",0)
print("Z =",Z)








