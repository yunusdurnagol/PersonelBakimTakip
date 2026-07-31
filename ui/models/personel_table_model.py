from ui.models.base_table_model import BaseTableModel


class PersonelTableModel(BaseTableModel):

    def __init__(self):

        super().__init__(

            headers=[

                "ID",

                "Sicil",

                "Ad",

                "Soyad",

                "Telefon",

                "Pozisyon",

            ]

        )

    def get_value(
        self,
        personel,
        column,
    ):

        values = [

            personel.id,

            personel.sicil_no,

            personel.ad,

            personel.soyad,

            personel.telefon,

            personel.pozisyon.ad
            if personel.pozisyon
            else "",

        ]

        return str(values[column])