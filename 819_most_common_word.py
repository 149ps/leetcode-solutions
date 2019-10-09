class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        re_paragraph = re.split('\W+',paragraph)
        lower_paragraph = [item.lower() for item in re_paragraph]
        for item in banned:
            while item in lower_paragraph:
                lower_paragraph.remove(item)
        return collections.Counter(lower_paragraph).most_common(1)[0][0]
