# Maze in a 75x75 grid
# Nodes: 968
# Edges: 1007


adjList = [
    [22],
    [52, 2],
    [24, 3, 1],
    [28, 2],
    [30],
    [59, 6],
    [60, 5],
    [31, 8],
    [35, 9, 7],
    [8],
    [48, 11],
    [38, 10],
    [39, 13],
    [50, 12],
    [67, 15],
    [40, 14],
    [41, 17],
    [43, 16],
    [72, 19],
    [44, 18],
    [45, 21],
    [47, 20],
    [51, 0, 23],
    [66, 22],
    [2, 25],
    [54, 24],
    [55, 27],
    [56, 26],
    [3],
    [75, 30],
    [58, 4, 29],
    [7, 32],
    [81, 31],
    [62, 34],
    [128, 33],
    [8, 36],
    [64, 35],
    [49, 38],
    [11, 39, 37],
    [12, 38],
    [15, 41],
    [16, 40],
    [70, 43],
    [17, 42],
    [19, 45],
    [20, 44],
    [74, 47],
    [21, 46],
    [65, 10, 49],
    [84, 37, 48],
    [13, 51],
    [22, 50],
    [1, 53],
    [78, 52],
    [25, 55],
    [26, 54],
    [27, 57],
    [92, 56],
    [30, 59],
    [5, 58],
    [6, 61],
    [80, 60],
    [33],
    [129, 64],
    [82, 36, 63],
    [48],
    [23, 67],
    [14, 66],
    [69],
    [88, 68],
    [42, 71],
    [106, 70],
    [18, 73],
    [95, 72],
    [46, 75],
    [29, 74],
    [102, 77],
    [76],
    [53, 79],
    [117, 78],
    [61, 81],
    [32, 80],
    [64],
    [111, 84],
    [49, 83],
    [134, 86],
    [112, 85],
    [113, 88],
    [69, 89, 87],
    [115, 88],
    [118, 91],
    [90],
    [57, 93],
    [121, 94, 92],
    [107, 93],
    [73, 96],
    [123, 95],
    [124, 98],
    [125, 97],
    [126, 100],
    [146, 99],
    [152, 102],
    [131, 76, 101],
    [132, 104],
    [133, 103],
    [138, 106],
    [71, 105],
    [94],
    [147, 109],
    [127, 108],
    [206, 111],
    [83, 110],
    [156, 86, 113],
    [87, 112],
    [137, 115],
    [89, 114],
    [140, 117],
    [79, 116],
    [90, 119],
    [169, 118],
    [158, 121],
    [93, 120],
    [143, 123],
    [96, 124, 122],
    [97, 123],
    [98, 126],
    [99, 125],
    [148, 109, 128],
    [149, 34, 127],
    [63, 130],
    [163, 129],
    [102, 132],
    [103, 131],
    [104, 134],
    [85, 133],
    [145],
    [164, 137],
    [114, 136],
    [105, 139],
    [191, 138],
    [116, 141],
    [168, 140],
    [201, 143],
    [122, 142],
    [145],
    [135, 146, 144],
    [100, 147, 145],
    [108, 146],
    [127, 149],
    [128, 150, 148],
    [181, 149],
    [152],
    [101, 151],
    [173, 154],
    [198, 153],
    [184, 156],
    [112, 155],
    [166],
    [120, 159],
    [200, 158],
    [196, 161],
    [175, 160],
    [182, 163],
    [130, 162],
    [136, 165],
    [188, 164],
    [189, 157, 167],
    [166],
    [141, 169],
    [193, 119, 168],
    [234, 171],
    [226, 170],
    [208, 173],
    [153, 172],
    [192],
    [161, 176],
    [202, 175],
    [203, 178],
    [224, 177],
    [225, 180],
    [233, 179],
    [150],
    [162, 183],
    [205, 182],
    [155, 185],
    [210, 184],
    [258, 187],
    [211, 186],
    [165, 189],
    [213, 166, 188],
    [214, 191],
    [139, 190],
    [216, 174, 193],
    [219, 169, 194, 192],
    [193],
    [244, 196],
    [160, 195],
    [228, 198],
    [154, 199, 197],
    [209, 198],
    [221, 159, 201],
    [142, 200],
    [176, 203],
    [177, 202],
    [255, 205],
    [256, 183, 204],
    [110, 207],
    [268, 208, 206],
    [172, 207],
    [235, 199, 210],
    [185, 209],
    [187, 212],
    [237, 213, 211],
    [189, 212],
    [190, 215],
    [240, 214],
    [230, 192, 217],
    [216],
    [250, 219],
    [193, 220, 218],
    [241, 219],
    [200],
    [273, 223],
    [245, 222],
    [178, 225],
    [179, 224],
    [171, 227],
    [279, 226],
    [197, 229],
    [248, 228],
    [216],
    [274, 232],
    [251, 231],
    [180, 234],
    [170, 233],
    [271, 209, 236],
    [294, 235],
    [212, 238],
    [237],
    [262, 240],
    [215, 239],
    [220, 242],
    [266, 241],
    [267, 244],
    [195, 243],
    [223],
    [269],
    [292, 248],
    [229, 247],
    [286, 250],
    [218, 249],
    [232, 252],
    [297, 253, 251],
    [276, 254, 252],
    [253],
    [204, 256],
    [281, 205, 255],
    [258],
    [186, 257],
    [296, 260],
    [282, 259],
    [283, 262],
    [239, 261],
    [285, 264],
    [306, 263],
    [266],
    [242, 267, 265],
    [243, 266],
    [207, 269],
    [246, 268],
    [304, 271],
    [235, 270],
    [273],
    [222, 274, 272],
    [231, 275, 273],
    [318, 274],
    [298, 253, 277],
    [299, 276],
    [300, 279],
    [227, 278],
    [319, 281],
    [256, 280],
    [260, 283],
    [261, 282],
    [329, 285],
    [263, 284],
    [249, 287],
    [308, 288, 286],
    [310, 287],
    [312, 290],
    [313, 289],
    [336, 292],
    [247, 291],
    [305, 294],
    [236, 293],
    [324, 296],
    [259, 295],
    [252, 298],
    [331, 276, 297],
    [277, 300],
    [278, 299],
    [333, 302],
    [334, 303, 301],
    [395, 302],
    [351, 270, 305],
    [321, 293, 304],
    [264, 307],
    [340, 306],
    [287, 309],
    [342, 308],
    [288, 311],
    [343, 312, 310],
    [289, 311],
    [290, 314],
    [345, 313],
    [346, 316],
    [347, 315],
    [318],
    [275, 317],
    [280, 320],
    [350, 319],
    [305, 322],
    [353, 321],
    [354, 324],
    [295, 323],
    [326],
    [366, 327, 325],
    [355, 326],
    [356, 329],
    [284, 328],
    [357, 331],
    [298, 330],
    [333],
    [301, 334, 332],
    [360, 302, 333],
    [413],
    [291, 337],
    [362, 336],
    [339],
    [381, 340, 338],
    [367, 307, 339],
    [342],
    [369, 309, 341],
    [370, 311, 344],
    [372, 343],
    [373, 314, 346],
    [315, 345],
    [316, 348],
    [375, 347],
    [396, 350],
    [320, 349],
    [304, 352],
    [378, 351],
    [322, 354],
    [363, 323, 353],
    [327, 356],
    [328, 355],
    [330, 358],
    [385, 357],
    [386, 360],
    [334, 359],
    [387, 362],
    [337, 361],
    [354, 364],
    [390, 363],
    [399, 366],
    [326, 365],
    [340, 368],
    [391, 367],
    [392, 342, 370],
    [343, 369],
    [438, 372],
    [344, 371],
    [345, 374],
    [373],
    [348, 376],
    [408, 375],
    [398, 378],
    [352, 377],
    [401, 380],
    [416, 381, 379],
    [339, 382, 380],
    [418, 381],
    [406, 384],
    [407, 383],
    [358, 386],
    [359, 385],
    [361, 388],
    [428, 387],
    [432, 390],
    [364, 389],
    [368, 392],
    [369, 391],
    [394],
    [425, 395, 393],
    [303, 394],
    [349, 397],
    [427, 396],
    [377],
    [365, 400],
    [434, 399],
    [379],
    [422],
    [439, 404],
    [440, 403],
    [441, 406],
    [383, 405],
    [384, 408],
    [376, 407],
    [410],
    [444, 411, 409],
    [423, 412, 410],
    [411],
    [477, 335, 414],
    [413],
    [472, 416],
    [436, 380, 415],
    [418],
    [382, 419, 417],
    [446, 418],
    [447, 421],
    [448, 422, 420],
    [402, 421],
    [411],
    [451, 425],
    [394, 424],
    [453, 427],
    [469, 397, 426],
    [388, 429],
    [456, 428],
    [457, 431],
    [430],
    [389, 433],
    [482, 432],
    [400, 435],
    [459, 434],
    [416],
    [449, 438],
    [371, 439, 437],
    [403, 438],
    [404, 441],
    [405, 440],
    [491, 443],
    [465, 444, 442],
    [410, 443],
    [446],
    [419, 447, 445],
    [420, 446],
    [421, 449],
    [476, 437, 448],
    [495, 451],
    [424, 452, 450],
    [496, 453, 451],
    [426, 452],
    [478, 455],
    [479, 454],
    [429, 457],
    [430, 456],
    [483, 459],
    [435, 458],
    [499, 461],
    [485, 460],
    [488, 463],
    [490, 462],
    [493, 465],
    [504, 443, 464],
    [522, 467],
    [494, 466],
    [507, 469],
    [427, 468],
    [514, 471],
    [470],
    [540, 415, 473],
    [498, 472],
    [475],
    [501, 476, 474],
    [449, 475],
    [509, 413, 478],
    [454, 477],
    [455, 480],
    [513, 479],
    [515, 482],
    [433, 481],
    [517, 458, 484],
    [539, 483],
    [461, 486],
    [500, 487, 485],
    [518, 486],
    [462, 489],
    [521, 488],
    [463, 491],
    [442, 490],
    [526, 493],
    [464, 492],
    [467, 495],
    [450, 494],
    [506, 452, 497],
    [496],
    [473, 499],
    [460, 498],
    [486],
    [475, 502],
    [501],
    [504],
    [528, 465, 503],
    [530, 506],
    [496, 505],
    [468, 508],
    [533, 507],
    [477, 510],
    [534, 509],
    [535, 512],
    [548, 511],
    [480, 514],
    [470, 515, 513],
    [537, 481, 514],
    [517],
    [483, 516],
    [487, 519],
    [544, 518],
    [551, 521],
    [489, 520],
    [466, 523],
    [547, 522],
    [525],
    [553, 524],
    [492, 527],
    [568, 526],
    [504],
    [555, 530],
    [505, 531, 529],
    [530],
    [558, 533],
    [583, 508, 532],
    [510, 535],
    [511, 534],
    [550, 537],
    [515, 538, 536],
    [574, 539, 537],
    [484, 538],
    [472, 541],
    [540],
    [564, 543],
    [565, 542],
    [519, 545],
    [575, 544],
    [570, 547],
    [523, 546],
    [512, 549],
    [597, 548],
    [536],
    [520, 552],
    [576, 551],
    [525, 554],
    [567, 553],
    [529, 556],
    [580, 555],
    [581, 558],
    [582, 532, 557],
    [593, 560],
    [572, 559],
    [626, 562],
    [601, 561],
    [602, 564],
    [542, 563],
    [543, 566],
    [587, 565],
    [579, 554, 568],
    [527, 569, 567],
    [617, 568],
    [546, 571],
    [590, 570],
    [560],
    [599, 574],
    [538, 573],
    [545, 576],
    [552, 577, 575],
    [608, 578, 576],
    [609, 579, 577],
    [610, 567, 578],
    [592, 556, 581],
    [557, 582, 580],
    [613, 558, 583, 581],
    [660, 533, 582],
    [596],
    [615, 586],
    [627, 585],
    [605, 566, 588],
    [653, 587],
    [618, 590],
    [571, 589],
    [619, 592],
    [580, 591],
    [559, 594],
    [634, 593],
    [635, 596],
    [584, 597, 595],
    [549, 596],
    [599],
    [623, 573, 600, 598],
    [624, 599],
    [562, 602],
    [563, 601],
    [628, 604],
    [652, 605, 603],
    [587, 604],
    [654, 607],
    [642, 606],
    [577, 609],
    [578, 608],
    [579, 611],
    [632, 610],
    [646, 613],
    [582, 612],
    [640, 615],
    [585, 614],
    [629],
    [569, 618],
    [589, 617],
    [591, 620],
    [619],
    [622],
    [648, 623, 621],
    [599, 622],
    [600, 625],
    [649, 626, 624],
    [561, 625],
    [586, 628],
    [603, 627],
    [616, 630],
    [656, 631, 629],
    [657, 632, 630],
    [611, 631],
    [661, 634],
    [594, 633],
    [595, 636],
    [663, 635],
    [691, 638],
    [637],
    [666, 640],
    [614, 641, 639],
    [672, 640],
    [607, 643],
    [674, 642],
    [715, 645],
    [667, 644],
    [612, 647],
    [659, 646],
    [622, 649],
    [680, 625, 648],
    [651],
    [681, 652, 650],
    [604, 651],
    [588, 654],
    [606, 653],
    [696, 656],
    [675, 630, 655],
    [631, 658],
    [678, 657],
    [686, 647, 660],
    [742, 583, 659],
    [727, 633, 662],
    [669, 661],
    [636, 664],
    [701, 663],
    [692, 666],
    [639, 665],
    [684, 645, 668],
    [685, 667],
    [687, 662, 670],
    [669],
    [705, 672],
    [641, 671],
    [695, 674],
    [643, 673],
    [656, 676],
    [713, 675],
    [697, 678],
    [658, 677],
    [703, 680],
    [649, 679],
    [651, 682],
    [708, 681],
    [684],
    [667, 683],
    [668, 686],
    [659, 685],
    [669, 688],
    [720, 687],
    [700],
    [702],
    [637, 692],
    [665, 691],
    [724],
    [709],
    [673, 696],
    [710, 655, 695],
    [677, 698],
    [714, 697],
    [728, 700],
    [689, 701, 699],
    [664, 700],
    [690, 703],
    [721, 679, 702],
    [773, 705],
    [671, 704],
    [731, 707],
    [733, 708, 706],
    [682, 709, 707],
    [694, 708],
    [696, 711],
    [710],
    [774, 713],
    [676, 712],
    [726, 698, 715],
    [644, 716, 714],
    [740, 715],
    [768, 718],
    [741, 717],
    [743, 720],
    [744, 688, 719],
    [703, 722],
    [745, 721],
    [747, 724],
    [730, 693, 723],
    [766, 726],
    [714, 725],
    [661],
    [699, 729],
    [780, 728],
    [748, 724, 731],
    [759, 706, 730],
    [760, 733],
    [707, 734, 732],
    [762, 733],
    [763, 736],
    [764, 735],
    [765, 738],
    [815, 737],
    [767, 740],
    [716, 739],
    [718, 742],
    [660, 741],
    [752, 719, 744],
    [753, 720, 743],
    [722, 746],
    [772, 745],
    [781, 723, 748],
    [758, 730, 747],
    [775, 750],
    [802, 749],
    [777, 752],
    [743, 751],
    [744],
    [798, 755],
    [779, 754],
    [800, 757],
    [805, 756],
    [748, 759],
    [731, 758],
    [732, 761],
    [784, 760],
    [734, 763],
    [735, 764, 762],
    [736, 765, 763],
    [737, 764],
    [725, 767],
    [791, 739, 766],
    [717, 769],
    [794, 768],
    [882],
    [772],
    [746, 773, 771],
    [704, 772],
    [712, 775],
    [749, 774],
    [777],
    [751, 778, 776],
    [796, 777],
    [755, 780],
    [729, 779],
    [809, 747, 782],
    [781],
    [812, 784],
    [761, 783],
    [786],
    [829, 787, 785],
    [813, 786],
    [814, 789],
    [788],
    [835, 791],
    [818, 767, 792, 790],
    [819, 791],
    [820],
    [769, 795],
    [851, 794],
    [804, 778, 797],
    [822, 798, 796],
    [754, 797],
    [825, 800],
    [756, 799],
    [845, 802],
    [750, 801],
    [837, 804],
    [796, 803],
    [757, 806],
    [840, 805],
    [842, 808],
    [807],
    [877, 781, 810],
    [809],
    [861, 812],
    [826, 783, 811],
    [830, 787, 814],
    [831, 788, 813],
    [738, 816],
    [844, 815],
    [846, 818],
    [791, 817],
    [792, 820],
    [849, 793, 821, 819],
    [820],
    [797, 823],
    [854, 822],
    [825],
    [857, 799, 824],
    [812, 827],
    [862, 828, 826],
    [864, 829, 827],
    [786, 828],
    [813],
    [814, 832],
    [867, 833, 831],
    [868, 832],
    [870, 835],
    [790, 834],
    [837],
    [803, 838, 836],
    [852, 837],
    [875, 840],
    [806, 839],
    [859, 842],
    [807, 843, 841],
    [876, 842],
    [816, 845],
    [801, 844],
    [817, 847],
    [899, 846],
    [849],
    [873, 820, 848],
    [880, 851],
    [795, 850],
    [884, 838, 853],
    [852],
    [823, 855],
    [886, 854],
    [914, 857],
    [825, 858, 856],
    [874, 857],
    [841],
    [905, 861],
    [811, 860],
    [827, 863],
    [890, 862],
    [828, 865],
    [891, 864],
    [893, 867],
    [832, 868, 866],
    [833, 869, 867],
    [878, 868],
    [834, 871],
    [897, 872, 870],
    [898, 871],
    [849],
    [858, 875],
    [887, 839, 874],
    [843, 877],
    [809, 876],
    [909, 869, 879],
    [878],
    [850, 881],
    [912, 882, 880],
    [770, 881],
    [948, 884],
    [852, 883],
    [927, 886],
    [855, 885],
    [875, 888],
    [932, 887],
    [915, 890],
    [863, 889],
    [865, 892],
    [918, 893, 891],
    [866, 892],
    [895],
    [908, 894],
    [920, 897],
    [871, 898, 896],
    [872, 897],
    [847, 900],
    [924, 899],
    [929, 902],
    [930, 901],
    [956, 904],
    [934, 903],
    [860, 906],
    [936, 905],
    [917],
    [939, 895, 909],
    [878, 910, 908],
    [942, 909],
    [946, 912],
    [881, 911],
    [951, 914],
    [856, 913],
    [889, 916],
    [959, 915],
    [960, 907, 918],
    [892, 919, 917],
    [962, 918],
    [896, 921],
    [943, 920],
    [944, 923],
    [966, 922],
    [900, 925],
    [945, 924],
    [949, 927],
    [950, 885, 926],
    [952, 929],
    [953, 901, 928],
    [902, 931],
    [954, 930],
    [888, 933],
    [955, 932],
    [904, 935],
    [957, 934],
    [906, 937],
    [958, 936],
    [963, 939],
    [964, 908, 938],
    [947],
    [965],
    [910, 943],
    [921, 944, 942],
    [922, 943],
    [925, 946],
    [911, 947, 945],
    [940, 946],
    [883, 949],
    [926, 950, 948],
    [927, 951, 949],
    [913, 950],
    [928, 953],
    [929, 952],
    [931, 955],
    [933, 956, 954],
    [903, 955],
    [935, 958],
    [937, 957],
    [916, 960],
    [917, 959],
    [962],
    [919, 963, 961],
    [938, 962],
    [939, 965],
    [941, 964],
    [923, 967],
    [966]]




# x coord, y coord
nodeData = [
    (12, 1),
    (29, 1),
    (31, 1),
    (41, 1),
    (56, 1),
    (58, 1),
    (61, 1),
    (63, 1),
    (72, 1),
    (73, 1),
    (1, 2),
    (6, 2),
    (8, 2),
    (10, 2),
    (16, 2),
    (20, 2),
    (22, 2),
    (26, 2),
    (44, 2),
    (46, 2),
    (48, 2),
    (52, 2),
    (12, 3),
    (14, 3),
    (31, 3),
    (33, 3),
    (35, 3),
    (38, 3),
    (41, 3),
    (54, 3),
    (56, 3),
    (63, 3),
    (65, 3),
    (67, 3),
    (69, 3),
    (72, 3),
    (75, 3),
    (5, 4),
    (6, 4),
    (8, 4),
    (20, 4),
    (22, 4),
    (24, 4),
    (26, 4),
    (46, 4),
    (48, 4),
    (50, 4),
    (52, 4),
    (1, 5),
    (5, 5),
    (10, 5),
    (12, 5),
    (29, 5),
    (31, 5),
    (33, 5),
    (35, 5),
    (38, 5),
    (40, 5),
    (56, 5),
    (58, 5),
    (61, 5),
    (63, 5),
    (67, 5),
    (72, 5),
    (75, 5),
    (1, 6),
    (14, 6),
    (16, 6),
    (18, 6),
    (21, 6),
    (24, 6),
    (28, 6),
    (44, 6),
    (46, 6),
    (50, 6),
    (54, 6),
    (8, 7),
    (11, 7),
    (31, 7),
    (33, 7),
    (63, 7),
    (65, 7),
    (75, 7),
    (3, 8),
    (5, 8),
    (14, 8),
    (17, 8),
    (19, 8),
    (21, 8),
    (23, 8),
    (35, 8),
    (37, 8),
    (40, 8),
    (42, 8),
    (44, 8),
    (46, 8),
    (49, 8),
    (52, 8),
    (54, 8),
    (57, 8),
    (62, 8),
    (6, 9),
    (8, 9),
    (10, 9),
    (12, 9),
    (26, 9),
    (28, 9),
    (44, 9),
    (64, 9),
    (67, 9),
    (1, 10),
    (3, 10),
    (17, 10),
    (19, 10),
    (21, 10),
    (23, 10),
    (31, 10),
    (33, 10),
    (35, 10),
    (37, 10),
    (40, 10),
    (42, 10),
    (47, 10),
    (49, 10),
    (52, 10),
    (54, 10),
    (57, 10),
    (67, 10),
    (69, 10),
    (72, 10),
    (75, 10),
    (8, 11),
    (10, 11),
    (12, 11),
    (14, 11),
    (59, 11),
    (19, 12),
    (21, 12),
    (26, 12),
    (29, 12),
    (31, 12),
    (34, 12),
    (45, 12),
    (47, 12),
    (54, 12),
    (59, 12),
    (62, 12),
    (64, 12),
    (67, 12),
    (69, 12),
    (70, 12),
    (4, 13),
    (6, 13),
    (8, 13),
    (10, 13),
    (13, 13),
    (17, 13),
    (24, 13),
    (40, 13),
    (42, 13),
    (49, 13),
    (52, 13),
    (72, 13),
    (75, 13),
    (19, 14),
    (22, 14),
    (24, 14),
    (25, 14),
    (34, 14),
    (37, 14),
    (65, 14),
    (67, 14),
    (4, 15),
    (8, 15),
    (31, 15),
    (52, 15),
    (54, 15),
    (56, 15),
    (58, 15),
    (60, 15),
    (62, 15),
    (70, 15),
    (72, 15),
    (75, 15),
    (13, 16),
    (15, 16),
    (17, 16),
    (19, 16),
    (22, 16),
    (24, 16),
    (26, 16),
    (29, 16),
    (31, 16),
    (37, 16),
    (40, 16),
    (47, 16),
    (49, 16),
    (7, 17),
    (10, 17),
    (11, 17),
    (42, 17),
    (45, 17),
    (54, 17),
    (56, 17),
    (71, 17),
    (75, 17),
    (1, 18),
    (2, 18),
    (4, 18),
    (11, 18),
    (15, 18),
    (19, 18),
    (20, 18),
    (24, 18),
    (26, 18),
    (28, 18),
    (31, 18),
    (32, 18),
    (35, 18),
    (37, 18),
    (38, 18),
    (42, 18),
    (49, 18),
    (52, 18),
    (58, 18),
    (60, 18),
    (67, 18),
    (69, 18),
    (7, 19),
    (9, 19),
    (31, 19),
    (54, 19),
    (56, 19),
    (62, 19),
    (65, 19),
    (11, 20),
    (13, 20),
    (20, 20),
    (22, 20),
    (26, 20),
    (28, 20),
    (38, 20),
    (40, 20),
    (44, 20),
    (47, 20),
    (52, 20),
    (4, 21),
    (6, 21),
    (9, 21),
    (33, 21),
    (35, 21),
    (56, 21),
    (58, 21),
    (60, 21),
    (66, 21),
    (71, 21),
    (75, 21),
    (15, 22),
    (17, 22),
    (19, 22),
    (21, 22),
    (23, 22),
    (26, 22),
    (28, 22),
    (30, 22),
    (38, 22),
    (40, 22),
    (44, 22),
    (2, 23),
    (4, 23),
    (8, 23),
    (11, 23),
    (48, 23),
    (49, 23),
    (54, 23),
    (56, 23),
    (60, 23),
    (62, 23),
    (65, 23),
    (69, 23),
    (73, 23),
    (75, 23),
    (21, 24),
    (23, 24),
    (26, 24),
    (28, 24),
    (33, 24),
    (36, 24),
    (40, 24),
    (43, 24),
    (45, 24),
    (3, 25),
    (6, 25),
    (10, 25),
    (13, 25),
    (16, 25),
    (19, 25),
    (58, 25),
    (60, 25),
    (62, 25),
    (65, 25),
    (67, 25),
    (69, 25),
    (71, 25),
    (8, 26),
    (10, 26),
    (30, 26),
    (33, 26),
    (36, 26),
    (38, 26),
    (40, 26),
    (41, 26),
    (43, 26),
    (45, 26),
    (48, 26),
    (50, 26),
    (52, 26),
    (55, 26),
    (56, 26),
    (73, 26),
    (75, 26),
    (10, 27),
    (12, 27),
    (14, 27),
    (16, 27),
    (19, 27),
    (20, 27),
    (22, 27),
    (24, 27),
    (26, 27),
    (58, 27),
    (60, 27),
    (64, 27),
    (67, 27),
    (69, 27),
    (1, 28),
    (3, 28),
    (6, 28),
    (28, 28),
    (31, 28),
    (33, 28),
    (37, 28),
    (38, 28),
    (41, 28),
    (45, 28),
    (48, 28),
    (50, 28),
    (52, 28),
    (55, 28),
    (73, 28),
    (75, 28),
    (8, 29),
    (10, 29),
    (12, 29),
    (14, 29),
    (22, 29),
    (24, 29),
    (58, 29),
    (60, 29),
    (64, 29),
    (69, 29),
    (4, 30),
    (6, 30),
    (14, 30),
    (16, 30),
    (18, 30),
    (20, 30),
    (33, 30),
    (35, 30),
    (38, 30),
    (41, 30),
    (43, 30),
    (45, 30),
    (48, 30),
    (50, 30),
    (55, 30),
    (57, 30),
    (8, 31),
    (10, 31),
    (22, 31),
    (28, 31),
    (31, 31),
    (32, 31),
    (52, 31),
    (54, 31),
    (60, 31),
    (64, 31),
    (4, 32),
    (6, 32),
    (14, 32),
    (16, 32),
    (35, 32),
    (38, 32),
    (68, 32),
    (69, 32),
    (71, 32),
    (73, 32),
    (75, 32),
    (8, 33),
    (18, 33),
    (20, 33),
    (22, 33),
    (41, 33),
    (45, 33),
    (47, 33),
    (49, 33),
    (52, 33),
    (54, 33),
    (57, 33),
    (60, 33),
    (61, 33),
    (63, 33),
    (64, 33),
    (1, 34),
    (3, 34),
    (25, 34),
    (28, 34),
    (31, 34),
    (32, 34),
    (36, 34),
    (38, 34),
    (40, 34),
    (41, 34),
    (63, 34),
    (67, 34),
    (69, 34),
    (72, 34),
    (75, 34),
    (6, 35),
    (8, 35),
    (10, 35),
    (12, 35),
    (14, 35),
    (17, 35),
    (20, 35),
    (22, 35),
    (28, 35),
    (42, 35),
    (43, 35),
    (45, 35),
    (47, 35),
    (49, 35),
    (51, 35),
    (58, 35),
    (61, 35),
    (35, 36),
    (36, 36),
    (38, 36),
    (40, 36),
    (42, 36),
    (65, 36),
    (67, 36),
    (69, 36),
    (72, 36),
    (3, 37),
    (6, 37),
    (8, 37),
    (10, 37),
    (20, 37),
    (22, 37),
    (30, 37),
    (32, 37),
    (44, 37),
    (48, 37),
    (55, 37),
    (58, 37),
    (61, 37),
    (63, 37),
    (73, 37),
    (75, 37),
    (12, 38),
    (13, 38),
    (25, 38),
    (27, 38),
    (38, 38),
    (39, 38),
    (42, 38),
    (1, 39),
    (3, 39),
    (6, 39),
    (10, 39),
    (15, 39),
    (17, 39),
    (20, 39),
    (22, 39),
    (32, 39),
    (33, 39),
    (35, 39),
    (44, 39),
    (46, 39),
    (48, 39),
    (51, 39),
    (53, 39),
    (55, 39),
    (63, 39),
    (65, 39),
    (69, 39),
    (70, 39),
    (27, 40),
    (30, 40),
    (33, 40),
    (39, 40),
    (42, 40),
    (57, 40),
    (58, 40),
    (67, 40),
    (69, 40),
    (73, 40),
    (75, 40),
    (1, 41),
    (3, 41),
    (5, 41),
    (8, 41),
    (10, 41),
    (12, 41),
    (15, 41),
    (19, 41),
    (20, 41),
    (35, 41),
    (37, 41),
    (44, 41),
    (46, 41),
    (61, 41),
    (63, 41),
    (49, 42),
    (51, 42),
    (53, 42),
    (55, 42),
    (58, 42),
    (65, 42),
    (67, 42),
    (69, 42),
    (73, 42),
    (75, 42),
    (3, 43),
    (5, 43),
    (14, 43),
    (15, 43),
    (17, 43),
    (22, 43),
    (25, 43),
    (26, 43),
    (30, 43),
    (33, 43),
    (37, 43),
    (41, 43),
    (61, 43),
    (63, 43),
    (8, 44),
    (11, 44),
    (14, 44),
    (44, 44),
    (47, 44),
    (51, 44),
    (53, 44),
    (65, 44),
    (67, 44),
    (69, 44),
    (73, 44),
    (2, 45),
    (6, 45),
    (20, 45),
    (23, 45),
    (26, 45),
    (30, 45),
    (33, 45),
    (37, 45),
    (53, 45),
    (55, 45),
    (58, 45),
    (61, 45),
    (63, 45),
    (6, 46),
    (15, 46),
    (17, 46),
    (41, 46),
    (47, 46),
    (49, 46),
    (51, 46),
    (53, 46),
    (67, 46),
    (69, 46),
    (73, 46),
    (75, 46),
    (8, 47),
    (29, 47),
    (31, 47),
    (37, 47),
    (39, 47),
    (61, 47),
    (63, 47),
    (65, 47),
    (67, 47),
    (2, 48),
    (4, 48),
    (7, 48),
    (8, 48),
    (11, 48),
    (14, 48),
    (15, 48),
    (17, 48),
    (23, 48),
    (26, 48),
    (33, 48),
    (36, 48),
    (37, 48),
    (41, 48),
    (44, 48),
    (49, 48),
    (51, 48),
    (53, 48),
    (55, 48),
    (71, 48),
    (73, 48),
    (27, 49),
    (29, 49),
    (47, 49),
    (58, 49),
    (61, 49),
    (65, 49),
    (67, 49),
    (12, 50),
    (13, 50),
    (15, 50),
    (17, 50),
    (19, 50),
    (20, 50),
    (31, 50),
    (33, 50),
    (47, 50),
    (51, 50),
    (53, 50),
    (55, 50),
    (2, 51),
    (4, 51),
    (7, 51),
    (9, 51),
    (21, 51),
    (22, 51),
    (26, 51),
    (27, 51),
    (30, 51),
    (44, 51),
    (46, 51),
    (63, 51),
    (67, 51),
    (71, 51),
    (73, 51),
    (13, 52),
    (19, 52),
    (33, 52),
    (34, 52),
    (36, 52),
    (39, 52),
    (41, 52),
    (48, 52),
    (51, 52),
    (53, 52),
    (61, 52),
    (73, 52),
    (75, 52),
    (2, 53),
    (5, 53),
    (9, 53),
    (12, 53),
    (24, 53),
    (26, 53),
    (67, 53),
    (69, 53),
    (5, 54),
    (6, 54),
    (28, 54),
    (30, 54),
    (43, 54),
    (46, 54),
    (51, 54),
    (57, 54),
    (59, 54),
    (61, 54),
    (17, 55),
    (19, 55),
    (34, 55),
    (38, 55),
    (65, 55),
    (67, 55),
    (69, 55),
    (73, 55),
    (5, 56),
    (7, 56),
    (10, 56),
    (15, 56),
    (21, 56),
    (24, 56),
    (31, 56),
    (40, 56),
    (43, 56),
    (48, 56),
    (59, 56),
    (61, 56),
    (9, 57),
    (10, 57),
    (12, 57),
    (15, 57),
    (17, 57),
    (26, 57),
    (28, 57),
    (33, 57),
    (37, 57),
    (38, 57),
    (40, 57),
    (48, 57),
    (50, 57),
    (52, 57),
    (57, 57),
    (61, 57),
    (63, 57),
    (66, 57),
    (69, 57),
    (72, 57),
    (5, 58),
    (7, 58),
    (17, 58),
    (22, 58),
    (29, 58),
    (31, 58),
    (58, 58),
    (61, 58),
    (2, 59),
    (9, 59),
    (14, 59),
    (31, 59),
    (33, 59),
    (36, 59),
    (37, 59),
    (40, 59),
    (42, 59),
    (44, 59),
    (46, 59),
    (50, 59),
    (64, 59),
    (66, 59),
    (72, 59),
    (75, 59),
    (5, 60),
    (7, 60),
    (22, 60),
    (24, 60),
    (29, 60),
    (31, 60),
    (54, 60),
    (56, 60),
    (3, 61),
    (5, 61),
    (7, 61),
    (10, 61),
    (12, 61),
    (17, 61),
    (20, 61),
    (31, 61),
    (33, 61),
    (36, 61),
    (38, 61),
    (40, 61),
    (42, 61),
    (44, 61),
    (46, 61),
    (58, 61),
    (64, 61),
    (69, 61),
    (71, 61),
    (75, 61),
    (23, 62),
    (24, 62),
    (26, 62),
    (52, 62),
    (54, 62),
    (2, 63),
    (3, 63),
    (5, 63),
    (12, 63),
    (14, 63),
    (29, 63),
    (31, 63),
    (35, 63),
    (38, 63),
    (41, 63),
    (42, 63),
    (44, 63),
    (46, 63),
    (48, 63),
    (58, 63),
    (64, 63),
    (66, 63),
    (68, 63),
    (71, 63),
    (73, 63),
    (5, 64),
    (7, 64),
    (10, 64),
    (15, 64),
    (17, 64),
    (54, 64),
    (56, 64),
    (3, 65),
    (5, 65),
    (20, 65),
    (22, 65),
    (25, 65),
    (27, 65),
    (29, 65),
    (30, 65),
    (33, 65),
    (35, 65),
    (44, 65),
    (46, 65),
    (50, 65),
    (52, 65),
    (61, 65),
    (64, 65),
    (66, 65),
    (68, 65),
    (69, 65),
    (7, 66),
    (9, 66),
    (12, 66),
    (15, 66),
    (35, 66),
    (36, 66),
    (40, 66),
    (42, 66),
    (44, 66),
    (46, 66),
    (47, 66),
    (49, 66),
    (56, 66),
    (58, 66),
    (1, 67),
    (3, 67),
    (5, 67),
    (19, 67),
    (22, 67),
    (24, 67),
    (25, 67),
    (27, 67),
    (52, 67),
    (54, 67),
    (61, 67),
    (63, 67),
    (66, 67),
    (68, 67),
    (71, 67),
    (73, 67),
    (5, 68),
    (6, 68),
    (9, 68),
    (11, 68),
    (13, 68),
    (15, 68),
    (17, 68),
    (24, 68),
    (31, 68),
    (33, 68),
    (36, 68),
    (38, 68),
    (40, 68),
    (42, 68),
    (45, 68),
    (47, 68),
    (49, 68),
    (51, 68),
    (56, 68),
    (58, 68),
    (60, 68),
    (68, 68),
    (17, 69),
    (19, 69),
    (27, 69),
    (29, 69),
    (51, 69),
    (54, 69),
    (71, 69),
    (73, 69),
    (75, 69),
    (2, 70),
    (5, 70),
    (8, 70),
    (11, 70),
    (19, 70),
    (23, 70),
    (36, 70),
    (38, 70),
    (42, 70),
    (43, 70),
    (45, 70),
    (48, 70),
    (49, 70),
    (57, 70),
    (58, 70),
    (60, 70),
    (63, 70),
    (66, 70),
    (16, 71),
    (18, 71),
    (27, 71),
    (29, 71),
    (31, 71),
    (33, 71),
    (41, 71),
    (49, 71),
    (51, 71),
    (54, 71),
    (70, 71),
    (73, 71),
    (11, 72),
    (13, 72),
    (36, 72),
    (38, 72),
    (41, 72),
    (43, 72),
    (45, 72),
    (57, 72),
    (59, 72),
    (61, 72),
    (64, 72),
    (66, 72),
    (68, 72),
    (4, 73),
    (8, 73),
    (14, 73),
    (16, 73),
    (18, 73),
    (20, 73),
    (23, 73),
    (25, 73),
    (29, 73),
    (31, 73),
    (33, 73),
    (35, 73),
    (47, 73),
    (49, 73),
    (74, 73),
    (51, 74),
    (54, 74),
    (59, 74),
    (61, 74),
    (68, 74),
    (70, 74),
    (74, 74),
    (2, 75),
    (4, 75),
    (8, 75),
    (11, 75),
    (14, 75),
    (16, 75),
    (20, 75),
    (25, 75),
    (27, 75),
    (31, 75),
    (35, 75),
    (38, 75),
    (41, 75),
    (44, 75),
    (45, 75),
    (47, 75),
    (49, 75),
    (51, 75),
    (64, 75),
    (65, 75)]
