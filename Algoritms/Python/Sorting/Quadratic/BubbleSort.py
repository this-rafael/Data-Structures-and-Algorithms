from Sorting.Util import swapInArray


class BubbleSort:


    def sort(self, array):
        for i in range(0, len(array)):
            for j in range(0, len(array) - 1):
                if array[j] > array[j + 1]:
                    swapInArray(array, j, j + 1)


