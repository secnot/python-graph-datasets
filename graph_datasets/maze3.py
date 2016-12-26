# Maze in a 50x50 grid
# Nodes: 456
# Edges: 490


adjList=
[   [35, 1],
    [18, 0],
    [15, 3],
    [22, 4, 2],
    [23, 5, 3],
    [24, 6, 4],
    [25, 5],
    [8],
    [43, 9, 7],
    [27, 8],
    [28, 11],
    [29, 10],
    [31],
    [32, 14],
    [33, 13],
    [2],
    [30],
    [18],
    [1, 17],
    [37, 20],
    [38, 19],
    [39, 22],
    [3, 21],
    [4, 24],
    [5, 23],
    [6, 26],
    [53, 25],
    [44, 9, 28],
    [10, 27],
    [11, 30],
    [46, 16, 29],
    [59, 12, 32],
    [13, 31],
    [14, 34],
    [48, 35, 33],
    [0, 34],
    [54, 37],
    [19, 36],
    [20, 39],
    [21, 38],
    [41],
    [58, 42, 40],
    [41],
    [79, 8, 44],
    [84, 27, 43],
    [46],
    [30, 45],
    [71, 48],
    [34, 49, 47],
    [61, 48],
    [62, 51],
    [74, 50],
    [66, 53],
    [26, 52],
    [36, 55],
    [76, 54],
    [64, 57],
    [90, 58, 56],
    [41, 57],
    [31, 60],
    [81, 59],
    [49, 62],
    [50, 61],
    [64],
    [88, 56, 63],
    [82, 66],
    [52, 65],
    [85, 68],
    [93, 67],
    [95, 70],
    [117, 69],
    [47, 72],
    [104, 71],
    [99, 74],
    [51, 73],
    [101, 76],
    [55, 75],
    [78],
    [91, 79, 77],
    [43, 78],
    [125, 81],
    [60, 80],
    [65, 83],
    [102, 82],
    [44, 85],
    [67, 84],
    [98],
    [121, 88],
    [64, 87],
    [108, 90],
    [57, 89],
    [78, 92],
    [111, 91],
    [68, 94],
    [115, 95, 93],
    [69, 94],
    [126, 97],
    [148, 96],
    [86, 99],
    [118, 73, 98],
    [101],
    [120, 75, 100],
    [83, 103],
    [124, 102],
    [72, 105],
    [128, 104],
    [129, 107],
    [131, 108, 106],
    [89, 109, 107],
    [108],
    [132, 111],
    [133, 92, 110],
    [113],
    [134, 112],
    [141, 115],
    [94, 116, 114],
    [142, 117, 115],
    [143, 70, 116],
    [99, 119],
    [135, 118],
    [136, 101, 121],
    [87, 122, 120],
    [154, 121],
    [138, 124],
    [103, 123],
    [80, 126],
    [96, 125],
    [149, 128],
    [105, 127],
    [106, 130],
    [146, 131, 129],
    [107, 130],
    [110, 133],
    [111, 134, 132],
    [139, 113, 133],
    [119, 136],
    [120, 135],
    [155, 138],
    [123, 137],
    [134, 140],
    [161, 141, 139],
    [114, 140],
    [116, 143],
    [181, 117, 142],
    [165],
    [151],
    [169, 130, 147],
    [170, 146],
    [97, 149],
    [127, 148],
    [151],
    [166, 145, 150],
    [153],
    [215, 154, 152],
    [122, 153],
    [171, 137, 156],
    [189, 157, 155],
    [174, 156],
    [175, 159],
    [176, 160, 158],
    [177, 161, 159],
    [140, 162, 160],
    [179, 163, 161],
    [180, 162],
    [182, 165],
    [144, 164],
    [173, 151, 167],
    [185, 166],
    [217, 169],
    [146, 168],
    [147, 171],
    [155, 170],
    [204, 173],
    [192, 166, 172],
    [157, 175],
    [194, 158, 174],
    [159, 177],
    [160, 176],
    [198, 179],
    [162, 178],
    [163, 181],
    [143, 180],
    [164, 183],
    [202, 184, 182],
    [183],
    [167, 186],
    [214, 185],
    [206, 188],
    [207, 189, 187],
    [156, 188],
    [197],
    [210, 192],
    [211, 173, 191],
    [205],
    [221, 175, 195],
    [222, 194],
    [224, 197],
    [190, 198, 196],
    [178, 197],
    [226, 200],
    [199],
    [258, 202],
    [228, 183, 201],
    [229, 204],
    [172, 203],
    [193, 206],
    [219, 187, 207, 205],
    [188, 208, 206],
    [234, 207],
    [220],
    [191, 211],
    [192, 212, 210],
    [247, 211],
    [230],
    [231, 186, 215],
    [232, 153, 214],
    [233, 217],
    [168, 218, 216],
    [250, 217],
    [206],
    [235, 209, 221],
    [194, 220],
    [195, 223],
    [242, 224, 222],
    [243, 196, 223],
    [226],
    [199, 227, 225],
    [245, 226],
    [259, 202, 229],
    [203, 228],
    [248, 213, 231],
    [214, 230],
    [249, 215, 233],
    [285, 216, 232],
    [239, 208, 235],
    [269, 220, 234],
    [263, 237],
    [260, 236],
    [252, 239],
    [234, 238],
    [254],
    [255, 242],
    [223, 243, 241],
    [224, 244, 242],
    [274, 245, 243],
    [276, 227, 244],
    [261, 247],
    [212, 246],
    [230, 249],
    [232, 248],
    [218, 251],
    [267, 250],
    [268, 238, 253],
    [278, 252],
    [240, 255],
    [241, 254],
    [272, 257],
    [273, 256],
    [330, 201, 259],
    [228, 258],
    [237, 261],
    [246, 260],
    [280, 263],
    [236, 262],
    [297, 265],
    [284, 264],
    [286, 267],
    [251, 266],
    [252],
    [235, 270],
    [288, 269],
    [310, 272],
    [256, 271],
    [257, 274],
    [244, 273],
    [292, 276],
    [245, 275],
    [296],
    [253, 279],
    [299, 278],
    [262, 281],
    [301, 280],
    [283],
    [303, 284, 282],
    [265, 285, 283],
    [233, 284],
    [266, 287],
    [306, 286],
    [308, 270, 289],
    [309, 288],
    [311, 291],
    [290],
    [275, 293],
    [313, 294, 292],
    [314, 293],
    [302, 296],
    [277, 297, 295],
    [264, 296],
    [320, 299],
    [279, 298],
    [321, 301],
    [281, 302, 300],
    [315, 295, 301],
    [318, 283, 304],
    [303],
    [333, 306],
    [287, 305],
    [325, 308],
    [337, 288, 307],
    [289, 310],
    [271, 309],
    [327, 290, 312],
    [328, 313, 311],
    [293, 314, 312],
    [294, 313],
    [323, 302, 316],
    [343, 315],
    [318],
    [362, 303, 317],
    [335, 320],
    [298, 319],
    [300, 322],
    [342, 323, 321],
    [315, 322],
    [346, 325],
    [347, 307, 324],
    [349, 327],
    [350, 311, 326],
    [312, 329],
    [370, 328],
    [258, 331],
    [353, 330],
    [363, 333],
    [305, 332],
    [335],
    [319, 336, 334],
    [357, 335],
    [367, 308, 338],
    [337],
    [340],
    [372, 339],
    [358, 342],
    [359, 322, 341],
    [316, 344],
    [360, 345, 343],
    [361, 344],
    [324, 347],
    [366, 325, 346],
    [368, 349],
    [326, 348],
    [327, 351],
    [369, 350],
    [431, 353],
    [374, 331, 352],
    [383, 355],
    [376, 354],
    [377, 357],
    [336, 356],
    [341, 359],
    [342, 360, 358],
    [390, 344, 359],
    [345, 362],
    [318, 361],
    [332, 364],
    [382, 363],
    [409, 366],
    [347, 365],
    [337, 368],
    [348, 367],
    [351, 370],
    [329, 369],
    [396, 372],
    [397, 340, 371],
    [404, 374],
    [353, 375, 373],
    [386, 374],
    [355, 377],
    [392, 356, 376],
    [412, 379],
    [394, 378],
    [399, 381],
    [400, 380],
    [364, 383],
    [354, 382],
    [410, 385],
    [411, 384],
    [375, 387],
    [406, 386],
    [407, 389],
    [408, 390, 388],
    [360, 389],
    [421, 392],
    [377, 393, 391],
    [403, 392],
    [379, 395],
    [415, 394],
    [429, 371, 397],
    [372, 396],
    [437, 399],
    [380, 398],
    [381, 401],
    [418, 402, 400],
    [420, 401],
    [393],
    [373, 405],
    [433, 404],
    [387, 407],
    [388, 406],
    [389],
    [365, 410],
    [384, 409],
    [385, 412],
    [378, 411],
    [441],
    [427, 415],
    [395, 414],
    [425],
    [438],
    [401, 419],
    [442, 418],
    [402, 421],
    [391, 420],
    [443, 423],
    [444, 424, 422],
    [451, 425, 423],
    [416, 426, 424],
    [425],
    [414, 428],
    [454, 427],
    [396, 430],
    [455, 429],
    [352],
    [445, 433],
    [405, 432],
    [446, 435],
    [447, 434],
    [448, 437],
    [398, 436],
    [449, 417, 439],
    [450, 438],
    [452, 441],
    [453, 413, 440],
    [419, 443],
    [422, 444, 442],
    [423, 443],
    [432, 446],
    [434, 445],
    [435, 448],
    [436, 449, 447],
    [438, 448],
    [439],
    [424, 452],
    [440, 451],
    [441, 454],
    [428, 455, 453],
    [430, 454]]




# x coord, y coord
nodeData=
[   (8, 1),
    (13, 1),
    (16, 1),
    (26, 1),
    (28, 1),
    (30, 1),
    (33, 1),
    (37, 1),
    (39, 1),
    (41, 1),
    (44, 1),
    (46, 1),
    (1, 2),
    (4, 2),
    (6, 2),
    (16, 2),
    (49, 2),
    (11, 3),
    (13, 3),
    (19, 3),
    (22, 3),
    (24, 3),
    (26, 3),
    (28, 3),
    (30, 3),
    (33, 3),
    (36, 3),
    (41, 3),
    (44, 3),
    (46, 3),
    (49, 3),
    (1, 4),
    (4, 4),
    (6, 4),
    (7, 4),
    (8, 4),
    (17, 5),
    (19, 5),
    (22, 5),
    (24, 5),
    (28, 5),
    (30, 5),
    (31, 5),
    (39, 5),
    (41, 5),
    (45, 5),
    (49, 5),
    (5, 6),
    (7, 6),
    (10, 6),
    (12, 6),
    (15, 6),
    (34, 6),
    (36, 6),
    (17, 7),
    (20, 7),
    (25, 7),
    (29, 7),
    (30, 7),
    (1, 8),
    (3, 8),
    (10, 8),
    (12, 8),
    (23, 8),
    (25, 8),
    (31, 8),
    (34, 8),
    (44, 8),
    (46, 8),
    (48, 8),
    (50, 8),
    (5, 9),
    (8, 9),
    (13, 9),
    (15, 9),
    (17, 9),
    (20, 9),
    (36, 9),
    (37, 9),
    (39, 9),
    (1, 10),
    (3, 10),
    (31, 10),
    (33, 10),
    (41, 10),
    (44, 10),
    (11, 11),
    (19, 11),
    (25, 11),
    (27, 11),
    (29, 11),
    (37, 11),
    (39, 11),
    (46, 11),
    (47, 11),
    (48, 11),
    (3, 12),
    (5, 12),
    (11, 12),
    (13, 12),
    (16, 12),
    (17, 12),
    (33, 12),
    (35, 12),
    (8, 13),
    (10, 13),
    (24, 13),
    (26, 13),
    (27, 13),
    (30, 13),
    (37, 13),
    (39, 13),
    (42, 13),
    (43, 13),
    (46, 13),
    (47, 13),
    (48, 13),
    (50, 13),
    (13, 14),
    (15, 14),
    (17, 14),
    (19, 14),
    (21, 14),
    (33, 14),
    (35, 14),
    (1, 15),
    (3, 15),
    (8, 15),
    (10, 15),
    (24, 15),
    (25, 15),
    (26, 15),
    (37, 15),
    (39, 15),
    (43, 15),
    (15, 16),
    (17, 16),
    (29, 16),
    (33, 16),
    (43, 16),
    (44, 16),
    (46, 16),
    (48, 16),
    (50, 16),
    (3, 17),
    (12, 17),
    (25, 17),
    (27, 17),
    (5, 18),
    (8, 18),
    (11, 18),
    (12, 18),
    (18, 18),
    (19, 18),
    (21, 18),
    (29, 18),
    (31, 18),
    (33, 18),
    (35, 18),
    (37, 18),
    (39, 18),
    (44, 18),
    (46, 18),
    (48, 18),
    (1, 19),
    (3, 19),
    (12, 19),
    (15, 19),
    (22, 19),
    (25, 19),
    (27, 19),
    (29, 19),
    (8, 20),
    (12, 20),
    (33, 20),
    (35, 20),
    (37, 20),
    (39, 20),
    (44, 20),
    (46, 20),
    (48, 20),
    (50, 20),
    (1, 21),
    (4, 21),
    (5, 21),
    (15, 21),
    (17, 21),
    (27, 21),
    (29, 21),
    (31, 21),
    (42, 21),
    (10, 22),
    (12, 22),
    (25, 22),
    (35, 22),
    (38, 22),
    (41, 22),
    (42, 22),
    (44, 22),
    (47, 22),
    (49, 22),
    (2, 23),
    (4, 23),
    (6, 23),
    (8, 23),
    (25, 23),
    (27, 23),
    (29, 23),
    (31, 23),
    (33, 23),
    (10, 24),
    (12, 24),
    (13, 24),
    (15, 24),
    (17, 24),
    (19, 24),
    (21, 24),
    (22, 24),
    (24, 24),
    (27, 24),
    (33, 24),
    (35, 24),
    (38, 24),
    (39, 24),
    (41, 24),
    (45, 24),
    (47, 24),
    (49, 24),
    (4, 25),
    (6, 25),
    (15, 25),
    (17, 25),
    (19, 25),
    (21, 25),
    (31, 25),
    (33, 25),
    (7, 26),
    (9, 26),
    (28, 26),
    (31, 26),
    (36, 26),
    (38, 26),
    (39, 26),
    (41, 26),
    (45, 26),
    (49, 26),
    (11, 27),
    (13, 27),
    (15, 27),
    (19, 27),
    (24, 28),
    (26, 28),
    (28, 28),
    (30, 28),
    (36, 28),
    (38, 28),
    (41, 28),
    (43, 28),
    (2, 29),
    (4, 29),
    (9, 29),
    (11, 29),
    (5, 30),
    (7, 30),
    (13, 30),
    (19, 30),
    (23, 30),
    (26, 30),
    (28, 30),
    (33, 30),
    (35, 30),
    (39, 30),
    (41, 30),
    (43, 30),
    (45, 30),
    (47, 30),
    (49, 30),
    (10, 31),
    (30, 31),
    (32, 31),
    (5, 32),
    (7, 32),
    (16, 32),
    (17, 32),
    (19, 32),
    (21, 32),
    (23, 32),
    (25, 32),
    (35, 32),
    (37, 32),
    (42, 32),
    (43, 32),
    (47, 32),
    (48, 32),
    (50, 32),
    (9, 33),
    (10, 33),
    (13, 33),
    (29, 33),
    (32, 33),
    (5, 34),
    (7, 34),
    (9, 34),
    (17, 34),
    (18, 34),
    (21, 34),
    (25, 34),
    (33, 34),
    (35, 34),
    (37, 34),
    (39, 34),
    (42, 34),
    (44, 34),
    (48, 34),
    (50, 34),
    (9, 35),
    (11, 35),
    (14, 35),
    (17, 35),
    (27, 35),
    (29, 35),
    (5, 36),
    (8, 36),
    (9, 36),
    (31, 36),
    (33, 36),
    (40, 36),
    (42, 36),
    (44, 36),
    (46, 36),
    (2, 37),
    (4, 37),
    (19, 37),
    (21, 37),
    (24, 37),
    (27, 37),
    (29, 37),
    (35, 37),
    (36, 37),
    (49, 37),
    (50, 37),
    (6, 38),
    (8, 38),
    (11, 38),
    (12, 38),
    (15, 38),
    (31, 38),
    (33, 38),
    (38, 38),
    (40, 38),
    (42, 38),
    (44, 38),
    (1, 39),
    (4, 39),
    (23, 39),
    (25, 39),
    (27, 39),
    (29, 39),
    (6, 40),
    (8, 40),
    (12, 40),
    (15, 40),
    (17, 40),
    (19, 40),
    (21, 40),
    (30, 40),
    (33, 40),
    (35, 40),
    (38, 40),
    (44, 40),
    (46, 40),
    (48, 40),
    (50, 40),
    (3, 41),
    (4, 41),
    (5, 41),
    (25, 41),
    (27, 41),
    (39, 41),
    (43, 41),
    (15, 42),
    (17, 42),
    (21, 42),
    (23, 42),
    (32, 42),
    (37, 42),
    (5, 43),
    (7, 43),
    (9, 43),
    (11, 43),
    (12, 43),
    (25, 43),
    (27, 43),
    (28, 43),
    (43, 43),
    (46, 43),
    (48, 43),
    (50, 43),
    (13, 44),
    (15, 44),
    (17, 44),
    (19, 44),
    (23, 44),
    (28, 44),
    (3, 45),
    (5, 45),
    (7, 45),
    (9, 45),
    (11, 45),
    (30, 45),
    (32, 45),
    (37, 45),
    (39, 45),
    (42, 45),
    (44, 45),
    (46, 45),
    (34, 46),
    (16, 47),
    (19, 47),
    (21, 47),
    (23, 47),
    (25, 47),
    (27, 47),
    (29, 47),
    (32, 47),
    (34, 47),
    (37, 47),
    (44, 47),
    (46, 47),
    (48, 47),
    (50, 47),
    (1, 48),
    (3, 48),
    (5, 48),
    (7, 48),
    (9, 48),
    (11, 48),
    (13, 48),
    (16, 48),
    (18, 48),
    (40, 48),
    (42, 48),
    (21, 49),
    (27, 49),
    (29, 49),
    (3, 50),
    (7, 50),
    (9, 50),
    (11, 50),
    (16, 50),
    (18, 50),
    (32, 50),
    (40, 50),
    (42, 50),
    (46, 50),
    (50, 50)]
