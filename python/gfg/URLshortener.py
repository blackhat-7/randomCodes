class URLshortener:
    def __init__(self):
        self.url = ''
        self.map = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    def shortenURL(self, id):
        while id > 0:
            self.url = self.map[id%62] + self.url
            id //= 62
    
    def originalURL(self):
        id = 0
        for c in self.url:
            id = id*62 + self.map.index(c)
        print(id)

if __name__ == '__main__':
    url = URLshortener()
    url.shortenURL(12345)
    print(url.url)
    url.originalURL()




# 12345%62 = 7

# (12345/62)%62 = 13
# (12345/62)/62 % 62 = 3
# 7