import os
import customtkinter as ctk
from tkinter import messagebox

# Importamos la función del servicio y las ventanas de los paneles
from servicios.servicio_autenticacion import autenticar
from interfaz.panel_socio import PanelSocio
from interfaz.panel_admin import PanelAdmin

# Configuración del tema gráfico
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class LoginBocaHandball(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.title("Boca Juniors - Handball | Inicio de Sesión")
        self.geometry("420x620")
        self.resizable(False, False)
        
        # Color de fondo principal (Azul Oscuro)
        self.configure(fg_color="#0A182E")

        self.crear_interfaz()

    def crear_interfaz(self):
        # Tarjeta central con bordes dorados
        self.card_frame = ctk.CTkFrame(
            master=self,
            width=360,
            height=560,
            corner_radius=20,
            fg_color="#001F3F",       # Azul Boca
            border_width=2,
            border_color="#FFC72C"    # Amarillo Oro Boca
        )
        self.card_frame.pack(padx=20, pady=30, fill="both", expand=True)

        # Encabezado (Icono y Títulos)
        self.lbl_escudo = ctk.CTkLabel(
            master=self.card_frame,
            text="🤾‍♂️",
            font=("Arial", 48)
        )
        self.lbl_escudo.pack(pady=(30, 5))

        self.lbl_titulo = ctk.CTkLabel(
            master=self.card_frame,
            text="BOCA JUNIORS",
            font=("Arial Bold", 22),
            text_color="#FFC72C"      # Amarillo Oro
        )
        self.lbl_titulo.pack(pady=(0, 2))

        self.lbl_subtitulo = ctk.CTkLabel(
            master=self.card_frame,
            text="H A N D B A L L",
            font=("Arial", 14, "bold"),
            text_color="#FFFFFF"
        )
        self.lbl_subtitulo.pack(pady=(0, 25))

        # Campo: Usuario
        self.lbl_usuario = ctk.CTkLabel(
            master=self.card_frame,
            text="Usuario / DNI:",
            font=("Arial", 12, "bold"),
            text_color="#CBD5E1"
        )
        self.lbl_usuario.pack(anchor="w", padx=40, pady=(10, 2))

        self.txt_usuario = ctk.CTkEntry(
            master=self.card_frame,
            placeholder_text="Ingresá tu usuario",
            width=280,
            height=40,
            corner_radius=10,
            fg_color="#0A182E",
            border_color="#FFC72C",
            text_color="#FFFFFF",
            placeholder_text_color="#64748B"
        )
        self.txt_usuario.pack(padx=40, pady=(0, 15))

        # Campo: Contraseña (show="*" oculta la contraseña al escribir)
        self.lbl_password = ctk.CTkLabel(
            master=self.card_frame,
            text="Contraseña:",
            font=("Arial", 12, "bold"),
            text_color="#CBD5E1"
        )
        self.lbl_password.pack(anchor="w", padx=40, pady=(0, 2))

        self.txt_password = ctk.CTkEntry(
            master=self.card_frame,
            placeholder_text="••••••••••••",
            show="*",
            width=280,
            height=40,
            corner_radius=10,
            fg_color="#0A182E",
            border_color="#FFC72C",
            text_color="#FFFFFF",
            placeholder_text_color="#64748B"
        )
        self.txt_password.pack(padx=40, pady=(0, 10))

        # Enlace Olvidé mi contraseña
        self.btn_olvido = ctk.CTkButton(
            master=self.card_frame,
            text="¿Olvidaste tu contraseña?",
            font=("Arial", 11, "underline"),
            text_color="#FFC72C",
            hover_color="#001F3F",
            fg_color="transparent",
            width=100,
            command=self.accion_olvido
        )
        self.btn_olvido.pack(anchor="e", padx=40, pady=(0, 20))

        # Botón Principal: Iniciar Sesión
        self.btn_login = ctk.CTkButton(
            master=self.card_frame,
            text="INICIAR SESIÓN",
            font=("Arial Bold", 14),
            width=280,
            height=45,
            corner_radius=22,
            fg_color="#FFC72C",         # Amarillo Oro
            text_color="#001F3F",       # Texto Azul
            hover_color="#E6B000",
            command=self.validar_login
        )
        self.btn_login.pack(padx=40, pady=(10, 20))

        # Tecla Enter para procesar el login
        self.bind('<Return>', lambda event: self.validar_login())

    def validar_login(self):
        usuario = self.txt_usuario.get().strip()
        password = self.txt_password.get().strip()

        # 1. Validar campos no vacíos
        if not usuario or not password:
            messagebox.showwarning("Atención", "Por favor completa todos los campos.")
            return

        # 2. Llamar al servicio autenticar() en lugar de hacer la consulta a la BD directamente
        socio = autenticar(usuario, password)

        # 3. Evaluar el resultado de autenticar()
        if socio:
            # Ocultar la ventana de Login sin destruirla inmediatamente para sostener los Toplevel
            self.withdraw()
            self.abrir_panel_segun_rol(socio)
        else:
            # Mismo mensaje genérico si falla
            messagebox.showerror("Error de Acceso", "Usuario o contraseña incorrectos.")
            self.txt_password.delete(0, 'end')

    def abrir_panel_segun_rol(self, socio):
        # 4. Mirar socio.rol para abrir el panel correspondiente (como Toplevel)
        rol = str(socio.rol).lower()

        if rol in ["admin", "administrador"]:
            panel = PanelAdmin(master=self, socio=socio)
        elif rol in ["socio", "cliente"]:
            panel = PanelSocio(master=self, socio=socio)
        else:
            messagebox.showerror("Error de Rol", f"El rol '{socio.rol}' no tiene un panel asignado.")
            self.deiconify()
            return

        # Cuando el panel secundario se destruye (al hacer clic en "Cerrar"), volvemos a mostrar el login
        panel.protocol("WM_DELETE_WINDOW", lambda: self.al_cerrar_panel(panel))

    def al_cerrar_panel(self, panel):
        panel.destroy()
        self.txt_password.delete(0, 'end')
        self.deiconify()

    def accion_olvido(self):
        messagebox.showinfo("Restablecer Clave", "Comunicate con la administración del club para blanquear tu clave.")


if __name__ == "__main__":
    app = LoginBocaHandball()
    app.mainloop()