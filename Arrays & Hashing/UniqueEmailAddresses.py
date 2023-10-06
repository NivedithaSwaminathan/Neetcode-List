# To return the count of distinct email addresses based on the given conditions for uniqueness.
# We create a hashset to keep track of the unique addresses. We loop through each address in the list, and we get the local and domain names of each address using split.
# We check character by character, if it constitutes and address and reconstruct the local name.
# We combine the local and domain names to add an email ID to the hashset.
# The length of the hashset gives hte count of distinct addresses.

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:

        hashset = set()

        for e in emails:

            local, domain = e.split("@")
            new_local = ""

            for ch in local:

                if ch == ".":
                    continue

                elif ch == "+":
                    break
                
                else:
                    new_local += ch

            addr = new_local + "@" + domain

            hashset.add(addr)

        return len(hashset)
