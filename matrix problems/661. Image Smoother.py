#https://leetcode.com/problems/image-smoother/description/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:

        # ROWS = len(img)
        # COLS = len(img[0])
        
        # res = [([0] * COLS) for _ in range(ROWS)]

        # for r in range(ROWS):
        #     for c in range(COLS):
        #         tot = 0
        #         count = 0
        #         for i in range(r-1,r+2):
        #             for j in range(c-1,c+2):
        #                 if  0 <= i < ROWS and 0 <= j < COLS:
        #                     count+= 1
        #                     tot += img[i][j]
        #         res[r][c] = tot // count
        # return res


        ####### solution with constant space:
        # we can use the constraint 0 <= img[i][j] <= 255, it means that only the first 8 bit are use to store the number, we can use the remain bit to store the new number 

        
        ROWS = len(img)
        COLS = len(img[0])

        for r in range(ROWS):
            for c in range(COLS):
                tot = 0
                count = 0
                for i in range(r-1,r+2):
                    for j in range(c-1,c+2):
                        if  0 <= i < ROWS and 0 <= j < COLS:
                            count+= 1
                            tot += (img[i][j] % 256) # take the first 8 bit 
                img[r][c] = img[r][c]  | (tot // count) << 8
        for r in range(ROWS):
            for c in range(COLS):
                img[r][c] = img[r][c] >> 8 
        return img

        