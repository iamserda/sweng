class BrowserHistory:

    def __init__(self, homepage: str):
        """Constructor"""

    def visit(self, url: str) -> None:
        """Function when user visits a page-url"""

    def back(self, steps: int) -> str:
        """Function when user hits back-button"""

    def forward(self, steps: int) -> str:
        """Function when user hits fwd-button"""
        
    def print_props(self):
        """ print each prof in __init__ to the console."""



# TESTING ARENA:

# Your BrowserHistory object will be instantiated and called as such:
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

browserHistory.visit("youtube.com")      # You are in "facebook.com". Visit "youtube.com"
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