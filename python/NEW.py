
# From Uphaar dubey to Everyone:  10:31 AM
# https://codeshare.io/axJZxD
# https://codeshare.io/axJZxD
# From Uphaar dubey to Everyone:  11:11 AM





class Node:
    val = None
    next = None
    prev = None
    def __init__(self, val, prev, next):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory(object):
    root = None
    currUrl = None
    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.root = Node(homepage, None, None)
        self.currUrl = self.root
        

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        self.currUrl.next = Node(url, self.currUrl, None)
        self.currUrl = self.currUrl.next
        

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while self.currUrl and steps != 0:
            steps -= 1
            self.currUrl = self.currUrl.prev
        

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while self.currUrl and steps != 0:
            steps -= 1
            self.currUrl = self.currUrl.next
    
def main():
    browser = BrowserHistory("google")
    browser.visit("facebook")
    print(browser.currUrl.val)
    browser.visit("reddit")
    print(browser.currUrl.val)
    browser.back(2);
    print(browser.currUrl.val)
    browser.visit("Youtube")
    print(browser.currUrl.val)
    
main()



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
