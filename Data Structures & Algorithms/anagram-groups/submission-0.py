class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sorted letters: index in result
        sort_map = dict()
        num_of_grams = 0
        result = []

        for i, word in enumerate(strs):
            letters = "".join(sorted(word))
            if letters not in sort_map:
                num_of_grams += 1
                sort_map[letters] = num_of_grams - 1
                result.append([word])
            else:
                ans_index = sort_map[letters]
                result[ans_index].append(word)
        return result



            
        

                
        