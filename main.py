import flet as ft

from utils import first_run, get_options

if_first_run = first_run()

options = get_options()

# print(options)


def main(page: ft.Page):
    page.title = options["app_title"]
    page.theme_mode = (
        ft.ThemeMode.DARK
        if options["theme_mode"] == "dark"
        else ft.ThemeMode.LIGHT
        if options["theme_mode"] == "light"
        else ft.ThemeMode.SYSTEM
    )
    page.window_maximized = True
    page.padding = 0

    # set page transitions for each platform (optional)
    theme = ft.Theme()
    theme.page_transitions.android = ft.PageTransitionTheme.OPEN_UPWARDS
    theme.page_transitions.ios = ft.PageTransitionTheme.CUPERTINO
    theme.page_transitions.macos = ft.PageTransitionTheme.FADE_UPWARDS
    theme.page_transitions.linux = ft.PageTransitionTheme.ZOOM
    theme.page_transitions.windows = ft.PageTransitionTheme.NONE
    page.theme = theme

    def view_pop(e):
        print("View pop:", e.view)
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    print("Initial route:", page.route)

    def on_keyboard(e: ft.KeyboardEvent):
        if e.key == "Backspace":
            # not implemented yet
            pass

    app_bar = ft.AppBar(
        leading_width=40,
        automatically_imply_leading=False,
        title=ft.TextButton(
            expand=10,
            content=ft.Text(
                options["app_title"],
                color=ft.colors.WHITE,
                size=20,
            ),
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(),
            ),
            on_click=lambda e: page.go("/"),
        ),
        bgcolor=ft.colors.GREY_900,
        actions=[
            ft.TextButton(
                expand=1,
                text="Home",
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(),
                ),
                on_click=lambda e: page.go("/"),
            ),
            ft.TextButton(
                expand=1,
                text="Search",
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(),
                ),
                on_click=lambda e: page.go("/search"),
            ),
            ft.TextButton(
                expand=1,
                text="Template Apps",
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(),
                ),
                on_click=lambda e: page.go("/templates"),
            ),
            ft.TextButton(
                expand=1,
                text="Page and Components",
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(),
                ),
                on_click=lambda e: page.go("/page_and_components"),
            ),
            ft.TextButton(
                expand=1,
                text="Contact Us",
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(),
                ),
                on_click=lambda e: page.go("/contact_us"),
            ),
            ft.IconButton(
                icon=ft.icons.SETTINGS,
                style=ft.ButtonStyle(
                    shape=ft.RoundedRectangleBorder(),
                ),
                on_click=lambda e: page.go("/settings"),
            ),
        ],
    )

    def route_change(e):
        print("Route change:", e.route)
        page.views.clear()
        page.views.append(
            ft.View(
                padding=0,
                scroll="adaptive",
                route="/",
                appbar=app_bar,
                controls=[
                    ft.Container(
                        alignment=ft.alignment.center,
                        height=500,
                        padding=0,
                        gradient=ft.LinearGradient(
                            tile_mode=ft.GradientTileMode.REPEATED,
                            colors=[
                                "#161C1E",
                                "#282542",
                                "#41302E",
                                "#312940",
                                "#433031",
                                "#26223C",
                                "#41302F",
                                "#3E2F2F",
                                "#161C1E",
                            ],
                        ),
                        content=ft.Column(
                            alignment=ft.alignment.center,
                            controls=[
                                ft.Text(
                                    "Flet Marketplace",
                                    text_align=ft.alignment.center,
                                    color=ft.colors.WHITE70,
                                    size=50,
                                ),
                                ft.Text(
                                    "Search hundreds of free templates to quickly get started on your next big idea.",
                                    col=2,
                                    color=ft.colors.GREY_500,
                                    size=25,
                                    text_align=ft.alignment.center,
                                ),
                                ft.SearchBar(
                                    bar_hint_text="Search for a template.",
                                    controls=[
                                        ft.Text(
                                            "Search",
                                            color=ft.colors.WHITE,
                                            size=20,
                                        ),
                                    ],
                                    bar_trailing=[
                                        ft.TextButton(
                                            text="Search",
                                            style=ft.ButtonStyle(
                                                bgcolor=ft.colors.BLUE,
                                                shape=ft.RoundedRectangleBorder(
                                                    radius=10
                                                ),
                                            ),
                                            on_click=lambda e: page.go("/search"),
                                        ),
                                    ],
                                    on_submit=lambda e: page.go("/search"),
                                ),
                                ft.Container(
                                    padding=5,
                                    width=800,
                                    alignment=ft.alignment.center,
                                    content=ft.Text(
                                        "Or use one of the popular tags below.",
                                        color=ft.colors.GREY_500,
                                        size=15,
                                    ),
                                ),
                                ft.Row(
                                    width=800,
                                    controls=[
                                        ft.ElevatedButton(
                                            expand=1,
                                            text="Animation",
                                            style=ft.ButtonStyle(
                                                color=ft.colors.WHITE,
                                                bgcolor="#3A2E73",
                                                shape=ft.RoundedRectangleBorder(
                                                    radius=15
                                                ),
                                            ),
                                            on_click=lambda e: page.go("/search"),
                                        ),
                                        ft.ElevatedButton(
                                            expand=1,
                                            text="Business",
                                            style=ft.ButtonStyle(
                                                color=ft.colors.WHITE,
                                                bgcolor="#6E4848",
                                                shape=ft.RoundedRectangleBorder(
                                                    radius=15
                                                ),
                                            ),
                                            on_click=lambda e: page.go("/search"),
                                        ),
                                        ft.ElevatedButton(
                                            expand=1,
                                            text="E-Commerce",
                                            style=ft.ButtonStyle(
                                                color=ft.colors.WHITE,
                                                bgcolor="#704946",
                                                shape=ft.RoundedRectangleBorder(
                                                    radius=15
                                                ),
                                            ),
                                            on_click=lambda e: page.go("/search"),
                                        ),
                                        ft.ElevatedButton(
                                            expand=1,
                                            text="Dashboard",
                                            style=ft.ButtonStyle(
                                                color=ft.colors.WHITE,
                                                bgcolor="#3E316E",
                                                shape=ft.RoundedRectangleBorder(
                                                    radius=15
                                                ),
                                            ),
                                            on_click=lambda e: page.go("/search"),
                                        ),
                                        ft.ElevatedButton(
                                            expand=1,
                                            text="Clean",
                                            style=ft.ButtonStyle(
                                                color=ft.colors.WHITE,
                                                bgcolor="#3D5E60",
                                                shape=ft.RoundedRectangleBorder(
                                                    radius=15
                                                ),
                                            ),
                                            on_click=lambda e: page.go("/search"),
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ),
                    
                    ft.Container(
                        bgcolor=ft.colors.GREY_900,
                        alignment=ft.alignment.center,
                        content=ft.Column(
                            alignment=ft.alignment.center,
                            controls=[
                                ft.Text(
                                    "Featured Templates",
                                    width=1000,
                                    color=ft.colors.WHITE70,
                                    size=30,
                                ),
                                ft.Text(
                                    "Spotlighted products for you to discover.",
                                    width=1000,
                                    color=ft.colors.WHITE70,
                                    size=15,
                                ),
                                
                                ft.GridView(
                                    #expand=1,
                                    horizontal=True,
                                    height=400,
                                    width=1200,
                                    spacing=2,
                                    padding=3,
                                    col=2,
                                    
                                    controls=[
                                        ft.Container(
                                            border_radius=10,
                                            padding=5,
                                            content=ft.Column(
                                                spacing=1,
                                                controls=[
                                                    ft.Container(
                                                        border_radius=10,
                                                        width=300,
                                                        height=200,
                                                        content=ft.Image(
                                                            fit=ft.ImageFit.FILL,
                                                            src="assets/marketplace_items_1682278859558.jpg",
                                                        ),
                                                        on_click=lambda e: page.go("/search"),
                                                    ),
                                                    ft.Column(
                                                        spacing=1,
                                                        controls=[
                                                            ft.Text(
                                                                "Health & Fitness App Template",
                                                                width=800,
                                                                color=ft.colors.WHITE,
                                                                size=15,
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ),
                                        ft.Container(
                                            alignment=ft.alignment.center,
                                            border_radius=10,
                                            content=ft.Column(
                                                spacing=1,
                                                controls=[
                                                    ft.Container(
                                                        border_radius=10,
                                                        width=300,
                                                        height=200,
                                                        content=ft.Image(
                                                            fit=ft.ImageFit.FILL,
                                                            src="assets/marketplace_items_1676727415510.png",
                                                        ),
                                                        on_click=lambda e: page.go("/search"),
                                                    ),
                                                    ft.Column(
                                                        spacing=1,
                                                        controls=[
                                                            ft.Text(
                                                                "Flowtify (Spotify Redesign)",
                                                                width=800,
                                                                color=ft.colors.WHITE,
                                                                size=15,
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ),
                                        ft.Container(
                                            alignment=ft.alignment.center,
                                            border_radius=10,
                                            content=ft.Column(
                                                spacing=1,
                                                controls=[
                                                    ft.Container(
                                                        border_radius=10,
                                                        width=300,
                                                        height=200,
                                                        content=ft.Image(
                                                            fit=ft.ImageFit.FILL,
                                                            src="assets/marketplace_items_1697893921410.jpg",
                                                        ),
                                                        on_click=lambda e: page.go("/search"),
                                                    ),
                                                    ft.Column(
                                                        spacing=1,
                                                        controls=[
                                                            ft.Text(
                                                                "The Best Groceries App UI",
                                                                width=800,
                                                                color=ft.colors.WHITE,
                                                                size=15,
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                            ),
                                        ),
                                    ],
                                ),
                                ft.Text(
                                    "Browse our featured templates.",
                                    width=1000,
                                    color=ft.colors.WHITE70,
                                    size=20,
                                ),
                            ],
                        ),
                    ),
                ],
            )
        )
        if page.route == "/settings":
            page.views.append(
                ft.View(
                    "/settings",
                    [
                        app_bar,
                        ft.Container(
                            expand=10,
                            alignment=ft.alignment.center,
                            content=ft.Text("Settings page not yet implemented."),
                        ),
                    ],
                )
            )
        if page.route == "/search":
            page.views.append(
                ft.View(
                    "/search",
                    [
                        app_bar,
                        ft.Container(
                            expand=10,
                            alignment=ft.alignment.center,
                            content=ft.Text("Search page not yet implemented."),
                        ),
                    ],
                )
            )
        if page.route == "/templates":
            page.views.append(
                ft.View(
                    "/templates",
                    [
                        app_bar,
                        ft.Container(
                            expand=10,
                            alignment=ft.alignment.center,
                            content=ft.Text("Templates page not yet implemented."),
                        ),
                    ],
                )
            )
        if page.route == "/page_and_components":
            page.views.append(
                ft.View(
                    "/page_and_components",
                    [
                        app_bar,
                        ft.Container(
                            expand=10,
                            alignment=ft.alignment.center,
                            content=ft.Text("Not yet implemented."),
                        ),
                    ],
                )
            )

        if page.route == "/contact_us":
            page.views.append(
                ft.View(
                    "/contact_us",
                    [
                        app_bar,
                        ft.Container(
                            expand=10,
                            alignment=ft.alignment.center,
                            content=ft.Text("Page is Empty."),
                        ),
                    ],
                )
            )

        page.update()

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.on_keyboard_event = on_keyboard

    page.go(page.route)


ft.app(
    target=main,
    # view=ft.WEB_BROWSER
)
