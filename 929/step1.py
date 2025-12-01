from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        
        for email in emails:
            pre, post = email.split("@", 1)
            pre = pre.replace(".", "")
            pre = pre.split("+")[0]
            fixed_email = pre + "@" + post
            unique_emails.add(fixed_email)
        
        return len(unique_emails)