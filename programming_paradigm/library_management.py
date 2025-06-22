class Library:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out= False

    def checked_out(self):
        if not self._is_checked_out:
            self._is_checked_out=True
            print(f"{self.title} has been checked out" )
        else:
            print(f"{self.title} is already checked out")    
    def return_book(self):
        if  self._is_checked_out:
            self._is_checked_out=False
            print(f"{self.title} is available")  
        else :
            print(f"{self.title} has been issued")
    def _is_checked_out(self):
        return self._is_checked_out              