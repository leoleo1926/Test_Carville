def calc_prices(InputPriceWithNDS, ProcNDS):
    
    if (0 <= ProcNDS <= 99):
        
        CorrectedPriceWithoutNDS = round(InputPriceWithNDS / (1 + ProcNDS / 100), 2)
     # ������� ������� �����, ���� ����
        CorrectedPriceWithoutNDS = int( CorrectedPriceWithoutNDS * 100) / 100
    # ������ ���� � ���
    # �������� � ������� ����, ��������� �� 2 ������ ����� ������� ��� ����������
        CorrectedPriceWithNDS = round(CorrectedPriceWithoutNDS * (1 + ProcNDS / 100), 2)
    # �������� �� ������������ ������� �� ����� (�������� 2 ����� ����� �������)
        CorrectedPriceWithoutNDS= int(CorrectedPriceWithoutNDS * 100) / 100
    
        return CorrectedPriceWithNDS, CorrectedPriceWithoutNDS
    else: 
        return "NDS value error. The value must be in the range from 0 to 99"
