# python-basic-lec19-Nov-24-24

## subjects learned:

* tuple- continue:
    * result += (t,) vs list.append(): += create a new tuple in the memory and combined, and the old one remains in the
      memory and waits for the GC.
      therefore it's better to use list.append() and not "adding" the tuple items
* enumerate(tuple)= to get the index and value from list/tuple:

    ```
    for i,v in enumerate(t1): *(i,v)=item-tuple
    ```

* datetime library - how to print date/time in format
    * need import: from datetime import datetime
    ```
    from datetime import datetime
    ```
    * now()-now time in user location
    * utcnow()- datetime.datetime.utcnow() is deprecated, instead: datetime.now(timezone.utc)
    * strftime()- to format the date/time:
        * %H:%M:%S:.%f %Y-%d-%m h-hour, minute,second,day,month,year
        * %B- month in word, %A day in word
    * now()+ timedelta(days=1): added 1 day to now
* set - new structure: like a dictionary, but on keys. only uniques.
    * in the backend, there is a mathematics calculation to find the location of the value in the set.
    * create:
    ```
    s1:set ={1,2,3}
    ```
    * functions with the data (like in sql):
        * set1.intersection(set2)- the shared between 2 sets # = set1 & set2
        * set1.isdisjoint(s2)- returns True if there are **no shared items** between 2 sets, else return False
        * set1.issubset(s2)- if set1 is sub set of set2 (check by values and size)  == set1 <= s2 
        * set1 < s2= if euqal will return False, because it's smaller and not equal too.
        * set1.issuperset(s2)= opposite from subset = set1>=s2
        * set1>s2 - if s2 is subset of set1
    * len
    * copy - deep copy
    * clear empty set look like set()
    * access:
        * not with indexes (s1[0]), don't have permanent location in the set, there is no use in the index.
    * convert list to set: set(list)
    * automatically minimized the duplicate items and sort the remains.
    
## extra subjects:

    * not subscriptable= not working with indexes.