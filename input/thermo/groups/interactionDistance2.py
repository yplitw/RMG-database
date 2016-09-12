#!/usr/bin/env python
# encoding: utf-8

name = "Interaction Corrections with distance 2"
shortDesc = u""
longDesc = u"""

"""

entry(
    index = 0,
    label = "aromatic-meta",
    group = 
"""
1 *1 Cb u0 {2,B}
2    Cb u0 {1,B} {3,B}
3 *2 Cb u0 {2,B}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0,0,0,0,0,0,0],'cal/(mol*K)'),
        H298 = (0,'kcal/mol'),
        S298 = (0,'cal/(mol*K)'),
    ),
    shortDesc = u"""Root for Aromatics NNI correction""",
    longDesc = 
u"""

""",
)

entry(
    index = 20,
    label = "m_CHO_CHO",
    group = 
"""
1 *1 Cb u0 {2,B} {4,S}
2    Cb u0 {1,B} {3,B}
3 *2 Cb u0 {2,B} {7,S}
4    C  u0 {1,S} {5,D} {6,S}
5    O  u0 {4,D}
6    H  u0 {4,S}
7    C  u0 {3,S} {8,D} {9,S}
8    O  u0 {7,D}
9    H  u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.20, 0.12, 0.06, 0.01, -0.05, -0.08, -0.10],'cal/(mol*K)'),
        H298 = (0.57,'kcal/mol'),
        S298 = (0.01,'cal/(mol*K)'),
    ),
    shortDesc = u"""Half value. Aromatics NNI correction.""",
    longDesc = 
u"""
""",
)

entry(
    index = 19,
    label = "m_Oj_OCH3",
    group = 
"""
1 *1 Cb u0 {2,B} {4,S}
2    Cb u0 {1,B} {3,B}
3 *2 Cb u0 {2,B} {5,S}
4    O  u1 {1,S}
5    O  u0 {3,S} {6,S}
6    C  u0 {5,S} {7,S} {8,S} {9,S}
7    H  u0 {6,S}
8    H  u0 {6,S}
9    H  u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.22, 0.76, 0.98, 1.03, 0.81, 0.55, 0.22],'cal/(mol*K)'),
        H298 = (-1.65,'kcal/mol'),
        S298 = (-1.00,'cal/(mol*K)'),
    ),
    shortDesc = u"""NNI6. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
u"""
""",
)

entry(
    index = 20,
    label = "m_Oj_CHO",
    group = 
"""
1 *1 Cb u0 {2,B} {4,S}
2    Cb u0 {1,B} {3,B}
3 *2 Cb u0 {2,B} {5,S}
4    O  u1 {1,S}
5    C  u0 {3,S} {6,D} {7,S}
6    O  u0 {5,D}
7    H  u0 {5,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.38, -0.38, -0.38, -0.38, 0.29, 0.22, 0.12],'cal/(mol*K)'),
        H298 = (1.12,'kcal/mol'),
        S298 = (0.86,'cal/(mol*K)'),
    ),
    shortDesc = u"""NNI9. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
u"""
""",
)

entry(
    index = 21,
    label = "m_Cj=O_CHO",
    group = 
"""
1 *1 Cb u0 {2,B} {4,S}
2    Cb u0 {1,B} {3,B}
3 *2 Cb u0 {2,B} {6,S}
4    C  u1 {1,S} {5,D}
5    O  u0 {4,D}
6    C  u0 {3,S} {7,D} {8,S}
7    O  u0 {6,D}
8    H  u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.07, 0.17, 0.17, 0.12, 0.00, -0.07, 0.02],'cal/(mol*K)'),
        H298 = (1.10,'kcal/mol'),
        S298 = (0.81,'cal/(mol*K)'),
    ),
    shortDesc = u"""NNI17. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
u"""
""",
)

tree(
"""
L1: aromatic-meta
    L2: m_CHO_CHO
    L2: m_Oj_OCH3
    L2: m_Oj_CHO
    L2: m_Cj=O_CHO
"""
)
