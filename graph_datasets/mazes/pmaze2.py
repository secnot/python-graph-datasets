# Perfect maze (tree) in a 40x40 grid
# Nodes: 260
# Edges: 259


adjList=[   
	[1],
    [9, 0],
    [24, 3],
    [11, 2],
    [12, 5],
    [14, 4],
    [7],
    [17, 8, 6],
    [19, 7],
    [22, 1, 10],
    [40, 9],
    [3, 12],
    [4, 13, 11],
    [12],
    [5, 15],
    [29, 14],
    [32, 17],
    [7, 16],
    [23, 19],
    [8, 20, 18],
    [30, 19],
    [31, 22],
    [9, 21],
    [18],
    [2, 25],
    [41, 24],
    [42, 27],
    [59, 26],
    [43, 29],
    [15, 28],
    [20, 31],
    [21, 30],
    [61, 16, 33],
    [45, 32],
    [46, 35],
    [47, 34],
    [49, 37],
    [50, 36],
    [39],
    [52, 40, 38],
    [10, 39],
    [25, 42],
    [26, 41],
    [28, 44],
    [43],
    [33, 46],
    [34, 45],
    [35, 48],
    [65, 49, 47],
    [36, 48],
    [37, 51],
    [67, 50],
    [39, 53],
    [70, 52],
    [57],
    [68, 56],
    [79, 55],
    [71, 54, 58],
    [57],
    [27, 60],
    [75, 59],
    [32, 62],
    [77, 61],
    [89, 64],
    [92, 63],
    [48, 66],
    [81, 65],
    [51, 68],
    [55, 67],
    [82, 70],
    [53, 69],
    [57, 72],
    [116, 73, 71],
    [84, 72],
    [85, 75],
    [60, 74],
    [77],
    [62, 76],
    [105, 79],
    [56, 78],
    [81],
    [90, 66, 80],
    [69, 83],
    [110, 82],
    [73, 85],
    [74, 84],
    [99, 87],
    [100, 86],
    [102, 89],
    [63, 88],
    [94, 81, 91],
    [90],
    [64, 93],
    [106, 92],
    [90],
    [108, 96],
    [109, 95],
    [98],
    [129, 99, 97],
    [86, 98],
    [87, 101],
    [112, 100],
    [88, 103],
    [113, 102],
    [114, 105],
    [78, 104],
    [93, 107],
    [122, 106],
    [95],
    [96, 110],
    [126, 83, 109],
    [112],
    [101, 113, 111],
    [103, 112],
    [139, 104, 115],
    [124, 114],
    [72, 117],
    [128, 116],
    [130, 119],
    [131, 118],
    [135, 121],
    [120],
    [107, 123],
    [138, 122],
    [115, 125],
    [147, 124],
    [110],
    [149, 128],
    [117, 127],
    [98, 130],
    [118, 129],
    [119, 132],
    [142, 131],
    [143],
    [144, 135],
    [120, 136, 134],
    [145, 135],
    [146, 138],
    [123, 137],
    [114, 140],
    [156, 139],
    [165, 142],
    [132, 141],
    [167, 133, 144],
    [134, 143],
    [136, 146],
    [137, 145],
    [125, 148],
    [161, 147],
    [127, 150],
    [162, 149],
    [163, 152],
    [164, 151],
    [189, 154],
    [158, 153],
    [156],
    [140, 157, 155],
    [170, 156],
    [174, 154, 159],
    [176, 158],
    [183, 161],
    [148, 160],
    [150, 163],
    [151, 162],
    [152, 165],
    [141, 164],
    [181, 167],
    [143, 166],
    [188],
    [170],
    [182, 157, 169],
    [178],
    [186, 173],
    [172],
    [158, 175],
    [196, 174],
    [159, 177],
    [191, 176],
    [215, 171, 179],
    [185, 178],
    [193, 181],
    [166, 180],
    [170],
    [160, 184],
    [209, 183],
    [197, 179, 186],
    [172, 185],
    [202, 188],
    [168, 189, 187],
    [153, 188],
    [204],
    [177, 192],
    [206, 191],
    [180, 194],
    [210, 193],
    [213, 196],
    [175, 195],
    [185, 198],
    [217, 197],
    [218, 200],
    [219, 199],
    [202],
    [187, 201],
    [223, 204],
    [214, 190, 203],
    [230, 206],
    [192, 205],
    [225, 208],
    [254, 209, 207],
    [184, 208],
    [194, 211],
    [228, 210],
    [226, 213],
    [195, 212],
    [204],
    [178, 216],
    [247, 215],
    [198, 218],
    [199, 217],
    [200, 220],
    [234, 219],
    [222],
    [237, 223, 221],
    [203, 222],
    [231, 225],
    [207, 224],
    [212, 227],
    [235, 226],
    [211, 229],
    [244, 228],
    [205, 231],
    [224, 230],
    [248],
    [255, 234],
    [220, 233],
    [227, 236],
    [259, 235],
    [249, 222, 238],
    [251, 237],
    [252, 240],
    [253, 239],
    [246],
    [256, 243],
    [257, 242],
    [229, 245],
    [258, 244],
    [241, 247],
    [216, 248, 246],
    [232, 247],
    [237, 250],
    [249],
    [238, 252],
    [239, 251],
    [240, 254],
    [208, 253],
    [233, 256],
    [242, 255],
    [243, 258],
    [245, 259, 257],
    [236, 258]]




# x coord, y coord
nodeData=[
	(31, 1),
    (38, 1),
    (1, 2),
    (4, 2),
    (7, 2),
    (12, 2),
    (16, 2),
    (23, 2),
    (28, 2),
    (38, 2),
    (40, 2),
    (4, 4),
    (7, 4),
    (9, 4),
    (12, 4),
    (14, 4),
    (17, 4),
    (23, 4),
    (26, 4),
    (28, 4),
    (30, 4),
    (32, 4),
    (38, 4),
    (26, 5),
    (1, 6),
    (3, 6),
    (6, 6),
    (8, 6),
    (11, 6),
    (14, 6),
    (30, 6),
    (32, 6),
    (17, 7),
    (19, 7),
    (22, 7),
    (24, 7),
    (27, 7),
    (29, 7),
    (35, 7),
    (37, 7),
    (40, 7),
    (3, 9),
    (6, 9),
    (11, 9),
    (15, 9),
    (19, 9),
    (22, 9),
    (24, 9),
    (25, 9),
    (27, 9),
    (29, 9),
    (31, 9),
    (37, 9),
    (40, 9),
    (1, 10),
    (33, 10),
    (36, 10),
    (1, 11),
    (5, 11),
    (8, 11),
    (12, 11),
    (17, 11),
    (19, 11),
    (21, 12),
    (23, 12),
    (25, 12),
    (29, 12),
    (31, 12),
    (33, 12),
    (38, 12),
    (40, 12),
    (1, 13),
    (2, 13),
    (5, 13),
    (8, 13),
    (12, 13),
    (15, 13),
    (19, 13),
    (34, 13),
    (36, 13),
    (27, 14),
    (29, 14),
    (38, 14),
    (40, 14),
    (5, 15),
    (8, 15),
    (12, 15),
    (15, 15),
    (19, 15),
    (21, 15),
    (29, 15),
    (30, 15),
    (23, 16),
    (25, 16),
    (29, 16),
    (36, 16),
    (38, 16),
    (5, 17),
    (6, 17),
    (12, 17),
    (15, 17),
    (17, 17),
    (19, 17),
    (21, 17),
    (32, 17),
    (34, 17),
    (25, 18),
    (28, 18),
    (36, 18),
    (38, 18),
    (40, 18),
    (13, 19),
    (17, 19),
    (21, 19),
    (32, 19),
    (34, 19),
    (2, 20),
    (4, 20),
    (8, 20),
    (10, 20),
    (22, 20),
    (25, 20),
    (28, 20),
    (30, 20),
    (34, 21),
    (37, 21),
    (40, 21),
    (2, 22),
    (4, 22),
    (6, 22),
    (8, 22),
    (10, 22),
    (15, 22),
    (17, 22),
    (19, 22),
    (22, 22),
    (25, 22),
    (28, 22),
    (30, 22),
    (32, 23),
    (34, 23),
    (13, 24),
    (15, 24),
    (17, 24),
    (19, 24),
    (25, 24),
    (28, 24),
    (37, 24),
    (40, 24),
    (2, 25),
    (4, 25),
    (6, 25),
    (10, 25),
    (22, 25),
    (24, 25),
    (31, 25),
    (34, 25),
    (36, 25),
    (24, 26),
    (29, 26),
    (38, 26),
    (40, 26),
    (4, 27),
    (6, 27),
    (10, 27),
    (13, 27),
    (15, 27),
    (17, 27),
    (20, 27),
    (35, 27),
    (36, 27),
    (1, 28),
    (7, 28),
    (9, 28),
    (24, 28),
    (26, 28),
    (29, 28),
    (32, 28),
    (1, 29),
    (3, 29),
    (11, 29),
    (15, 29),
    (36, 29),
    (38, 29),
    (40, 29),
    (3, 30),
    (7, 30),
    (18, 30),
    (20, 30),
    (22, 30),
    (30, 30),
    (32, 30),
    (34, 30),
    (11, 31),
    (13, 31),
    (23, 31),
    (26, 31),
    (3, 32),
    (5, 32),
    (7, 32),
    (9, 32),
    (16, 32),
    (18, 32),
    (28, 32),
    (30, 32),
    (32, 32),
    (34, 32),
    (37, 32),
    (39, 32),
    (40, 32),
    (13, 33),
    (15, 33),
    (19, 33),
    (23, 33),
    (30, 33),
    (1, 34),
    (3, 34),
    (5, 34),
    (7, 34),
    (9, 34),
    (12, 34),
    (25, 34),
    (26, 34),
    (28, 34),
    (34, 34),
    (37, 34),
    (19, 35),
    (21, 35),
    (15, 36),
    (18, 36),
    (32, 36),
    (34, 36),
    (6, 37),
    (8, 37),
    (12, 37),
    (21, 37),
    (24, 37),
    (26, 37),
    (30, 37),
    (35, 37),
    (37, 37),
    (1, 38),
    (13, 38),
    (15, 38),
    (18, 38),
    (20, 38),
    (1, 39),
    (3, 39),
    (6, 39),
    (26, 39),
    (27, 39),
    (30, 39),
    (35, 39),
    (37, 39),
    (39, 39),
    (8, 40),
    (13, 40),
    (15, 40),
    (20, 40),
    (24, 40)]
