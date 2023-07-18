class ColumnSum:
    def sum(self, array):
        x = len(array)
        for i in range(row):
            sum = 0
            for j in range(x):
                sum += array[j][i]

            print(sum, end =" ")

row = int(input("Enter no of rows"))

array = []
for i in range(row):
    column = list(map(int, input().split()))
    array.append(column)

object = ColumnSum()
print(object.sum(array))



