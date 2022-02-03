
var 0..15: a;
var 0..15: b;
var 0..15: c;
var 0..15: d;
var 0..15: e;

constraint -2 - 2*a + b + e >= 0;
constraint 5 + a -2*b + d >= 0;
constraint -1 -c + e >= 0;
constraint -2 + b + e -2*d >= 0;
constraint 2 + a + d - 3*e + c >= 0;


solve satisfy;

output ["  a:  \(a)\n",
        "  b:  \(b)\n",
        "  c:  \(c)\n",
        "  d:  \(d)\n",
        "  e:  \(e)\n"
];

