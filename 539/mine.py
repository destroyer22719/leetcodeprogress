from typing import List

#Python, Firebase, Vuejs, Google Drive, Regular Expressions, Azure, Data Validation, Friendly, .net, Quickbooks, Asp.net Mvc, Flask, Mobile, Ionic, Application, Azure Devops, Ai, C#, Developer, Api, Google Docs, Powershell Scripting, Typescript, Javascript, Rest Api, Net Core, Mongodb, Nodejs, React, Rest, Java, Html, Scss, C++, Sql, Mvc, Asp, Css, Github, Linkedin, Computing, Specialization, Aws, Serving, Web Scraping, Aws Lambda, Mysql, Flask

class Solution:
  def findMinDifference(self, timePoints: List[str]) -> int:
    def time_diff(a, b):
      a_mins = int(a[:2])*60 + int(a[3:])
      b_mins = int(b[:2])*60 + int(b[3:])
      
      return min(abs(a_mins-b_mins),abs(24*60 - max(a_mins, b_mins) + min(a_mins, b_mins)))

    min_mins = 24*60+ 59

    timePoints = sorted(timePoints)

    for i in range(-1, len(timePoints) - 1):
      min_mins = min(time_diff(timePoints[i], timePoints[i+1]), min_mins)
    
    return min_mins

sol = Solution()
a = sol.findMinDifference(["12:12","00:13"])
print(a)