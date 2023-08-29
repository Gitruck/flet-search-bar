import flet as ft

from gitruck.flet_search_bar import DropDownSearchBar


class MinitoolsMain(object):
    def __init__(self):
        self.program_title = "同合智创工具箱"

    def main(self, page: ft.Page):
        names = [
            "George",
            "Shawn",
            "Robert",
            "Steven",
            "William",
            "James",
            "Christopher",
            "James",
            "Michael",
            "Donovan",
            "Jessica",
            "Stephanie",
            "Ann",
            "Emma",
            "Heather",
            "Anna",
            "Kelli",
            "Pauline",
            "Tanya",
            "Kathy",
            "鸡你太美",
        ]

        page.title = self.program_title
        # page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.theme_mode = ft.ThemeMode.LIGHT
        page.padding = ft.padding.only(top=50)

        page.window_width = 560
        page.window_height = 760

        page.window_max_width = 560
        page.window_max_height = 850

        page.window_min_width = 560
        page.window_min_height = 650

        page.window_top = 200
        page.window_left = 400

        page.add(
            DropDownSearchBar(names),
        )
        page.update()


if __name__ == "__main__":
    mtm = MinitoolsMain()
    ft.app(target=mtm.main)
