# Graph data from:
# http://mathematica.stackexchange.com/questions/28456/building-graph-based-on-the-cities-connection

adjList = [   
    [9, 23, 40, 8],
    [41, 16, 34, 22, 40, 23],
    [3, 30, 42, 31],
    [31, 35, 2],
    [42, 48, 30, 27, 14, 34],
    [37, 17, 32],
    [43, 18],
    [18, 36, 29],
    [9, 0],
    [8, 38, 25, 0, 40],
    [12, 46, 21, 39, 27, 22],
    [45, 35, 31, 42, 48, 24],
    [10, 46, 13, 15, 22],
    [33, 20, 12, 15],
    [34, 4, 22, 27],
    [12, 22, 40, 43, 47, 33, 13],
    [41, 23, 1],
    [44, 28, 32, 37, 5],
    [7, 36, 43, 47],
    [28],
    [13, 33, 46],
    [46, 10, 39, 26],
    [10, 27, 14, 34, 1, 40, 15, 12],
    [0, 16, 1, 40],
    [11, 48, 39, 26],
    [38, 43, 40, 9],
    [39, 21, 24],
    [14, 4, 48, 39, 10, 22],
    [19, 44, 17],
    [32, 36, 7],
    [41, 2, 4, 34],
    [3, 2, 42, 11, 35],
    [29, 44, 36, 17, 5],
    [13, 47, 36, 15, 20],
    [41, 4, 14, 30, 1, 22],
    [3, 31, 11, 45],
    [47, 7, 18, 29, 32, 33],
    [17, 5],
    [9, 25],
    [26, 24, 48, 27, 10, 21],
    [15, 22, 1, 23, 0, 9, 25, 43],
    [34, 16, 30, 1],
    [4, 48, 11, 31, 2],
    [47, 18, 25, 40, 15],
    [28, 17, 32],
    [35, 11],
    [12, 20, 10, 21],
    [43, 33, 36, 18, 15],
    [24, 11, 42, 4, 27, 39]]

adjDict = {n: k for n, k in enumerate(adjList)}



# State Abbreviation, Latitude, Longitude
nodeData = {
    0:  ("AL", 32.7990, -86.8073), 
    1:  ("AR", 34.9513, -92.3809), 
    2:  ("AZ", 33.7712, -111.3877), 
    3:  ("CA", 36.1700, -119.7462), 
    4:  ("CO", 39.0646, -105.3272), 
    5:  ("CT", 41.5834, -72.7622), 
    6:  ("DC", 38.8964, -77.0262), 
    7:  ("DE", 39.3498, -75.5148), 
    8:  ("FL", 27.8333, -81.7170), 
    9:  ("GA", 32.9866, -83.6487), 
    10: ("IA", 42.0046, -93.2140),
    11: ("ID", 44.2394, -114.5103), 
    12: ("IL", 40.3363, -89.0022),
    13: ("IN", 39.8647, -86.2604), 
    14: ("KS", 38.5111, -96.8005),
    15: ("KY", 37.6690, -84.6514), 
    16: ("LA", 31.1801, -91.8749),
    17: ("MA", 42.2373, -71.5314), 
    18: ("MD", 39.0724, -76.7902),
    19: ("ME", 44.6074, -69.3977), 
    20: ("MI", 43.3504, -84.5603),
    21: ("MN", 45.7326, -93.9196), 
    22: ("MO", 38.4623, -92.3020),
    23: ("MS", 32.7673, -89.6812), 
    24: ("MT", 46.9048, -110.3261),
    25: ("NC", 35.6411, -79.8431), 
    26: ("ND", 47.5362, -99.7930),
    27: ("NE", 41.1289, -98.2883), 
    28: ("NH", 43.4108, -71.5653),
    29: ("NJ", 40.3140, -74.5089), 
    30: ("NM", 34.8375, -106.2371),
    31: ("NV", 38.4199, -117.1219), 
    32: ("NY", 42.1497, -74.9384), 
    33: ("OH", 40.3736, -82.7755), 
    34: ("OK", 35.5376, -96.9247),
    35: ("OR", 44.5672, -122.1269), 
    36: ("PA", 40.5773, -77.2640),
    37: ("RI", 41.6772, -71.5101), 
    38: ("SC", 33.8191, -80.9066),
    39: ("SD", 44.2853, -99.4632), 
    40: ("TN", 35.7449, -86.7489),
    41: ("TX", 31.1060, -97.6475), 
    42: ("UT", 40.1135, -111.8535),
    43: ("VA", 37.7680, -78.2057), 
    44: ("VT", 44.0407, -72.7093),
    45: ("WA", 47.3917, -121.5708), 
    46: ("WI", 44.2563, -89.6385),
    47: ("WV", 38.4680, -80.9696), 
    48: ("WY", 42.7475, -107.2085)}
