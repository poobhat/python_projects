class Solution:
    def binarySearchableNumbers(self, nums):
        ans, n = 0, len(nums)
        prefix = [False] * n                  # Create prefix array and initialize them as False
        cur_max, cur_min = nums[0], nums[-1]  # Initialize prefix_max & suffix_min
        for i in range(n):                    # Update prefix from left to right
            prefix[i] = cur_max <= nums[i]
            cur_max = max(cur_max, nums[i])
        for i in range(n-1, -1, -1):          # Update suffix and count from right to left
            prefix[i] &= cur_min >= nums[i]   # Use `&` operation (`and` is also fine) to make sure 2 condition hold at the same time
            ans += prefix[i]                  # +1 when `prefix[i]` is True, otherwise +0 (no change)
            cur_min = min(cur_min, nums[i])
        return ans

s=Solution()
# nums=[-9997,-9973,-9951,-9928,-9926,-9909,-9896,-9811,-9810,-9796,-9762,-9761,-9743,-9698,-9648,-9637,-9590,-9530,-9491,-9489,-9484,-9463,-9386,-9381,-9365,-9357,-9323,-9276,-9262,-9232,-9206,-9197,-9142,-9133,-9109,-9080,-9074,-9053,-9047,-9037,-9036,-9030,-9008,-9003,-8957,-8928,-8921,-8828,-8823,-8804,-8789,-8771,-8770,-8763,-8747,-8736,-8726,-8718,-8717,-8710,-8706,-8700,-8692,-8678,-8667,-8633,-8608,-8490,-8476,-8471,-8463,-8462,-8453,-8450,-8438,-8433,-8416,-8406,-8377,-8373,-8335,-8261,-8232,-8210,-8199,-8163,-8094,-8068,-8028,-8003,-7974,-7963,-7918,-7877,-7875,-7856,-7851,-7849,-7839,-7831,-7812,-7771,-7747,-7739,-7730,-7683,-7681,-7680,-7660,-7658,-7643,-7633,-7610,-7588,-7580,-7563,-7534,-7514,-7503,-7486,-7484,-7473,-7436,-7417,-7400,-7377,-7370,-7359,-7345,-7336,-7295,-7233,-7183,-7180,-7175,-7140,-7126,-7104,-7093,-7085,-7081,-7067,-7057,-7054,-7042,-6950,-6937,-6936,-6894,-6876,-6874,-6856,-6836,-6789,-6725,-6678,-6661,-6658,-6654,-6632,-6622,-6617,-6615,-6568,-6547,-6540,-6513,-6495,-6492,-6485,-6484,-6479,-6477,-6451,-6425,-6408,-6405,-6368,-6347,-6259,-6250,-6248,-6237,-6228,-6221,-6213,-6172,-6167,-6135,-6133,-6132,-6098,-6058,-6043,-5986,-5947,-5937,-5936,-5908,-5882,-5844,-5832,-5819,-5809,-5793,-5779,-5753,-5738,-5737,-5734,-5727,-5725,-5718,-5703,-5683,-5672,-5668,-5657,-5656,-5620,-5614,-5567,-5566,-5557,-5545,-5519,-5508,-5499,-5453,-5433,-5428,-5424,-5412,-5405,-5391,-5377,-5354,-5331,-5283,-5281,-5251,-5236,-5216,-5212,-5194,-5193,-5154,-5134,-5128,-5127,-5125,-5124,-5112,-5052,-5050,-5043,-5034,-5030,-4974,-4965,-4855,-4842,-4837,-4826,-4824,-4818,-4803,-4799,-4794,-4736,-4711,-4700,-4692,-4691,-4659,-4625,-4624,-4593,-4581,-4571,-4570,-4556,-4523,-4520,-4511,218,211,196,194,176,171,166,155,154,147,34,28,13,-21,-77,-86,-111,-137,-173,-195,-217,-225,-228,-231,-264,-284,-289,-312,-392,-409,-410,-439,-441,-478,-576,-586,-587,-598,-600,-610,-611,-670,-682,-734,-750,-753,-764,-771,-800,-810,-853,-858,-885,-906,-918,-948,-982,-999,-1002,-1006,-1011,-1038,-1043,-1044,-1051,-1058,-1078,-1116,-1140,-1160,-1161,-1172,-1175,-1269,-1294,-1339,-1346,-1371,-1374,-1390,-1395,-1449,-1459,-1498,-1513,-1515,-1529,-1569,-1571,-1573,-1621,-1625,-1656,-1676,-1690,-1707,-1724,-1725,-1730,-1755,-1769,-1793,-1796,-1814,-1817,-1827,-1884,-1928,-1949,-1954,-1966,-1975,-1980,-1996,-2005,-2010,-2023,-2034,-2054,-2065,-2082,-2156,-2202,-2257,-2275,-2278,-2297,-2300,-2302,-2348,-2371,-2383,-2388,-2410,-2458,-2489,-2494,-2522,-2523,-2532,-2537,-2546,-2550,-2564,-2566,-2578,-2640,-2652,-2667,-2672,-2715,-2764,-2775,-2783,-2785,-2846,-2857,-2865,-2867,-2876,-2890,-2899,-2902,-2931,-2960,-2989,-2994,-3000,-3046,-3049,-3067,-3081,-3107,-3129,-3131,-3135,-3154,-3176,-3177,-3180,-3194,-3196,-3203,-3225,-3254,-3265,-3313,-3316,-3330,-3331,-3375,-3390,-3423,-3442,-3443,-3455,-3463,-3474,-3482,-3498,-3507,-3548,-3626,-3651,-3672,-3683,-3686,-3700,-3707,-3713,-3732,-3764,-3766,-3771,-3802,-3824,-3830,-3846,-3872,-3894,-3897,-3912,-3924,-3925,-3945,-3972,-4004,-4012,-4017,-4024,-4032,-4041,-4045,-4067,-4074,-4129,-4132,-4146,-4227,-4293,-4313,-4356,-4372,-4391,-4420,-4431,-4441,-4482,-4491,-4507,223,226,240,315,341,355,363,365,391,426,505,553,592,611,615,642,644,656,659,661,736,822,827,849,897,974,979,990,1061,1062,1067,1068,1070,1096,1142,1181,1184,1271,1279,1309,1314,1336,1344,1347,1391,1393,1398,1400,1429,1447,1489,1496,1526,1530,1559,1560,1570,1593,1595,1616,1649,1692,1711,1733,1749,1765,1779,1807,1821,1851,1857,1859,1864,1869,1886,1897,1937,1963,1964,1968,2018,2046,2115,2124,2136,2151,2195,2242,2254,2264,2275,2297,2302,2307,2349,2386,2392,2421,2438,2450,2464,2472,2474,2486,2490,2495,2501,2504,2512,2514,2517,2519,2558,2561,2622,2624,2635,2637,2640,2660,2662,2687,2753,2770,2774,2775,2798,2843,2848,2868,2900,2922,2927,2938,2940,2946,2952,2970,2991,3001,3004,3021,3022,3039,3046,3047,3061,3075,3090,3096,3104,3125,3153,3162,3178,3220,3226,3236,3242,3257,3260,3299,3322,3351,3354,3383,3391,3400,3426,3481,3507,3515,3531,3547,3562,3573,3612,3661,3706,3719,3739,3758,3777,3791,3818,3850,3895,3902,3916,3956,3975,4010,4051,4099,4115,4179,4193,4204,4211,4267,4270,4272,4287,4321,4339,4402,4434,4440,4446,4455,4537,4547,4549,4568,4578,4625,4658,4687,4688,4706,4719,4741,4750,4788,4844,4883,4985,4987,4990,5003,5053,5069,5071,5107,5115,5139,5145,5149,5150,5169,5207,5209,5225,5226,5229,5245,5281,5300,5306,5310,5315,5319,5328,5359,5384,5417,5435,5447,5486,5507,5508,5510,5551,5586,5589,5597,5602,5624,5656,5658,5683,5695,5724,5740,5779,5800,5911,5913,5925,5945,5949,5951,5954,5984,6060,6092,6111,6115,6117,6158,6196,6200,6205,6221,6263,6295,6379,6382,6383,6393,6416,6431,6444,6481,6522,6530,6582,6614,6628,6636,6659,6684,6716,6722,6748,6765,6767,6769,6783,6787,6797,6847,6858,6880,6885,6886,6887,6900,6925,6970,6983,6987,6988,7005,7014,7031,7033,7055,7062,7065,7081,7092,7121,7138,7147,7150,7177,7226,7237,7316,7320,7334,7383,7435,7447,7454,7462,7474,7492,7517,7559,7572,7573,7584,7585,7658,7733,7746,7758,7782,7867,7946,7955,8004,8008,8010,8019,8037,8054,8063,8107,8144,8148,8149,8173,8177,8202,8229,8239,8295,8310,8346,8401,8405,8412,8425,8429,8463,8480,8500,8513,8524,8534,8568,8574,8607,8630,8638,8660,8671,8674,8699,8703,8725,8732,8737,8947,8954,8977,9030,9060,9100,9114,9172,9182,9184,9208,9293,9314,9315,9316,9318,9387,9444,9484,9526,9535,9536,9563,9598,9614,9624,9632,9676,9677,9706,9721,9733,9764,9782,9839,9856,9867,9874,9884,9885,9914,9923,9929,9935,9950,9969,9974,9983,9987]
# nums=[3,2,1,4,5]
nums=[-1,1,2,3,5,4,0,10,11,12]
# nums=[-1,2,19,20,12,13]
# nums=[1,2,0,7,8]
print(s.binarySearchableNumbers(nums))