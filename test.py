from main import knapsack
import unittest


class TestStringMethods(unittest.TestCase):

    def test_small_weights(self):
        self.assertEqual(knapsack([1, 2], 9), [0, 1, 2, 3])

    def test_small_W(self):
        self.assertEqual(knapsack([1, 2], 0), [])

    def test_10_small(self):
        self.assertEqual(knapsack([3, 6, 8, 7, 6, 10, 1, 1], 21),
                         [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
        self.assertEqual(knapsack([7, 6, 3, 1, 6], 11), [0, 1, 3, 4, 6, 7, 8, 9, 10])

    def test_10_big(self):
        self.assertEqual(knapsack([623946, 761087, 938363, 454, 992617, 742205], 2029336),
                         [0, 454, 623946, 624400, 742205, 742659, 761087, 761541, 938363, 938817, 992617, 993071,
                          1366151, 1366605, 1385033, 1385487, 1503292, 1503746, 1562309, 1562763, 1616563, 1617017,
                          1680568, 1681022, 1699450, 1699904, 1734822, 1735276, 1753704, 1754158, 1930980, 1931434])
        self.assertEqual(knapsack([262677], 131338), [0])

    def test_rand_ws(self):
        self.assertEqual(knapsack([1, 20, 129, 208, 171, 95, 11, 164, 127, 105], 515),
                         [0, 1, 11, 12, 20, 21, 31, 32, 95, 96, 105, 106, 107, 115, 116, 117, 125, 126, 127, 128, 129,
                          130, 136, 137, 138, 139, 140, 141, 147, 148, 149, 150, 158, 159, 160, 161, 164, 165, 171, 172,
                          175, 176, 182, 183, 184, 185, 191, 192, 195, 196, 200, 201, 202, 203, 208, 209, 211, 212, 219,
                          220, 221, 222, 223, 224, 225, 228, 229, 231, 232, 233, 234, 235, 236, 239, 240, 242, 243, 244,
                          245, 246, 252, 253, 254, 255, 256, 257, 259, 260, 263, 264, 265, 266, 267, 268, 269, 270, 271,
                          276, 277, 278, 279, 280, 281, 286, 287, 288, 289, 290, 291, 292, 293, 294, 296, 297, 298, 299,
                          300, 301, 302, 303, 304, 305, 307, 308, 309, 310, 311, 312, 313, 314, 315, 318, 319, 320, 321,
                          322, 323, 324, 325, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341,
                          344, 345, 346, 347, 348, 349, 350, 351, 352, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364,
                          365, 366, 367, 368, 369, 371, 372, 373, 375, 376, 379, 380, 381, 382, 383, 384, 385, 386, 387,
                          388, 389, 390, 391, 392, 393, 394, 395, 396, 397, 398, 399, 400, 402, 403, 404, 405, 406, 407,
                          408, 409, 410, 411, 413, 414, 415, 416, 417, 418, 419, 420, 421, 423, 424, 425, 426, 427, 428,
                          429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 447, 448, 450,
                          451, 452, 453, 454, 456, 457, 458, 459, 460, 461, 462, 463, 464, 465, 467, 468, 471, 472, 473,
                          474, 475, 476, 477, 478, 479, 482, 483, 484, 485, 486, 487, 488, 489, 491, 492, 493, 494, 495,
                          496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 511, 512, 513,
                          514])


if __name__ == '__main__':
    unittest.main()
