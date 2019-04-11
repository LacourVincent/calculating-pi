# Calculating Pi (π)

Implementation of how to calculate the value of π with Python.

## Polygon to approximate a cercle

The first and most obvious way to calculate Pi (π) is to take the most perfect circle you can, and then measure its circumference and diameter to work out Pi (π).

$$
π = \frac{circumference}{diameter}
$$


## Gregory-Leibniz Series

One of the most well known and beautiful ways to calculate Pi (π) is to use the Gregory-Leibniz Series:

$$
\frac{π}{4} = 1 - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \frac{1}{9} + ...
$$

$$
\frac{π}{4} = 1 + \sum_{i=1}^{N} (-1)^{i}\times\frac{1}{2i+1}
$$


## Nilakantha Series


Another series which converges more quickly is the Nilakantha Series which was developed in the 15th century. Converges more quickly means that you need to work out fewer terms for your answer to become closer to Pi (π) :

$$
π = 3 + \frac{1}{2\times3\times4} - \frac{1}{4\times5\times6} + \frac{1}{6\times7\times8} - \frac{1}{8\times9\times10} + ...
$$

$$
π = 3 + \sum_{i=1}^{N} (-1)^{i-1}\times\frac{4}{2i\times(2i+1)\times(2i+2)}
$$

## References

[Calculating pi](http://www.mathscareers.org.uk/article/calculating-pi/)

[How to Calculate Pi](https://www.wikihow.com/Calculate-Pi)


## LICENSE
MIT




