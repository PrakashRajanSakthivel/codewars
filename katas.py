class Codewars:

    def series_sum(val):
        """
        sum series to nth digit
        1+1/4+1/7+1/10
        :return:
        """
        result = 1
        if val <= 1:
            return "{:.2f}".format(val)
        else:
            den = 1
            for number in enumerate(range(val-1), 1):
                den = den + 3
                result = result + (1/den)
        return "{:.2f}".format(result)

    def duplicate_count(val):
        """
        find duplicates count in the given string.
        Example: indivisibility -> 6
        :return:
        """
        new_ls = []
        ls = []
        for char in val.lower():
            if char not in new_ls:
                new_ls.append(char)
            else:
                ls.append(char)
        return len(set(ls))

    def disemvowel(val):
        """
        remove vowel in the string.
        Example: "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".
        :return:
        """
        c_list = list(val)
        for char in list(val):
            if char.lower() in ["a", "e", "i", "o", "u"]:
                c_list.remove(char)
        return "".join(c_list)

    def find_it(val):
        """
        Find the number that is repeated odd number of
        times in the given array.
        Example: [2,3,4,2,3,2,4]

        :return:
        """
        val = sorted(val, key=int)
        temp_val = val[0]
        counter = 0
        for i, number in enumerate(val):
            if not number in val:
                # number repeated odd times
                return temp_val
            else:
                if number == temp_val:
                    counter = counter + 1
                else:
                    if counter % 2 != 0:
                        return temp_val
                    counter = 1
                    temp_val = number
        return temp_val
