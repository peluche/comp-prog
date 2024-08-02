class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products = sorted(products)
        res = []
        pos = 0
        prefix = ''
        for c in searchWord:
            prefix += c
            while True:
                if pos >= len(products):
                    res.append([])
                    break
                if products[pos].startswith(prefix):
                    r = []
                    for j in range(3):
                        if pos + j < len(products) and products[pos + j].startswith(prefix):
                            r.append(products[pos + j])
                    res.append(r)
                    break
                pos += 1
        return res
