# What is it?

My dirty experiments and my wet fantasies about how front-end development would look like if we used
Python instead of JavaScript.

Meanwhile here's a dev server for application written on Python. It runs a page with Python code in it and restart the page every time when application code is changed.

That's just a start. More cool features will come.

# Why?

Because I got sick of JavaScript in general, of all those ES6/7 attempts to make JS better which eventually made things only worse, of over 9000 JS frameworks, libraries doing the same and for sure of all the packaging systems, test runners etc. [Look here for more details](https://hackernoon.com/how-it-feels-to-learn-javascript-in-2016-d3a717dd577f).

As Python is clear, clever, easy to use and popular language why shouldn't it be used for front-end? I don't see any reason why not. Well the (Brython)[http://brython.info/index.html] I'm using now is to be compiled to javascript anyway but so is true for your beloved ES6/7. Yeah! Stop lying and pretending that you're using ES6 for front-end development. It still transpelled by babel into vanila JavaScript which is run by browser at the end of the day. So why not to use some really good language with good concepts if it's going to be transpelled anyway. One day I beleive python code may be compiled with [Nuitka](https://nuitka.net/) into C and then with [ECMAScript](https://en.wikipedia.org/wiki/ECMAScript) to WebAssembly for the sake of performance - but meanwhile I want to do fast prototyping on human-friendly language, so to make sure that business logic works. And then I'll think how to optimize performance if needed.

And not only this - I want to disrupt entirely the way we do front-end, so it looks more like normal GUI development. Not like making Frankenstein monster out of dead flesh. I want to do it Pythonic way, the only right and logical way to do software development.

# Installation

Just clone it and install all requirements:

```
$ git clone https://github.com/nskrypnik/brython-dev-server.git
$ cd brython-dev-server
$ pip install -r requirements.txt
```

# Run dev server

I like simplicity. So just:

```
$ python -m server.start
```
