install: numpy, matplotlib, open-cv

Code editing pictures:

1. gamma.py:
   origin gamma value: 1
   
   remove auto white balance caused by the lab scan machine: gamma below 1 (e.g. 0.5, 0.7, 0.3)
   
   adding more light / exposure: gamma above 1 (e.g. 1.5, 2)
   
2. inverting negatives into positive images:
   
   step one: removing color mask by normalizing the color
   
   step two: negate the value for the three channels: red, green, blue
   
   step three: merge three channels to get the positive picture


Part of the scripts are from public resources, and also with the help of ChatGPT. I do not claim the originality of the algorithm. 
Feel free to use those files and try editing your film pictures!
