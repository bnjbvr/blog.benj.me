Title: Previous writings about Mozilla work
Date: 2016-03-09 18:00
Author: Benjamin Bouvier
Tags: opensource, mozilla
Slug: previous-writing-about-mozilla-work

I am currently a compiler engineer at Mozilla corporation, the company making
the Firefox browser among else. Our JavaScript virtual machine, Spidermonkey,
is split in several tiers, including an highly optimizing Just-In-Time (JIT)
compiler able to compile JavaScript to assembly at runtime. My previous work
has involved efficiently compiling Float32 arithmetic to hardware instructions
and implement a new SIMD API for the Web.

## About Float32 optimizations

The full blog post is
[there](https://blog.mozilla.org/javascript/2013/11/07/efficient-float32-arithmetic-in-javascript/).
It has been written in November 2013.

The main idea is that if you have float32 inputs to an operation; and you cast
them to doubles; and you apply an arithmetic operation to these inputs; and you
cast the result back to a float32, then you'd have the same result as if you
did the entire computation with float32 values and operations.

So we've introduced an operation in JavaScript that converts a Number to its
closest float32 IEEE754 representation: `Math.fround`. Said differently, the
above equivalence says that:

```javascript
function f(x, y) {
    return x + y;
}

function g(x, y) {
    var xf = Math.fround(x);
    var yf = Math.fround(y);
    return Math.fround(xf + yf);
}

// For all x, y that can be represented exactly as float32:
assert(f(x, y) === g(x, y));
```

Yes, `===`. The same `===` you've been told **not** to use for floating-point
Numbers. But here, we have *bitwise* equality, so we can use strict equality*.

Processors have special instructions for carrying out float32 arithmetic, which
have higher throughput than the equivalent double ones. With this result in
mind, we could add a pass that would spot opportunities where the computations
are equivalent (thanks to `Math.fround` hints) and emit float32 instructions
instead of double instructions. This sped up a some numerical applications and
games engines by a few points.

\* a careful reader would object that this is wrong for `x = y = NaN`, which
I've put away for the sake of simplicity.

## About SIMD.js

The full blog post is
[there](https://blog.mozilla.org/javascript/2015/03/10/state-of-simd-js-performance-in-firefox/).
It has been written in March 2015.

Nowadays, processors have instructions sets that allow them to execute several
simple arithmetic operations at once. For instance, let's say you have two
arrays of integers and you want to add each element to the corresponding one in
the other array. If both arrays have size `N`, this means you'll have to carry
out `N` scalar additions. But processors can actually group these into bundles
of several additions, with SIMD; for the case of 32-bits wide integers, on most
modern processors, you need at most `Math.ceil(N / 4)` instructions. The blog
post details what SIMD.js is and what bottlenecks we hit during implementation.

## Conclusion

This was a small reminder about previously written blog posts. If you're into
JavaScript, compilers or low-level optimization, I can only recommend you to go
read the [Mozilla's JavaScript blog](https://blog.mozilla.org/javascript/).

