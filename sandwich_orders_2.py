def sandwich_order(sandwich, **order):
    lst = {}
    lst['Your sandwich:'] = sandwich
    for item, typpe in order.items():
        lst[item] = typpe
    for i, v in lst.items():
        print(i + ' ' + v)

sandwich_order('America', Size=': Small', Roasting=': Medium')






