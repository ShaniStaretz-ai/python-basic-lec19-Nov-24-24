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

## extra subjects:
