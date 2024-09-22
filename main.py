import flet as ft

def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def handle_close(e):
        dlg_modal.open = False
        page.add(ft.Text(f"Modal dialog closed with action: {e.control.text}"))

    def handle_dismiss(e):
        page.add(ft.Text("Modal dialog dismissed"))

    def handle_click(e):
        dlg_modal.open = True
        page.add(ft.Text(f"Modal dialog opened with action: {e.control.text}"))

    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Please confirm"),
        content=ft.Text("Do you really want to ...?"),
        actions=[
            ft.TextButton("Yes", on_click=handle_close),
            ft.TextButton("No", on_click=handle_close),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=handle_dismiss,
    )

    def minus_click(e):
        txt_number.value = str(int(txt_number.value) - 1)
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        dlg_modal,
        ft.Column(
            [
                ft.Row(
                    [
                        ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                        txt_number,
                        ft.IconButton(ft.icons.ADD, on_click=plus_click),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.ElevatedButton("Open dialog", on_click=handle_click)
    )

ft.app(main)
