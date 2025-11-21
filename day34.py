ep1={10:53, 34:56, 45:67}
ep2={12:34, 32:34, 67:89}
ep1.update(ep2)    #ep1 ma ep2 ko values haru jodera update gardinxxa
ep1.clear()         #ep1 lai pura clear gardinxa

ep3={}          #a way to create empty dictionary
ep1.pop(10)     #it will remove  10 wala key value pair
ep1.popitem()      #last wala remove hunxa
del ep1   #deletes ep1
del ep1["34"]       #tei 34 wala delete garxa but it is a string not integer so using ""
