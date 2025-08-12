class Solution():
    def canPlaceFlowers(self,flowerbed, n):
        l = len(flowerbed)

    if l == 1:
        if flowerbed[0] == 0 and n <= 1:
            return True if n <= 1 else False
        return n == 0

    if flowerbed[0] == 0 and flowerbed[1] == 0:
        flowerbed[0] = 1
        n -= 1

    if flowerbed[l - 1] == 0 and flowerbed[l - 2] == 0:
        flowerbed[l - 1] = 1
        n -= 1

    if n == 0:
        for i in range(l):
            print(flowerbed[i], end=" ")
        return True

    for i in range(1, l - 1):
        if n == 0:
            return True
        if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
            flowerbed[i] = 1
            n -= 1

    for i in range(l):
        print(flowerbed[i])

    return n == 0


    
