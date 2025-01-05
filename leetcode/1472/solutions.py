class BrowserHistory:

    def __init__(self, homepage: str):
        self.backlog = []
        self.fwd_log = []
        self.current_page = homepage

    def visit(self, url: str) -> None:
        self.backlog.append(self.current_page)
        self.current_page = url
        self.fwd_log = []

    def back(self, steps: int) -> str:        
        for i in range(steps):
            if not self.backlog:
                return self.current_page
            self.fwd_log.append(self.current_page)
            self.current_page = self.backlog.pop()
        return self.current_page

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if not self.fwd_log:
                return self.current_page
            self.backlog.append(self.current_page)
            self.current_page = self.fwd_log.pop()
        return self.current_page
        

#Testing Arena: Your BrowserHistory object will be instantiated and called as such:
browserHistory = BrowserHistory("leetcode.com");

browserHistory.visit("google.com") # You are in "leetcode.com". Visit "google.com"
assert browserHistory.backlog[len(browserHistory.backlog)-1] == "leetcode.com"
assert len(browserHistory.backlog) == 1
assert len(browserHistory.fwd_log) == 0
assert browserHistory.current_page == "google.com"

browserHistory.visit("facebook.com") # You are in "google.com". Visit "facebook.com"
assert browserHistory.backlog[len(browserHistory.backlog)-1] == "google.com"
assert len(browserHistory.backlog) == 2
assert len(browserHistory.fwd_log) == 0
assert browserHistory.current_page == "facebook.com"

browserHistory.visit("youtube.com") # You are in "facebook.com". Visit "youtube.com"
assert browserHistory.backlog[len(browserHistory.backlog)-1] == "facebook.com"
assert len(browserHistory.backlog) == 3
assert len(browserHistory.fwd_log) == 0
assert browserHistory.current_page == "youtube.com"

browserHistory.back(1) # You are in "youtube.com", move back to "facebook.com" return "facebook.com"
assert browserHistory.backlog[len(browserHistory.backlog)-1] == "google.com"
assert browserHistory.fwd_log[len(browserHistory.fwd_log)-1] == "youtube.com" 
assert len(browserHistory.backlog) == 2
assert len(browserHistory.fwd_log) == 1
assert browserHistory.current_page == "facebook.com"

browserHistory.back(1) # You are in "facebook.com", move back to "google.com" return "google.com"
assert browserHistory.backlog[len(browserHistory.backlog)-1] == "leetcode.com"
assert browserHistory.fwd_log[len(browserHistory.fwd_log)-1] == "facebook.com" 
assert len(browserHistory.backlog) == 1
assert len(browserHistory.fwd_log) == 2
assert browserHistory.current_page == "google.com"

browserHistory.forward(1) # You are in "google.com", move forward to "facebook.com" return "facebook.com"
assert browserHistory.backlog[len(browserHistory.backlog)-1] == "google.com"
assert browserHistory.fwd_log[len(browserHistory.fwd_log)-1] == "youtube.com" 
assert len(browserHistory.backlog) == 2
assert len(browserHistory.fwd_log) == 1
assert browserHistory.current_page == "facebook.com"

browserHistory.visit("linkedin.com") # You are in "facebook.com". Visit "linkedin.com"
assert browserHistory.backlog[len(browserHistory.backlog)-1] == "facebook.com"
assert len(browserHistory.backlog) == 3
assert len(browserHistory.fwd_log) == 0
assert browserHistory.current_page == "linkedin.com"

browserHistory.forward(2) # You are in "linkedin.com", you cannot move forward any steps.
#None

browserHistory.back(2) # You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
assert browserHistory.backlog[len(browserHistory.backlog)-1] == "leetcode.com"
assert browserHistory.fwd_log[len(browserHistory.fwd_log)-1] == "facebook.com" 
assert len(browserHistory.backlog) == 1
assert len(browserHistory.fwd_log) == 2
assert browserHistory.current_page == "google.com"

browserHistory.back(7) # You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"
assert browserHistory.fwd_log[len(browserHistory.fwd_log)-1] == "google.com"
assert len(browserHistory.backlog) == 0
assert len(browserHistory.fwd_log) == 3
assert browserHistory.current_page == "leetcode.com"

print("forward_list:", browserHistory.fwd_log)
print("back_list:", browserHistory.backlog)
print("current_page:", browserHistory.current_page)