# Perfect maze (tree) in a 60x60 grid
# Nodes: 616
# Edges: 615


adjList = [
	[25, 1],
    [47, 2, 0],
    [16, 3, 1],
    [2],
    [29, 5],
    [17, 4],
    [30, 7],
    [39, 6],
    [40, 9],
    [41, 8],
    [23, 11],
    [34, 12, 10],
    [11],
    [36, 14],
    [43, 15, 13],
    [14],
    [2],
    [37, 5, 18],
    [17],
    [38, 20],
    [69, 21, 19],
    [20],
    [42, 23],
    [74, 10, 22],
    [45, 25],
    [0, 24],
    [49, 27],
    [51, 26],
    [52, 29],
    [4, 28],
    [6, 31],
    [54, 30],
    [75, 33],
    [60, 32],
    [11],
    [55, 36],
    [13, 35],
    [17, 38],
    [19, 37],
    [7, 40],
    [59, 8, 39],
    [9, 42],
    [22, 41],
    [14, 44],
    [93, 43],
    [24, 46],
    [63, 45],
    [1, 48],
    [64, 47],
    [26, 50],
    [86, 49],
    [27, 52],
    [28, 51],
    [70, 54],
    [31, 53],
    [35, 56],
    [81, 55],
    [67],
    [98, 59],
    [40, 58],
    [33, 61],
    [80, 60],
    [133, 63],
    [46, 62],
    [48, 65],
    [85, 64],
    [87, 67],
    [57, 68, 66],
    [97, 67],
    [20, 70],
    [53, 69],
    [91, 72],
    [113, 71],
    [77],
    [23, 75],
    [32, 74],
    [99, 77],
    [73, 78, 76],
    [100, 77],
    [102],
    [61, 81],
    [56, 80],
    [134, 83],
    [94, 84, 82],
    [83],
    [65, 86],
    [50, 87, 85],
    [66, 86],
    [89],
    [110, 88],
    [111, 91],
    [71, 90],
    [120, 93],
    [44, 92],
    [83],
    [96],
    [128, 97, 95],
    [68, 96],
    [58, 99],
    [76, 98],
    [78, 101],
    [139, 102, 100],
    [79, 101],
    [118, 104],
    [119, 103],
    [122, 106],
    [123, 105],
    [124, 108],
    [125, 107],
    [158, 110],
    [89, 109],
    [90, 112],
    [185, 111],
    [72, 114],
    [148, 113],
    [159, 116],
    [138, 115],
    [140, 118],
    [103, 117],
    [104, 120],
    [92, 119],
    [143, 122],
    [105, 121],
    [106, 124],
    [107, 123],
    [108, 126],
    [154, 125],
    [155],
    [96, 129],
    [157, 128],
    [142, 131],
    [149, 130],
    [151],
    [62, 134],
    [82, 135, 133],
    [153, 134],
    [178, 137],
    [184, 136],
    [116, 139],
    [101, 138],
    [117, 141],
    [162, 140],
    [130],
    [121, 144],
    [163, 143],
    [146],
    [165, 145],
    [186, 148],
    [114, 147],
    [131, 150],
    [171, 151, 149],
    [223, 132, 150],
    [202, 153],
    [135, 152],
    [126, 155],
    [127, 154],
    [175, 157],
    [129, 158, 156],
    [109, 157],
    [115, 160],
    [159],
    [180, 162],
    [141, 161],
    [144, 164],
    [194, 165, 163],
    [146, 164],
    [187, 167],
    [188, 166],
    [201, 169],
    [190, 168],
    [191, 171],
    [150, 170],
    [203, 173],
    [204, 172],
    [183, 175],
    [156, 176, 174],
    [197, 175],
    [216, 178],
    [136, 177],
    [218, 180],
    [161, 179],
    [199, 182],
    [200, 181],
    [174],
    [137, 185],
    [112, 184],
    [147, 187],
    [166, 186],
    [167, 189],
    [217, 188],
    [169, 191],
    [170, 190],
    [205],
    [211, 194],
    [164, 193],
    [214, 196],
    [215, 195],
    [176],
    [240, 199],
    [181, 198],
    [182, 201],
    [168, 200],
    [152, 203],
    [172, 202],
    [173, 205],
    [234, 192, 204],
    [227, 207],
    [228, 206],
    [229, 209],
    [231, 208],
    [222],
    [193, 212],
    [236, 211],
    [237, 214],
    [195, 213],
    [196, 216],
    [177, 215],
    [189, 218],
    [179, 217],
    [232, 220],
    [248, 219],
    [249, 222],
    [210, 223, 221],
    [151, 222],
    [253, 225],
    [254, 224],
    [243, 227],
    [206, 226],
    [207, 229],
    [208, 228],
    [262, 231],
    [246, 209, 230],
    [219],
    [252],
    [205, 235],
    [255, 234],
    [212, 237],
    [213, 236],
    [258],
    [263, 240],
    [198, 241, 239],
    [271, 240],
    [268, 243],
    [226, 242],
    [270, 245],
    [244],
    [280, 231, 247],
    [246],
    [220, 249],
    [221, 250, 248],
    [284, 249],
    [285],
    [286, 233, 253],
    [224, 252],
    [225, 255],
    [235, 254],
    [266, 257],
    [275, 256],
    [276, 238, 259],
    [291, 258],
    [267],
    [278, 262],
    [230, 261],
    [239, 264],
    [296, 263],
    [266],
    [302, 256, 265],
    [260, 268],
    [293, 242, 267],
    [294, 270],
    [244, 269],
    [241, 272],
    [309, 271],
    [310, 274],
    [298, 273],
    [257, 276],
    [258, 275],
    [304, 278],
    [295, 261, 277],
    [280],
    [246, 281, 279],
    [280],
    [306, 283],
    [307, 282],
    [250, 285],
    [251, 284],
    [252, 287],
    [311, 286],
    [312, 289],
    [319, 288],
    [300],
    [259, 292],
    [315, 291],
    [268, 294],
    [321, 269, 293],
    [278],
    [308, 264, 297],
    [296],
    [274, 299],
    [317, 298],
    [290, 301],
    [335, 302, 300],
    [266, 301],
    [346, 304],
    [368, 277, 303],
    [323, 306],
    [282, 305],
    [283, 308],
    [296, 307],
    [272, 310],
    [273, 309],
    [287, 312],
    [288, 311],
    [331, 314],
    [313],
    [292, 316],
    [361, 315],
    [299, 318],
    [344, 317],
    [289, 320],
    [334, 319],
    [294],
    [347, 323],
    [305, 322],
    [350, 325],
    [351, 326, 324],
    [340, 325],
    [341, 328],
    [327],
    [332],
    [331],
    [358, 313, 330],
    [405, 329, 333],
    [354, 332],
    [320, 335],
    [301, 334],
    [359, 337],
    [360, 338, 336],
    [337],
    [349],
    [326, 341],
    [363, 327, 342, 340],
    [341],
    [364, 344],
    [318, 343],
    [366, 346],
    [303, 345],
    [322, 348],
    [370, 347],
    [339, 350],
    [324, 349],
    [325, 352],
    [373, 351],
    [374, 354],
    [333, 353],
    [376, 356],
    [377, 357, 355],
    [356],
    [379, 331, 359],
    [336, 358],
    [337, 361],
    [316, 360],
    [384, 363],
    [341, 362],
    [343, 365],
    [428, 364],
    [419, 345, 367],
    [399, 366],
    [304, 369],
    [383, 368],
    [348, 371],
    [390, 370],
    [391, 373],
    [352, 372],
    [353, 375],
    [386, 376, 374],
    [355, 375],
    [356, 378],
    [394, 377],
    [358, 380],
    [396, 379],
    [382],
    [417, 381],
    [369],
    [362, 385],
    [384],
    [375],
    [422, 388],
    [407, 387],
    [408, 390],
    [371, 389],
    [372, 392],
    [411, 391],
    [413, 394],
    [378, 393],
    [433, 396],
    [380, 395],
    [415, 398],
    [416, 397],
    [367, 400],
    [421, 399],
    [424, 402],
    [425, 401],
    [426, 404],
    [427, 403],
    [332, 406],
    [461, 405],
    [388, 408],
    [389, 407],
    [410],
    [435, 411, 409],
    [392, 410],
    [436, 413],
    [393, 412],
    [438, 415],
    [397, 414],
    [398, 417],
    [382, 418, 416],
    [453, 417],
    [366, 420],
    [440, 419],
    [400, 422],
    [387, 421],
    [458, 424],
    [401, 423],
    [402, 426],
    [403, 425],
    [404, 428],
    [365, 429, 427],
    [447, 428],
    [463, 431],
    [449, 430],
    [450, 433],
    [395, 432],
    [457, 435],
    [479, 410, 434],
    [412, 437],
    [462, 436],
    [414, 439],
    [466, 438],
    [420, 441],
    [474, 440],
    [443],
    [456, 442],
    [469, 445],
    [444],
    [481, 447],
    [429, 446],
    [460],
    [431, 450],
    [432, 449],
    [472],
    [473, 453],
    [418, 452],
    [475, 455],
    [476, 454],
    [477, 443, 457],
    [434, 456],
    [423, 459],
    [488, 458],
    [482, 448, 461],
    [406, 460],
    [437, 463],
    [430, 462],
    [494, 465],
    [495, 466, 464],
    [439, 465],
    [498, 468],
    [499, 467],
    [444, 470],
    [490, 469],
    [484],
    [451, 473],
    [452, 472],
    [441, 475],
    [454, 474],
    [455, 477],
    [500, 456, 476],
    [479],
    [435, 478],
    [504, 481],
    [446, 480],
    [460, 483],
    [542, 482],
    [507, 471, 485],
    [484],
    [493],
    [519, 488],
    [459, 487],
    [521, 490],
    [470, 489],
    [506],
    [508, 493],
    [486, 494, 492],
    [464, 493],
    [465, 496],
    [511, 495],
    [512, 498],
    [467, 497],
    [468, 500],
    [477, 499],
    [517, 502],
    [518, 501],
    [528, 504],
    [480, 503],
    [506],
    [529, 491, 505],
    [530, 484, 508],
    [492, 507],
    [532, 510],
    [543, 509],
    [496, 512],
    [524, 497, 511],
    [526],
    [533, 515],
    [535, 514],
    [537, 517],
    [501, 516],
    [502, 519],
    [487, 518],
    [521],
    [551, 489, 520],
    [541],
    [544],
    [512, 525],
    [547, 524],
    [548, 513, 527],
    [549, 526],
    [503, 529],
    [554, 506, 528],
    [507, 531],
    [557, 532, 530],
    [509, 531],
    [514, 534],
    [559, 533],
    [515, 536],
    [561, 535],
    [516, 538],
    [562, 537],
    [540],
    [550, 539],
    [578, 522, 542],
    [483, 541],
    [510, 544],
    [523, 543],
    [606, 546],
    [566, 545],
    [525, 548],
    [526, 547],
    [527],
    [573, 540, 551],
    [521, 552, 550],
    [551],
    [576, 554],
    [529, 553],
    [579, 556],
    [582, 555],
    [531],
    [580, 559],
    [534, 558],
    [561],
    [570, 536, 560],
    [538, 563],
    [592, 562],
    [585, 565],
    [586, 564],
    [546, 567],
    [597, 566],
    [589, 569],
    [609, 568],
    [561, 571],
    [590, 570],
    [573],
    [550, 574, 572],
    [599, 575, 573],
    [614, 574],
    [553, 577],
    [595, 576],
    [541, 579],
    [555, 578],
    [558, 581],
    [610, 580],
    [556, 583],
    [602, 582],
    [603, 585],
    [564, 584],
    [565, 587],
    [605, 586],
    [608, 589],
    [568, 588],
    [571, 591],
    [612, 590],
    [563, 593],
    [613, 592],
    [615, 595],
    [577, 594],
    [597],
    [607, 567, 596],
    [611],
    [574, 600],
    [599],
    [602],
    [583, 603, 601],
    [584, 602],
    [605],
    [587, 606, 604],
    [545, 605],
    [597, 608],
    [588, 607],
    [569, 610],
    [581, 609],
    [598, 612],
    [591, 613, 611],
    [593, 612],
    [575, 615],
    [594, 614]]




# x coord, y coord
nodeData = [
	(3, 1),
    (5, 1),
    (7, 1),
    (14, 1),
    (18, 1),
    (20, 1),
    (31, 1),
    (36, 1),
    (38, 1),
    (40, 1),
    (44, 1),
    (51, 1),
    (52, 1),
    (56, 1),
    (58, 1),
    (59, 1),
    (7, 2),
    (20, 2),
    (22, 2),
    (25, 2),
    (27, 2),
    (28, 2),
    (42, 2),
    (44, 2),
    (1, 3),
    (3, 3),
    (10, 3),
    (14, 3),
    (16, 3),
    (18, 3),
    (31, 3),
    (34, 3),
    (46, 3),
    (48, 3),
    (51, 3),
    (53, 3),
    (56, 3),
    (20, 4),
    (25, 4),
    (36, 4),
    (38, 4),
    (40, 4),
    (42, 4),
    (58, 4),
    (60, 4),
    (1, 5),
    (3, 5),
    (5, 5),
    (7, 5),
    (10, 5),
    (12, 5),
    (14, 5),
    (16, 5),
    (30, 5),
    (34, 5),
    (53, 5),
    (57, 5),
    (18, 6),
    (36, 6),
    (38, 6),
    (48, 6),
    (52, 6),
    (1, 7),
    (3, 7),
    (7, 7),
    (9, 7),
    (14, 7),
    (18, 7),
    (24, 7),
    (27, 7),
    (30, 7),
    (32, 7),
    (34, 7),
    (41, 7),
    (44, 7),
    (46, 7),
    (38, 8),
    (41, 8),
    (42, 8),
    (48, 8),
    (52, 8),
    (57, 8),
    (3, 9),
    (5, 9),
    (6, 9),
    (9, 9),
    (12, 9),
    (14, 9),
    (27, 9),
    (28, 9),
    (30, 9),
    (32, 9),
    (58, 9),
    (60, 9),
    (5, 10),
    (17, 10),
    (22, 10),
    (24, 10),
    (36, 10),
    (38, 10),
    (42, 10),
    (44, 10),
    (48, 10),
    (50, 10),
    (55, 10),
    (8, 11),
    (10, 11),
    (12, 11),
    (14, 11),
    (26, 11),
    (28, 11),
    (30, 11),
    (32, 11),
    (34, 12),
    (37, 12),
    (39, 12),
    (42, 12),
    (47, 12),
    (50, 12),
    (55, 12),
    (58, 12),
    (6, 13),
    (8, 13),
    (10, 13),
    (12, 13),
    (14, 13),
    (17, 13),
    (19, 13),
    (22, 13),
    (24, 13),
    (51, 13),
    (54, 13),
    (60, 13),
    (1, 14),
    (3, 14),
    (4, 14),
    (28, 14),
    (30, 14),
    (42, 14),
    (44, 14),
    (47, 14),
    (49, 14),
    (51, 14),
    (6, 15),
    (8, 15),
    (12, 15),
    (14, 15),
    (34, 15),
    (37, 15),
    (54, 15),
    (58, 15),
    (60, 15),
    (2, 16),
    (4, 16),
    (17, 16),
    (19, 16),
    (21, 16),
    (24, 16),
    (26, 16),
    (39, 16),
    (41, 16),
    (45, 16),
    (49, 16),
    (8, 17),
    (13, 17),
    (14, 17),
    (36, 17),
    (38, 17),
    (52, 17),
    (54, 17),
    (56, 17),
    (58, 17),
    (4, 18),
    (6, 18),
    (16, 18),
    (21, 18),
    (24, 18),
    (26, 18),
    (28, 18),
    (43, 18),
    (45, 18),
    (48, 18),
    (50, 18),
    (16, 19),
    (30, 19),
    (32, 19),
    (34, 19),
    (36, 19),
    (38, 19),
    (40, 19),
    (54, 19),
    (56, 19),
    (8, 20),
    (10, 20),
    (13, 20),
    (18, 20),
    (20, 20),
    (24, 20),
    (46, 20),
    (48, 20),
    (50, 20),
    (52, 20),
    (2, 21),
    (4, 21),
    (6, 21),
    (8, 21),
    (29, 21),
    (32, 21),
    (34, 21),
    (38, 21),
    (57, 21),
    (10, 22),
    (13, 22),
    (15, 22),
    (18, 22),
    (20, 22),
    (26, 22),
    (40, 22),
    (43, 22),
    (50, 22),
    (52, 22),
    (54, 22),
    (57, 22),
    (60, 22),
    (4, 23),
    (6, 23),
    (27, 23),
    (29, 23),
    (32, 23),
    (34, 23),
    (36, 23),
    (38, 23),
    (50, 23),
    (1, 24),
    (8, 24),
    (11, 24),
    (13, 24),
    (15, 24),
    (18, 24),
    (43, 24),
    (46, 24),
    (48, 24),
    (25, 25),
    (27, 25),
    (30, 25),
    (31, 25),
    (38, 25),
    (40, 25),
    (52, 25),
    (54, 25),
    (58, 25),
    (60, 25),
    (1, 26),
    (4, 26),
    (6, 26),
    (11, 26),
    (14, 26),
    (16, 26),
    (18, 26),
    (20, 26),
    (22, 26),
    (34, 26),
    (36, 26),
    (43, 26),
    (46, 26),
    (13, 27),
    (14, 27),
    (22, 27),
    (25, 27),
    (28, 27),
    (30, 27),
    (48, 27),
    (50, 27),
    (52, 27),
    (55, 27),
    (16, 28),
    (18, 28),
    (32, 28),
    (34, 28),
    (37, 28),
    (38, 28),
    (39, 28),
    (42, 28),
    (44, 28),
    (58, 28),
    (60, 28),
    (1, 29),
    (3, 29),
    (5, 29),
    (7, 29),
    (9, 29),
    (20, 29),
    (22, 29),
    (25, 29),
    (28, 29),
    (34, 29),
    (46, 29),
    (47, 29),
    (55, 29),
    (57, 29),
    (9, 30),
    (12, 30),
    (14, 30),
    (30, 30),
    (32, 30),
    (37, 30),
    (42, 30),
    (44, 30),
    (46, 30),
    (50, 30),
    (52, 30),
    (3, 31),
    (5, 31),
    (16, 31),
    (19, 31),
    (22, 31),
    (25, 31),
    (57, 31),
    (60, 31),
    (7, 32),
    (9, 32),
    (28, 32),
    (35, 32),
    (37, 32),
    (41, 32),
    (43, 32),
    (50, 32),
    (52, 32),
    (54, 32),
    (1, 33),
    (15, 33),
    (16, 33),
    (1, 34),
    (7, 34),
    (9, 34),
    (12, 34),
    (18, 34),
    (20, 34),
    (22, 34),
    (39, 34),
    (50, 34),
    (52, 34),
    (54, 34),
    (56, 34),
    (60, 34),
    (28, 35),
    (30, 35),
    (35, 35),
    (37, 35),
    (39, 35),
    (41, 35),
    (43, 35),
    (47, 35),
    (4, 36),
    (7, 36),
    (9, 36),
    (11, 36),
    (12, 36),
    (16, 36),
    (18, 36),
    (20, 36),
    (25, 36),
    (49, 36),
    (52, 36),
    (56, 36),
    (59, 36),
    (28, 37),
    (30, 37),
    (32, 37),
    (34, 37),
    (37, 37),
    (42, 37),
    (44, 37),
    (47, 37),
    (4, 38),
    (5, 38),
    (9, 38),
    (11, 38),
    (13, 38),
    (16, 38),
    (18, 38),
    (22, 38),
    (25, 38),
    (34, 38),
    (49, 38),
    (55, 38),
    (5, 39),
    (36, 39),
    (38, 39),
    (40, 39),
    (42, 39),
    (44, 39),
    (47, 39),
    (8, 40),
    (13, 40),
    (16, 40),
    (18, 40),
    (20, 40),
    (22, 40),
    (30, 40),
    (32, 40),
    (50, 40),
    (52, 40),
    (55, 40),
    (57, 40),
    (1, 41),
    (3, 41),
    (38, 41),
    (40, 41),
    (43, 41),
    (45, 41),
    (47, 41),
    (5, 42),
    (8, 42),
    (18, 42),
    (20, 42),
    (22, 42),
    (25, 42),
    (26, 42),
    (28, 42),
    (30, 42),
    (32, 42),
    (36, 42),
    (48, 42),
    (50, 42),
    (52, 42),
    (55, 42),
    (57, 42),
    (59, 42),
    (60, 42),
    (10, 43),
    (12, 43),
    (14, 43),
    (16, 43),
    (43, 43),
    (45, 43),
    (5, 44),
    (8, 44),
    (18, 44),
    (20, 44),
    (30, 44),
    (33, 44),
    (40, 44),
    (41, 44),
    (52, 44),
    (55, 44),
    (58, 44),
    (60, 44),
    (1, 45),
    (12, 45),
    (14, 45),
    (22, 45),
    (24, 45),
    (26, 45),
    (35, 45),
    (37, 45),
    (41, 45),
    (43, 45),
    (48, 45),
    (50, 45),
    (1, 46),
    (3, 46),
    (8, 46),
    (10, 46),
    (15, 46),
    (17, 46),
    (20, 46),
    (27, 46),
    (30, 46),
    (52, 46),
    (54, 46),
    (6, 47),
    (22, 47),
    (24, 47),
    (33, 47),
    (35, 47),
    (37, 47),
    (41, 47),
    (44, 47),
    (45, 47),
    (56, 47),
    (58, 47),
    (1, 48),
    (3, 48),
    (6, 48),
    (7, 48),
    (12, 48),
    (48, 48),
    (50, 48),
    (52, 48),
    (54, 48),
    (60, 48),
    (10, 49),
    (12, 49),
    (15, 49),
    (17, 49),
    (20, 49),
    (24, 49),
    (27, 49),
    (30, 49),
    (41, 49),
    (44, 49),
    (46, 49),
    (54, 50),
    (56, 50),
    (59, 50),
    (60, 50),
    (6, 51),
    (10, 51),
    (13, 51),
    (15, 51),
    (20, 51),
    (24, 51),
    (28, 51),
    (33, 51),
    (37, 51),
    (41, 51),
    (44, 51),
    (46, 51),
    (48, 51),
    (51, 51),
    (52, 51),
    (1, 52),
    (18, 52),
    (24, 52),
    (26, 52),
    (28, 52),
    (30, 52),
    (54, 52),
    (60, 52),
    (6, 53),
    (10, 53),
    (13, 53),
    (33, 53),
    (35, 53),
    (37, 53),
    (39, 53),
    (41, 53),
    (43, 53),
    (46, 53),
    (49, 53),
    (1, 54),
    (3, 54),
    (15, 54),
    (18, 54),
    (20, 54),
    (22, 54),
    (26, 54),
    (28, 54),
    (30, 54),
    (49, 54),
    (52, 54),
    (55, 54),
    (58, 54),
    (60, 54),
    (5, 55),
    (7, 55),
    (10, 55),
    (33, 55),
    (35, 55),
    (38, 55),
    (39, 55),
    (43, 55),
    (45, 55),
    (13, 56),
    (16, 56),
    (22, 56),
    (25, 56),
    (29, 56),
    (31, 56),
    (39, 56),
    (41, 56),
    (48, 56),
    (49, 56),
    (50, 56),
    (55, 56),
    (58, 56),
    (60, 56),
    (1, 57),
    (5, 57),
    (33, 57),
    (36, 57),
    (7, 58),
    (9, 58),
    (11, 58),
    (13, 58),
    (16, 58),
    (18, 58),
    (27, 58),
    (29, 58),
    (41, 58),
    (43, 58),
    (45, 58),
    (47, 58),
    (58, 58),
    (60, 58),
    (23, 59),
    (25, 59),
    (38, 59),
    (50, 59),
    (52, 59),
    (2, 60),
    (9, 60),
    (11, 60),
    (15, 60),
    (18, 60),
    (20, 60),
    (25, 60),
    (27, 60),
    (31, 60),
    (36, 60),
    (38, 60),
    (43, 60),
    (47, 60),
    (55, 60),
    (58, 60)]
