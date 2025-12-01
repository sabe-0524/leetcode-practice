from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique_emails = set()
        
        for email in emails:
            local, domain = email.split("@", 1)
            local = local.split("+")[0]
            local = local.replace(".", "")
            fixed_email = local + "@" + domain
            unique_emails.add(fixed_email)
        
        return len(unique_emails)