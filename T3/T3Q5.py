def sortedzip_regular(lists):
    # פונקציה רקורסיבית למיון כל רשימה פנימית
    def sort_each(lst_of_lsts):
        if not lst_of_lsts:
            return []
        return [sorted(lst_of_lsts[0])] + sort_each(lst_of_lsts[1:])
    
    return zip(*sort_each(lists))

def sortedzip_tail(lists):
    def helper(lst_of_lsts, acc):
        if not lst_of_lsts:
            return acc[::-1]  # להפוך כי צברנו מהסוף להתחלה
        return helper(lst_of_lsts[1:], [sorted(lst_of_lsts[0])] + acc)
    
    return zip(*helper(lists, []))

print(list(sortedzip_regular([[3,1,2],[5,6,4],['a','b','c']])))
print(list(sortedzip_tail([[3,1,2],[5,6,4],['a','b','c']])))
