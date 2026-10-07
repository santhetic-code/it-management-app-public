import reflex as rx


# ==========================================
# 1. MODEL & CONTROLLER (STATE)
# ==========================================
class LoginState(rx.State):
    username: str = ""
    password: str = ""
    show_password: bool = False
    error_message: str = ""

    def toggle_password(self):
        """Controller: Mengubah status show/hide password."""
        self.show_password = not self.show_password

    def process_login(self):
        """Controller: Logika validasi login dengan pesan error generik."""
        self.error_message = ""

        if not self.username or not self.password:
            self.error_message = "Incorrect username or password."
            return

        if self.username == "admin" and self.password == "admin123":
            return rx.window_alert("Login Sukses! Mengalihkan ke Dashboard...")
        else:
            self.error_message = "Incorrect username or password."


# ==========================================
# 2. VIEW: PANEL KIRI (Branding & Identitas)
# ==========================================
def left_panel() -> rx.Component:
    return rx.vstack(
        # Wadah Atas: Logo & Teks
        rx.vstack(
            # Logo Kustom: Kotak biru dengan ikon boxes
            rx.box(
                rx.icon(tag="boxes", size=48, color="white", stroke_width="1.5"),
                background_color="#2563EB",
                padding="16px",
                border_radius="xl",
                margin_bottom="8",
                box_shadow="0 10px 15px -3px rgb(37 99 235 / 0.4)",  # Bayangan lebih elegan
            ),
            # Judul Utama
            rx.heading(
                "Kelola Aset IT, Lebih Terpusat. 🖥️",
                size="9",  # Dibuat lebih besar
                weight="bold",
                color="#0F172A",
                line_height="1.2",
                margin_bottom="5",
                font_family="Plus Jakarta Sans",
            ),
            # Deskripsi
            rx.text(
                "Pantau perangkat, jaringan, dan jadwal perawatan dalam satu dashboard. Data lengkap, keputusan lebih cepat.",
                size="5",
                color="#475569",
                line_height="1.6",
                max_width="480px",
                font_family="Plus Jakarta Sans",
            ),
            align_items="start",
            padding_top=[
                "2em",
                "2em",
                "6em",
            ],  # Menurunkan konten sedikit dari atas di desktop
        ),
        rx.spacer(),
        # Footer Kiri Bawah
        rx.text(
            "© 2026 XMLTRONIK. Internal use only.",
            size="2",
            color="#64748B",
            weight="medium",
            font_family="Plus Jakarta Sans",
            padding_bottom="2em",
        ),
        # Styling Panel Kiri
        width=["100%", "100%", "45%"],
        height=["auto", "auto", "100%"],
        min_height=["40vh", "40vh", "100vh"],
        background="linear-gradient(145deg, #DBEAFE 0%, #EFF6FF 50%, #BFDBFE 100%)",  # Gradien lebih halus
        padding_x=[
            "2em",
            "3em",
            "6em",
        ],  # Padding kiri-kanan lebih lebar agar konten bernafas
        padding_y="2em",
        align_items="start",
        justify_content="space-between",
    )


# ==========================================
# 3. VIEW: PANEL KANAN (Formulir Login)
# ==========================================
def right_panel() -> rx.Component:
    return rx.vstack(
        # Wadah Form
        rx.vstack(
            # Teks Pojok Kanan Atas (ITAM)
            rx.text(
                "ITAM",
                weight="bold",
                size="7",
                color="#0F172A",
                margin_bottom="10",
                font_family="Plus Jakarta Sans",
            ),
            # Sapaan & Subtitle
            rx.heading(
                "Welcome",
                size="9",
                weight="bold",
                color="#0F172A",
                margin_bottom="2",
                font_family="Plus Jakarta Sans",
            ),
            rx.text(
                "The account is created by the IT Administrator. Don't have access yet? Contact the IT team.",
                size="3",
                color="#64748B",
                margin_bottom="8",
                line_height="1.5",
                font_family="Plus Jakarta Sans",
            ),
            # Area Notifikasi Error
            rx.cond(
                LoginState.error_message != "",
                rx.box(
                    rx.text(
                        LoginState.error_message,
                        color="#EF4444",
                        size="2",
                        weight="medium",
                        font_family="Plus Jakarta Sans",
                    ),
                    background_color="#FEF2F2",
                    padding="3",
                    border_radius="md",
                    width="100%",
                    margin_bottom="6",
                    border="1px solid #FCA5A5",
                ),
            ),
            # Input Username
            rx.text(
                "Username",
                size="3",
                weight="bold",
                color="#1E293B",
                width="100%",
                margin_bottom="2",
                font_family="Plus Jakarta Sans",
            ),
            rx.input(
                placeholder="Enter your username",
                value=LoginState.username,
                on_change=LoginState.set_username,
                width="100%",
                size="3",  # Ukuran input besar
                padding="6",
                radius="large",
                margin_bottom="5",
                border_color="#CBD5E1",
                font_family="Plus Jakarta Sans",
                _focus={"border_color": "#2563EB", "box_shadow": "0 0 0 1px #2563EB"},
            ),
            # Input Password
            rx.text(
                "Password",
                size="3",
                weight="bold",
                color="#1E293B",
                width="100%",
                margin_bottom="2",
                font_family="Plus Jakarta Sans",
            ),
            rx.box(
                rx.input(
                    placeholder="Enter your password",
                    type=rx.cond(LoginState.show_password, "text", "password"),
                    value=LoginState.password,
                    on_change=LoginState.set_password,
                    width="100%",
                    size="3",
                    padding="6",
                    radius="large",
                    padding_right="3em",
                    border_color="#CBD5E1",
                    font_family="Plus Jakarta Sans",
                    _focus={
                        "border_color": "#2563EB",
                        "box_shadow": "0 0 0 1px #2563EB",
                    },
                ),
                rx.box(
                    rx.cond(
                        LoginState.show_password,
                        rx.icon(
                            tag="eye-off",
                            cursor="pointer",
                            on_click=LoginState.toggle_password,
                            size=20,
                        ),
                        rx.icon(
                            tag="eye",
                            cursor="pointer",
                            on_click=LoginState.toggle_password,
                            size=20,
                        ),
                    ),
                    position="absolute",
                    right="4",
                    top="50%",
                    transform="translateY(-50%)",
                    color="#64748B",
                    _hover={"color": "#0F172A"},
                ),
                position="relative",
                width="100%",
                margin_bottom="8",
            ),
            # Tombol Login
            rx.button(
                "Login Now",
                on_click=LoginState.process_login,
                width="100%",
                size="4",  # Tombol besar
                background_color="#2563EB",
                color="white",
                cursor="pointer",
                radius="large",
                font_family="Plus Jakarta Sans",
                weight="bold",
                box_shadow="0 4px 6px -1px rgb(37 99 235 / 0.2)",
                _hover={
                    "background_color": "#1D4ED8",
                    "box_shadow": "0 10px 15px -3px rgb(37 99 235 / 0.3)",
                },
                margin_bottom="6",
            ),
            # Teks Lupa Password
            rx.text(
                "Forgot password? ",
                rx.text("Contact the IT Administrator.", as_="span", color="#2563EB", cursor="pointer", _hover={"text_decoration": "underline"}),
                size="3",
                color="#64748B",
                width="100%",
                font_family="Plus Jakarta Sans",
            ),
            width="100%",
            max_width="480px",  # Lebar form diperbesar sedikit agar proporsional
            align_items="start",
        ),
        # Styling Panel Kanan
        width=["100%", "100%", "55%"],
        height="100vh",
        background_color="#FFFFFF",
        padding_x=["2em", "3em", "8em"],  # Padding kiri-kanan lebih lebar
        padding_y="2em",
        align_items="start",  # Mengubah align_items agar form bisa di tengah via justify
        justify_content="center",
    )


# ==========================================
# 4. VIEW: HALAMAN UTAMA (Main Container)
# ==========================================
def login_page() -> rx.Component:
    return rx.flex(
        left_panel(),
        right_panel(),
        width="100vw",
        height="100vh",
        flex_direction=["column", "column", "row"],
        overflow="hidden",
    )


# Inisialisasi Aplikasi dan Font
app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap",
    ],
    theme=rx.theme(
        appearance="light", has_background=True, radius="large", accent_color="blue",
    ),
    style={"font_family": "Plus Jakarta Sans, sans-serif"}
)
app.add_page(login_page, route="/", title="Login - ITAM XMLTRONIK")
