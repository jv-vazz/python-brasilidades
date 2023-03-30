from datetime import datetime, timedelta

class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()


    def mes_cadastro(self):
        meses_do_ano = ["janeiro",
                       "fevereiro",
                       "março",
                       "abril",
                       "maio",
                       "junho",
                       "julho",
                       "agosto",
                       "setembro",
                       "outubro",
                       "novembro",
                       "dezembro"]
        mes_cadastro = self.momento_cadastro.month -1
        return meses_do_ano[mes_cadastro]

    def __str__(self):
        return self.data_formatada()

    def dia_semana(self):
        dias_semana = [
            "segunda", "terça", "quarta",
            "quinta", "sexta","sábado","domingo"
        ]
        dia_semana = self.momento_cadastro.weekday()
        return dias_semana[dia_semana]

    def data_formatada(self):
        self.momento_cadastro_formatado = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return self.momento_cadastro_formatado

    def tempo_cadastro(self):
        tempo_cadastro = (datetime.today()) + timedelta(days=30) - self.momento_cadastro
        return tempo_cadastro