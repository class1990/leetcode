class Solution(object):
    def addBinary_initial(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        sum_num = ''
        carry_over = 0
        min_len = len(a) if len(a) <= len(b) else len(b)
        a_index = len(a) - 1
        b_index = len(b) - 1
        index = min_len
        while index > 0:
            local_sum = int(a[a_index]) + int(b[b_index]) if carry_over == 0 else int(a[a_index]) + int(b[b_index]) + 1
            if local_sum >= 2:
                local_sum = local_sum - 2
                carry_over = 1
            else:
                carry_over = 0
            sum_num = str(local_sum) + sum_num
            a_index -= 1
            b_index -= 1
            index -= 1

        if len(a) >= len(b):
            for index in range(len(a) - min_len - 1, -1, -1):
                local_sum = int(a[index]) + carry_over
                if local_sum == 2:
                    local_sum = 0
                    carry_over = 1
                else:
                    carry_over = 0
                sum_num = str(local_sum) + sum_num
        if len(b) > len(a):
            for index in range(len(b) - min_len - 1, -1, -1):
                local_sum = int(b[index]) + carry_over
                if local_sum == 2:
                    local_sum = 0
                    carry_over = 1
                else:
                    carry_over = 0
                sum_num = str(local_sum) + sum_num

        if carry_over == 1:
            sum_num = '1' + str(sum_num)

        return sum_num


    def addBinary(self, a, b):
        carry = 0
        result = ''
        for i in range(max(len(a), len(b))):
            sum_num = carry
            if i < len(a):
                sum_num += int(a[-i - 1])
            if i < len(b):
                sum_num += int(b[-i - 1])
            carry = sum_num / 2
            result += str(sum_num % 2)
        if carry:
            result += '1'
        return result[::-1]

if __name__ == '__main__':
    result = Solution().addBinary('11', '1')
    print result