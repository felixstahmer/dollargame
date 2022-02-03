
var 0..15: a;
var 0..15: b;
var 0..15: c;
var 0..15: d;
var 0..15: e;

constraint 3 -3*a + b + d + c >= 0;
constraint 3 -2*b + a + e >= 0;
constraint 0 -3*c + d + a + e >= 0;
constraint -2 -2*d + a + c >= 0;
constraint -3 -2*e + b + c >= 0;


solve satisfy;

output ["  a:  \(a)\n",
        "  b:  \(b)\n",
        "  c:  \(c)\n",
        "  d:  \(d)\n",
        "  e:  \(e)\n"
];

