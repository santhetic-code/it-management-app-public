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
        # Reset pesan error sebelum pengecekan
        self.error_message = ""
        
        # Validasi kosong
        if not self.username or not self.password:
            self.error_message = "Incorrect username or password."
            return

        # Simulasi validasi ke database (Mock)
        if self.username == "admin" and self.password == "admin123":
            return rx.window_alert("Login Sukses! Mengalihkan ke Dashboard...")
        else:
            # Pesan error generik demi keamanan (tidak memberi tahu bagian mana yang salah)
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
                rx.icon(tag="boxes", size=32, color="white"),
                background_color="#2563EB", # Biru utama
                padding="12px",
                border_radius="xl",
                margin_bottom="6",
                box_shadow="0 4px 6px -1px rgb(37 99 235 / 0.3)",
            ),
            
            # Judul Utama
            rx.heading(
                "Kelola Aset IT, Lebih Terpusat. 🖥️",
                size="8",
                weight="bold",
                color="#0F172A",
                line_height="1.2",
                margin_bottom="4",
            ),
            
            # Deskripsi
            rx.text(
                "Pantau perangkat, jaringan, dan jadwal perawatan dalam satu dashboard. Data lengkap, keputusan lebih cepat.",
                size="4",
                color="#64748B",
                line_height="1.6",
                max_width="400px",
            ),
            align_items="start",
        ),
        
        rx.spacer(), # Mendorong footer ke bagian paling bawah
        
        # Footer Kiri Bawah
        rx.text(
            "© 2026 XMLTRONIK. Internal use only.",
            size="2",
            color="#64748B",
            weight="medium",
        ),
        
        # Styling Panel Kiri
        width=["100%", "100%", "45%"], # Responsif: Penuh di mobile, 45% di desktop
        height=["auto", "auto", "100%"],
        min_height=["40vh", "40vh", "100vh"],
        background="linear-gradient(135deg, #DBEAFE 0%, #BFDBFE 100%)", # Gradien biru muda
        padding="4em",
        align_items="start",
        justify_content="space-between",
    )

# ==========================================
# 3. VIEW: PANEL KANAN (Formulir Login)
# ==========================================
def right_panel() -> rx.Component:
    return rx.vstack(
        # Wadah Form (Agar berada di tengah vertikal)
        rx.vstack(
            # Teks Pojok Kanan Atas (ITAM)
            rx.text("ITAM", weight="bold", size="6", color="#0F172A", margin_bottom="8"),
            
            # Sapaan & Subtitle
            rx.heading("Welcome", size="8", weight="bold", color="#0F172A", margin_bottom="2"),
            rx.text(
                "The account is created by the IT Administrator. Don't have access yet? Contact the IT team.",
                size="3",
                color="#64748B",
                margin_bottom="6",
            ),

            # Area Notifikasi Error
            rx.cond(
                LoginState.error_message != "",
                rx.box(
                    rx.text(LoginState.error_message, color="#EF4444", size="2", weight="medium"),
                    background_color="#FEE2E2",
                    padding="3",
                    border_radius="md",
                    width="100%",
                    margin_bottom="4",
                    border="1px solid #F87171"
                ),
            ),

            # Input Username
            rx.text("Username", size="2", weight="bold", color="#0F172A", width="100%", margin_bottom="1"),
            rx.input(
                placeholder="Enter your username",
                value=LoginState.username,
                on_change=LoginState.set_username,
                width="100%",
                size="3",
                margin_bottom="4",
                border_color="#CBD5E1",
            ),

            # Input Password dengan Ikon Mata (Show/Hide)
            rx.text("Password", size="2", weight="bold", color="#0F172A", width="100%", margin_bottom="1"),
            rx.box(
                rx.input(
                    placeholder="Enter your password",
                    type=rx.cond(LoginState.show_password, "text", "password"),
                    value=LoginState.password,
                    on_change=LoginState.set_password,
                    width="100%",
                    size="3",
                    padding_right="2.5em", # Memberi ruang agar teks tidak tertutup ikon
                    border_color="#CBD5E1",
                ),
                # Ikon Mata (Mata terbuka/tertutup)
                rx.icon(
                    tag=rx.cond(LoginState.show_password, "eye-off", "eye"),
                    position="absolute",
                    right="3",
                    top="50%",
                    transform="translateY(-50%)",
                    color="#64748B",
                    cursor="pointer",
                    on_click=LoginState.toggle_password,
                    _hover={"color": "#0F172A"}
                ),
                position="relative", # Penting agar ikon absolute mengikuti kotak ini
                width="100%",
                margin_bottom="6",
            ),

            # Tombol Login
            rx.button(
                "Login Now",
                on_click=LoginState.process_login,
                width="100%",
                size="3",
                background_color="#2563EB", # Biru utama
                color="white",
                cursor="pointer",
                _hover={"background_color": "#1D4ED8"}, # Biru lebih gelap saat di-hover
                margin_bottom="6",
            ),

            # Teks Lupa Password
            rx.text(
                "Forgot password? ",
                rx.text.span("Contact the IT Administrator.", color="#2563EB", cursor="pointer", _hover={"text_decoration": "underline"}),
                size="2",
                color="#64748B",
                width="100%",
            ),
            
            width="100%",
            max_width="450px", # Membatasi lebar form agar rapi
            align_items="start",
        ),
        
        # Styling Panel Kanan
        width=["100%", "100%", "55%"], # Responsif: Penuh di mobile, 55% di desktop
        height="100vh",
        background_color="#FFFFFF",
        padding="4em",
        align_items="center",
        justify_content="center", # Memposisikan form di tengah layar vertikal
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
        flex_direction=["column", "column", "row"], # Responsif: Atas-bawah di HP, Kiri-Kanan di Laptop
        overflow="hidden",
    )

# Inisialisasi Aplikasi
app = rx.App(
    theme=rx.theme(
        appearance="light", has_background=True, radius="large", accent_color="blue"
    )
)
app.add_page(login_page, route="/", title="Login - ITAM XMLTRONIK")
