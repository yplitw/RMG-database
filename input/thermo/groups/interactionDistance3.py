#!/usr/bin/env python
# encoding: utf-8

name = "Interaction Corrections with distence 3"
shortDesc = u""
longDesc = u"""

"""

entry(
    index = 0,
    label = "R",
    group = 
"""
1 *1 R u0 {2,B}
2    R u0 {1,B} {3,B}
3    R u0 {2,B} {4,B}
4 *2 R u0 {3,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""Root""",
    longDesc = 
u"""
""",
)

entry(
    index = 0,
    label = "aromatic-para",
    group = 
"""
1 *1 Cb u0 {2,B}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B}
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
    index = 22,
    label = "p_OH",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B}
5    O u0 {1,S} {6,S}
6    H u0 {5,S}
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
    index = 22,
    label = "p_OH_OH",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B} {7,S}
5    O u0 {1,S} {6,S}
6    H u0 {5,S}
7    O u0 {4,S} {8,S}
8    H u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.20, 0.05, -0.10, -0.20, -0.27, -0.27, -0.20],'cal/(mol*K)'),
        H298 = (0.87,'kcal/mol'),
        S298 = (0.48,'cal/(mol*K)'),
    ),
    shortDesc = u"""Half value. This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""
""",
)

entry(
    index = 23,
    label = "p_OH_MeO",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B} {7,S}
5    O u0 {1,S} {6,S}
6    H u0 {5,S}
7    O u0 {4,S} {8,S}
8    C u0 {7,S} {9,S} {10,S} {11,S}
9    H u0 {8,S}
10   H u0 {8,S}
11   H u0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.41, 0.10, -0.19, -0.41, -0.55, -0.55, -0.41],'cal/(mol*K)'),
        H298 = (1.74,'kcal/mol'),
        S298 = (0.96,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""
""",
)

entry(
    index = 24,
    label = "p_MeO",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B}
5    O u0 {1,S} {6,S}
6    C u0 {5,S} {7,S} {8,S} {9,S}
7    H u0 {6,S}
8    H u0 {6,S}
9    H u0 {6,S}
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
    label = "p_MeO_MeO",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B} {7,S}
5    O u0 {1,S} {6,S}
6    C u0 {5,S} {12,S} {13,S} {14,S}
7    O u0 {4,S} {8,S}
8    C u0 {7,S} {9,S} {10,S} {11,S}
9    H u0 {8,S}
10   H u0 {8,S}
11   H u0 {8,S}
12   H u0 {6,S}
13   H u0 {6,S}
14   H u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.20, 0.05, -0.10, -0.20, -0.27, -0.27, -0.20],'cal/(mol*K)'),
        H298 = (0.87,'kcal/mol'),
        S298 = (0.48,'cal/(mol*K)'),
    ),
    shortDesc = u"""Half value. This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""
""",
)

entry(
    index = 25,
    label = "p_CHO",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B}
5    C u0 {1,S} {6,S} {7,D}
6    H u0 {5,S}
7    O u0 {5,D}
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
    index = 25,
    label = "p_CHO_CHO",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B} {7,S}
5    C u0 {1,S} {6,S} {10,D}
6    H u0 {5,S}
7    C u0 {4,S} {8,D} {9,S}
8    O u0 {7,D}
9    H u0 {7,S}
10   O u0 {5,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.22, 0.17, 0.12, 0.08, 0.01, -0.04, -0.11],'cal/(mol*K)'),
        H298 = (1.18,'kcal/mol'),
        S298 = (-0.10,'cal/(mol*K)'),
    ),
    shortDesc = u"""Half value. This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""
""",
)

entry(
    index = 26,
    label = "p_OH_CHO",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B} {7,S}
5    O u0 {1,S} {6,S}
6    H u0 {5,S}
7    C u0 {4,S} {8,D} {9,S}
8    O u0 {7,D}
9    H u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.38, -0.24, -0.07, 0.05, 0.22, 0.29, 0.36],'cal/(mol*K)'),
        H298 = (-1.10,'kcal/mol'),
        S298 = (-0.19,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""
""",
)

entry(
    index = 27,
    label = "p_MeO_CHO",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B} {7,S}
5    O u0 {1,S} {6,S}
6    C u0 {5,S} {10,S} {11,S} {12,S}
7    C u0 {4,S} {8,D} {9,S}
8    O u0 {7,D}
9    H u0 {7,S}
10   H u0 {6,S}
11   H u0 {6,S}
12   H u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.38, -0.24, -0.07, 0.05, 0.22, 0.29, 0.36],'cal/(mol*K)'),
        H298 = (-1.10,'kcal/mol'),
        S298 = (-0.19,'cal/(mol*K)'),
    ),
    shortDesc = u"""This is NNI correction from Ince & Reyniers, AIChE 2015, DOI 10.1002/aic.15008""",
    longDesc = 
u"""
""",
)


tree(
"""
L1: R
    L2: aromatic-para
        L3: p_OH
            L4: p_OH_OH
            L4: p_OH_MeO
            L4: p_OH_CHO
        L3: p_MeO
            L4: p_MeO_MeO
            L4: p_MeO_CHO
        L3: p_CHO
            L4: p_CHO_CHO
"""
)
