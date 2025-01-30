class Solution:        
    def reverseWords(self, s: str) -> str:
        word = ""
        result_array = []
        "read the sentence backwards"
        for str_index in range(len(s)-1, -1, -1):
            # reversing word var and store each word
            if s[str_index] == " ":
                if len(word) > 0:
                    w = ""
                    for word_index in range(len(word)-1, -1, -1):
                        w += word[word_index]
                    result_array.append(w)
                word = ""
            else:
                word += s[str_index]
            
            # reversing any last word left
            if str_index == 0:
                if len(word) > 0:
                    stack1 = [w for w in word]
                    stack1_reversed = [stack1[i] for i in range(len(stack1)-1, -1, -1)]
                    result_array.append("".join(stack1_reversed))
        answer = ""
        for each_word in result_array:
            answer += " " + each_word if len(answer) > 0 else each_word
        return answer

my_sol = Solution()
print(my_sol.reverseWords("the sky is blue"))