
var 0..15: a;
var 0..15: b;
var 0..15: c;
var 0..15: d;
var 0..15: e;
var 0..15: f;
var 0..15: g;

constraint -2-3*a+g+d+b >= 0;
constraint -1-3*b+g+a+d >= 0;
constraint -4-2*c+e+f >= 0;
constraint 0-3*d+a+f+b >= 0;
constraint 2-2*e+g+c >= 0;
constraint 3-3*f+g+d+c >= 0;
constraint 3-4*g+b+a+e+f >= 0;


solve satisfy;

output ["  a:  \(a)\n",
        "  b:  \(b)\n",
        "  c:  \(c)\n",
        "  d:  \(d)\n",
        "  e:  \(e)\n",
        "  f:  \(f)\n",
        "  g:  \(g)\n",
];

