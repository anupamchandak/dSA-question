class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if not strs:
            return ""

        # Assume the first string is the common prefix
        prefix = strs[0]

        # Compare the prefix with each string
        for s in strs[1:]:
            while s[:len(prefix)] != prefix:
                prefix = prefix[:-1]  # Remove last character

                if prefix == "":
                    return ""

        return prefix