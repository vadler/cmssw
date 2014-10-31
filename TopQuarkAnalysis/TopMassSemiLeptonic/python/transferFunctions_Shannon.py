import FWCore.ParameterSet.Config as cms

process = cms.PSet(

### Light Jets

UdcsJet = cms.PSet(

##         |eta| < 0.87

  Eta0 = cms.PSet(

#       E <  20 (Shannon:       E <  40)

    E0 = cms.PSet(
      params = cms.vdouble(-4.20454, 5.05465, 0.14965, -15.14236, 9.98744)
    ),

#  20 <= E <  30 (Shannon:       E <  40)

    E1 = cms.PSet(
      params = cms.vdouble(-4.20454, 5.05465, 0.14965, -15.14236, 9.98744)
    ),

#  30 <= E <  40 (Shannon:       E <  40)

    E2 = cms.PSet(
      params = cms.vdouble(-4.20454, 5.05465, 0.14965, -15.14236, 9.98744)
    ),

#  40 <= E <  50 (Shannon:  40 <= E <  50)

    E3 = cms.PSet(
      params = cms.vdouble(0.18188, 6.07481, 0.21449, -9.79929, 8.24822)
    ),

#  50 <= E <  60 (Shannon:  50 <= E <  60)

    E4 = cms.PSet(
      params = cms.vdouble(0.39177, 8.61794, 0.09012, -9.70501, 14.08675)
    ),

#  60 <= E <  70 (Shannon:  60 <= E <  70)

    E5 = cms.PSet(
      params = cms.vdouble(-0.84096, 6.31516, 1.48212, 0.25866, 12.32986)
    ),

#  70 <= E <  80 (Shannon:  70 <= E <  80)

    E6 = cms.PSet(
      params = cms.vdouble(-1.64559, 6.98284, 1.70523, 0.70077, 13.32173)
    ),

#  80 <= E <  90 (Shannon:  80 <= E <  90)

    E7 = cms.PSet(
      params = cms.vdouble(-1.43613, 8.17102, 0.86078, 1.52545, 15.71609)
    ),

#  90 <= E < 100 (Shannon:  90 <= E < 100)

    E8 = cms.PSet(
      params = cms.vdouble(-1.47950, 9.12235, 0.85154, 1.43915, 17.03359)
    ),

# 100 <= E < 120 (Shannon: 100 <= E < 125)

    E9 = cms.PSet(
      params = cms.vdouble(-1.72038, 10.69761, 0.62094, 1.36790, 19.74902)
    ),

# 120 <= E < 150 (Shannon: 125 <= E < 150)

    E10 = cms.PSet(
      params = cms.vdouble(-2.46924, 13.01808, 0.31826, 1.57421, 25.27662)
    ),

# 150 <= E < 200 (Shannon: 150 <= E < 200)

    E11 = cms.PSet(
      params = cms.vdouble(-4.02499, 13.50102, 0.86738, -0.93525, 23.75232)
    ),

# 200 <= E < 400 (Shannon: 200 <= E < 5000)

    E12 = cms.PSet(
      params = cms.vdouble(-10.67007, 40.60198, 3.42336, -5.34458, 19.07871)
    ),

# 300 <= E < 500 (Shannon: 200 <= E < 5000)

    E13 = cms.PSet(
      params = cms.vdouble(-10.67007, 40.60198, 3.42336, -5.34458, 19.07871)
    )

  ),


## 0.87  <= |eta| < 1.479

  Eta1 = cms.PSet(

#       E <  20 (Shannon:       E <  50)

    E0 = cms.PSet(
      params = cms.vdouble(-10.18912, 6.95865, 0.21289, -27.56040, 13.63945)
    ),

#  20 <= E <  30 (Shannon:       E <  50)

    E1 = cms.PSet(
      params = cms.vdouble(-10.18912, 6.95865, 0.21289, -27.56040, 13.63945)
    ),

#  30 <= E <  40 (Shannon:       E <  50)

    E2 = cms.PSet(
      params = cms.vdouble(-10.18912, 6.95865, 0.21289, -27.56040, 13.63945)
    ),

#  40 <= E <  50 (Shannon:       E <  50)

    E3 = cms.PSet(
      params = cms.vdouble(-10.18912, 6.95865, 0.21289, -27.56040, 13.63945)
    ),

#  50 <= E <  60 (Shannon:  50 <= E <  60)

    E4 = cms.PSet(
      params = cms.vdouble(-4.51038, 8.09564, 0.20643, -18.94812, 13.77890)
    ),

#  60 <= E <  70 (Shannon:  60 <= E <  70)

    E5 = cms.PSet(
      params = cms.vdouble(-1.60354, 9.68782, 0.24321, -16.76435, 13.57188)
    ),

#  70 <= E <  80 (Shannon:  70 <= E <  80)

    E6 = cms.PSet(
      params = cms.vdouble(-0.34205, 11.81646, 0.18510, -17.90728, 16.55040)
    ),

#  80 <= E <  90 (Shannon:  80 <= E <  90)

    E7 = cms.PSet(
      params = cms.vdouble(-35.46778, 8.09786, 18.36471, -1.16136, 14.89404)
    ),

#  90 <= E < 100 (Shannon:  90 <= E < 100)

    E8 = cms.PSet(
      params = cms.vdouble(-1.09042, 18.74484, 0.32006, -2.65728, 9.56680)
    ),

# 100 <= E < 120 (Shannon: 100 <= E < 125)

    E9 = cms.PSet(
      params = cms.vdouble(-1.09741, 15.68543, 0.45409, -1.20219, 26.91795)
    ),

# 120 <= E < 150 (Shannon: 125 <= E < 150)

    E10 = cms.PSet(
      params = cms.vdouble(2.37959, 30.11030, 1.93483, -3.34997, 17.31258)
    ),

# 150 <= E < 200 (Shannon: 150 <= E < 200)

    E11 = cms.PSet(
      params = cms.vdouble(-4.80616, 19.05093, 0.60804, 0.90921, 33.88476)
    ),

# 200 <= E < 400 (Shannon: 200 <= E < 5000)

    E12 = cms.PSet(
      params = cms.vdouble(-3.62144, 46.65183, 2.16143, -7.20150, 25.41298)
    ),

# 300 <= E < 500 (Shannon: 200 <= E < 5000)

    E13 = cms.PSet(
      params = cms.vdouble(-3.62144, 46.65183, 2.16143, -7.20150, 25.41298)
    )

  ),


## 1.479 <= |eta| < 2.5

  Eta2 = cms.PSet(

#       E <  20 (Shannon:       E < 100)

    E0 = cms.PSet(
      params = cms.vdouble(-39.08108, 23.65660, 3.65734, -11.88477, 14.54337)
    ),

#  20 <= E <  30 (Shannon:       E < 100)

    E1 = cms.PSet(
      params = cms.vdouble(-39.08108, 23.65660, 3.65734, -11.88477, 14.54337)
    ),

#  30 <= E <  40 (Shannon:       E < 100)

    E2 = cms.PSet(
      params = cms.vdouble(-39.08108, 23.65660, 3.65734, -11.88477, 14.54337)
    ),

#  40 <= E <  50 (Shannon:       E < 100)

    E3 = cms.PSet(
      params = cms.vdouble(-39.08108, 23.65660, 3.65734, -11.88477, 14.54337)
    ),

#  50 <= E <  60 (Shannon:       E < 100)

    E4 = cms.PSet(
      params = cms.vdouble(-39.08108, 23.65660, 3.65734, -11.88477, 14.54337)
    ),

#  60 <= E <  70 (Shannon:       E < 100)

    E5 = cms.PSet(
      params = cms.vdouble(-39.08108, 23.65660, 3.65734, -11.88477, 14.54337)
    ),

#  70 <= E <  80 (Shannon:       E < 100)

    E6 = cms.PSet(
      params = cms.vdouble(-39.08108, 23.65660, 3.65734, -11.88477, 14.54337)
    ),

#  80 <= E <  90 (Shannon:       E < 100)

    E7 = cms.PSet(
      params = cms.vdouble(-39.08108, 23.65660, 3.65734, -11.88477, 14.54337)
    ),

#  90 <= E < 100 (Shannon:       E < 100)

    E8 = cms.PSet(
      params = cms.vdouble(-39.08108, 23.65660, 3.65734, -11.88477, 14.54337)
    ),

# 100 <= E < 120 (Shannon: 100 <= E < 125)

    E9 = cms.PSet(
      params = cms.vdouble(-34.46691, 27.51067, 3.60007, -4.08569, 18.83242)
    ),

# 120 <= E < 150 (Shannon: 125 <= E < 150)

    E10 = cms.PSet(
      params = cms.vdouble(-53.72734, 33.77462, 10.74937, -5.93801, 25.22355)
    ),

# 150 <= E < 200 (Shannon: 150 <= E < 200)

    E11 = cms.PSet(
      params = cms.vdouble(-24.04790, 57.73109, 9.22596, -6.96886, 29.24629)
    ),

# 200 <= E < 400 (Shannon: 200 <= E < 5000)

    E12 = cms.PSet(
      params = cms.vdouble(-13.63476, 33.28022, 0.41350, -11.92008, 66.29067)
    ),

# 300 <= E < 500 (Shannon: 200 <= E < 5000)

    E13 = cms.PSet(
      params = cms.vdouble(-13.63476, 33.28022, 0.41350, -11.92008, 66.29067)
    )

  )

),



### b-Jets

BJet = cms.PSet(


##         |eta| < 0.87

  Eta0 = cms.PSet(

#       E <  20 (Shannon:       E <  40)

    E0 = cms.PSet(
      params = cms.vdouble(-2.27102, 4.50768, 0.13765, -11.50658, 8.70579)
    ),

#  20 <= E <  30 (Shannon:       E <  40)

    E1 = cms.PSet(
      params = cms.vdouble(-2.27102, 4.50768, 0.13765, -11.50658, 8.70579)
    ),

#  30 <= E <  40 (Shannon:       E <  40)

    E2 = cms.PSet(
      params = cms.vdouble(-2.27102, 4.50768, 0.13765, -11.50658, 8.70579)
    ),

#  40 <= E <  50 (Shannon:  40 <= E <  50)

    E3 = cms.PSet(
      params = cms.vdouble(0.95695, 6.27054, 0.17897, -7.76903, 9.53203)
    ),

#  50 <= E <  60 (Shannon:  50 <= E <  60)

    E4 = cms.PSet(
      params = cms.vdouble(0.93419, 9.00675, 0.03040, -23.80878, 9.39666)
    ),

#  60 <= E <  70 (Shannon:  60 <= E <  70)

    E5 = cms.PSet(
      params = cms.vdouble(-0.86380, 5.91444, 1.58724, 1.63954, 12.68738)
    ),

#  70 <= E <  80 (Shannon:  70 <= E <  80)

    E6 = cms.PSet(
      params = cms.vdouble(-1.51138, 7.52949, 0.78394, 3.62595, 15.48598)
    ),

#  80 <= E <  90 (Shannon:  80 <= E <  90)

    E7 = cms.PSet(
      params = cms.vdouble(-1.57821, 8.14017, 0.64002, 4.74699, 17.46932)
    ),

#  90 <= E < 100 (Shannon:  90 <= E < 100)

    E8 = cms.PSet(
      params = cms.vdouble(-1.58700, 9.59213, 0.48527, 6.49765, 19.79911)
    ),

# 100 <= E < 120 (Shannon: 100 <= E < 125)

    E9 = cms.PSet(
      params = cms.vdouble(-1.77745, 11.00485, 0.39746, 8.66217, 22.90547)
    ),

# 120 <= E < 150 (Shannon: 125 <= E < 150)

    E10 = cms.PSet(
      params = cms.vdouble(-2.15325, 12.51384, 0.31040, 10.55344, 28.51742)
    ),

# 150 <= E < 200 (Shannon: 150 <= E < 200)

    E11 = cms.PSet(
      params = cms.vdouble(-2.71514, 14.54195, 0.27037, 13.94783, 34.77923)
    ),

# 200 <= E < 400 (Shannon: 200 <= E < 5000)

    E12 = cms.PSet(
      params = cms.vdouble(-3.66999, 18.38016, 0.22435, 13.43166, 52.47518)
    ),

# 300 <= E < 500 (Shannon: 200 <= E < 5000)

    E13 = cms.PSet(
      params = cms.vdouble(-3.66999, 18.38016, 0.22435, 13.43166, 52.47518)
    )

  ),


## 0.87  <= |eta| < 1.479

  Eta1 = cms.PSet(

#       E <  20 (Shannon:       E <  50)

    E0 = cms.PSet(
      params = cms.vdouble(-5.89506, 5.40070, 0.2868, -17.37618, 9.70652)
    ),

#  20 <= E <  30 (Shannon:       E <  50)

    E1 = cms.PSet(
      params = cms.vdouble(-5.89506, 5.40070, 0.2868, -17.37618, 9.70652)
    ),

#  30 <= E <  40 (Shannon:       E <  50)

    E2 = cms.PSet(
      params = cms.vdouble(-5.89506, 5.40070, 0.2868, -17.37618, 9.70652)
    ),

#  40 <= E <  50 (Shannon:       E <  50)

    E3 = cms.PSet(
      params = cms.vdouble(-5.89506, 5.40070, 0.2868, -17.37618, 9.70652)
    ),

#  50 <= E <  60 (Shannon:  50 <= E <  60)

    E4 = cms.PSet(
      params = cms.vdouble(-1.48168, 6.80131, 0.23519, -14.47600, 10.94886)
    ),

#  60 <= E <  70 (Shannon:  60 <= E <  70)

    E5 = cms.PSet(
      params = cms.vdouble(0.70802, 9.17206, 0.21572, -13.98361, 12.57718)
    ),

#  70 <= E <  80 (Shannon:  70 <= E <  80)

    E6 = cms.PSet(
      params = cms.vdouble(-19.66318, 17.76051, 11.51395, 1.03156, 12.03286)
    ),

#  80 <= E <  90 (Shannon:  80 <= E <  90)

    E7 = cms.PSet(
      params = cms.vdouble(0.83719, 14.72050, 0.02620, -40.94210, 13.75291)
    ),

#  90 <= E < 100 (Shannon:  90 <= E < 100)

    E8 = cms.PSet(
      params = cms.vdouble(1.13895, 18.30911, 0.23090, -2.69347, 7.60538)
    ),

# 100 <= E < 120 (Shannon: 100 <= E < 125)

    E9 = cms.PSet(
      params = cms.vdouble(-2.87190, 11.34464, 1.58163, 3.44734, 22.84513)
    ),

# 120 <= E < 150 (Shannon: 125 <= E < 150)

    E10 = cms.PSet(
      params = cms.vdouble(-3.36564, 15.47452, 0.79342, 7.54415, 28.57433)
    ),

# 150 <= E < 200 (Shannon: 150 <= E < 200)

    E11 = cms.PSet(
      params = cms.vdouble(-3.80657, 18.59653, 0.52096, 11.61024, 36.31792)
    ),

# 200 <= E < 400 (Shannon: 200 <= E < 5000)

    E12 = cms.PSet(
      params = cms.vdouble(-5.17009, 24.17130, 0.38043, 18.28372, 51.72652)
    ),

# 300 <= E < 500 (Shannon: 200 <= E < 5000)

    E13 = cms.PSet(
      params = cms.vdouble(-5.17009, 24.17130, 0.38043, 18.28372, 51.72652)
    )

  ),


## 1.479 <= |eta| < 2.5

  Eta2 = cms.PSet(

#       E <  20 (Shannon:       E < 100)

    E0 = cms.PSet(
      params = cms.vdouble(-23.47922, 19.28557, 2.79780, -4.79352, 12.39335)
    ),

#  20 <= E <  30 (Shannon:       E < 100)

    E1 = cms.PSet(
      params = cms.vdouble(-23.47922, 19.28557, 2.79780, -4.79352, 12.39335)
    ),

#  30 <= E <  40 (Shannon:       E < 100)

    E2 = cms.PSet(
      params = cms.vdouble(-23.47922, 19.28557, 2.79780, -4.79352, 12.39335)
    ),

#  40 <= E <  50 (Shannon:       E < 100)

    E3 = cms.PSet(
      params = cms.vdouble(-23.47922, 19.28557, 2.79780, -4.79352, 12.39335)
    ),

#  50 <= E <  60 (Shannon:       E < 100)

    E4 = cms.PSet(
      params = cms.vdouble(-23.47922, 19.28557, 2.79780, -4.79352, 12.39335)
    ),

#  60 <= E <  70 (Shannon:       E < 100)

    E5 = cms.PSet(
      params = cms.vdouble(-23.47922, 19.28557, 2.79780, -4.79352, 12.39335)
    ),

#  70 <= E <  80 (Shannon:       E < 100)

    E6 = cms.PSet(
      params = cms.vdouble(-23.47922, 19.28557, 2.79780, -4.79352, 12.39335)
    ),

#  80 <= E <  90 (Shannon:       E < 100)

    E7 = cms.PSet(
      params = cms.vdouble(-23.47922, 19.28557, 2.79780, -4.79352, 12.39335)
    ),

#  90 <= E < 100 (Shannon:       E < 100)

    E8 = cms.PSet(
      params = cms.vdouble(-23.47922, 19.28557, 2.79780, -4.79352, 12.39335)
    ),

# 100 <= E < 120 (Shannon: 100 <= E < 125)

    E9 = cms.PSet(
      params = cms.vdouble(-26.24386, 26.22737, 4.73644, 0.98931, 18.23159)
    ),

# 120 <= E < 150 (Shannon: 125 <= E < 150)

    E10 = cms.PSet(
      params = cms.vdouble(0.77890, 24.97716, 0.06297, -42.45201, 32.09654)
    ),

# 150 <= E < 200 (Shannon: 150 <= E < 200)

    E11 = cms.PSet(
      params = cms.vdouble(0.33156, 37.31930, 0.53501, -2.84156, 21.16707)
    ),

# 200 <= E < 400 (Shannon: 200 <= E < 5000)

    E12 = cms.PSet(
      params = cms.vdouble(-10.36101, 32.58836, 0.64584, 6.87262, 65.24700)
    ),

# 300 <= E < 500 (Shannon: 200 <= E < 5000)

    E13 = cms.PSet(
      params = cms.vdouble(-10.36101, 32.58836, 0.64584, 6.87262, 65.24700)
    )

  )

)

)
