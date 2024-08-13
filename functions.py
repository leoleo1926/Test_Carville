def calc_prices(InputPriceWithNDS, ProcNDS):
    
    if (0 <= ProcNDS <= 99):
        
        CorrectedPriceWithoutNDS = round(InputPriceWithNDS / (1 + ProcNDS / 100), 2)
     # Убираем дробную часть, если надо
        CorrectedPriceWithoutNDS = int( CorrectedPriceWithoutNDS * 100) / 100
    # Расчет цены с НДС
    # Приводим к нужному виду, округляем до 2 знаков после запятой без округления
        CorrectedPriceWithNDS = round(CorrectedPriceWithoutNDS * (1 + ProcNDS / 100), 2)
    # Проверка на соответствие условию по ценам (максимум 2 знака после запятой)
        CorrectedPriceWithoutNDS= int(CorrectedPriceWithoutNDS * 100) / 100
    
        return CorrectedPriceWithNDS, CorrectedPriceWithoutNDS
    else: 
        return "NDS value error. The value must be in the range from 0 to 99"
