import dataclasses
from dataclasses import field

import flet as ft


@dataclasses.dataclass
class DropdownSearchInputStyle:
    """搜索框样式"""

    border_color: str = field(default="transparent")
    height: int = field(default=20)
    text_size: int | float = field(default=12)
    content_padding: int = field(default=2)
    cursor_color: str = field(default="white")
    cursor_width: int = field(default=1)
    hint_text: str = field(default="搜索中……")


@dataclasses.dataclass
class DropdownSearchItemNumberStyle:
    """搜索结果数量样式"""

    size: int = field(default=9)
    italic: bool = field(default=False)
    color: str = field(default=ft.colors.BLACK54)


@dataclasses.dataclass
class DropdownSearchContainerStyle:
    """搜索组件样式"""

    width: int = field(default=450)
    height: int = field(default=50)
    bgcolor: str = field(default=ft.colors.BLACK12)
    border_radius: int = field(default=6)
    padding: ft.Padding = field(default=ft.padding.only(top=15, left=21, right=21, bottom=15))
    clip_behavior: ft.ClipBehavior = field(default=ft.ClipBehavior.HARD_EDGE)
    animate: ft.animation.Animation = field(
        default=ft.animation.Animation(
            400,
            ft.animation.AnimationCurve.DECELERATE,
        )
    )


@dataclasses.dataclass
class DropdownSearchResultButtonStyle:
    """搜索结果按钮样式"""

    height: int = field(default=26)


@dataclasses.dataclass
class DropdownSearchIconStyle:
    """搜索图标样式"""

    name: str = field(default=ft.icons.SEARCH_ROUNDED)
    size: int = field(default=15)
    opacity: float = field(default=0.90)


class DropDownSearchBarStyle:
    """下拉搜索组件样式"""

    def __init__(
        self,
        search_input: DropdownSearchInputStyle = None,
        item_number: DropdownSearchItemNumberStyle = None,
        container: DropdownSearchContainerStyle = None,
        result_button: DropdownSearchResultButtonStyle = None,
        icon: DropdownSearchIconStyle = None,
    ):
        self.search_input = search_input or DropdownSearchInputStyle()
        self.item_number = item_number or DropdownSearchItemNumberStyle()
        self.container = container or DropdownSearchContainerStyle()
        self.result_button = result_button or DropdownSearchResultButtonStyle()
        self.icon = icon or DropdownSearchIconStyle()
