import datetime


def convert(str):
    year, month, day = str.split("-")
    month = month if month[0] != "0" else month[1]
    day = day if day[0] != "0" else day[1]
    return datetime.date(int(year), int(month), int(day))


class SimpleReport:
    @classmethod
    def generate(cls, arr):
        now = datetime.datetime.date(datetime.datetime.today())
        m_f_date = convert(arr[0]["data_de_fabricacao"])
        m_v_date = datetime.date(2800, 1, 1)
        days_distance = m_v_date - now
        companys = {}
        for pr in arr:
            if not companys.get(pr["nome_da_empresa"]):
                companys[pr["nome_da_empresa"]] = 0
            companys[pr["nome_da_empresa"]] += 1

            if convert(pr["data_de_fabricacao"]) < m_f_date:
                m_f_date = convert(pr["data_de_fabricacao"])

            validate_pr = convert(pr["data_de_validade"])
            if validate_pr > now:
                distance = validate_pr - now
                if distance < days_distance:
                    days_distance = distance
                    m_v_date = validate_pr

        max_products = max([x for x in companys.values()])
        company = [x for x in companys if companys[x] == max_products]

        return f"""Data de fabricação mais antiga: {m_f_date}
Data de validade mais próxima: {m_v_date}
Empresa com mais produtos: {company[0]}"""
