class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer=[]
        for number in range(1,n+1):
            if (number % 3 == 0) and (number % 5 == 0):
                answer.append("FizzBuzz")
            elif (number % 3 == 0):
                answer.append("Fizz")
            elif (number %5==0):
                answer.append("Buzz")
            else:
                answer.append(str(number))
                
                
        return answer
        
        
Footer
© 2022 GitHub, Inc.
