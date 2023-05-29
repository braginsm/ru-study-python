class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        if len(input_list) == 0:
            return input_list

        max_value = input_list[0]
        for item in input_list:
            if item > max_value:
                max_value = item

        return list(map(lambda element: element if element < 0 else max_value, input_list))

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        def search_in_sublist(input_sub_list: list[int], start_index: int) -> int:
            length = len(input_sub_list)
            if length == 0:
                return -1
            
            middle_index = len(input_sub_list) // 2
            if input_sub_list[middle_index] == query:
                return middle_index + start_index
            
            if input_sub_list[middle_index] < query:
                new_start_index = middle_index + 1
                return search_in_sublist(input_sub_list[new_start_index:], new_start_index + start_index)
            else:
                return search_in_sublist(input_sub_list[:middle_index], start_index)
            
        return search_in_sublist(input_list, 0)
