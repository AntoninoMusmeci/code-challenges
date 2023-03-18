#https://leetcode.com/problems/design-browser-history/editorial/
class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.history = [homepage]
        self.current = 0
        

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        self.current += 1
        self.history = self.history[:self.current]    
        self.history.append(url)
    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        self.current -= steps
        if self.current < 0: self.current = 0
        return self.history[self.current]
        

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str

        """
        self.current += steps
        if self.current >= len(self.history):
            self.current = len(self.history) - 1
        return self.history[self.current]