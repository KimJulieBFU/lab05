def medians(nums1, nums2):
    sorted_list = []
    nums1_index = nums2_index = 0
    nums1_length, nums2_length = len(nums1), len(nums2)
    # Обрабатываем случаи, когда один из списков пустой
    if nums1_length==0:
        sorted_list=nums2
        if len(sorted_list) % 2 == 0:
            return (sorted_list[(len(sorted_list)-1) // 2] + sorted_list[(len(sorted_list) // 2 - 1) + 1]) / 2

        else:
            return sorted_list[len(sorted_list) // 2]

    if nums2_length==0:
        sorted_list=nums1
        if len(sorted_list) % 2 == 0:
            return (sorted_list[(len(sorted_list)-1) // 2] + sorted_list[(len(sorted_list)-1) // 2 + 1]) / 2

        else:
            return sorted_list[len(sorted_list) // 2]


    # Объединяем и сортируем списки методом merge sort

    for _ in range(nums1_length + nums2_length):
        if nums1_index < nums1_length and nums2_index < nums2_length:
            # Проверяем, какое значение с начала каждого списка меньше
            # Если элемент в начале левого списка меньше, добавляем его в отсортированный список
            if nums1[nums1_index] <= nums2[nums2_index]:
                sorted_list.append(nums1[nums1_index])
                nums1_index += 1
            # Если элемент в начале правого списка меньше, добавляем его в отсортированный список
            else:
                sorted_list.append(nums2[nums2_index])
                nums2_index += 1
        # Если достигнут конец левого списка, добавляем элементы из правого списка
        elif nums1_index == nums1_length:
            sorted_list.append(nums2[nums2_index])
            nums2_index += 1
        # Если достигнут конец правого списка, добавляем элементы из левого списка
        elif nums2_index == nums2_length:
            sorted_list.append(nums1[nums1_index])
            nums1_index += 1
    if len(sorted_list)%2==0:
        return (sorted_list[(len(sorted_list)-1) // 2] + sorted_list[(len(sorted_list)-1) // 2 + 1]) / 2

    else:
        return sorted_list[len(sorted_list)//2]
