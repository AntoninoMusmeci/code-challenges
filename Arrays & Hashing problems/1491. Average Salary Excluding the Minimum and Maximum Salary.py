#https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/description/
class Solution:
    def average(self, salary: List[int]) -> float:
        salary_min = salary[0]
        salary_max = salary[0]
        salary_sum = 0
        for s in salary:
            salary_min = min(s, salary_min)
            salary_max = max(s, salary_max)
            salary_sum += s
        return (salary_sum - (salary_min + salary_max)) / (len(salary) - 2)