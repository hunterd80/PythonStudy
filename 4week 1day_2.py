class House:
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location 
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year
    
    def show_detail(self):
        print("{0} {1} {2} {3} 원 {4}년 \n".format(self.location, self.house_type, self.deal_type, self.price, self.completion_year))

   
mamul1 = House("강남", "아파트", "매매", "10억", "2010")
mamul2 = House("마포", "오피스텔", "전새", "5억", "2017")
mamul3 = House("송파", "빌라", "월세", "500/50억", "2000")

mamullist = []
mamullist.append(mamul1)
mamullist.append(mamul2)
mamullist.append(mamul3)

print("총 {0} 가지 매물이 있습니다.".format(len(mamullist)))
for mamul in mamullist:
    House.show_detail(mamul)