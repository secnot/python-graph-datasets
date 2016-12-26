# Maze in a 45x45 grid
# Nodes: 375
# Edges: 404


adjList = [
    [16, 1],
    [17, 2, 0],
    [18, 3, 1],
    [2],
    [5],
    [20, 6, 4],
    [21, 5],
    [36, 8],
    [7],
    [24, 10],
    [31, 11, 9],
    [10],
    [26, 13],
    [43, 14, 12],
    [27, 13],
    [37, 16],
    [0, 15],
    [1, 18],
    [39, 2, 17],
    [47, 20],
    [5, 19],
    [6, 22],
    [34, 21],
    [40, 24],
    [9, 23],
    [41, 26],
    [12, 25],
    [14, 28],
    [46, 27],
    [56, 30],
    [49, 29],
    [10, 32],
    [51, 31],
    [53, 34],
    [22, 33],
    [63, 36],
    [7, 37, 35],
    [15, 36],
    [50, 39],
    [18, 40, 38],
    [23, 39],
    [52, 25, 42],
    [41],
    [13, 44],
    [62, 43],
    [67, 46],
    [28, 45],
    [19, 48],
    [70, 47],
    [30, 50],
    [74, 38, 49],
    [32, 52],
    [41, 51],
    [33, 54],
    [88, 53],
    [65, 56],
    [29, 55],
    [75, 58],
    [76, 57],
    [77],
    [95, 61],
    [66, 62, 60],
    [44, 61],
    [35, 64],
    [80, 65, 63],
    [71, 55, 64],
    [61],
    [45, 68],
    [84, 67],
    [85, 70],
    [86, 48, 69],
    [81, 65, 72],
    [89, 71],
    [74],
    [50, 75, 73],
    [91, 57, 74],
    [93, 58, 77],
    [59, 78, 76],
    [99, 77],
    [106, 80],
    [64, 79],
    [71],
    [132, 83],
    [100, 82],
    [68, 85],
    [69, 84],
    [70],
    [104, 88],
    [54, 87],
    [72, 90],
    [109, 89],
    [75, 92],
    [111, 93, 91],
    [76, 94, 92],
    [97, 93],
    [60, 96],
    [113, 95],
    [124, 94, 98],
    [125, 97],
    [78],
    [83, 101],
    [114, 100],
    [115, 103],
    [116, 102],
    [117, 87, 105],
    [129, 104],
    [79, 107],
    [119, 106],
    [120, 109],
    [90, 110, 108],
    [122, 111, 109],
    [123, 92, 110],
    [130, 113],
    [96, 112],
    [101, 115],
    [102, 114],
    [103, 117],
    [127, 104, 116],
    [137, 119],
    [138, 107, 120, 118],
    [108, 119],
    [140, 122],
    [110, 121],
    [111, 124],
    [97, 123],
    [98, 126],
    [145, 125],
    [117, 128],
    [148, 129, 127],
    [105, 128],
    [112, 131],
    [151, 130],
    [82, 133],
    [154, 132],
    [135],
    [147, 134],
    [157],
    [118, 138],
    [158, 119, 137],
    [173, 140],
    [121, 139],
    [160, 142],
    [179, 141],
    [176, 144],
    [143],
    [126, 146],
    [145],
    [156, 135, 148],
    [128, 149, 147],
    [171, 148],
    [164, 151],
    [165, 131, 150],
    [153],
    [167, 154, 152],
    [133, 155, 153],
    [169, 156, 154],
    [147, 155],
    [136, 158],
    [138, 157],
    [174, 160],
    [141, 159],
    [178, 162],
    [163, 161],
    [181, 162, 164],
    [150, 163],
    [151, 166],
    [184, 167, 165],
    [185, 153, 166],
    [209, 169],
    [155, 168],
    [194, 171],
    [149, 170],
    [187, 173],
    [139, 172],
    [189, 159, 175],
    [197, 174],
    [180, 143, 177],
    [191, 178, 176],
    [161, 177],
    [142, 180],
    [176, 179],
    [163, 182],
    [200, 181],
    [201, 184],
    [208, 166, 185, 183],
    [193, 167, 184],
    [203],
    [172, 188],
    [205, 187],
    [174],
    [199, 191],
    [177, 192, 190],
    [218, 191],
    [185],
    [170, 195],
    [211, 196, 194],
    [212, 195],
    [214, 175, 198],
    [215, 199, 197],
    [216, 190, 198],
    [182, 201],
    [183, 200],
    [210],
    [234, 186, 204],
    [235, 203],
    [188, 206],
    [221, 205],
    [226, 208],
    [184, 207],
    [168, 210],
    [230, 202, 209],
    [232, 195, 212],
    [196, 211],
    [222, 214],
    [197, 215, 213],
    [198, 214],
    [199, 217],
    [236, 216],
    [238, 192, 219],
    [239, 218],
    [231],
    [206, 222],
    [242, 213, 221],
    [243, 224],
    [244, 223],
    [268, 226],
    [207, 225],
    [247, 228],
    [250, 229, 227],
    [228],
    [210, 231],
    [253, 220, 230],
    [211, 233],
    [255, 232],
    [256, 203, 235],
    [240, 204, 234],
    [217, 237],
    [266, 238, 236],
    [218, 239, 237],
    [219, 238],
    [235, 241],
    [262, 240],
    [222, 243],
    [223, 242],
    [224, 245],
    [265, 244],
    [258, 247],
    [259, 227, 246],
    [267, 249],
    [277, 248],
    [228, 251],
    [270, 250],
    [271, 253],
    [231, 252],
    [279, 255],
    [233, 254],
    [234, 257],
    [273, 256],
    [269, 246, 259],
    [247, 260, 258],
    [291, 259],
    [274],
    [241, 263],
    [282, 262],
    [283, 265],
    [287, 245, 264],
    [237, 267],
    [248, 266],
    [225, 269],
    [258, 268],
    [251, 271],
    [293, 252, 272, 270],
    [278, 271],
    [257, 274],
    [261, 275, 273],
    [295, 274],
    [289, 277],
    [249, 276],
    [272],
    [254, 280],
    [326, 279],
    [296, 282],
    [263, 283, 281],
    [264, 282],
    [301, 285],
    [302, 284],
    [303, 287],
    [265, 288, 286],
    [304, 287],
    [276],
    [291],
    [260, 290],
    [307, 293],
    [308, 271, 292],
    [310],
    [275, 296],
    [314, 281, 295],
    [321, 298],
    [338, 297],
    [312],
    [315, 301],
    [284, 300],
    [285, 303],
    [286, 302],
    [288, 305],
    [319, 304],
    [322, 307],
    [292, 306],
    [293, 309],
    [325, 308],
    [294, 311],
    [346, 312, 310],
    [327, 299, 313, 311],
    [312],
    [296, 315],
    [300, 314],
    [317],
    [335, 318, 316],
    [336, 319, 317],
    [305, 318],
    [321],
    [367, 297, 320],
    [306, 323],
    [329, 322],
    [343, 325],
    [309, 326, 324],
    [345, 280, 325],
    [312, 328],
    [331, 327],
    [341, 323, 330],
    [342, 329],
    [357, 328, 332],
    [331],
    [348, 334],
    [349, 335, 333],
    [317, 334],
    [318, 337],
    [353, 336],
    [298, 339],
    [369, 338],
    [370, 341],
    [329, 340],
    [372, 330, 343],
    [324, 342],
    [356, 345],
    [374, 326, 344],
    [311, 347],
    [361, 346],
    [358, 333, 349],
    [334, 350, 348],
    [363, 349],
    [364, 352],
    [365, 351],
    [337, 354],
    [366, 353],
    [373, 356],
    [344, 355],
    [331, 358],
    [362, 348, 357],
    [368],
    [361],
    [347, 360],
    [358],
    [350, 364],
    [351, 365, 363],
    [352, 366, 364],
    [354, 367, 365],
    [321, 366],
    [359, 369],
    [339, 370, 368],
    [340, 369],
    [372],
    [342, 373, 371],
    [355, 372],
    [345]]




# x coord, y coord
nodeData = [
    (7, 1),
    (11, 1),
    (13, 1),
    (14, 1),
    (36, 1),
    (40, 1),
    (43, 1),
    (2, 2),
    (3, 2),
    (17, 2),
    (20, 2),
    (22, 2),
    (26, 2),
    (29, 2),
    (33, 2),
    (5, 3),
    (7, 3),
    (11, 3),
    (13, 3),
    (38, 3),
    (40, 3),
    (43, 3),
    (45, 3),
    (15, 4),
    (17, 4),
    (24, 4),
    (26, 4),
    (33, 4),
    (35, 4),
    (8, 5),
    (10, 5),
    (20, 5),
    (22, 5),
    (42, 5),
    (45, 5),
    (1, 6),
    (2, 6),
    (5, 6),
    (12, 6),
    (13, 6),
    (15, 6),
    (24, 6),
    (26, 6),
    (29, 6),
    (31, 6),
    (33, 6),
    (35, 6),
    (38, 6),
    (40, 6),
    (10, 7),
    (12, 7),
    (22, 7),
    (24, 7),
    (42, 7),
    (44, 7),
    (5, 8),
    (8, 8),
    (14, 8),
    (17, 8),
    (19, 8),
    (27, 8),
    (29, 8),
    (31, 8),
    (1, 9),
    (3, 9),
    (5, 9),
    (29, 9),
    (33, 9),
    (36, 9),
    (38, 9),
    (40, 9),
    (5, 10),
    (8, 10),
    (11, 10),
    (12, 10),
    (14, 10),
    (17, 10),
    (19, 10),
    (24, 10),
    (1, 11),
    (3, 11),
    (5, 11),
    (31, 11),
    (33, 11),
    (36, 11),
    (38, 11),
    (40, 11),
    (42, 11),
    (44, 11),
    (8, 12),
    (10, 12),
    (14, 12),
    (16, 12),
    (17, 12),
    (18, 12),
    (27, 12),
    (29, 12),
    (18, 13),
    (21, 13),
    (24, 13),
    (33, 13),
    (35, 13),
    (37, 13),
    (39, 13),
    (42, 13),
    (45, 13),
    (1, 14),
    (5, 14),
    (7, 14),
    (10, 14),
    (12, 14),
    (16, 14),
    (27, 15),
    (29, 15),
    (35, 15),
    (37, 15),
    (39, 15),
    (42, 15),
    (3, 16),
    (5, 16),
    (7, 16),
    (10, 16),
    (12, 16),
    (16, 16),
    (18, 16),
    (21, 16),
    (23, 16),
    (42, 16),
    (43, 16),
    (45, 16),
    (27, 17),
    (29, 17),
    (31, 17),
    (36, 17),
    (39, 17),
    (41, 17),
    (1, 18),
    (3, 18),
    (5, 18),
    (7, 18),
    (10, 18),
    (12, 18),
    (14, 18),
    (17, 18),
    (19, 18),
    (23, 18),
    (25, 18),
    (41, 18),
    (43, 18),
    (45, 18),
    (27, 19),
    (29, 19),
    (33, 19),
    (34, 19),
    (36, 19),
    (38, 19),
    (41, 19),
    (1, 20),
    (5, 20),
    (9, 20),
    (12, 20),
    (21, 20),
    (23, 20),
    (23, 21),
    (27, 21),
    (29, 21),
    (32, 21),
    (34, 21),
    (36, 21),
    (38, 21),
    (41, 21),
    (45, 21),
    (3, 22),
    (7, 22),
    (9, 22),
    (11, 22),
    (17, 22),
    (19, 22),
    (21, 22),
    (14, 23),
    (17, 23),
    (23, 23),
    (25, 23),
    (28, 23),
    (32, 23),
    (34, 23),
    (1, 24),
    (3, 24),
    (5, 24),
    (9, 24),
    (18, 24),
    (19, 24),
    (22, 24),
    (34, 24),
    (41, 24),
    (42, 24),
    (44, 24),
    (11, 25),
    (13, 25),
    (18, 25),
    (25, 25),
    (28, 25),
    (38, 25),
    (1, 26),
    (3, 26),
    (5, 26),
    (7, 26),
    (30, 26),
    (32, 26),
    (36, 26),
    (38, 26),
    (42, 26),
    (44, 26),
    (10, 27),
    (11, 27),
    (13, 27),
    (18, 27),
    (20, 27),
    (22, 27),
    (25, 27),
    (40, 27),
    (7, 28),
    (10, 28),
    (14, 28),
    (16, 28),
    (28, 28),
    (30, 28),
    (32, 28),
    (34, 28),
    (35, 28),
    (38, 28),
    (40, 28),
    (42, 28),
    (45, 28),
    (1, 29),
    (3, 29),
    (20, 29),
    (21, 29),
    (22, 29),
    (25, 29),
    (3, 30),
    (8, 30),
    (10, 30),
    (14, 30),
    (16, 30),
    (19, 30),
    (30, 30),
    (32, 30),
    (23, 31),
    (26, 31),
    (34, 31),
    (36, 31),
    (38, 31),
    (40, 31),
    (43, 31),
    (45, 31),
    (1, 32),
    (3, 32),
    (30, 32),
    (32, 32),
    (33, 32),
    (6, 33),
    (8, 33),
    (10, 33),
    (12, 33),
    (19, 33),
    (21, 33),
    (23, 33),
    (28, 33),
    (30, 33),
    (36, 33),
    (38, 33),
    (41, 33),
    (3, 34),
    (6, 34),
    (7, 34),
    (24, 34),
    (26, 34),
    (41, 34),
    (43, 34),
    (45, 34),
    (9, 35),
    (10, 35),
    (12, 35),
    (14, 35),
    (16, 35),
    (18, 35),
    (19, 35),
    (21, 35),
    (24, 35),
    (32, 35),
    (33, 35),
    (36, 35),
    (38, 35),
    (1, 36),
    (7, 36),
    (9, 36),
    (27, 36),
    (30, 36),
    (4, 37),
    (12, 37),
    (14, 37),
    (16, 37),
    (18, 37),
    (21, 37),
    (23, 37),
    (33, 37),
    (36, 37),
    (38, 37),
    (43, 37),
    (1, 38),
    (2, 38),
    (4, 38),
    (6, 38),
    (9, 39),
    (12, 39),
    (16, 39),
    (17, 39),
    (21, 39),
    (23, 39),
    (25, 39),
    (27, 39),
    (33, 39),
    (36, 39),
    (41, 39),
    (43, 39),
    (45, 39),
    (4, 40),
    (6, 40),
    (36, 40),
    (38, 40),
    (6, 41),
    (7, 41),
    (10, 41),
    (12, 41),
    (17, 41),
    (21, 41),
    (23, 41),
    (30, 41),
    (32, 41),
    (34, 41),
    (36, 41),
    (38, 41),
    (41, 41),
    (43, 41),
    (45, 41),
    (2, 43),
    (4, 43),
    (10, 43),
    (12, 43),
    (14, 43),
    (17, 43),
    (19, 43),
    (23, 43),
    (25, 43),
    (41, 43),
    (43, 43),
    (6, 44),
    (10, 44),
    (29, 44),
    (3, 45),
    (4, 45),
    (10, 45),
    (14, 45),
    (17, 45),
    (19, 45),
    (25, 45),
    (27, 45),
    (29, 45),
    (32, 45),
    (34, 45),
    (36, 45),
    (38, 45),
    (41, 45),
    (45, 45)]
