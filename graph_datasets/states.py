# Graph data from:
# http://mathematica.stackexchange.com/questions/28456/building-graph-based-on-the-cities-connection
# Nodes: 49
# Edges: 107


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



# Latitude, Longitude, State Abbreviation
nodeData = [   
    (32.799, -86.8073, 'AL'),
    (34.9513, -92.3809, 'AR'),
    (33.7712, -111.3877, 'AZ'),
    (36.17, -119.7462, 'CA'),
    (39.0646, -105.3272, 'CO'),
    (41.5834, -72.7622, 'CT'),
    (38.8964, -77.0262, 'DC'),
    (39.3498, -75.5148, 'DE'),
    (27.8333, -81.717, 'FL'),
    (32.9866, -83.6487, 'GA'),
    (42.0046, -93.214, 'IA'),
    (44.2394, -114.5103, 'ID'),
    (40.3363, -89.0022, 'IL'),
    (39.8647, -86.2604, 'IN'),
    (38.5111, -96.8005, 'KS'),
    (37.669, -84.6514, 'KY'),
    (31.1801, -91.8749, 'LA'),
    (42.2373, -71.5314, 'MA'),
    (39.0724, -76.7902, 'MD'),
    (44.6074, -69.3977, 'ME'),
    (43.3504, -84.5603, 'MI'),
    (45.7326, -93.9196, 'MN'),
    (38.4623, -92.302, 'MO'),
    (32.7673, -89.6812, 'MS'),
    (46.9048, -110.3261, 'MT'),
    (35.6411, -79.8431, 'NC'),
    (47.5362, -99.793, 'ND'),
    (41.1289, -98.2883, 'NE'),
    (43.4108, -71.5653, 'NH'),
    (40.314, -74.5089, 'NJ'),
    (34.8375, -106.2371, 'NM'),
    (38.4199, -117.1219, 'NV'),
    (42.1497, -74.9384, 'NY'),
    (40.3736, -82.7755, 'OH'),
    (35.5376, -96.9247, 'OK'),
    (44.5672, -122.1269, 'OR'),
    (40.5773, -77.264, 'PA'),
    (41.6772, -71.5101, 'RI'),
    (33.8191, -80.9066, 'SC'),
    (44.2853, -99.4632, 'SD'),
    (35.7449, -86.7489, 'TN'),
    (31.106, -97.6475, 'TX'),
    (40.1135, -111.8535, 'UT'),
    (37.768, -78.2057, 'VA'),
    (44.0407, -72.7093, 'VT'),
    (47.3917, -121.5708, 'WA'),
    (44.2563, -89.6385, 'WI'),
    (38.468, -80.9696, 'WV'),
    (42.7475, -107.2085, 'WY')]
