# python-basic-lec19-Nov-24-24
## subjects learned:
* tuple- continue:
  *   result += (t,) vs list.append(): += create a new tuple in the memory and combined, and the old one remains in the memory and waits for the GC.
        therefore it's better to use list.append() and not "adding" the tuple items
* enumerate(tuple)= to get the index and value from list/tuple:
```
     for i,v in enumerate(t1): *(i,v)=item-tuple
```

## extra subjects:
