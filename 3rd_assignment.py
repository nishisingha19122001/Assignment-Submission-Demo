# -*- coding: utf-8 -*-
"""3rd Assignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18Wwa7C4j0AaY9acLEX06BpRtdBxf77YC
"""

#Assignment 3

altitude=int(input("This is ATC Mumbai Airport, Whats your altitude pilot :"))
if altitude <1000:
   print("HC 978, You are allowed to land")
elif altitude >=1000 and altitude < 5000:
   print("HC 978, Come down to 1000ft")
elif altitude >= 5000: 
   print("HC 978, Go around and try later")

