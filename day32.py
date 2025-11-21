s1={1,2,3,4}
s2={3,5,6,8}
print(s1.union(s2)) #dubaima vako kura ek choti matra lekhxa algebra set jastai
print(s1,s2)
print(s1.update(s2)) #s1 ma s2 ko value haru ni add hunxa navako value haru
print(s1.intersection(s2)) #j common ho teii kura matra lekhxa
s1.intersection_update(s2) #esley chai j j common thyo tyo kura matra gayera s1 ma haldinxa ani aru sab s1 ko aru value haru hataidinxa
s3={4,6,7,2,5}
s4=s2.symmetric_difference(s3)  #elsey chai dubai set ko common kura haru hataidinxa ani common navako value haru matra assign gardinxa
s5=s1.difference(s3)    #esley chai s1-s3 ko kam garxa like s1 sanga s3 common kei value xa vaney tyo chai hataidinxa
print(s1.disjoint(s3))   #true or false to check if both are disjoint sets(kei common navako)
print(s1.issuperset(s2))  #true of false if s2 ko sab value s1 ma xa
s1.remove(2)   #remove the value 2 in s1
s1.discard(3)    #same as remove but gives error message
s1.pop()   #random value for s1 will be removed
del s1   #deletes the whole set