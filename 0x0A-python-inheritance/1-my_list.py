#!/usr/bin/python3
"""_summary_"""
class MyList(list):
    """

    Args:
        list (paret): mylist inherits from list
    """
    def print_sorted(self):
        """
        prints 
        """
        sorted_list = sorted(self)
        print(sorted_list)
