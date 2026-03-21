class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        cha = {"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],"6":["m","n","o"],
        "7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}
        listofalpha = []
        if len(digits) == 1:
            return cha[digits]
        else:
            for i in digits:
                listofalpha.append(cha[i])

        multiply = len(listofalpha)-1
        count = 0
        result = []
        while count<multiply:
            if count == 0:
                result = [x + y for x in listofalpha[count] for y in listofalpha[count+1]]
                count += 1
            else:
                result = [x + y for x in result for y in listofalpha[count+1]]
                count += 1
        return result
        