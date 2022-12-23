def solution(price):
    if 100000 <= price < 300000:
        return price * 0.95
    elif 300000 <= price < 500000:
        return price * 0.9
    elif price >= 500000:
        return price * 0.8
    else:     # 가격의 범위가 100000원부터가 아닌 10원부터이므로 할인 적용이 되지 않는 가격도 고려해 주어야 한다.
        return price


# 다른 풀이(딕셔너리 사용!)
# def solution(price):
#     discount_rates = {500000: 0.8, 300000: 0.9, 100000: 0.95, 0: 1}
#     for discount_price, discount_rate in discount_rates.items():     item() 함수를 사용하면 딕셔너리에 있는 키와 값들의 쌍을 얻을 수 있다.
#         if price >= discount_price:      또한 discunt_price가 500000부터 적용되도록 하여 올바르게 할인이 적용될 수 있게 한다.
#             return int(price * discount_rate)