class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        couple_num = (len(row) + 1) / 2
        error_index = []
        error_num = 0
        for i in range(couple_num):
            i = i * 2
            if row[i] < row[i + 1]:
                if row[i] % 2 != 0:
                    error_num += 1
                    error_index.append(i)
                    continue
                elif row[i] + 1 != row[i + 1]:
                    error_num += 1
                    error_index.append(i)
                    continue
            else:
                if row[i + 1] % 2 != 0:
                    error_num += 1
                    error_index.append(i)
                    continue
                elif row[i + 1] + 1 != row[i]:
                    error_num += 1
                    error_index.append(i)
                    continue
        group_list = []
        slod_index = []
        for m in range(len(error_index)):
            group_size = 1
            if m in slod_index:
                continue
            point = m
            while not(((row[error_index[point]] % 2 == 0) & ((row[error_index[point]] + 1) == row[error_index[point] + 1])) | (((row[error_index[point] + 1]) % 2 == 0) & (row[error_index[point]] == (row[error_index[point] + 1] + 1)))):
                if row[error_index[point]] < row[error_index[point] + 1]:
                    if row[error_index[point]] % 2 == 0:
                        target = row[error_index[point]] + 1
                        for i in range(0, len(error_index)):
                            if i in slod_index:
                                continue
                            elif i == point:
                                continue
                            if target == row[error_index[i]]:
                                temp = row[error_index[point] + 1] 
                                row[error_index[point] + 1] = row[error_index[i]]
                                row[error_index[i]] = temp
                                slod_index.append(point)
                                point = i
                                group_size += 1
                                break
                            elif target == row[error_index[i] + 1]:
                                temp = row[error_index[point] + 1] 
                                row[error_index[point] + 1] = row[error_index[i] + 1]
                                row[error_index[i] + 1] = temp
                                slod_index.append(point)
                                point = i
                                group_size += 1
                                break
                    else:
                        target = row[error_index[point]] - 1
                        for i in range(0, len(error_index)):
                            if i in slod_index:
                                continue
                            elif i == point:
                                continue
                            if target == row[error_index[i]]:
                                temp = row[error_index[point] + 1] 
                                row[error_index[point] + 1] = row[error_index[i]]
                                row[error_index[i]] = temp
                                slod_index.append(point)
                                point = i
                                group_size += 1
                                break
                            elif target == row[error_index[i] + 1]:
                                temp = row[error_index[point] + 1] 
                                row[error_index[point] + 1] = row[error_index[i] + 1]
                                row[error_index[i] + 1] = temp
                                slod_index.append(point)
                                point = i
                                group_size += 1
                                break
                else:
                    if row[error_index[point] + 1] % 2 == 0:
                        target = row[error_index[point] + 1] + 1
                        for i in range(1, len(error_index)):
                            if i in slod_index:
                                continue
                            elif i == point:
                                continue
                            if target == row[error_index[i]]:
                                temp = row[error_index[point]]
                                row[error_index[point]] = row[error_index[i]]
                                row[error_index[i]] = temp
                                slod_index.append(point)
                                point = i
                                group_size += 1
                                break
                            elif target == row[error_index[i] + 1]:
                                temp = row[error_index[point]]
                                row[error_index[point]] = row[error_index[i] + 1]
                                row[error_index[i] + 1] = temp
                                slod_index.append(point)
                                point = i
                                group_size += 1
                                break
                    else:
                        target = row[error_index[point] + 1] - 1
                        for i in range(1, len(error_index)):
                            if i in slod_index:
                                continue
                            elif i == point:
                                continue
                            if target == row[error_index[i]]:
                                temp = row[error_index[point]]
                                row[error_index[point]] = row[error_index[i]]
                                row[error_index[i]] = temp
                                slod_index.append(point)
                                point = i
                                group_size += 1
                                break
                            elif target == row[error_index[i] + 1]:
                                temp = row[error_index[point]]
                                row[error_index[point]] = row[error_index[i] + 1]
                                row[error_index[i] + 1] = temp
                                slod_index.append(point)
                                point = i
                                group_size += 1
                                break
            group_list.append(group_size)
        sum_change = 0 
        for i in group_list:
            sum_change += i - 1
        return sum_change
