import flet as ft
from flet import Ref
from flet_core.control_event import ControlEvent

from .search_bar_style import (
    DropDownSearchBarStyle,
    DropdownSearchContainerStyle,
    DropdownSearchIconStyle,
    DropdownSearchInputStyle,
    DropdownSearchItemNumberStyle,
    DropdownSearchResultButtonStyle,
)


class DropDownSearchBar(ft.UserControl):
    obj: ft.Container
    search_input = Ref[ft.TextField]()
    item_number = Ref[ft.Text]()
    search_results_column = Ref[ft.Column]()
    is_hover_container: bool = False

    def __init__(
        self,
        origin_data: list | dict,
        on_result_click=None,
        search_input_style: DropdownSearchInputStyle = None,
        item_number_style: DropdownSearchItemNumberStyle = None,
        container_style: DropdownSearchContainerStyle = None,
        result_button_style: DropdownSearchResultButtonStyle = None,
        icon_style: DropdownSearchIconStyle = None,
    ):
        self.style = DropDownSearchBarStyle(
            search_input=search_input_style,
            item_number=item_number_style,
            container=container_style,
            result_button=result_button_style,
            icon=icon_style,
        )
        self.origin_data = origin_data
        self.on_result_click = on_result_click if on_result_click is not None else self.on_result_selectd
        self.selected_item = None
        """搜索结果点击后的数据"""
        super().__init__()

    def check_instance(self, e: ControlEvent, height):
        if height == 0:
            self.item_number.current.value = "无结果"
            self.leave(e)
        else:
            self.obj.height = min(60 + (height * 30), 300)
            self.obj.update()

    def leave(self, _=None):
        self.obj.height = 50
        self.obj.update()

    def on_blur(self, _):
        """搜索框失去焦点事件"""
        if not self.is_hover_container:
            self.leave(_)

    def remove_search_result(self):
        """移除搜索结果"""
        self.search_results_column.current.controls.clear()
        self.item_number.current.value = ""
        self.leave()

    def on_result_selectd(self, e: ControlEvent):
        """搜索结果点击事件"""
        self.selected_item = e.control.data
        self.search_input.current.value = e.control.data
        self.remove_search_result()

    def on_container_hover(self, e: ControlEvent):
        """搜索组件鼠标悬停事件"""
        self.is_hover_container = e.data == "true"

    def on_focus(self, e: ControlEvent):
        """搜索框获取焦点事件"""
        if self.search_input.current.value == "":
            return
        count = len(self.search_results_column.current.controls)
        if count == 0:
            self.filter_data_table(e)
        else:
            self.check_instance(e, count)

    def add_search_result(self, *, key, data, **kwargs):
        """添加搜索结果"""
        row = ft.Row(
            [ft.Text(data, size=12)],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        )
        if isinstance(self.origin_data, dict):
            row.controls.append(
                ft.Text(
                    self.origin_data[data],
                    italic=True,
                    size=10,
                    color=ft.colors.BLACK54,
                )
            )
        self.search_results_column.current.controls.append(
            ft.TextButton(
                key=key,
                data=data,
                content=ft.Container(
                    content=row,
                ),
                width=self.style.container.width - 50,
                height=self.style.result_button.height,
                on_click=self.on_result_click,
                **kwargs,
            )
        )

    def filter_data_table(self, e: ControlEvent):
        if self.search_input.current.value == "":
            self.item_number.current.value = ""
            self.leave(e)
        else:
            count = 0
            self.remove_search_result()
            for index, name in enumerate(self.origin_data):
                if self.search_input.current.value.lower() in name.lower():
                    count += 1
                    self.add_search_result(key=index, data=name)
            self.item_number.current.value = f"找到 {count} 条结果"
            self.check_instance(e, count)

    def drop_down_search(self):
        """下拉搜索组件"""
        _object_ = ft.Container(
            width=self.style.container.width,
            height=self.style.container.height,
            bgcolor=self.style.container.bgcolor,
            border_radius=self.style.container.border_radius,
            padding=self.style.container.padding,
            clip_behavior=self.style.container.clip_behavior,
            animate=self.style.container.animate,
            on_hover=self.on_container_hover,
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.START,
                controls=[
                    ft.Row(
                        spacing=10,
                        vertical_alignment=ft.CrossAxisAlignment.CENTER,
                        controls=[
                            ft.Icon(
                                name=self.style.icon.name,
                                size=self.style.icon.size,
                                opacity=self.style.icon.opacity,
                            ),
                            ft.TextField(
                                ref=self.search_input,
                                border_color=self.style.search_input.border_color,
                                height=self.style.search_input.height,
                                text_size=self.style.search_input.text_size,
                                content_padding=self.style.search_input.content_padding,
                                cursor_color=self.style.search_input.cursor_color,
                                cursor_width=self.style.search_input.cursor_width,
                                hint_text=self.style.search_input.hint_text,
                                on_change=self.filter_data_table,
                                on_focus=self.on_focus,
                                on_blur=self.on_blur,
                            ),
                            ft.Text(
                                ref=self.item_number,
                                size=self.style.item_number.size,
                                italic=self.style.item_number.italic,
                                color=self.style.item_number.color,
                            ),
                        ],
                    ),
                    ft.Column(
                        scroll=ft.ScrollMode.AUTO,
                        expand=True,
                        ref=self.search_results_column,
                        spacing=4,
                    ),
                ],
            ),
        )
        self.search_input.current.value = ""
        self.item_number.current.value = ""
        self.obj = _object_
        return _object_

    def build(self):
        return self.drop_down_search()
