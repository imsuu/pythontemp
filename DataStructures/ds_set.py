#集合（Set）是简单对象的无序集合（Collection）。当集合中的项目存在与否比起次序或其出现次数更加重要时，我们就会使用集合
bri = set(['brazil', 'russia', 'india'])
print('india' in bri)
print('indi' in bri)

bric = bri.copy()
bric.add('china')
print(bric.issuperset(bri))

bri.remove('russia')
print(bri & bric)
 # OR bri.intersection(bric)
