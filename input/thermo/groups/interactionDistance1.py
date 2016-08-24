#!/usr/bin/env python
# encoding: utf-8

name = "Interaction Corrections with distance 1"
shortDesc = u""
longDesc = u"""

"""

entry(
    index = 0,
    label = "R",
    group = 
"""
1 *1 [Cs,Os,Cd,Ss] u0 {2,S}
2 *2 Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 1,
    label = "CsCs",
    group = 
"""
1 *1 Cs u0 {2,S}
2 *2 Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "CsCs-PP",
    group = 
"""
1 *1 Cs                         u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs                         u0 {1,S} {6,S} {7,S} {8,S}
3   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {1,S}
4   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {1,S}
5   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {1,S}
6   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {2,S}
7   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {2,S}
8   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {2,S}
""",

    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 3,
    label = "CsCs-PS",
    group = 
"""
1 *1 Cs                         u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs                         u0 {1,S} {6,S} {7,S} {8,S}
3   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {1,S}
4   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {1,S}
5   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {1,S}
6   Cs                         u0 {2,S}
7   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {2,S}
8   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {2,S}
""",

    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 4,
    label = "CsCs-PT",
    group = 
"""
1 *1 Cs                         u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs                         u0 {1,S} {6,S} {7,S} {8,S}
3   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {1,S}
4   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {1,S}
5   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {1,S}
6   Cs                         u0 {2,S}
7   Cs                         u0 {2,S}
8   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {2,S}
""",

    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 5,
    label = "CsCs-PQ",
    group = 
"""
1 *1 Cs                         u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs                         u0 {1,S} {6,S} {7,S} {8,S}
3   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {1,S}
4   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {1,S}
5   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {1,S}
6   Cs                         u0 {2,S}
7   Cs                         u0 {2,S}
8   Cs                         u0 {2,S}
""",

    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 6,
    label = "CsCs-SS",
    group = 
"""
1 *1 Cs                         u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs                         u0 {1,S} {6,S} {7,S} {8,S}
3   Cs                         u0 {1,S}
4   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {1,S}
5   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {1,S}
6   Cs                         u0 {2,S}
7   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {2,S}
8   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {2,S}
""",

    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 7,
    label = "CsCs-ST",
    group = 
"""
1 *1 Cs                         u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs                         u0 {1,S} {6,S} {7,S} {8,S}
3   Cs                         u0 {1,S}
4   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {1,S}
5   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {1,S}
6   Cs                         u0 {2,S}
7   Cs                         u0 {2,S}
8   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {2,S}
""",

    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0.8,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 8,
    label = "CsCs-SQ",
    group = 
"""
1 *1 Cs                         u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs                         u0 {1,S} {6,S} {7,S} {8,S}
3   Cs                         u0 {1,S}
4   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {1,S}
5   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {1,S}
6   Cs                         u0 {2,S}
7   Cs                         u0 {2,S}
8   Cs                         u0 {2,S}
""",

    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (1.6,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 9,
    label = "CsCs-TT",
    group = 
"""
1 *1 Cs                         u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs                         u0 {1,S} {6,S} {7,S} {8,S}
3   Cs                         u0 {1,S}
4   Cs                         u0 {1,S}
5   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {1,S}
6   Cs                         u0 {2,S}
7   Cs                         u0 {2,S}
8   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {2,S}
""",

    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0.8,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Half Value!!!
""",
)

entry(
    index = 9,
    label = "CsCs-T(TTP)",
    group = 
"""
1 *1 Cs                         u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs                         u0 {1,S} {6,S} {7,S} {8,S}
3   Cs                         u0 {1,S} {9,S} {10,S} {11,S}
4   Cs                         u0 {1,S} {12,S} {13,S} {14,S}
5   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {1,S}
6   Cs                         u0 {2,S}
7   Cs                         u0 {2,S}
8   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {2,S}
9   Cs                         u0 {3,S}
10   Cs                         u0 {3,S}
11   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {3,S}
12   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {4,S}
13   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {4,S}
14   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {4,S}
""",

    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (1.2,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
(2 GI)/2 + (1 GI)/2 The additional 1 GI is for TTT structure!!!
""",
)

entry(
    index = 9,
    label = "CsCs-T(TTS)",
    group = 
"""
1 *1 Cs                         u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs                         u0 {1,S} {6,S} {7,S} {8,S}
3   Cs                         u0 {1,S} {9,S} {10,S} {11,S}
4   Cs                         u0 {1,S} {12,S} {13,S} {14,S}
5   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {1,S}
6   Cs                         u0 {2,S}
7   Cs                         u0 {2,S}
8   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {2,S}
9   Cs                         u0 {3,S}
10   Cs                         u0 {3,S}
11   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {3,S}
12   Cs u0 {4,S}
13   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {4,S}
14   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {4,S}
""",

    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (1.2,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
(2 GI)/2 + (1 GI)/2 The additional 1 GI is for TTT structure!!!
""",
)

entry(
    index = 9,
    label = "CsCs-T(TTT)",
    group = 
"""
1 *1 Cs                         u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs                         u0 {1,S} {6,S} {7,S} {8,S}
3   Cs                         u0 {1,S} {9,S} {10,S} {11,S}
4   Cs                         u0 {1,S} {12,S} {13,S} {14,S}
5   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {1,S}
6   Cs                         u0 {2,S}
7   Cs                         u0 {2,S}
8   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {2,S}
9   Cs                         u0 {3,S}
10   Cs                         u0 {3,S}
11   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {3,S}
12   Cs u0 {4,S}
13   Cs u0 {4,S}
14   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {4,S}
""",

    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (1.067,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
(2 GI) / 2 + (1 GI) / 3 The additional 1 GI is for TTT structure!!!
""",
)

entry(
    index = 9,
    label = "CsCs-T(TTQ)",
    group = 
"""
1 *1 Cs                         u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs                         u0 {1,S} {6,S} {7,S} {8,S}
3   Cs                         u0 {1,S} {9,S} {10,S} {11,S}
4   Cs                         u0 {1,S} {12,S} {13,S} {14,S}
5   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {1,S}
6   Cs                         u0 {2,S}
7   Cs                         u0 {2,S}
8   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {2,S}
9   Cs                         u0 {3,S}
10   Cs                         u0 {3,S}
11   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {3,S}
12   Cs u0 {4,S}
13   Cs u0 {4,S}
14   Cs u0 {4,S}
""",

    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (1.2,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
(2 GI)/2 + (1 GI)/2 The additional 1 GI is for TTT structure!!!
""",
)

entry(
    index = 10,
    label = "CsCs-TQ",
    group = 
"""
1 *1 Cs                         u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs                         u0 {1,S} {6,S} {7,S} {8,S}
3   Cs                         u0 {1,S}
4   Cs                         u0 {1,S}
5   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {1,S}
6   Cs                         u0 {2,S}
7   Cs                         u0 {2,S}
8   Cs                         u0 {2,S}
""",

    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (3.2,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 11,
    label = "CsCs-QQ",
    group = 
"""
1 *1 Cs                         u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs                         u0 {1,S} {6,S} {7,S} {8,S}
3   Cs                         u0 {1,S}
4   Cs                         u0 {1,S}
5   Cs                         u0 {1,S}
6   Cs                         u0 {2,S}
7   Cs                         u0 {2,S}
8   Cs                         u0 {2,S}
""",

    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (2.4,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""
Half Value!!!
""",
)

entry(
    index = 12,
    label = "OsCs",
    group = 
"""
1 *1 Os u0 {2,S}
2 *2 Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 13,
    label = "OsCs-P",
    group = 
"""
1 *1 Os                         u0 {2,S} {3,S}
2 *2 Cs                         u0 {1,S}
3   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 14,
    label = "OsCs-SP",
    group = 
"""
1 *1 Os                         u0 {2,S} {3,S}
2 *2 Cs                         u0 {1,S} {4,S} {5,S} {6,S}
3   Cs                         u0 {1,S}
4   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {2,S}
5   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {2,S}
6   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 15,
    label = "OsCs-SS",
    group = 
"""
1 *1 Os                         u0 {2,S} {3,S}
2 *2 Cs                         u0 {1,S} {4,S} {5,S} {6,S}
3   Cs                         u0 {1,S}
4   Cs                         u0 {2,S}
5   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {2,S}
6   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 16,
    label = "OsCs-ST",
    group = 
"""
1 *1 Os                         u0 {2,S} {3,S}
2 *2 Cs                         u0 {1,S} {4,S} {5,S} {6,S}
3   Cs                         u0 {1,S}
4   Cs                         u0 {2,S}
5   Cs                         u0 {2,S}
6   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0.5,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 17,
    label = "OsCs-SQ",
    group = 
"""
1 *1 Os                         u0 {2,S} {3,S}
2 *2 Cs                         u0 {1,S} {4,S} {5,S} {6,S}
3   Cs                         u0 {1,S}
4   Cs                         u0 {2,S}
5   Cs                         u0 {2,S}
6   Cs                         u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (1.0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "CdCs",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S}
2   Cd u0 {1,D}
3 *2 Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 18,
    label = "CdCs-P",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {1,S}
4 *2 Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 19,
    label = "CdCs-SP",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Cs u0 {1,S}
4 *2 Cs u0 {1,S} {5,S} {6,S} {7,S}
5   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {4,S}
6   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {4,S}
7   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
    label = "CdCs-SS",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Cs u0 {1,S}
4 *2 Cs u0 {1,S} {5,S} {6,S} {7,S}
5   Cs                         u0 {4,S}
6   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {4,S}
7   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 21,
    label = "CdCs-ST",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Cs u0 {1,S}
4 *2 Cs u0 {1,S} {5,S} {6,S} {7,S}
5   Cs                         u0 {4,S}
6   Cs                         u0 {4,S}
7   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (1,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 22,
    label = "CdCs-SQ",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Cs u0 {1,S}
4 *2 Cs u0 {1,S} {5,S} {6,S} {7,S}
5   Cs                         u0 {4,S}
6   Cs                         u0 {4,S}
7   Cs                         u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (1,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 23,
    label = "SsCs",
    group = 
"""
1 *1 Ss u0 {2,S}
2 *2 Cs u0 {1,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

entry(
    index = 24,
    label = "Ss(Cs(CsHH)H)",
    group = 
"""
1 *1 Ss u0 {2,S} {3,S}
2 *2 Cs u0 {1,S} {4,S} {5,S} {6,S}
3   H  u0 {1,S}
4   H  u0 {2,S}
5   H  u0 {2,S}
6   Cs u0 {2,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.33,0.62,0.67,0.59,0.38,0.21,-0.01],'cal/(mol*K)'),
        H298 = (-0.97,'kcal/mol'),
        S298 = (-1.01,'cal/(mol*K)'),
    ),
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

tree(
"""
L1: R
    L2: CsCs
        L3: CsCs-PP
        L3: CsCs-PS
        L3: CsCs-PT
        L3: CsCs-PQ
        L3: CsCs-SS
        L3: CsCs-ST
        L3: CsCs-SQ
        L3: CsCs-TT
            L4: CsCs-T(TTP)
            L4: CsCs-T(TTS)
            L4: CsCs-T(TTT)
            L4: CsCs-T(TTQ)
        L3: CsCs-TQ
        L3: CsCs-QQ
    L2: OsCs
        L3: OsCs-P
        L3: OsCs-SP
        L3: OsCs-SS
        L3: OsCs-ST
        L3: OsCs-SQ
    L2: CdCs
        L3: CdCs-P
        L3: CdCs-SP
        L3: CdCs-SS
        L3: CdCs-ST
        L3: CdCs-SQ
    L2: SsCs
        L3: Ss(Cs(CsHH)H)
"""
)
