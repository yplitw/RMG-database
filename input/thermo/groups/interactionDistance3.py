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

entry(
    index = 23,
    label = "p_OCH2j",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B}
5    O  u0 {1,S} {6,S}
6    C  u1 {5,S} {7,S} {8,S}
7    H  u0 {6,S}
8    H  u0 {6,S}
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
    index = 23,
    label = "p_OCH2j_OH",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B} {9,S}
5    O  u0 {1,S} {6,S}
6    C  u1 {5,S} {7,S} {8,S}
7    H  u0 {6,S}
8    H  u0 {6,S}
9    O  u0 {4,S} {10,S}
10    H  u0 {9,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.10, -0.19, -0.43, -0.57, -0.65, -0.60, -0.33],'cal/(mol*K)'),
        H298 = (1.43,'kcal/mol'),
        S298 = (0.91,'cal/(mol*K)'),
    ),
    shortDesc = u"""NNI1. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
u"""
""",
)

entry(
    index = 24,
    label = "p_OCH2j_OCH3",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B} {9,S}
5    O  u0 {1,S} {6,S}
6    C  u1 {5,S} {7,S} {8,S}
7    H  u0 {6,S}
8    H  u0 {6,S}
9    O  u0 {4,S} {10,S}
10    C  u0 {9,S} {11,S} {12,S} {13,S}
11    H  u0 {10,S}
12    H  u0 {10,S}
13    H  u0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.10, -0.19, -0.43, -0.57, -0.65, -0.60, -0.33],'cal/(mol*K)'),
        H298 = (1.43,'kcal/mol'),
        S298 = (0.91,'cal/(mol*K)'),
    ),
    shortDesc = u"""NNI1. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
u"""
""",
)

entry(
    index = 25,
    label = "p_Oj",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B}
5    O  u1 {1,S}
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
    label = "p_Oj_OH",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B} {6,S}
5    O  u1 {1,S}
6    O  u0 {4,S} {7,S}
7    H  u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.67, -0.60, -0.45, -0.29, -0.02, 0.17, 0.38],'cal/(mol*K)'),
        H298 = (-3.78,'kcal/mol'),
        S298 = (-0.67,'cal/(mol*K)'),
    ),
    shortDesc = u"""NNI7. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
u"""
""",
)

entry(
    index = 26,
    label = "p_Oj_OCH3",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B} {6,S}
5    O  u1 {1,S}
6    O  u0 {4,S} {7,S}
7    C  u0 {6,S} {8,S} {9,S} {10,S}
8    H  u0 {7,S}
9    H  u0 {7,S}
10    H  u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.67, -0.60, -0.45, -0.29, -0.02, 0.17, 0.38],'cal/(mol*K)'),
        H298 = (-3.78,'kcal/mol'),
        S298 = (-0.67,'cal/(mol*K)'),
    ),
    shortDesc = u"""NNI7. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
u"""
""",
)

entry(
    index = 27,
    label = "p_Oj_C=C",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B} {6,S}
5    O  u1 {1,S}
6    C  u0 {4,S} {7,D} {8,S}
7    C  u0 {6,D} {9,S} {10,S}
8    H  u0 {6,S}
9    H  u0 {7,S}
10    H  u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.07, 0.05, 0.05, 0.12, 0.22, 0.29, 0.26],'cal/(mol*K)'),
        H298 = (-3.08,'kcal/mol'),
        S298 = (-0.72,'cal/(mol*K)'),
    ),
    shortDesc = u"""NNI11. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
u"""
""",
)

entry(
    index = 28,
    label = "p_Oj_Cs",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B} {6,S}
5    O  u1 {1,S}
6    C  u0 {4,S} {7,S} {8,S} {9,S}
7    H  u0 {6,S}
8    H  u0 {6,S}
9    [H,Cs]  u0 {6,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.17, -0.12, -0.10, -0.10, -0.07, -0.05, -0.05],'cal/(mol*K)'),
        H298 = (-1.39,'kcal/mol'),
        S298 = (0.07,'cal/(mol*K)'),
    ),
    shortDesc = u"""NNI13. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
u"""
""",
)

entry(
    index = 29,
    label = "p_Cj=O",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B}
5    C  u1 {1,S} {6,D}
6    O  u0 {5,D}
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
    index = 29,
    label = "p_Cj=O_OH",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B} {7,S}
5    C  u1 {1,S} {6,D}
6    O  u0 {5,D}
7    O  u0 {4,S} {8,S}
8    H  u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.79, -0.65, -0.48, -0.24, 0.05, 0.19, 0.36],'cal/(mol*K)'),
        H298 = (-2.06,'kcal/mol'),
        S298 = (-0.88,'cal/(mol*K)'),
    ),
    shortDesc = u"""NNI15. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
u"""
""",
)

entry(
    index = 30,
    label = "p_Cj=O_OCH3",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B} {7,S}
5    C  u1 {1,S} {6,D}
6    O  u0 {5,D}
7    O  u0 {4,S} {8,S}
8    C  u0 {7,S} {9,S} {10,S} {11,S}
9    H  u0 {8,S}
10    H  u0 {8,S}
11    H  u0 {8,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.79, -0.65, -0.48, -0.24, 0.05, 0.19, 0.36],'cal/(mol*K)'),
        H298 = (-2.06,'kcal/mol'),
        S298 = (-0.88,'cal/(mol*K)'),
    ),
    shortDesc = u"""NNI15. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
u"""
""",
)

entry(
    index = 31,
    label = "p_Cj=O_CHO",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B} {7,S}
5    C  u1 {1,S} {6,D}
6    O  u0 {5,D}
7    C  u0 {4,S} {8,D} {9,S}
8    O  u0 {7,D}
9    H  u0 {7,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.24, -0.57, -0.84, -0.98, -1.08, -1.03, -0.76],'cal/(mol*K)'),
        H298 = (1.29,'kcal/mol'),
        S298 = (3.25,'cal/(mol*K)'),
    ),
    shortDesc = u"""NNI18. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
u"""
""",
)

entry(
    index = 32,
    label = "p_Csj",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B}
5    C  u1 {1,S} {6,S} {7,S}
6    H  u0 {5,S}
7    [H,Cs]  u0 {5,S}
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
    index = 32,
    label = "p_Csj_C=C",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B} {8,S}
5    C  u1 {1,S} {6,S} {7,S}
6    H  u0 {5,S}
7    [H,Cs]  u0 {5,S}
8    C  u0 {4,S} {9,S} {10,D}
9    H  u0 {8,S}
10    C  u0 {8,D} {11,S} {12,S}
11    H  u0 {10,S}
12    H  u0 {10,S}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([0.22, 0.26, 0.29, 0.33, 0.38, 0.38, 0.31],'cal/(mol*K)'),
        H298 = (-1.39,'kcal/mol'),
        S298 = (-0.88,'cal/(mol*K)'),
    ),
    shortDesc = u"""NNI25. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
    longDesc = 
u"""
""",
)

entry(
    index = 33,
    label = "p_Csj_CHO",
    group = 
"""
1 *1 Cb u0 {2,B} {5,S}
2    Cb u0 {1,B} {3,B}
3    Cb u0 {2,B} {4,B}
4 *2 Cb u0 {3,B} {8,S}
5    C  u1 {1,S} {6,S} {7,S}
6    H  u0 {5,S}
7    [H,Cs]  u0 {5,S}
8    C  u0 {4,S} {9,S} {10,D}
9    H  u0 {8,S}
10    O  u0 {8,D}
""",
    thermo = ThermoData(
        Tdata = ([300,400,500,600,800,1000,1500],'K'),
        Cpdata = ([-0.29, -0.22, -0.14, -0.10, -0.07, -0.02, 0.07],'cal/(mol*K)'),
        H298 = (-1.24,'kcal/mol'),
        S298 = (0.14,'cal/(mol*K)'),
    ),
    shortDesc = u"""NNI27. This is NNI correction from Ince & Reyniers, AIChE 2016, reviewing""",
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
        L3: p_Oj
            L4: p_Oj_OH
            L4: p_Oj_OCH3
            L4: p_Oj_C=C
            L4: p_Oj_Cs
        L3: p_OCH2j
            L4: p_OCH2j_OH
            L4: p_OCH2j_OCH3
        L3: p_Cj=O
            L4: p_Cj=O_OH
            L4: p_Cj=O_OCH3
            L4: p_Cj=O_CHO
        L3: p_Csj
            L4: p_Csj_C=C
            L4: p_Csj_CHO
"""
)
