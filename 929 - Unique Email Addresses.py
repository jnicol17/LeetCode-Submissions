class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        rSet = set()
        for email in emails:
            splitEmail = email.split("@")
            localName = splitEmail[0]
            domainName = splitEmail[1]
            localName = localName.split("+")[0]
            localName = localName.replace(".", "")
            rSet.add(localName + "@" + domainName)
        return len(rSet)
