
var 0..15: a;
var 0..15: b;
var 0..15: c;
var 0..15: d;
var 0..15: e;
var 0..15: f;
var 0..15: g;

constraint 2-3*a+d+e+g >= 0;
constraint 1-2*b+d+c >= 0;
constraint 0-2*c+f+b >= 0;
constraint 3-4*d+a+e+b+f >= 0;
constraint 3-3*e+d+a+g >= 0;
constraint 3-3*f+g+d+c >= 0;
constraint -2-3*g+f+a+e >= 0;


solve satisfy;

output ["  a:  \(a)\n",
        "  b:  \(b)\n",
        "  c:  \(c)\n",
        "  d:  \(d)\n",
        "  e:  \(e)\n",
        "  f:  \(f)\n",
        "  g:  \(g)\n",
];

