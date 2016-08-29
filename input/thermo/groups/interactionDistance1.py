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
1 *1 R u0
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
    index = 0,
    label = "gauche",
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
    label = "CsCs-P",
    group = 
"""
1 *1 Cs                         u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs                         u0 {1,S}
3   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {1,S}
4   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {1,S}
5   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {1,S}
""",

    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""Lumped PP/PS/PT/PQ, because they all counted as 0 as long as the first carbon is primary carbon""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "CsCs-S",
    group = 
"""
1 *1 Cs                         u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs                         u0 {1,S}
3   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {1,S}
4   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {1,S}
5   Cs u0 {1,S}
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
    index = 2,
    label = "CsCs-T",
    group = 
"""
1 *1 Cs                         u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs                         u0 {1,S}
3   [Cd,Cdd,Ct,Cb,Cbf,Os,CO,H] u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
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
    index = 2,
    label = "CsCs-Q",
    group = 
"""
1 *1 Cs                         u0 {2,S} {3,S} {4,S} {5,S}
2 *2 Cs                         u0 {1,S}
3   Cs u0 {1,S}
4   Cs u0 {1,S}
5   Cs u0 {1,S}
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
    label = "OsCs-S",
    group = 
"""
1 *1 Os                         u0 {2,S} {3,S}
2 *2 Cs                         u0 {1,S}
3    Cs                         u0 {1,S}
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
    label = "CdCs-S",
    group = 
"""
1 *1 Cd u0 {2,D} {3,S} {4,S}
2   Cd u0 {1,D}
3   Cs u0 {1,S}
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
    shortDesc = u"""From old version - gauche.py""",
    longDesc = 
u"""

""",
)

entry(
    index = 25,
    label = "aromatic-ortho",
    group = 
"""
1 *1 Cb u0 {2,B}
2 *2 Cb u0 {1,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""Root for Aromatics NNI correction.""",
    longDesc = 
u"""

""",
)

entry(
    index = 2,
    label = "o_OH_CHO",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {5,S}
3    O u0 {1,S} {4,S}
4    H u0 {3,S}
5    C u0 {2,S} {6,S} {7,D}
6    H u0 {5,S}
7    O u0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-2.49, -2.15, -1.77, -1.43, -0.81, -0.33, 0.43],'cal/(mol*K)'),
        H298 = (-6.55,'kcal/mol'),
        S298 = (-5.09,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""
""",
)

entry(
    index = 3,
    label = "o_CHO",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B}
3    C u0 {1,S} {4,S} {5,D}
4    H u0 {3,S}
5    O u0 {3,D}
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
    label = "o_CHO_CHO",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {5,S}
3    C u0 {1,S} {4,S} {8,D}
4    H u0 {3,S}
5    C u0 {2,S} {6,S} {7,D}
6    H u0 {5,S}
7    O u0 {5,D}
8    O u0 {3,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.20, 0.20, 0.19, 0.17, 0.05, -0.10, -0.30],'cal/(mol*K)'),
        H298 = (2.52,'kcal/mol'),
        S298 = (0.76,'cal/(mol*K)'),
    ),
    shortDesc = u"""Half value. This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""
""",
)

entry(
    index = 4,
    label = "o_MeO",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B}
3    O u0 {1,S} {4,S}
4    C u0 {3,S} {5,S} {6,S} {7,S}
5    H u0 {4,S}
6    H u0 {4,S}
7    H u0 {4,S}
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
    label = "o_MeO_MeO",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {8,S}
3    O u0 {1,S} {4,S}
4    C u0 {3,S} {5,S} {6,S} {7,S}
5    H u0 {4,S}
6    H u0 {4,S}
7    H u0 {4,S}
8    O u0 {2,S} {9,S}
9    C u0 {8,S} {10,S} {11,S} {12,S}
10   H u0 {9,S}
11   H u0 {9,S}
12   H u0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.00, -0.41, -0.56, -0.60, -0.53, -0.44, -0.26],'cal/(mol*K)'),
        H298 = (1.76,'kcal/mol'),
        S298 = (0.93,'cal/(mol*K)'),
    ),
    shortDesc = u"""Half value. This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""
""",
)

entry(
    index = 5,
    label = "o_CHO_vinyl",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {6,S}
3    C u0 {1,S} {4,S} {5,D}
4    H u0 {3,S}
5    O u0 {3,D}
6    C u0 {2,S} {7,D} {8,S}
7    C u0 {6,D} {9,S} {10,S}
8    H u0 {6,S}
9    H u0 {7,S}
10   H u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.31, 0.38, 0.50, 0.60, 0.57, 0.43, 0.07],'cal/(mol*K)'),
        H298 = (2.84,'kcal/mol'),
        S298 = (-0.62,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""
""",
)

entry(
    index = 6,
    label = "o_vinyl",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B}
3    C u0 {1,S} {4,S} {5,D}
4    H u0 {3,S}
5    C u0 {3,D} {6,S} {7,S}
6   H u0 {5,S}
7   H u0 {5,S}
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
    label = "o_vinyl_vinyl",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {6,S}
3    C u0 {1,S} {4,S} {5,D}
4    H u0 {3,S}
5    C u0 {3,D} {11,S} {12,S}
6    C u0 {2,S} {7,D} {8,S}
7    C u0 {6,D} {9,S} {10,S}
8    H u0 {6,S}
9    H u0 {7,S}
10   H u0 {7,S}
11   H u0 {5,S}
12   H u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.55, 0.38, 0.25, 0.16, 0.02, -0.02, -0.06],'cal/(mol*K)'),
        H298 = (0.97,'kcal/mol'),
        S298 = (-0.27,'cal/(mol*K)'),
    ),
    shortDesc = u"""Half value. This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""
""",
)

entry(
    index = 7,
    label = "o_CHO_CH3",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {6,S}
3    C u0 {1,S} {4,S} {5,D}
4    H u0 {3,S}
5    O u0 {3,D}
6    C u0 {2,S} {7,S} {8,S} {9,S}
7    H u0 {6,S}
8    H u0 {6,S}
9    H u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.96, 0.72, 0.48, 0.26, 0.00, -0.14, -0.22],'cal/(mol*K)'),
        H298 = (1.94,'kcal/mol'),
        S298 = (-0.57,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""
""",
)

entry(
    index = 8,
    label = "o_CHO_C2H5",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {6,S}
3    C u0 {1,S} {4,S} {5,D}
4    H u0 {3,S}
5    O u0 {3,D}
6    C u0 {2,S} {7,S} {8,S} {9,S}
7    H u0 {6,S}
8    H u0 {6,S}
9    C u0 {6,S} {10,S} {11,S} {12,S}
10    H u0 {9,S}
11    H u0 {9,S}
12    H u0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.96, 0.72, 0.48, 0.26, 0.00, -0.14, -0.22],'cal/(mol*K)'),
        H298 = (1.94,'kcal/mol'),
        S298 = (-0.57,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""
""",
)

entry(
    index = 9,
    label = "o_vinyl_CH3",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {8,S}
3    C u0 {1,S} {4,S} {5,D}
4    H u0 {3,S}
5    C u0 {3,D} {6,S} {7,S}
6    H u0 {5,S}
7    H u0 {5,S}
8    C u0 {2,S} {9,S} {10,S} {11,S}
9    H u0 {8,S}
10   H u0 {8,S}
11   H u0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.36, 1.34, 1.17, 1.00, 0.69, 0.50, 0.24],'cal/(mol*K)'),
        H298 = (1.10,'kcal/mol'),
        S298 = (-1.36,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""
""",
)

entry(
    index = 10,
    label = "o_vinyl_C2H5",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {8,S}
3    C u0 {1,S} {4,S} {5,D}
4    H u0 {3,S}
5    C u0 {3,D} {6,S} {7,S}
6    H u0 {5,S}
7    H u0 {5,S}
8    C u0 {2,S} {9,S} {10,S} {11,S}
9    H u0 {8,S}
10   H u0 {8,S}
11   C u0 {8,S} {12,S} {13,S} {14,S}
12   H u0 {11,S}
13   H u0 {11,S}
14   H u0 {11,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([1.36, 1.34, 1.17, 1.00, 0.69, 0.50, 0.24],'cal/(mol*K)'),
        H298 = (1.10,'kcal/mol'),
        S298 = (-1.36,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""
""",
)

entry(
    index = 11,
    label = "o_CHO_MeO",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {6,S}
3    C u0 {1,S} {4,S} {5,D}
4    H u0 {3,S}
5    O u0 {3,D}
6    O u0 {2,S} {7,S}
7    C u0 {6,S} {8,S} {9,S} {10,S}
8    H u0 {7,S}
9    H u0 {7,S}
10   H u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.62, 0.07, 0.62, 0.93, 0.98, 0.79, 0.31],'cal/(mol*K)'),
        H298 = (1.89,'kcal/mol'),
        S298 = (-0.41,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""
""",
)

entry(
    index = 12,
    label = "o_CH3",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B}
3    C u0 {1,S} {4,S} {5,S} {6,S}
4    H u0 {3,S}
5    H u0 {3,S}
6    H u0 {3,S}
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
    index = 12,
    label = "o_CH3_CH3",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {7,S}
3    C u0 {1,S} {4,S} {5,S} {6,S}
4    H u0 {3,S}
5    H u0 {3,S}
6    H u0 {3,S}
7    C u0 {2,S} {8,S} {9,S} {10,S}
8    H u0 {7,S}
9    H u0 {7,S}
10    H u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.39, 0.35, 0.31, 0.30, 0.27, 0.24, 0.18],'cal/(mol*K)'),
        H298 = (0.50,'kcal/mol'),
        S298 = (-0.79,'cal/(mol*K)'),
    ),
    shortDesc = u"""Half value. This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""
""",
)

entry(
    index = 13,
    label = "o_CH3_C2H5",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {7,S}
3    C u0 {1,S} {4,S} {5,S} {6,S}
4    H u0 {3,S}
5    H u0 {3,S}
6    H u0 {3,S}
7    C u0 {2,S} {8,S} {9,S} {10,S}
8    H u0 {7,S}
9    H u0 {7,S}
10   C u0 {7,S} {11,S} {12,S} {13,S}
11   H u0 {10,S}
12   H u0 {10,S}
13   H u0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.79, 0.69, 0.62, 0.60, 0.55, 0.48, 0.36],'cal/(mol*K)'),
        H298 = (1.00,'kcal/mol'),
        S298 = (-1.58,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""
""",
)

entry(
    index = 14,
    label = "o_C2H5",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B}
3    C u0 {1,S} {4,S} {5,S} {6,S}
4    H u0 {3,S}
5    H u0 {3,S}
6    C u0 {3,S} {7,S} {8,S} {9,S}
7   H u0 {6,S}
8   H u0 {6,S}
9   H u0 {6,S}
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
    label = "o_C2H5_C2H5",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {7,S}
3    C u0 {1,S} {4,S} {5,S} {6,S}
4    H u0 {3,S}
5    H u0 {3,S}
6    C u0 {3,S} {14,S} {15,S} {16,S}
7    C u0 {2,S} {8,S} {9,S} {10,S}
8    H u0 {7,S}
9    H u0 {7,S}
10   C u0 {7,S} {11,S} {12,S} {13,S}
11   H u0 {10,S}
12   H u0 {10,S}
13   H u0 {10,S}
14   H u0 {6,S}
15   H u0 {6,S}
16   H u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.39, 0.35, 0.31, 0.30, 0.27, 0.24, 0.18],'cal/(mol*K)'),
        H298 = (0.50,'kcal/mol'),
        S298 = (-0.79,'cal/(mol*K)'),
    ),
    shortDesc = u"""Half value. This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""
""",
)

entry(
    index = 15,
    label = "o_OH",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B}
3    O u0 {1,S} {4,S}
4    H u0 {3,S}
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
    label = "o_OH_OH",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {5,S}
3    O u0 {1,S} {4,S}
4    H u0 {3,S}
5    O u0 {2,S} {6,S}
6    H u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.32, -0.18, 0.02, 0.24, 0.50, 0.57, 0.44],'cal/(mol*K)'),
        H298 = (-0.36,'kcal/mol'),
        S298 = (-0.67,'cal/(mol*K)'),
    ),
    shortDesc = u"""Half value. This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""
""",
)

entry(
    index = 16,
    label = "o_OH_MeO",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {5,S}
3    O u0 {1,S} {4,S}
4    H u0 {3,S}
5    O u0 {2,S} {6,S}
6    C u0 {5,S} {7,S} {8,S} {9,S}
7    H u0 {6,S}
8    H u0 {6,S}
9    H u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.65, -0.36, 0.05, 0.48, 1.00, 1.15, 0.88],'cal/(mol*K)'),
        H298 = (-0.72,'kcal/mol'),
        S298 = (-1.34,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""
""",
)

entry(
    index = 17,
    label = "o_OH_vinyl",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {5,S}
3    O u0 {1,S} {4,S}
4    H u0 {3,S}
5    C u0 {2,S} {6,D} {7,S}
6    C u0 {5,D} {8,S} {9,S}
7    H u0 {5,S}
8    H u0 {6,S}
9    H u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.60, 0.65, 0.62, 0.60, 0.50, 0.43, 0.29],'cal/(mol*K)'),
        H298 = (0.62,'kcal/mol'),
        S298 = (-0.79,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""
""",
)

entry(
    index = 18,
    label = "o_MeO_vinyl",
    group = 
"""
1 *1 Cb u0 {2,B} {3,S}
2 *2 Cb u0 {1,B} {5,S}
3    O u0 {1,S} {4,S}
4    C u0 {3,S} {10,S} {11,S} {12,S}
5    C u0 {2,S} {6,D} {7,S}
6    C u0 {5,D} {8,S} {9,S}
7    H u0 {5,S}
8    H u0 {6,S}
9    H u0 {6,S}
10    H u0 {4,S}
11    H u0 {4,S}
12    H u0 {4,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.60, 0.65, 0.62, 0.60, 0.50, 0.43, 0.29],'cal/(mol*K)'),
        H298 = (0.62,'kcal/mol'),
        S298 = (-0.79,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""
""",
)

tree(
"""
L1: R
    L2: gauche
        L3: CsCs
            L4: CsCs-P
            L4: CsCs-S
                L5: CsCs-SS
                L5: CsCs-ST
                L5: CsCs-SQ
            L4: CsCs-T
                L5: CsCs-TT
                    L6: CsCs-T(TTP)
                    L6: CsCs-T(TTS)
                    L6: CsCs-T(TTT)
                    L6: CsCs-T(TTQ)
                L5: CsCs-TQ
            L4: CsCs-Q
                L5: CsCs-QQ
        L3: OsCs
            L4: OsCs-P
            L4: OsCs-S
                L5: OsCs-SP
                L5: OsCs-SS
                L5: OsCs-ST
                L5: OsCs-SQ
        L3: CdCs
            L4: CdCs-P
            L4: CdCs-S
                L5: CdCs-SP
                L5: CdCs-SS
                L5: CdCs-ST
                L5: CdCs-SQ
        L3: SsCs
            L4: Ss(Cs(CsHH)H)
    L2: aromatic-ortho
        L3: o_OH
            L4: o_OH_OH
            L4: o_OH_MeO
            L4: o_OH_vinyl
            L4: o_OH_CHO
        L3: o_CHO
            L4: o_CHO_CHO
            L4: o_CHO_vinyl
            L4: o_CHO_CH3
            L4: o_CHO_C2H5
            L4: o_CHO_MeO
        L3: o_vinyl
            L4: o_vinyl_vinyl
            L4: o_vinyl_CH3
            L4: o_vinyl_C2H5
        L3: o_MeO
            L4: o_MeO_MeO
            L4: o_MeO_vinyl
        L3: o_CH3
            L4: o_CH3_CH3
            L4: o_CH3_C2H5
        L3: o_C2H5
            L4: o_C2H5_C2H5
"""
)
