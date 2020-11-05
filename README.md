[![Build Status](https://travis-ci.com/palaciodaniel/lambda_swapi_v2.0.svg?branch=master)](https://travis-ci.com/palaciodaniel/lambda_swapi_v2.0)
[![codecov](https://codecov.io/gh/palaciodaniel/lambda_swapi_v2.0/branch/master/graph/badge.svg)](https://codecov.io/gh/palaciodaniel/lambda_swapi_v2.0)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/palaciodaniel/lambda_swapi_v2.0/master?filepath=lambda_swapi_v2.0.ipynb)

# Lambda SWAPI v.2.0

Instructions
------------
Simply choose two characters from the *Star Wars* universe, and the program will query **SWAPI** (https://swapi.dev/), a *Star Wars API*, to return the movies in which both of them appear.

If you have never executed a Jupyter Notebook before, just press the **Launch Binder** icon above, and wait until the program loads (it can take a while!). Once it is ready, go to **Cell** and choose **Run All**. If you want to try another combination, select the cell marked as [2] and press **Shift + Enter** (or click the **Run** button just below the Cell tab).

<p align="center"> 
<img src="https://images.unsplash.com/photo-1547700055-b61cacebece9?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80">
</p>

Important notes
---------------
- The original site (*SWAPI.co*) suddently stopped working, therefore this program is actually querying a forked version (**SWAPI.dev**).
- As of September 2020, **SWAPI** only covers the original and prequel trilogies.

Changelog
---------
**1.0 to 2.0**

The code has been rewritten from scratch.

- **Improved search:** The program no longer downloads the whole characters list and then loops over it. Now it "captures" dinamically the names and once it gets both characters' names it automatically stops the searching.
- **Use of fuzzywuzzy library:** With the use of this library, now it automatically detects if there are matches with the API, even if there are typing mistakes on user's input. And it even allows for considerable variations; for instance, while the character on the database is called "Jabba Desilijic Tiure", user still can write "Jabba the Hutt" and it will be detected as well.
- **More robust functions:** Now they are able to detect several anormal situations and stop the program accordingly (i.e.: list with invalid URLs).
- **Proper Unit Testing:** The Unit Tests now were properly implemented, and also a lot more were added, making an approximate total of 111.
- **Easier to use:** You only need to load the Jupyter Notebook file, write your two desired characters and simply wait for the program to return some results.
- **Preliminary Static Type Checking on Functions:** More information about this functionality can be read [here](https://medium.com/@ageitgey/learn-how-to-use-static-type-checking-in-python-3-6-in-10-minutes-12c86d72677b).

Credits
-------
Program written from scratch by **Daniel Palacio**.

*SWAPI* was written by **Paul Hallett** (https://github.com/phalt) and currently maintained by **Juriy Bura** (https://github.com/Juriy/swapi).

*Star Wars* image by **Agnieszka Kowalczyk** - *Unsplash.com* (https://unsplash.com/photos/c0VRNWVEjOA)


